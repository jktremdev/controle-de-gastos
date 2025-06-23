import os
import json
from calcular import Calculando

class Planejar(Calculando): 
    def planejamento(self):
        print('=== BEM-VINDO AO PLANEJAMENTO DE CONTROLE FINANCEIRO ===\n')

    def criar_banco_de_dados(self):
        data = input("Digite a data (dd/mm/aaaa): ")
        descricao = input("Digite a descrição: ")
        try:
            valor = float(input("Digite o valor: "))
        except ValueError:
            print("Valor inválido.")
            return
        categoria = input("Digite a categoria: ")

        dados = {
            'data': data,
            'descrição': descricao,
            'valor': valor,
            'categoria': categoria
        }

        pasta_name = 'gastos'
        os.makedirs(pasta_name, exist_ok=True)
        caminho_arquivo = os.path.join(pasta_name, 'dados.json')

        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4)

        print("✅ Arquivo JSON criado com sucesso!")

    def visualizar_banco_de_dados(self):
        pasta_name = 'gastos'
        caminho_arquivo = os.path.join(pasta_name, 'dados.json')

        if not os.path.exists(caminho_arquivo):
            print("❌ Nenhum arquivo de dados encontrado. Crie um primeiro.")
            return

        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        print("\n📄 Dados armazenados:")
        print(json.dumps(dados, indent=4, ensure_ascii=False))


# Cria o objeto de Planejar (que já herda de Calculando)
app = Planejar()
app.planejamento()

while True:
    menu = (
        "\nAbaixo, digite o número do que você quer usar:\n"
        "1. Calcular gastos\n"
        "2. Adicionar despesas\n"
        "3. Criar pasta com dados de gastos\n"
        "4. Visualizar dados salvos\n"
    )
    print(menu)
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        print("Você escolheu calcular gastos.")
        app.lancamentolist()
    elif opcao == '2':
        print("Você escolheu adicionar despesas.")
        app.add_despesa()
    elif opcao == '3':
        print("Você escolheu criar pasta com dados de gastos.")
        app.criar_banco_de_dados()
    elif opcao == '4':
        print("Você escolheu visualizar os dados salvos.")
        app.visualizar_banco_de_dados()
        break
    else:
        print("Opção inválida. Por favor, digite um número entre 1 e 4.")
