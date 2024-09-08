def calculadora():
    while True:
        # Menu de opções
        print("\nEscolha uma das operações:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        # Leitura da escolha do usuário
        opcao = input("\nDigite o número da operação desejada: ")

        # Verifica se a opção é válida
        if opcao == '0':
            print("Encerrando o programa...")
            break
        elif opcao not in ['1', '2', '3', '4']:
            print("Essa opção não existe. Tente novamente.")
            continue
        
        # Leitura dos números para a operação
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))

        # Executa a operação escolhida
        if opcao == '1':
            resultado = num1 + num2
            print(f"Resultado da soma: {resultado}")
        elif opcao == '2':
            resultado = num1 - num2
            print(f"Resultado da subtração: {resultado}")
        elif opcao == '3':
            resultado = num1 * num2
            print(f"Resultado da multiplicação: {resultado}")
        elif opcao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado da divisão: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        
# Executa a função calculadora
calculadora()
