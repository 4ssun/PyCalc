
print("\n Calculadora Python =)")

def soma(a,b):
    return a + b 
def subtrai(a,b):
    return a - b 
def multiplica(a,b):
    return a * b 
def divide(a,b):
    return a / b 

select_op = input("\n Selecione o número da operação matemática desejada: \n 1- Soma \n 2- Subtração \n 3- Multiplicação \n 4-Divisão")
num1 = float(input(" \n Digite o primeiro número"))
num2 = float(input("\n Digite o segundo número"))

if select_op == '1':
    print(num1 ,"+", num2, "=", (soma(num1,num2)))
if select_op == '2':
    print(num1 ,"-", num2, "=", (subtrai(num1,num2)))
if select_op == '3':
    print(num1 ,"*", num2, "=", (multiplica(num1,num2)))
if select_op == '4':
    print(num1 ,"/", num2, "=", (divide(num1,num2)))