es=''
limi=500
saldo =0
limitsa = 3
numssaq =0
valt=0
loop=True
while loop:
    i=int(input('escola uma opção \n 1- extrato \n 2- sacar \n 3- depositar \n 4- exit '))
    if(i==1):
       es = f'foram feito um total de {numssaq} saques \n valor total foi de {valt} \n seu salo é de {saldo}'
       print(es) 


    if(i==2):
         
        if(numssaq<3):
            sss=float(input('insira o valor do saque '))
            if(sss<=500):
                numssaq+=1
                saldo=saldo-sss
                valt=valt+sss
                es = f'foram feito um total de {numssaq} saques \n valor total foi de {valt} \n seu salo é de {saldo}'
            else: print('valor invalido')
        if(numssaq>=3): print('limite atingido')
    
    if(i==3):
        dep=float(input('insira o valor de deposito'))
        saldo=saldo+dep

    if(i==4):
        loop = False

    
    