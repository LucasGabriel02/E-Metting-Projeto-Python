def Program2():
    Clientes = ['joao']

    ClientesSenha =['123']

    presencaGestor = []

    Coorden = []

    Lista = []

    cont = 0
    contMenu2 = 0

    # Imprimir Menu

    def Matricula():

        matricula = int(input("Digite sua matricula:"))

    def Menu():

        print(" \n\n------------------ Menu ------------------")

        print(' 1 - Usuário Comum  ')

        print(" 2 - Gestor de Recurso")

        print(' 3 - Alteração do Coordenador ')

        print(' 4 - Login')

        print(' 5 - Coordenador')

        print(' 6 - Confirmação de Reunião ')

        print(' 7 - Exibir Lista Total de Presença')

        print(' 8 - Exibição de Presença do Gestor')

        print(' 9 - Exibição de Presença do Coordenador')


        print(" 0 - Sair do programa\n \n \n")

    # Verificação e adição de item

    # Usuário Comum


    def UsuárioComum():

        print("\n\n Vamos fazer o Cadastro")

        print(" ------------------ ---- ------------------ ")

        NovoCliente = input(" Digite seu NOME: \n")
        Matricula()
        NovoClienteSenha = input(" Digite sua SENHA: \n")

        ClientesSenha.append(NovoClienteSenha)




        # indice = Clientes.index(NovoCliente)

        if (NovoCliente in Clientes):

            print("Esse clinte já esta cadastrado!")

        else:

            Clientes.append(NovoCliente)

            print("Cliente cadastrado!")



    def Login():

        print('Você está Acessando sua Conta \n\n')

        login = input(" Digite seu NOME: \n")
        loginSenha = input(" Digite sua SENHA: \n")

        if (login in Clientes):

            print('Login de Usuário Correto! \n')



        if (loginSenha in ClientesSenha):

            print('Senha Correta! ')


        else:

            print('Senha Incorreta! Digite Novamente')

            ClientesSenha.append(loginSenha)
            loginSenha = input(" Digite sua SENHA: \n")
            print('Senha Correta! ')




    # Cadastro de Presenca da REUNIAO
    def ConfReuniao():

        print('Confirme as Seguintes Normas!\n\n')

        nome = input('Digite Seu NOME: \n')

        tema = input('Tema da Reunião: \n')

        horario = input('Horario da Reunião: \n')

        data = input('Data da Reunião: \n')

        sala = input('Digite o Nome da Sala ou Laboratório: \n')

        if nome in Clientes:
            print('Acesso Liberado com Sucesso!')


        else:
            print('ERRO NO SEU NOME DE ACESSO! Digite Seu Nome de Acordo com Seu CADASTRO! ')

        Lista.append(nome)
        Lista.append(tema)
        Lista.append(horario)
        Lista.append(data)
        Lista.append(sala)



    def Exibir():

        print('Lista da ATA de Reunião\n\n')


        print('Nomes de Usuários Cadastrado')
        for i in (Lista):
            print(i)


        for l in (Clientes):
            print(l)
            print('Estão Sendo Exibida ACIMA os Seguintes Pedidos: TEMA DA REUNIÃO, HORARIO, DATA, SALA E NOME DE USUÁRIO')




    # Gestor Confirma Presenca

    def GestorRecurso():

        print("\n Lista de Usuário Cadastrado:")

        # Clientes.soft()

        print(" ------------------ ---- ------------------ ")

        for j in (Clientes):
            print(j)

            print(" ------------------ ---- ------------------ ")

        print('\n\n Confirmação do Local de Reuniões')


        localReuniao = input("\n Gestor, Você Irá Participar da Reunião? : \n\n")


        print('\n Cadastrar o Novo Espaço de Reuniões:')

        novoDeNovoEspaco = input("\n Gestor Qual Local Você deseja? ")

        presencaGestor.append(localReuniao)

        presencaGestor.append(novoDeNovoEspaco)

        #presencaGestor.append(Lista)


    # Exibicao de Usuario Comum Para O Gestor Visualizar
    def ConfirGestor():

        print('Lista de Presença do Gestor de Recurso\n\n')

        #print('O Gestor Irá Participar das Seguintes Normas')

        for k in (presencaGestor):

            print('O Gestor Irá Participar das Seguintes Normas: Reunião e Espaço Reservado')

            print(k)

            #print('O Gestor Irá Participar das Seguintes Normas')




    #Alteracao do Coordenador se Ele Quer Add Algum Usuario ou Nao

    def CoordenadorAlteracao():

        print(" Editar ATA de Cadastro")

        Usuario = input(" Se Você Deseja Excluir Algum Usuário: DIGITE O NOME: \n")

        if (Usuario in Clientes):


            Clientes.remove(Usuario)

        else:

            print(" Usuário Não Encontrado!")


        print('Quer Fazer um Novo Cadastro ?')

        nome1 = input('Digite SIM ou NAO!\n')

        if (nome1 == 'sim'):

            print('Vamos Adicionar um Novo Usuário')

            novoUsua = input('Digite um Novo Usuário\n')

            Clientes.append(novoUsua)

        else:
            print('Saindo!')


    # Exibicao DeTodos Os Usuario

    def Coordenador():

        print('Atualizações do Seu Critério\n')

        print(" ------------------ ---- ------------------ ")

        for c in (Clientes):
            print("Lista de Usuários Cadastrados:")
            print(c)

            print(" ------------------ ---- ------------------ \n\n")


        print('Presença do Gestor e se Deseja Algum Espaço \n')

        print(" ------------------ ---- ------------------ ")

        for k in (presencaGestor):

            print(k)

            print(" ------------------ ---- ------------------ ")


    # Confirmacao Do Coordenador
    def PresencaCoordenador():

        print('Confirmação do Coordenador')

        nomeCoord = input('Coordenador, Você vai Participar da Reunião? ')

        Coorden.append(nomeCoord)

        for z in (Coorden):
            print(" ------------------ ---- ------------------ \n")

            print('Presença do Coordenador \n')

            print(z)

            print(" ------------------ ---- ------------------ \n")



    while cont != 10:

        Menu()

        cont = int(input(" Digite a Opção Desejada: "))

        if cont == 1:

            UsuárioComum()

        elif cont == 2:

            GestorRecurso()

        elif cont == 3:

            CoordenadorAlteracao()

        elif cont == 4:

            Login()

        elif cont == 5:

            Coordenador()

        elif cont == 6:
            ConfReuniao()

        elif cont == 7:
            Exibir()

        elif cont == 8:
            ConfirGestor()

        elif cont == 9:

            PresencaCoordenador()

        elif cont == 0:
            exit()


Program2()