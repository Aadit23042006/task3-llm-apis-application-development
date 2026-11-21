from unittest.mock import patch, MagicMock
from types import SimpleNamespace

from src.llm_client import generate_reply


class SimulatedRateLimitError(Exception):
    status_code = 429


# Simulate an API client
mock_client = MagicMock()

# First request: HTTP 429
# Second request: successful response
mock_client.chat.completions.create.side_effect = [
    SimulatedRateLimitError("Rate limit exceeded"),
    SimpleNamespace(
        choices=[
            SimpleNamespace(
                message=SimpleNamespace(content="Retry successful!")
            )
        ],
        usage=None,
    ),
]

messages = [
    {"role": "user", "content": "Say hello"}
]

with patch("openai.OpenAI", return_value=mock_client), \
     patch("src.llm_client.time.sleep") as mock_sleep:

    response, metadata = generate_reply(
        messages=messages,
        model="gemini-2.5-flash",
        temperature=0.7,
        max_tokens=100,
        demo_mode=False,
        api_key="fake-test-key",
        base_url="https://example.com/v1",
    )

    # Verification
    assert response == "Retry successful!"
    assert mock_client.chat.completions.create.call_count == 2
    mock_sleep.assert_called_once_with(1)

    print("=" * 50)
    print("RATE-LIMIT TEST: PASSED")
    print("=" * 50)
    print("First request: HTTP 429 simulated")
    print("Retry delay: 1 second")
    print("Second request: Successful")
    print("Total API attempts: 2")
    print("Infinite retries: No")
    print("API quota used: None")