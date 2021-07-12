troco = 57.80
resto = 0
for cedulas in 100,50,20,10,5,2,1,0.50,0.05:
    nota = resto//cedulas  # Atribui as quantidades de notas realizando a divisão inteira com o operador "//"
    resto = troco%cedulas  # Usa-se o operador "%" (módulo da divisão) que retorna o resto da divisão
    troco = resto
    if nota: #  Verifica se nota possui valor acima de 0, nesse caso retorna TRUE e imprime a mensagem
        if cedulas < 2:
             print(f'{int(nota)} moeda(as) de R$ {cedulas:.2f}') 
        else:
            print(f'{int(nota)} nota(as) de R$ {cedulas:.2f}')

