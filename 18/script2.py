import re

calculations = []
with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        calculations.append(line)

class myMath(int):
    def __mul__(self, b):
        return myMath(int(self) + b)
    def __sub__(self, b):
        return myMath(int(self) * b)

def myEval(expr):
    expr = re.sub(r"(\d+)", r"e(\1)", expr)
    expr = expr.replace("*", "-")
    expr = expr.replace("+", "*")
    return eval(expr, {}, {"e": myMath})

print(sum(myEval(equation) for equation in calculations))