from src.conversation import Conversation

def test_system_and_history_roles():
    c = Conversation("Custom")
    c.add_user("hello")
    c.add_assistant("hi")
    assert c.api_messages() == [
        {"role": "system", "content": "Custom"},
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "hi"},
    ]

def test_clear_history():
    c = Conversation()
    c.add_user("hello")
    c.clear()
    assert c.messages == []
