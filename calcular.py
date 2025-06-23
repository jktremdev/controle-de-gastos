class Calculando:
    def __init__(self):
        self.despesas = []
        self.total_entrada = 0
        self.total_saida = 0

    def lancamentolist(self):
        salario = float(input("Salário: "))
        economizar = float(input("Quanto você quer economizar: "))
        gastos = float(input("Gastos fixos: "))
        sobra = salario - economizar - gastos
        print("Vai sobrar para investir: R$", sobra)

    def add_despesa(self):
        while True:
            print("\n=== MENU DE DESPESAS ===")
            print("1. Adicionar despesa")
            print("2. Ver despesas")
            print("3. Apagar todas as despesas")
            print("4. Voltar ao menu principal")

            try:
                escolha = int(input("Escolha uma opção: "))
            except ValueError:
                print("Digite um número válido.")
                continue

            if escolha == 1:
                self.add()
            elif escolha == 2:
                self.lista()
            elif escolha == 3:
                self.despesas.clear()
                print("Todas as despesas foram apagadas.")
            elif escolha == 4:
                break
            else:
                print("Opção inválida.")

    def add(self):
        try:
            valor = float(input("Valor da despesa: R$ "))
        except ValueError:
            print("Valor inválido.")
            return

        categoria = input("Categoria (ex: alimentação, transporte): ")
        descricao = input("Descrição: ")
        data = input("Data (dd/mm/aaaa): ")

        self.despesas.append({
            "valor": valor,
            "categoria": categoria,
            "descricao": descricao,
            "data": data
        })

        print("✅ Despesa adicionada com sucesso!")

    def lista(self):
        if not self.despesas:
            print("Nenhuma despesa cadastrada.")
            return

        print("\n=== LISTA DE DESPESAS ===")
        for i, d in enumerate(self.despesas, start=1):
            print(f"{i}. R$ {d['valor']:.2f} - {d['categoria']} - {d['descricao']} - {d['data']}")
