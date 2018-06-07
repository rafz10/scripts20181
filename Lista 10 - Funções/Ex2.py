'''
Crie um programa que recebe dois valores reais inseridos pelo
usuário e imprima o maior deles.
'''

def valores_reais():
    n1 = float(input('Digite o primeiro valor : '))
    n2 = float(input('Digite o segundo valor : '))
    if n1 > n2 :
        print('O maior valor é {}'.format(n1))
    else:
        print('O maior valor é {}'.format(n2))
valores_reais()
