"""Simple calculator for happiness and sadness expressions."""


def calculate(expression: str) -> int:
    """Calculate score using `+ happiness` and `- sadness` tokens."""
    score = 0
    sign = 1

    for token in expression.split():
        if token == "+":
            sign = 1
        elif token == "-":
            sign = -1
        elif token == "happiness":
            score += sign
        elif token == "sadness":
            score += sign
        else:
            raise ValueError(f"Unsupported token: {token}")

    return score
