import os
from src.llm_client import generate_reply

def test_generate_reply_demo_mode():
    messages = [{"role":"system","content":"Helpful assistant"},
                {"role":"user","content":"What is an API?"}]
    reply, metadata = generate_reply(messages, demo_mode=True, api_key="", base_url="https://example.invalid")
    assert reply
    assert metadata["demo"] is True
    assert metadata["usage"] is None
