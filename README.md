# Task 3 — LLM APIs & Application Development

## AI Chat Lab — API-Powered Conversational AI Application

AI Chat Lab is a Streamlit application demonstrating how to integrate Large Language Models (LLMs) into an interactive application through an OpenAI-compatible API. It includes conversation management, configurable instructions and model parameters, JSON response mode, error handling, token-usage reporting, cost estimation, and Demo Mode.

## Project links

- **Live application:** https://task3-llm-apis-application-development-5ruqmpmufgwkuerqduerld.streamlit.app
- **GitHub repository:** https://github.com/Aadit23042006/task3-llm-apis-application-development
- **Notebook:** `notebooks/Task3_LLM_APIs_Application_Development.ipynb`

> The Streamlit URL is the deployment address. Confirm that it opens publicly and test a prompt before describing the hosted application or Live API mode as verified. Demo responses are simulated and are not live model inference.

## Features

- OpenAI-compatible chat-completion API integration and configurable provider endpoint/model
- Streamlit chat UI and session conversation history
- Custom system instructions
- Temperature and maximum output-token controls
- JSON response mode where supported by the provider/model
- Demo Mode for testing without credentials
- API error handling and limited retry handling for transient errors
- Provider-reported token usage when available
- Estimated token usage and cost when provider usage is unavailable
- Notebook examples for API configuration, live requests, JSON responses, usage normalization, cost estimation, error handling, retry logic, and regression tests

## Technology stack

| Technology | Purpose |
|---|---|
| Python | Application and utility code |
| Streamlit | Interactive web UI |
| OpenAI Python SDK | OpenAI-compatible API client |
| Google Gemini API | Configured provider used in the notebook/application setup |
| Jupyter / Google Colab | API experiments and notebook tests |
| pytest | Unit/regression tests |
| python-dotenv | Local environment configuration |
| Git / GitHub | Version control and source hosting |
| Streamlit Community Cloud | Hosting platform |

## Architecture

```text
User
  │
  ▼
Streamlit UI (app.py)
  │
  ├── Conversation/session state (src/conversation.py)
  ├── LLM client and request handling (src/llm_client.py)
  ├── Demo responses (src/demo.py)
  └── Usage and cost utilities (src/usage.py)
          │
          ▼
OpenAI-compatible LLM API endpoint
          │
          ▼
Model response → UI and usage summary
```

## Project structure

```text
task3-llm-apis-application-development/
├── .streamlit/
│   └── config.toml
├── notebooks/
│   └── Task3_LLM_APIs_Application_Development.ipynb
├── src/
│   ├── __init__.py
│   ├── conversation.py
│   ├── demo.py
│   ├── llm_client.py
│   └── usage.py
├── tests/
│   ├── test_conversation.py
│   ├── test_demo.py
│   ├── test_llm_client_demo.py
│   └── test_usage.py
├── .env.example
├── .gitignore
├── app.py
├── DEPLOYMENT_GUIDE.md
├── PROJECT_STRUCTURE.md
├── linkedin_post.md
├── requirements.txt
└── test_rate_limit.py
```

## Requirements

- Python 3.10+ recommended
- pip
- Internet connection for Live API mode
- Provider API key for Live API mode

Demo Mode can run without an API key.

## Local setup

### 1. Clone

```bash
git clone https://github.com/Aadit23042006/task3-llm-apis-application-development.git
cd task3-llm-apis-application-development
```

### 2. Create and activate a virtual environment

**Windows CMD:**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure local environment

Copy `.env.example` to `.env` and fill in your own values. Example:

```dotenv
DEMO_MODE=false
LLM_API_KEY=replace_with_your_api_key
LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
LLM_MODEL=gemini-2.5-flash
```

Do not commit `.env`, API keys, or Streamlit secrets. Keep `DEMO_MODE=true` if you want to run without a provider key.

### 5. Run

```bash
python -m streamlit run app.py
```

Open the local address Streamlit prints, normally `http://localhost:8501`.

## Notebook

Open the notebook in Google Colab or Jupyter. Configure the API key using Colab Secrets or secure runtime input, then run cells in order. The notebook demonstrates API requests, messages/roles, JSON mode, usage normalization, cost estimation, safe error handling, retries, parameter validation, and regression checks.

## Testing

Run the project's tests from the repository root:

```bash
pytest -q
```

The notebook's regression-test cells are separate from the pytest suite. Run the notebook from top to bottom to verify those checks. Do not report a test as passed unless it has actually been executed.

## Deployment

The app is configured for Streamlit Community Cloud. See [`DEPLOYMENT_GUIDE.md`](DEPLOYMENT_GUIDE.md) for GitHub setup, app configuration, secrets, and verification steps.

- Entry point: `app.py`
- Branch: `main`
- Dependencies: `requirements.txt`

Streamlit Community Cloud requires the repository, branch, entrypoint, dependencies, and deployment secrets to be configured. See the official [deployment documentation](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy).

## Security

- Never commit `.env` or `.streamlit/secrets.toml`.
- Use `.env.example` only for placeholder configuration.
- Store cloud credentials in the hosting platform's secret manager.
- If a key has been committed or shared, revoke it and create a replacement.
- Avoid printing API keys or raw provider exception messages.

## Limitations

- Live API mode depends on provider access, model availability, quota, and correct credentials.
- Demo Mode uses simulated responses and is not actual LLM inference.
- Token/cost estimates may be approximate; configured rates must be checked against current provider pricing.
- JSON mode is provider/model-dependent.
- The current hosted Live API path should be tested separately from local notebook/API tests.

## Assignment

**Task:** LLM APIs & Application Development  
**Project:** AI Chat Lab — API-Powered Conversational AI Application  
**Author:** Aadit Choudhary
