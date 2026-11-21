from src.demo import demo_response

def test_demo_response():
    assert "Zero-shot" in demo_response("Explain zero-shot prompting")

def test_empty_input():
    assert demo_response(" ") == "Please enter a message."
