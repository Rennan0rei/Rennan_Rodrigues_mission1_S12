def sair():
    print("Encerrando o programa...")

def menu_principal():
    while True:
        print("\n*Calculadora de Conversão de Unidades*")
        print("1. Conversor de Medidas")
        print("2. Conversor de Temperaturas")
        print("3. Sair")
        opção = input("Digite a opção desejada: ")
        return opção
escolha = menu_principal()
if escolha == "3":
    sair()