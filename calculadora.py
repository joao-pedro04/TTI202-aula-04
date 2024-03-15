def adicao(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    if  y == 0:
        print("Erro! Não é possível dividir por zero.")
    else:
        return x / y
    
print("Selecione uma opcao:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicacao")
print("4. Divisao")

escolha = input("Digite a sua escolha (1/2/3/4): ")

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if escolha == '1':
    print(num1, "+", num2, "=", adicao(num1, num2))
elif escolha == '2':
    print(num1, "-", num2, "=", subtracao(num1, num2))
elif escolha == '3':
    print(num1, "*", num2, "=", multiplicacao(num1, num2))
elif escolha == '4':
    print(num1, "/", num2, "=", divisao(num1, num2))
else:
    print("Opcao invalida! Tente novamente.")