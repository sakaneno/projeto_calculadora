from soma import soma
from subtracao import subtracao
from divisao import divisao
from multiplicacao import multiplicacao

print("+++++++++++++++Calculadora Básica++++++++++++++++")

estado = True
historico = []
while estado == True:
    print("+++++++++++Menu+++++++++++")
    print("1) - Soma")
    print("2) - Subtração")
    print("3) - Divisão")
    print("4) - Multiplicação")
    print("5) - Histórico")
    print("6) - Sair")
    opcao = int(input("Digite a opção que deseja: "))

    if opcao == 1:
        a = int(input("Digite o 1º valor: "))
        b = int(input("Digite o 2º valor: "))
        historico.append(f"{a} + {b} = {soma(a,b)}")
        print(f"A soma é: {soma(a,b)}")
    elif opcao == 2:
        a = int(input("Digite o 1º valor: "))
        b = int(input("Digite o 2º valor: "))
        historico.append(f"{a} - {b} = {subtracao(a,b)}")
        print(f"A subtração é: {subtracao(a, b)}")
    elif opcao == 3:
        a = int(input("Digite o 1º valor: "))
        b = int(input("Digite o 2º valor: "))
        historico.append(f"{a} ÷ {b} = {divisao(a,b)}")
        print(f"A divisão é: {divisao(a, b)}")
    elif opcao == 4:
        a = int(input("Digite o 1º valor: "))
        b = int(input("Digite o 2º valor: "))
        historico.append(f"{a} x {b} = {multiplicacao(a,b)}")
        print(f"A Multiplicação é: {multiplicacao(a, b)}")
    elif opcao == 5:
        print("+++++++++++Mostrando o Histórico++++++++++++++")
        for i in range(len(historico)):
            print((f"{i + 1}º {historico[i]}"))
    elif opcao == 6:
        print("Vc acabou de sair!")
        estado = False
    else:
        print("Opção inválida!")

print("Fim do programa!")


