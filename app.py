from getpass import getpass


opcao = input("Bem-vindo ao sistema de login\nEscolha uma opção\n[1] - Fazer Login\n[2] - Cadastrar novo usuário\nDigite sua opção: ")

#Verificar opcao escolhida
while opcao not in ['1','2']:
        print("\nPor favor, digite entre as opções apresentadas.\n")
        opcao = input("Bem-vindo ao sistema de login\nEscolha uma opção\n[1] - Fazer Login\n[2] - Cadastrar novo usuário\nDigite sua opção: ")
        break


#Usar usuário existente
if opcao == '1':
    user = input("Digite seu usuário: ")
    password = getpass("Digite sua senha: ")

    with open('usuarios.txt', 'r', encoding='latin-1') as file:  # Tenta abrir o arquivo com a codificação latin-1
        # Lê as linhas do arquivo
        lines = file.readlines()
        
        # Remove linhas em branco
        lines = [line.strip() for line in lines if line.strip()]

        # Verifica se há um número par de linhas
        if len(lines) % 2 != 0:
            print("Erro: Arquivo de usuários mal formatado.")
        else:
            # Itera sobre as linhas em pares
            for i in range(0, len(lines), 2):
                stored_user = lines[i].split(": ")[1]
                stored_password = lines[i+1].split(": ")[1]
                if user == stored_user and password == stored_password:
                    print(f"Bem-vindo, {user.capitalize()}, login feito com sucesso!")
                    break
            else:
                print("Usuário ou senha incorretos!")


#Cadastrar novo usuário
if opcao == '2':
    new_user = input("Nome do novo usuário: ")
    new_user_pass = getpass(f"Senha do usuário {new_user.capitalize()}: ")
    
    with open('usuarios.txt', 'a') as file:
            file.write("Usuário: " + new_user + '\n')
            file.write("Senha: " + new_user_pass + '\n' + '\n')
    
    print(f"Usuário {new_user.capitalize()} criado com sucesso!")