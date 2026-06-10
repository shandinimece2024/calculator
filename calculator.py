def add(a,b):
    """add two numbers"""
    return a+b
def sub(a,b):
    """subtract two"""
    return a-b
def mul(a,b):
    """multiply two numbers"""
    return a*b
def div(a,b):
    """division  two numbers"""
  if b==0:
    raise ValueError("division by zero")
  return a/b

# test
