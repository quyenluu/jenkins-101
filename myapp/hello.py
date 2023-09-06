import fire

def hello(name="World"):
  return "Hello, My name is %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
