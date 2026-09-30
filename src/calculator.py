"""Core calculation logic independent of the UI."""
def add(a: float, b: float) -> float:
    return a + b
def subtract(a: float, b: float) -> float:
    return a - b
def multiply(a: float, b: float) -> float:
    return a * b
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def evaluate_expression(expression: str) -> str:
    """Evaluates a basic math expression string safely."""
    try:
        allowed_chars = set("0123456789+-*/. ")
        if not set(expression).issubset(allowed_chars):
            return "Error"
        result = eval(expression, {"__builtins__": None}, {})
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        return str(round(result, 8))
    except Exception:
        return "Error"
