def primo(n):
    '''
    Metodo para checar se é primo
    '''

    for i in range(2,n):
        if n % i == 0 :
            print ('Não é primo')
            break
        else:
            print('È primo')
primo(8)

