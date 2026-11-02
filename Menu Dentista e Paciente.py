
   # ================= DATA DE HOJE =================
# transforma a data em número

print("Informe a data de hoje")
dia_hoje = int(input("Dia: "))
mes_hoje = int(input("Mês: "))
ano_hoje = int(input("Ano: "))
hoje = ano_hoje * 10000 + mes_hoje * 100 + dia_hoje

# ================= LISTAS =================

pacientes = []
dentistas = [
    ["Dr. Carlos", "CRO-1111", "Ortodontia", 1],
    ["Dra. Marina", "CRO-2222", "Clínico geral", 2],
]
proximo_id = 3

horarios = ["08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00"]

consultas = []
salas = []
vinculos = []

adm_usuario = "ADM"
adm_senha = "1234"

# ================= MENU INICIAL =================

modo = ""
while modo != "0":
    print("\n===== CLÍNICA ODONTOLÓGICA =====")
    print("1 - Sou paciente")
    print("2 - Sou ADM")
    print("0 - Sair")
    modo = input("Escolha: ")

    # ================= Parte do PACIENTE =================
    if modo == "1":
        cpf = input("Digite seu CPF: ")
        logado = -1

        for i in range(len(pacientes)):
            if pacientes[i][1] == cpf:
                logado = i

        if logado == -1:
            print("CPF não encontrado. Vamos fazer seu cadastro.")
            nome = input("Nome: ")
            senha = input("Senha: ")
            telefone = input("Telefone: ")
            pacientes.append([nome, cpf, senha, telefone, ""])
            logado = len(pacientes) - 1
            print("Cadastro feito!")
        else:
            senha = input("Senha: ")
            if pacientes[logado][2] != senha:
                print("Senha incorreta.")
                logado = -1

        if logado != -1:
            print("Bem-vindo(a),", pacientes[logado][0])
            opcao = ""
            while opcao != "0":
                print("\n--- MENU DO PACIENTE ---")
                print("1 - Ver dentistas")
                print("2 - Agendar consulta")
                print("3 - Minhas consultas")
                print("4 - Cancelar consulta")
                print("0 - Voltar")
                opcao = input("Escolha: ")

                # Ver dentistas
                if opcao == "1":
                    for i in range(len(dentistas)):
                        print(dentistas[i][0], "|", dentistas[i][2])

                # Agendar consulta
                elif opcao == "2":
                    for i in range(len(dentistas)):
                        print(i, "-", dentistas[i][0], "|", dentistas[i][2])
                    escolha = int(input("Número do dentista: "))

                    if escolha < 0 or escolha >= len(dentistas):
                        print("Dentista inválido.")
                    else:
                        cro = dentistas[escolha][1]
                        cpf_paciente = pacientes[logado][1]

                        print("Data da consulta")
                        dia = int(input("Dia: "))
                        mes = int(input("Mês: "))
                        ano = int(input("Ano: "))
                        data_num = ano * 10000 + mes * 100 + dia
                        data_texto = str(dia) + "/" + str(mes) + "/" + str(ano)

                        if dia < 1 or dia > 31 or mes < 1 or mes > 12:
                            print("Data inválida.")
                        elif data_num < hoje:
                            print("Não é possível marcar em data passada.")
                        else:
                            # mostra os horários livres e ocupados
                            for h in range(len(horarios)):
                                ocupado = False
                                for c in range(len(consultas)):
                                    if consultas[c][1] == cro and consultas[c][4] == data_num and consultas[c][3] == horarios[h]:
                                        ocupado = True
                                if ocupado:
                                    print(h, "-", horarios[h], "(ocupado)")
                                else:
                                    print(h, "-", horarios[h])
                            num = int(input("Número do horário: "))

                            if num < 0 or num >= len(horarios):
                                print("Horário inválido.")
                            else:
                                horario = horarios[num]
                                dentista_ocupado = False
                                paciente_ocupado = False

                                for c in range(len(consultas)):
                                    if consultas[c][4] == data_num and consultas[c][3] == horario:
                                        if consultas[c][1] == cro:
                                            dentista_ocupado = True
                                        if consultas[c][0] == cpf_paciente:
                                            paciente_ocupado = True

                                if dentista_ocupado:
                                    print("O dentista já tem consulta nesse horário.")
                                elif paciente_ocupado:
                                    print("Você já tem outra consulta nesse horário.")
                                else:
                                    consultas.append([cpf_paciente, cro, data_texto, horario, data_num])
                                    print("Consulta marcada para", data_texto, "às", horario)

                # Minhas consultas (só as futuras)
                elif opcao == "3":
                    tem = False
                    for c in range(len(consultas)):
                        if consultas[c][0] == pacientes[logado][1] and consultas[c][4] >= hoje:
                            nome_den = ""
                            for d in range(len(dentistas)):
                                if dentistas[d][1] == consultas[c][1]:
                                    nome_den = dentistas[d][0]
                            print(consultas[c][2], "às", consultas[c][3], "com", nome_den)
                            tem = True

                    if not tem:
                        print("Você não tem consultas futuras.")

                # Cancelar consulta
                elif opcao == "4":
                    minhas = []
                    for c in range(len(consultas)):
                        if consultas[c][0] == pacientes[logado][1]:
                            minhas.append(c)
                            print(len(minhas) - 1, "-", consultas[c][2], "às", consultas[c][3])

                    if len(minhas) == 0:
                        print("Você não tem consultas para cancelar.")
                    else:
                        num = int(input("Número da consulta para cancelar: "))
                        if num < 0 or num >= len(minhas):
                            print("Opção inválida.")
                        else:
                            nova = []
                            for c in range(len(consultas)):
                                if c != minhas[num]:
                                    nova.append(consultas[c])
                            consultas = nova
                            print("Consulta cancelada!")

                elif opcao != "0":
                    print("Opção inválida.")

    # ================= MÓDULO ADM =================
    elif modo == "2":
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == adm_usuario and senha == adm_senha:
            print("Bem-vindo(a), administrador!")
            op_adm = ""
            while op_adm != "0":
                print("\n--- AGENDA ---")
                print("1 - Ver todas as consultas")
                print("2 - Filtrar por dentista")
                print("3 - Filtrar por data")
                print("4 - Cancelar consulta")
                print("--- DENTISTAS ---")
                print("5 - Cadastrar dentista")
                print("6 - Listar dentistas")
                print("7 - Buscar dentista")
                print("8 - Atualizar dentista")
                print("9 - Remover dentista")
                print("--- PACIENTES ---")
                print("10 - Listar pacientes")
                print("11 - Buscar paciente")
                print("12 - Atualizar paciente")
                print("13 - Adicionar observação/alergia")
                print("--- CONSULTÓRIOS ---")
                print("14 - Cadastrar sala")
                print("15 - Vincular dentista a sala")
                print("16 - Ver salas")
                print("0 - Voltar")
                op_adm = input("Escolha: ")

                # Ver todas as consultas
                if op_adm == "1":
                    if len(consultas) == 0:
                        print("Nenhuma consulta marcada.")
                    for c in range(len(consultas)):
                        nome_pac = ""
                        for p in range(len(pacientes)):
                            if pacientes[p][1] == consultas[c][0]:
                                nome_pac = pacientes[p][0]

                        nome_den = ""
                        for d in range(len(dentistas)):
                            if dentistas[d][1] == consultas[c][1]:
                                nome_den = dentistas[d][0]

                        print(consultas[c][2], "às", consultas[c][3], "| Paciente:", nome_pac, "| Dentista:", nome_den)

                # Filtrar por dentista
                elif op_adm == "2":
                    for i in range(len(dentistas)):
                        print(i, "-", dentistas[i][0])
                    escolha = int(input("Número do dentista: "))

                    if escolha < 0 or escolha >= len(dentistas):
                        print("Dentista inválido.")
                    else:
                        cro = dentistas[escolha][1]
                        achou = False
                        for c in range(len(consultas)):
                            if consultas[c][1] == cro:
                                nome_pac = ""
                                for p in range(len(pacientes)):
                                    if pacientes[p][1] == consultas[c][0]:
                                        nome_pac = pacientes[p][0]
                                print(consultas[c][2], "às", consultas[c][3], "| Paciente:", nome_pac)
                                achou = True
                        if not achou:
                            print("Nenhuma consulta para esse dentista.")

                # Filtrar por data
                elif op_adm == "3":
                    dia = int(input("Dia: "))
                    mes = int(input("Mês: "))
                    ano = int(input("Ano: "))
                    data_num = ano * 10000 + mes * 100 + dia

                    achou = False
                    for c in range(len(consultas)):
                        if consultas[c][4] == data_num:
                            nome_pac = ""
                            for p in range(len(pacientes)):
                                if pacientes[p][1] == consultas[c][0]:
                                    nome_pac = pacientes[p][0]

                            nome_den = ""
                            for d in range(len(dentistas)):
                                if dentistas[d][1] == consultas[c][1]:
                                    nome_den = dentistas[d][0]

                            print(consultas[c][3], "| Paciente:", nome_pac, "| Dentista:", nome_den)
                            achou = True
                    if not achou:
                        print("Nenhuma consulta nessa data.")

                # Cancelar consulta de qualquer paciente
                elif op_adm == "4":
                    if len(consultas) == 0:
                        print("Nenhuma consulta marcada.")
                    else:
                        for c in range(len(consultas)):
                            print(c, "-", consultas[c][2], "às", consultas[c][3], "| CPF paciente:", consultas[c][0])
                        num = int(input("Número da consulta para cancelar: "))

                        if num < 0 or num >= len(consultas):
                            print("Opção inválida.")
                        else:
                            nova = []
                            for c in range(len(consultas)):
                                if c != num:
                                    nova.append(consultas[c])
                            consultas = nova
                            print("Consulta cancelada!")

                # Cadastrar dentista
                elif op_adm == "5":
                    nome = input("Nome: ")
                    cro = input("CRO: ")
                    esp = input("Especialidade: ")

                    existe = False
                    for i in range(len(dentistas)):
                        if dentistas[i][1] == cro:
                            existe = True

                    if existe:
                        print("CRO já cadastrado!")
                    else:
                        dentistas.append([nome, cro, esp, proximo_id])
                        print("Dentista cadastrado com ID", proximo_id)
                        proximo_id = proximo_id + 1

                # Listar dentistas
                elif op_adm == "6":
                    for i in range(len(dentistas)):
                        print("ID:", dentistas[i][3], "|", dentistas[i][0], "|", dentistas[i][1], "|", dentistas[i][2])

                # Buscar dentista pelo nome
                elif op_adm == "7":
                    busca = input("Nome do dentista: ")
                    achou = False
                    for i in range(len(dentistas)):
                        if dentistas[i][0] == busca:
                            print("ID:", dentistas[i][3], "|", dentistas[i][0], "|", dentistas[i][1], "|", dentistas[i][2])
                            achou = True
                    if not achou:
                        print("Nenhum dentista encontrado.")

                # Atualizar dentista
                elif op_adm == "8":
                    for i in range(len(dentistas)):
                        print(i, "-", dentistas[i][0])
                    escolha = int(input("Número do dentista: "))

                    if escolha < 0 or escolha >= len(dentistas):
                        print("Dentista inválido.")
                    else:
                        novo = input("Novo nome (Enter para manter): ")
                        if novo != "":
                            dentistas[escolha][0] = novo
                        novo = input("Nova especialidade (Enter para manter): ")
                        if novo != "":
                            dentistas[escolha][2] = novo
                        print("Dentista atualizado!")

                # Remover dentista
                elif op_adm == "9":
                    for i in range(len(dentistas)):
                        print(i, "-", dentistas[i][0])
                    escolha = int(input("Número do dentista: "))

                    if escolha < 0 or escolha >= len(dentistas):
                        print("Dentista inválido.")
                    else:
                        cro = dentistas[escolha][1]
                        tem_consulta = False
                        for c in range(len(consultas)):
                            if consultas[c][1] == cro:
                                tem_consulta = True

                        if tem_consulta:
                            print("Esse dentista tem consultas marcadas. Cancele-as antes.")
                        else:
                            # lista nova de dentistas sem o removido
                            nova = []
                            for i in range(len(dentistas)):
                                if i != escolha:
                                    nova.append(dentistas[i])
                            dentistas = nova

                            # tira o dentista das salas também
                            nova = []
                            for v in range(len(vinculos)):
                                if vinculos[v][1] != cro:
                                    nova.append(vinculos[v])
                            vinculos = nova
                            print("Dentista removido!")

                # Listar pacientes
                elif op_adm == "10":
                    if len(pacientes) == 0:
                        print("Nenhum paciente cadastrado.")
                    for i in range(len(pacientes)):
                        print(pacientes[i][0], "| CPF:", pacientes[i][1], "| Tel:", pacientes[i][3], "| Obs:", pacientes[i][4])

                # Buscar paciente por nome ou CPF
                elif op_adm == "11":
                    busca = input("Nome ou CPF: ")
                    achou = False
                    for i in range(len(pacientes)):
                        if pacientes[i][0] == busca or pacientes[i][1] == busca:
                            print(pacientes[i][0], "| CPF:", pacientes[i][1], "| Tel:", pacientes[i][3], "| Obs:", pacientes[i][4])
                            achou = True
                    if not achou:
                        print("Nenhum paciente encontrado.")

                # Atualizar paciente
                elif op_adm == "12":
                    cpf = input("CPF do paciente: ")
                    pos = -1
                    for i in range(len(pacientes)):
                        if pacientes[i][1] == cpf:
                            pos = i

                    if pos == -1:
                        print("Paciente não encontrado.")
                    else:
                        novo = input("Novo nome (Enter para manter): ")
                        if novo != "":
                            pacientes[pos][0] = novo
                        novo = input("Nova senha (Enter para manter): ")
                        if novo != "":
                            pacientes[pos][2] = novo
                        novo = input("Novo telefone (Enter para manter): ")
                        if novo != "":
                            pacientes[pos][3] = novo
                        print("Paciente atualizado!")

                # Adicionar observação/alergia
                elif op_adm == "13":
                    cpf = input("CPF do paciente: ")
                    pos = -1
                    for i in range(len(pacientes)):
                        if pacientes[i][1] == cpf:
                            pos = i

                    if pos == -1:
                        print("Paciente não encontrado.")
                    else:
                        obs = input("Observação/alergia: ")
                        if pacientes[pos][4] == "":
                            pacientes[pos][4] = obs
                        else:
                            pacientes[pos][4] = pacientes[pos][4] + "; " + obs
                        print("Observação adicionada!")

                # Cadastrar sala
                elif op_adm == "14":
                    nome_sala = input("Nome da sala (ex: Sala 1): ")
                    existe = False
                    for s in range(len(salas)):
                        if salas[s] == nome_sala:
                            existe = True

                    if existe:
                        print("Sala já cadastrada!")
                    else:
                        salas.append(nome_sala)
                        print("Sala cadastrada!")

                # Vincular dentista a sala
                elif op_adm == "15":
                    if len(salas) == 0:
                        print("Cadastre uma sala primeiro.")
                    else:
                        for s in range(len(salas)):
                            print(s, "-", salas[s])
                        num_sala = int(input("Número da sala: "))

                        if num_sala < 0 or num_sala >= len(salas):
                            print("Sala inválida.")
                        else:
                            for i in range(len(dentistas)):
                                print(i, "-", dentistas[i][0])
                            escolha = int(input("Número do dentista: "))

                            if escolha < 0 or escolha >= len(dentistas):
                                print("Dentista inválido.")
                            else:
                                ja_tem = False
                                for v in range(len(vinculos)):
                                    if vinculos[v][0] == salas[num_sala] and vinculos[v][1] == dentistas[escolha][1]:
                                        ja_tem = True

                                if ja_tem:
                                    print("Esse dentista já está nessa sala.")
                                else:
                                    vinculos.append([salas[num_sala], dentistas[escolha][1]])
                                    print(dentistas[escolha][0], "vinculado à", salas[num_sala])

                # Ver salas e seus dentistas
                elif op_adm == "16":
                    if len(salas) == 0:
                        print("Nenhuma sala cadastrada.")
                    for s in range(len(salas)):
                        print("\n" + salas[s] + ":")
                        for v in range(len(vinculos)):
                            if vinculos[v][0] == salas[s]:
                                for d in range(len(dentistas)):
                                    if dentistas[d][1] == vinculos[v][1]:
                                        print("  -", dentistas[d][0])

                elif op_adm != "0":
                    print("Opção inválida.")
        else:
            print("Usuário ou senha incorretos.")

    elif modo != "0":
        print("Opção inválida.")

print("Até logo!")