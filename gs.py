from time import sleep
import json
import os

# Função para calcular o tamanho da barra de progresso
def tamProg(titulo='MindWell - Monitoramento de Saúde Mental'):
    return len(titulo) * 3

# Função para imprimir uma linha simples
def linSimples(tam):
    print('-' * tam)

# Função para imprimir uma linha decorativa
def linDetalhe(tam):
    print('-=' * tam)

# Função para imprimir uma mensagem com sublinhado
def subli(frase, variavel):
    linSimples(len(frase + str(variavel)))
    sleep(1)

# Função para mostrar menu de voltar ou sair
def menuSairVoltar():
    sleep(0.4)
    print()
    print(' ' * 5, '~' * 46)
    print(' ' * 10, f'{"[888] Voltar ao Menu Principal":^{35}}')
    print(' ' * 10, f'{"[999] Sair do aplicativo":^{35}}')
    print(' ' * 5, '~' * 46)
    print()

# Função para imprimir mensagem de voltar ao menu
def voltandoMenu(menu):
    sleep(0.7)
    print('\n')
    linSimples(len(f'Voltando ao Menu {menu}...'))
    print(f'Voltando ao Menu {menu}...')
    linSimples(len(f'Voltando ao Menu {menu}...'))
    print()
    sleep(1.3)

# Função para imprimir mensagem de carregamento do menu
def carregandoMenu(menu):
    print('\n')
    linSimples(len(f'Carregando o Menu {menu}...'))
    print(f'Carregando o Menu {menu}...')
    linSimples(len(f'Carregando o Menu {menu}...'))
    print()
    sleep(0.5)

# Função para tratar erros de entrada
def tratarErro(inputTratamento='', tipo=''):
    try:
        if tipo == 'str':
            if not isinstance(inputTratamento, str):
                raise ValueError
        elif tipo == 'int':
            if not inputTratamento.isdigit():
                raise ValueError
            else:
                return int(inputTratamento)
        else:
            raise ValueError

    except Exception:
        print('\n')
        print('\033[31m', f"{'#~~~~~~~~~~~~~~~~~~~# ERRO DE INPUT #~~~~~~~~~~~~~~~~~~~#':^{tamProg()}}")
        print(f"{f'Opção {inputTratamento} inválida. Por favor, tente novamente':^{tamProg()}}", '\033[m')
        sleep(0.7)
        return inputTratamento

# Função para mostrar dicas personalizadas com base na emoção selecionada
def mostrarDicasPersonalizadas(emocional):
    print()
    print(f"{emocional.capitalize()}:\n")

    # Lógica para mostrar dicas com base na emoção selecionada
    if emocional == "1":
        print("Mantenha-se ativo fisicamente, incorporando exercícios regulares à sua rotina.")
        print("Estabeleça metas realistas e celebre suas conquistas, por menores que sejam.")
        print("Mantenha uma dieta equilibrada para sustentar níveis de energia consistentes.")

    # Adicione lógica semelhante para as outras emoções

# Verificar se o arquivo JSON de dados existe
if not os.path.exists("dados_mindwell.json"):
    with open("dados_mindwell.json", "w") as dados_mindwell_json:
        json.dump({}, dados_mindwell_json)

# Carregar dados do arquivo JSON
with open("dados_mindwell.json", "r") as dados_mindwell_json:
    dados_mindwell = json.load(dados_mindwell_json)

# Perguntar se a pessoa deseja fazer o cadastro
cadastro = input('\nVocê é um novo usuário? (Digite "sim" ou "não"): ')
if cadastro.lower() == 'sim':
    nome = input('Digite seu nome: ')
    emocional = input('\nComo você está se sentindo hoje?\n1. Disposto\n2. Bem\n3. Cansado\n4. Ansioso(a)\n5. Triste\n6. Irritado(a)\n\nEscolha o número correspondente: ')
    mostrarDicasPersonalizadas(emocional)

    # Salvar os dados no arquivo JSON
    dados_mindwell[nome] = {
        "Emocional": emocional,
        "UltimaAtividade": "",
        "SugestaoPersonalizada": ""
    }

    with open("dados_mindwell.json", "w") as dados_mindwell_json:
        json.dump(dados_mindwell, dados_mindwell_json)

# Loop principal
ligado = True
while ligado:
    tam_titulo = tamProg()

    print()
    linDetalhe(tam_titulo // 2)
    print(f'\n{"MindWell - Monitoramento de Saúde Mental":^{tam_titulo}}\n')
    linDetalhe(tam_titulo // 2)
    print()

    frase = len('[4] Dicas Personalizadas')
    tam_opcoes = ((tam_titulo - (frase)) // 2)
    print()
    linSimples(tam_titulo)
    print(f'\n{"MENU PRINCIPAL":^{tam_titulo}}\n')
    print(' ' * (tam_opcoes - 4), '-' * (frase + 6))
    print(' ' * (tam_opcoes - 1), '[1] Notificações')
    print(' ' * (tam_opcoes - 1), '[2] Preciso de ajuda')
    print(' ' * (tam_opcoes - 1), '[3] Enviar sugestões')
    print(' ' * (tam_opcoes - 1), '[4] Dicas Personalizadas')
    print(' ' * (tam_opcoes - 4), '-' * (frase + 6))
    print('\n')
    linSimples(tam_titulo)

    menuSairVoltar()

    resp = input('\nSelecione uma opção: ')
    subli('Selecione uma opção: ', resp)

    resp = tratarErro(resp, 'int')

    sleep(1)
    if resp == 1:  # Menu notificações
        print("Implemente a lógica para notificações aqui.")
        voltandoMenu('Principal')

    elif resp == 2:  # Menu ajuda
        print("Implemente a lógica para ajuda aqui.")
        voltandoMenu('Principal')

    elif resp == 3:  # Menu sugestões
        print("Implemente a lógica para enviar sugestões aqui.")
        voltandoMenu('Principal')

    elif resp == 4:  # Menu dicas personalizadas
        print('\n')
        emocional = dados_mindwell.get(nome, {}).get("Emocional", "")
        mostrarDicasPersonalizadas(emocional)
        menuSairVoltar()
        voltandoMenu('Principal')

    elif resp == 888:  # Voltar ao Menu Principal
        voltandoMenu('Principal')

    elif resp == 999:  # Sair do aplicativo
        print("\nAté logo! Obrigado por usar o MindWell.")
        ligado = False

    else:
        print('\nOpção inválida. Por favor, tente novamente.')
        menuSairVoltar()
