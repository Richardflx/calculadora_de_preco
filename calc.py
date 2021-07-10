valor_compra = float(input('Digite o valor da compra: '))  #  Recebe o valor e converte para número real
valor_pagamento =float(input('Digite o valor pago: '))  #  Recebe o valor e converte para número real

def CalculaTroco(compra, pagamento):  # Função para calcular o troco
    
    troco = round(pagamento - compra, 2)  # Arredenda o valor do troco com 2 casa decimais

    print(f'O valor do troco é de R$: {troco}')  # Informa o valor do troco

    if compra > pagamento:  # Verifica se o valor da compra é maior que o valor do pagamento
        print('Valor pago insuficiente!!!')

    if compra == pagamento:  # Verifica se o valor da compra é igual ao valor do pagamento
        print('Pagamento concluído, não é necessário troco.')

    elif compra < pagamento:  # Verifica se o valor da compra é menor que o pagamento
        
        #  Divide os valores até onde é possível de acordo com os valores das notas do Real
        resto1 = troco % 100  # Usa-se o operador "%" (módulo da divisão) que retorna o resto da divisão
        resto2 = resto1 % 50
        resto3 = resto2 % 20
        resto4 = resto3 % 10
        resto5 = resto4 % 5
        resto6 = resto5 % 2
        resto7 = resto6 % 1
        resto8 = resto7 % 0.50
        
        #  Atribui os valores acima às variáveis realizando a divisão inteira com o operador "//"
        nota100,nota50,nota20,nota10,nota5,nota2,moeda1,moeda050,moeda005 = troco//100,resto1//50,resto2//20,resto3//10,resto4//5,resto5//2,resto6//1,resto7//0.50,resto8//0.05

        #  Informa as quantidades de cada nota para fechar o valor do troco
        print(int(nota100),'Nota(as) de R$ 100,00')
        print(int(nota50),'Nota(as) de R$ 50,00')
        print(int(nota20),'Nota(as) de R$ 20,00')
        print(int(nota10),'Nota(as) de R$ 10,00')
        print(int(nota5),'Nota(as) de R$ 5,00')
        print(int(nota2),'Nota(as) de R$ 2,00')
        print(int(moeda1),'Moeda(as) de R$ 1,00')
        print(int(moeda050),'Moeda(as) de R$ 0,50')
        print(int(moeda005),'Moeda(as) de R$ 0,05')

    else:  # Caso nenhuma das operações acima funcionem, retorna a ensagem de erro
        print('Erro')

#  Chama a função de calcular o troco passando os parâmetros de valor da compra e pagamento
CalculaTroco(valor_compra, valor_pagamento)