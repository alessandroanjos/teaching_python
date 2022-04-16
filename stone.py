
opcoes = {
    1: 'Adicioanar',
    2: 'Atualizar',
    3: 'Sair',
}

def print_menu():
    for key in opcoes.keys():
        print(key, ' -- ', opcoes[key])
    print()
    

if __name__ == "__main__":

    while (True):
        print_menu()
        opcao = int(input("Informe a opcao: "))

        if opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            exit()
        else:
            print("Opcao inválida. Tente outra vez!")

        
