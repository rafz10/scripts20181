'''
​Crie uma função que recebe como parâmetro uma string e
imprima a quantidade de consoantes e de vogais da string.
'''
def cont_vogais_consoantes (palavra):
    vogais=0
    consoantes=0
    for char in palavra :
        if char in "aeiouAEIOU":
            vogais +=1
        else:
            consoantes +=1
    print('Quantidade vogais{}'.format(vogais))
    print('Quantidade vogais {}'.format(consoantes))
cont_vogais_consoantes('Python')
