# puzzle_generator.py
import random
from typing import Tuple

OPS = {
    'add': ('+', lambda a, b: a + b),
    'sub': ('-', lambda a, b: a - b),
    'mul': ('×', lambda a, b: a * b),
    'div': ('÷', lambda a, b: a // b)  # integer division for kids
}

def generate_puzzle(difficulty: str) -> Tuple[str, int]:
    """
    Returns (question_text, correct_answer)
    difficulty in {'Easy', 'Medium', 'Hard'}
    """
    if difficulty == 'Easy':
        ops = ['add', 'sub']
        a = random.randint(0, 10)
        b = random.randint(0, 10)
    elif difficulty == 'Medium':
        ops = ['add', 'sub', 'mul']
        a = random.randint(5, 20)
        b = random.randint(2, 12)
    elif difficulty == 'Hard':
        ops = ['add', 'sub', 'mul', 'div']
        a = random.randint(10, 50)
        b = random.randint(2, 12)
    else:
        raise ValueError("Unknown difficulty")

    op_key = random.choice(ops)
    symbol, func = OPS[op_key]

    # For division, ensure divisible to keep integers
    if op_key == 'div':
        a = a * b  # make divisible

    question = f"{a} {symbol} {b} = ?"
    answer = func(a, b)
    return question, answer
