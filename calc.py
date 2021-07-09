valor_compra = 86.45  # float(input('Digite o valor da compra: '))
valor_pagamento = 100  # float(input('Digite o valor pago: '))

def CalculaTroco(compra, pagamento):
    
    troco = round(pagamento - compra, 2)


    print(f'O valor do troco é de R$: {troco:2}')

    if compra > pagamento:
        print('Valor pago insuficiente!!!')

    elif compra < pagamento:
        
        resto1 = troco % 100
        resto2 = resto1 % 50
        resto3 = resto2 % 20
        resto4 = resto3 % 10
        resto5 = resto4 % 5
        resto6 = resto5 % 2
        resto7 = resto6 % 1
        resto8 = resto7 % 0.50
        
        nota100,nota50,nota20,nota10,nota5,nota2,moeda1,moeda050,moeda005 = troco//100,resto1//50,resto2//20,resto3//10,resto4//5,resto5//2,resto6//1,resto7//0.50,resto8//0.05

        
        print('R$ 100,00:',nota100)
        print('R$ 50,00:',nota50)
        print('R$ 20,00:',nota20)
        print('R$ 10,00:',nota10)
        print('R$ 5,00:',nota5)
        print('R$ 2,00:',nota2)
        print('R$ 1,00:',moeda1)
        print('R$ 0,50:',moeda050)
        print('R$ 0,05:',moeda005)


            
    
    else:
        print('Erro')

CalculaTroco(valor_compra, valor_pagamento)