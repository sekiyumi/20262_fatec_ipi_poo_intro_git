import calculadora 

def menu():
    while True:
        print("\n--- MENU DE OPÇÕES ---")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '0':
            print("Saindo do programa... Até mais!")
            break
        elif opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Por favor, digite apenas números válidos.")
                continue

            if opcao == '1':
                resultado = calculadora.soma(num1, num2)
                print(f"Resultado da Soma: {resultado}")
            elif opcao == '2':
                resultado = calculadora.subtracao(num1, num2)
                print(f"Resultado da Subtração: {resultado}")
            elif opcao == '3':
                resultado = calculadora.multiplicacao(num1, num2)
                print(f"Resultado da Multiplicação: {resultado}")
            elif opcao == '4':
                if num2 == 0:
                    print("Erro: Não é possível dividir por zero!")
                else:
                    resultado = calculadora.divisao(num1, num2)
                    print(f"Resultado da Divisão: {resultado}")
        else:
            print("Opção inválida! Tente novamente.")