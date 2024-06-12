import ai, stop_ai

def get_response(user_input: str) -> str:
    Lowered: str = user_input.lower()
    is_stop: bool = stop_ai.Thumbrix_AI(Lowered)
    if is_stop == "true" or is_stop == "True" or is_stop == "TRUE":
        return ai.Thumbrix_AI(Lowered)