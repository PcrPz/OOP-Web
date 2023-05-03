class First():
  def __init__(self):
    print("first")
    super().__init__()

class Second():
  def __init__(self):
    print("second")
    super().__init__()

class Third(Second, First):
  def __init__(self):
    print("third")
    super().__init__()

obj = Third()