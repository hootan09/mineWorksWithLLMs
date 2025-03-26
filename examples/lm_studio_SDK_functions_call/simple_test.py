import lmstudio as lms
import typing 
import math

model = lms.llm("gemma-3-4b-it")

### response only
# result = model.respond("hello")
# print(result)

### Stream chat
# for fragment in model.respond_stream("What is the meaning of life?"):
#     print(fragment.content, end="", flush=True)
# print() # Advance to a new line at the end of the response

def multiply(a: float, b: float) -> float:
    """Given two numbers a and b. Returns the product of them."""
    return a * b

def add(a: int, b: int) -> int:
    """Given two numbers a and b, returns the sum of them."""
    return a + b

def is_prime(n: int) -> bool:
    """Given a number n, returns True if n is a prime number."""
    if n < 2:
        return False
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt):
        if n % i == 0:
            return False
    return True

# model.act(
#   "What is the result of 2 multiplied by 2?",
#   [multiply],
#   on_message=print,
# )

model.act(
  "Is the result of 12345 + 45668 a prime? Think step by step.",
  [add, is_prime],
  on_message=print,
)