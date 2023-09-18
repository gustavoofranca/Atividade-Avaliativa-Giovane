Cabeças_Gado = {'Fazenda do Gustavo': 382.644, 'Fazenda do Matheus': 73.733, 'Fazenda do Guga': 200.132}
valores = Cabeças_Gado.values()
print("A maior fazenda tem ", max(valores))

fazendas = {'Fazenda do Gustavo': 'Terra viva', 'Fazenda do Matheus': 'Nascer do Sol', 'Fazenda do Guga': 'Dois limões'}

dicionarioL = input(
    '\nA = Fazenda do Gustavo \nB = Fazenda do Matheus \nC = Fazenda do Guga \nEscolha uma Fazenda: ').lower()

if dicionarioL == 'a':
    print(fazendas['Fazenda do Gustavo'])
elif dicionarioL == 'b':
    print(fazendas['Fazenda do Matheus'])
elif dicionarioL == 'c':
    print(fazendas['Fazenda do Guga'])
else:
    print("Fazenda não encontrada.")

# Lista para armazenar os animais na fazenda usando dicionários
fazenda = []

# Lista para armazenar os funcionários 
funcionarios = []

# Função para adicionar um novo funcionário 
def adicionar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo/função do funcionário: ")
    idade = int(input("Digite a idade do funcionário: "))
    data_contratacao = input("Digite a data de contratação do funcionário (DD/MM/AAAA): ")
    salario = float(input("Digite o salário do funcionário: "))

    funcionario = {
        "nome": nome,
        "cargo": cargo,
        "idade": idade,
        "data_contratacao": data_contratacao,
        "salario": salario
    }

    funcionarios.append(funcionario)
    print(f"Funcionário {nome} adicionado.")

# Função para listar os funcionários 
def listar_funcionarios():
    print("\nLista de Funcionários:")
    for idx, funcionario in enumerate(funcionarios, start=1):
        print(f"{idx}. Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}, Idade: {funcionario['idade']} anos, Data de Contratação: {funcionario['data_contratacao']}, Salário: R${funcionario['salario']}")

# Função para excluir um funcionário 
def excluir_funcionario():
    listar_funcionarios()
    indice = int(input("Digite o número do funcionário que deseja excluir: ")) - 1

    if 0 <= indice < len(funcionarios):
        funcionario_removido = funcionarios.pop(indice)
        print(f"Funcionário {funcionario_removido['nome']} removido.")
    else:
        print("Índice inválido. Nenhum funcionário foi removido.")

# Lista para armazenar as ações realizadas pelos usuários
fila_de_acoes = []

# Função para adicionar um novo animal à fazenda
def adicionar_animal():
    codigo = input("Digite o código do animal: ")

    while True:
        print("Escolha o sexo do animal:")
        print("1. Macho")
        print("2. Fêmea")
        sexo_opcao = input("Digite o número correspondente à opção desejada: ")
        if sexo_opcao == "1":
            sexo = "Macho"
            break
        elif sexo_opcao == "2":
            sexo = "Fêmea"
            break
        else:
            print("Opção inválida. Escolha 1 para Macho ou 2 para Fêmea.")

    nome = input("Digite o nome do animal: ")
    idade = int(input("Digite a idade do animal: "))
    peso = float(input("Digite o peso do animal: "))

    animal = {
        "codigo": codigo,
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "sexo": sexo, 
        "producao_leite": 0,
        "saude": {"vacinas": [], "tratamentos": []},
        "dieta": []
    }

    fazenda.append(animal)
    print(f"Animal {nome} ({sexo}) adicionado à fazenda.")

    # Registra a ação na fila
    fila_de_acoes.append(f"Adicionado animal: {nome} ({sexo})")

# Função para registrar a produção de leite de um animal
def registrar_producao_leite():
    codigo = input("Digite o código do animal: ")
    quantidade = float(input("Digite a quantidade de leite produzida: "))
    for animal in fazenda:
        if animal["codigo"] == codigo:
            if animal["sexo"] == "Macho":
                print("Machos não produzem leite.")
            else:
                animal["producao_leite"] += quantidade
                print(f"Produção de leite registrada para o animal {animal['nome']}.")
                # Registra a ação na fila
                fila_de_acoes.append(f"Registrada produção de leite para animal de código: {codigo}")
            break
    else:
        print("Animal não encontrado.")
        
    # Registra a ação na fila
    fila_de_acoes.append(f"Registrada produção de leite para animal de código: {codigo}")

# Função para registrar vacinação de um animal
def registrar_vacina():
    codigo = input("Digite o código do animal: ")
    vacina = input("Digite o nome da vacina: ")
    data = input("Digite a data da vacinação: ")
    for animal in fazenda:
        if animal["codigo"] == codigo:
            animal["saude"]["vacinas"].append({"vacina": vacina, "data": data})
            print(f"Vacinação registrada para o animal {animal['nome']}.")
            break
    else:
        print("Animal não encontrado.")
        
    # Registra a ação na fila
    fila_de_acoes.append(f"Registrada vacinação para animal de código: {codigo}")

# Função para registrar tratamento de um animal usando uma pilha
def registrar_tratamento():
    codigo = input("Digite o código do animal: ")
    tratamento = input("Digite o nome do tratamento: ")
    data = input("Digite a data do tratamento: ")
    for animal in fazenda:
        if animal["codigo"] == codigo:
            animal["saude"]["tratamentos"].append({"tratamento": tratamento, "data": data})
            print(f"Tratamento registrado para o animal {animal['nome']}.")
            
            # Adicionar o evento a pilha de eventos do animal
            if "tratamentos_recentes" not in animal:
                animal["tratamentos_recentes"] = []  # Cria uma pilha vazia se não existir
            animal["tratamentos_recentes"].append({"tratamento": tratamento, "data": data})
            
            break
    else:
        print("Animal não encontrado.")

    # Registra a ação na fila
    fila_de_acoes.append(f"Registrado tratamento para animal de código: {codigo}")
    
# Função para registrar dieta de um animal
def registrar_dieta():
    codigo = input("Digite o código do animal: ")
    alimento = input("Digite o nome do alimento: ")
    quantidade = float(input("Digite a quantidade de alimento: "))
    for animal in fazenda:
        if animal["codigo"] == codigo:
            animal["dieta"].append({"alimento": alimento, "quantidade": quantidade})
            print(f"Dieta registrada para o animal {animal['nome']}.")
            break
    else:
        print("Animal não encontrado.")

    # Registra a ação na fila
    fila_de_acoes.append(f"Registrada dieta para animal de código: {codigo}")
    
def exibir_animais():
    for animal in fazenda:
        dieta = ", ".join([f"{d['alimento']} {d['quantidade']} Kg" for d in animal['dieta']])
        print(f"Código: {animal['codigo']}, Nome: {animal['nome']}, Idade: {animal['idade']} anos, Peso: {animal['peso']} Kg, Produção de Leite: {animal['producao_leite']} L, Dieta: {dieta}")

# Função para exibir os tratamentos recentes de um animal
def exibir_tratamentos_recentes():
    codigo = input("Digite o código do animal para exibir os tratamentos recentes: ")
    for animal in fazenda:
        if animal["codigo"] == codigo and "tratamentos_recentes" in animal:
            print(f"Tratamentos recentes para o animal {animal['nome']}:")
            for evento in reversed(animal["tratamentos_recentes"]):
                print(f"Tratamento: {evento['tratamento']}, Data: {evento['data']}")
            break
    else:
        print("Animal não encontrado ou sem tratamentos recentes.")

def exibir_vacinas():
    codigo = input("Digite o código do animal para exibir as vacinas: ")
    for animal in fazenda:
        if animal["codigo"] == codigo:
            print(f"Vacinas para o animal {animal['nome']}:")
            for vacina in animal["saude"]["vacinas"]:
                print(f"Vacina: {vacina['vacina']}, Data: {vacina['data']}")
            break
    else:
        print("Animal não encontrado ou sem vacinas registradas.")

# Menu principal
while True:
    print("\nSistema de Gestão de Gado Leiteiro")
    print("1. Adicionar Animal")
    print("2. Registrar Produção de Leite")
    print("3. Registrar Vacina")
    print("4. Registrar Tratamento")
    print("5. Registrar Dieta")
    print("6. Exibir Informações dos Animais")
    print("7. Exibir Tratamentos Recentes")
    print("8. Exibir Vacinas do Animal")
    print("9. Funcionários") 
    print("10. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_animal()
    elif opcao == "2":
        registrar_producao_leite()
    elif opcao == "3":
        registrar_vacina()
    elif opcao == "4":
        registrar_tratamento()
    elif opcao == "5":
        registrar_dieta()
    elif opcao == "6":
        exibir_animais()
    elif opcao == "7":
        exibir_tratamentos_recentes()
    elif opcao == "8":
        exibir_vacinas()
    elif opcao == "9":
        while True:
            print("\nMenu de Funcionários")
            print("1. Adicionar Funcionário")
            print("2. Listar Funcionários")
            print("3. Excluir Funcionário")
            print("4. Voltar ao Menu Principal")
            opcao_funcionarios = input("Escolha uma opção: ")

            if opcao_funcionarios == "1":
                adicionar_funcionario()
            elif opcao_funcionarios == "2":
                listar_funcionarios()
            elif opcao_funcionarios == "3":
                excluir_funcionario()
            elif opcao_funcionarios == "4":
                break
            else:
                print("Opção inválida. Tente novamente.")
    elif opcao == "10":
        break
    else:
        print("Opção inválida. Tente novamente.")

# Exibe a fila de ações após sair do loop principal
print("\nFila de Ações Realizadas:")
for acao in fila_de_acoes:
    print(acao)