from contas import (Conta,Basedados)

contas = Basedados()

loop=True
x=0

while loop:
    i=int(input("qual opção deseja \n 1-cadastrar conta \n 2-pesquisar conta \n 3-sair "))

    if i==1:
        name=input('insira seu nome ')
        n=int(input('insira um numero '))
        contas.addcontas(Conta(nome=name,numeroc=n,saldo=0))
    elif i==2:
        conta=contas.encontrar(int(input('insira o numero da conta ')))
        a=int(input('para sacar tecle 1\n para depositar tecle 2 \n para consltar conta tecle 3 '))
        if a==1:
            v=float(input('valor do saque '))

            conta.sub(valor=v)
        if a==2:
            v=float(input('valor do deposito '))

            conta.somar(valor=v)
            
        if a==3:
            print(conta.tostring())
    elif i==3:
        loop=False

