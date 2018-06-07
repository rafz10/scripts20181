'''
Crie um menu onde o usuário pode escolher quais das funções
do exercício 08 será chamada. O programa deve imprimir o resultado e solicitar
que o usuário escolha uma outra função. O menu deve possuir uma opção de
saída do programa. Ex.
menu = """
======= MENU =======
1) SOMA(A, B)
2) SUBTRACAO(A, B)
3) MULTIPLICACAO(A, B)
4) DIVISAO(A, B)
5) SAIR DO PROGRAMA
"""
'''
def soma (a,b):
    print(a+b)
def subtracao (a,b):
    print(a-b)
def multiplicacao(a,b):
    print(a*b)
def divisao(a,b):
    print(a/b)

opcao = 0
while opcao != 5 :
    print('''======= MENU =======
1) SOMA
2) SUBTRACAO
3) MULTIPLICACAO
4) DIVISAO
5) SAIR DO PROGRAMA''')

    opcao = int(input('Digite o numero da opção : '))
    if opcao == 5 :
        print('Programa finalizado')
        break
    a=float(input('Digite um numero : '))
    b=float(input('Digite outro numero : '))
    if opcao >=1 and opcao <= 5 :
        if opcao == 1:
            soma(a,b)
        elif opcao == 2 :
            subtracao(a,b)
        elif opcao == 3 :
            multiplicacao(a,b)
        elif opção == 4 :
            divisao(a,b)
        else:
            print(" Valor invalido, digite uma opção valida" )





