def calculator():
    while True:
        print("Selecione a operação.")
        print("1.Adição")
        print("2.Subtração")
        print("3.Multiplicação")
        print("4.Divisão")
        print("5.exponenciação")
        print("6.Resto")
        print("7.Sair")
        
        escolha = input("escolha entre (1/2/3/4/5/6/7): ")

        if escolha in ('1', '2', '3', '4','5','6'):
            num1 = float(input("Escolha o primeiro numero: "))
            num2 = float(input("Escolha o segundo numero: "))

            if escolha == '1':
                print(num1, "+", num2, "=", num1 + num2)

            elif escolha == '2':
                print(num1, "-", num2, "=", num1 - num2)

            elif escolha == '3':
                print(num1, "*", num2, "=", num1 * num2)

            elif escolha == '4':
                print(num1, "/", num2, "=", num1 / num2)
            
            elif escolha == '5':
                print(num1, "**", num2, "=", num1 ** num2)
            
            elif escolha == '6':
                print(num1, "%", num2, "=", num1 % num2)
                
            else:
                break

calculator()