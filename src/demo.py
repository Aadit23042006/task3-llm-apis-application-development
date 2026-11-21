def demo_response(user_text: str, history=None, instructions: str = "") -> str:
    text = user_text.strip()
    if not text:
        return "Please enter a message."
    if "zero-shot" in text.lower():
        return ("Zero-shot prompting asks a model to perform a task without giving examples. "
                "You provide the instruction and context, then the model responds.")
    prefix = "Demo response (no live API call): "
    if instructions.strip():
        prefix += f"Your custom instruction is: {instructions.strip()[:120]}. "
    return prefix + f"You asked: {text[:500]}. Connect an API key to receive a live model response."
