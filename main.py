import art
print(art.logo)
def add(a,b):
  return a+b
def substract(a,b):
  return a-b
def multiply(a,b):
  return a * b
def divide(a,b):
  return a/b
data={}
n1=float(input("What is the First Number? "))
data["n1"]=n1
while 2>1:
  print("+")
  print("-")
  print("*")
  print("/")
  op=input("Pick your operation ")
  n2=float(input("What's your next number? "))
  data["n2"]=n2
  if op=="+":
    res=add(n1,n2)
    data[op]=res
    print(f"{n1} + {n2} = {res}")
  elif op=="-":
    res=substract(n1,n2)
    data[op]=res
    print(f"{n1} - {n2} = {res}")
  elif op=="*":
    res=multiply(n1,n2)
    data[op]=res
    print(f"{n1} * {n2} = {res}")
  elif op=="/":
    res=divide(n1,n2)
    data[op]=res
    print(f"{n1} / {n2} = {res}")
  choice=input(f"Type 'y' to continue calculating with {data[op]}, or type 'n' to start a new Calculator and type 'end' to exit the calculator -").lower()
  if choice=="y":
    n1=data[op]
  elif choice=="n":
    data={}
    n1=int(input("Whats's your first number? "))
  elif choice=="end":
    break
    
