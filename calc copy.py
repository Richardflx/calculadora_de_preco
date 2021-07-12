print('-'*10,'Realizar pagamento','-'*10)
valor_compra = float(input('Digite o valor total da compra: '))  #  Recebe o valor e converte para número real
valor_pagamento =float(input('Digite o valor total do pagamento: '))  #  Recebe o valor e converte para número real


def CalculaTroco(compra, pagamento):  # Função para calcular o troco
    
    troco = round(pagamento - compra, 2)  # Arredenda o valor do troco com 2 casa decimais

    if compra > pagamento:  # Verifica se o valor da compra é maior que o valor do pagamento
        print('Valor pago insuficiente!!!')

    if compra == pagamento:  # Verifica se o valor da compra é igual ao valor do pagamento
        print('Pagamento concluído, não é necessário troco.')

    elif compra < pagamento:  # Verifica se o valor da compra é menor que o pagamento

        print(f'\nO valor do troco é de: R$ {troco}\n')  # Informa o valor do troco
        
        #  Divide os valores até onde é possível de acordo com os valores das notas do Real

        resto1 = troco%100
        resto2 = 0
        for notas in 50,20,10,5,2,1,0.50,0.05:
            nota = resto2//notas #  Atribui as quantidades de notas realizando a divisão inteira com o operador "//"
            resto2 = resto1%notas # Usa-se o operador "%" (módulo da divisão) que retorna o resto da divisão
            
            if nota: #  Verifica se nota possui valor, nesse caso retorna TRUE e imprime a mensagem
                print(f'{int(nota)} nota(as)/moeda(as) de R$ {str(notas).replace(".", ",")}') 



    else:  # Caso nenhuma das operações acima funcionem, retorna a ensagem de erro
        print('Erro')

#  Chama a função de calcular o troco passando os parâmetros de valor da compra e pagamento

CalculaTroco(valor_compra, valor_pagamento)