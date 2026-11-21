from src.usage import estimate_tokens, estimate_usage

def test_token_estimate():
    assert estimate_tokens("") == 0
    assert estimate_tokens("abcd") == 1
    assert estimate_tokens("abcdefgh") == 2

def test_cost_estimate():
    usage = estimate_usage("abcd", "abcdefgh", 1.0, 2.0)
    assert usage.input_tokens == 1
    assert usage.output_tokens == 2
    assert usage.total_tokens == 3
    assert usage.estimated_cost_usd == 0.005
