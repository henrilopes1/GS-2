# ... (código anterior)

# Função para mostrar dicas de acordo com o problema escolhido
def mostrarDicasProblema(problema):
    print()
    print(f"{problema.capitalize()}:\n")

    # Lógica para mostrar dicas com base no problema escolhido
    if problema == "1":
        print("Converse com alguém de confiança sobre seus sentimentos.")
        print("Considere procurar a ajuda de um profissional, como um psicólogo.")
        print("Pratique técnicas de relaxamento, como meditação ou respiração profunda.")

    # Adicione lógica semelhante para os outros problemas

# ... (código anterior)

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
        print('\n')
        print("Como posso ajudar você hoje?")
        print("1. Preciso lidar com o estresse.")
        print("2. Estou enfrentando ansiedade.")
        print("3. Estou lidando com a tristeza.")
        print("4. Tenho problemas de relacionamento.")
        print("5. Outro problema.")

        problema_escolhido = input('\nEscolha o número correspondente ao seu problema: ')
        subli('Escolha o número correspondente ao seu problema: ', problema_escolhido)
        problema_escolhido = tratarErro(problema_escolhido, 'int')

        mostrarDicasProblema(str(problema_escolhido))
        menuSairVoltar()
        voltandoMenu('Principal')

    elif resp == 3:  # Menu sugestões
        print('\n')
        titulo_sugestao = input("Digite o título da sugestão: ")
        mensagem_sugestao = input("Digite a mensagem da sugestão: ")

        salvarSugestao(titulo_sugestao, mensagem_sugestao)

        print("Sugestão enviada com sucesso!")
        mostrarSugestoes()
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
