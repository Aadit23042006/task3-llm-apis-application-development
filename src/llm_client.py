import os
import time
from typing import Optional
from .demo import demo_response

class LLMConfigurationError(RuntimeError):
    pass

class LLMRequestError(RuntimeError):
    pass

def env_config():
    return {
        "api_key": os.getenv("LLM_API_KEY", "").strip(),
        "base_url": os.getenv("LLM_BASE_URL", "https://api.openai.com/v1").strip(),
        "model": os.getenv("LLM_MODEL", "gpt-4o-mini").strip(),
        "demo_mode": os.getenv("DEMO_MODE", "true").lower() in {"1", "true", "yes", "on"},
    }

def generate_reply(messages, model: Optional[str] = None, temperature: float = 0.7,
                   max_tokens: int = 500, json_mode: bool = False,
                   demo_mode: Optional[bool] = None, api_key: Optional[str] = None,
                   base_url: Optional[str] = None):
    cfg = env_config()
    use_demo = cfg["demo_mode"] if demo_mode is None else demo_mode
    key = api_key if api_key is not None else cfg["api_key"]
    url = base_url if base_url is not None else cfg["base_url"]
    chosen_model = model or cfg["model"]
    latest_user = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "")
    system = next((m["content"] for m in messages if m["role"] == "system"), "")
    if use_demo or not key:
        return demo_response(latest_user, messages, system), {"demo": True, "usage": None}
    if not key:
        raise LLMConfigurationError("Missing LLM_API_KEY. Add it to environment variables or enable Demo Mode.")
    from openai import OpenAI
    client = OpenAI(api_key=key, base_url=url, timeout=30.0, max_retries=0)
    kwargs = {"model": chosen_model, "messages": messages, "temperature": temperature,
              "max_tokens": max_tokens}
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}
    last_error = None
    for attempt in range(2):
        try:
            result = client.chat.completions.create(**kwargs)
            content = result.choices[0].message.content or ""
            usage = None
            if result.usage:
                usage = {"prompt_tokens": result.usage.prompt_tokens,
                         "completion_tokens": result.usage.completion_tokens,
                         "total_tokens": result.usage.total_tokens}
            return content, {"demo": False, "usage": usage}
        except Exception as exc:
            last_error = exc
            status = getattr(exc, "status_code", None)
            if attempt == 0 and (status == 429 or (status and status >= 500)):
                time.sleep(1)
                continue
            break
    # Avoid exposing provider details or secrets in the UI.
    raise LLMRequestError(f"LLM request failed. Check API settings, model access, quota, or network. (Error type: {type(last_error).__name__})")
