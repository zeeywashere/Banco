import json

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, valor):
        """Deposita dinheiro na conta."""
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de {valor} realizado. Novo saldo: {self._saldo}")
            self._salvar_conta()
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        """Retira dinheiro da conta."""
        if valor > 0:
            if valor <= self._saldo:
                self._saldo -= valor
                print(f"Saque de {valor} realizado. Novo saldo: {self._saldo}")
                self._salvar_conta()
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Valor inválido para saque.")

    def consultar_saldo(self):
        """Consulta o saldo da conta."""
        return f"Saldo atual: {self._saldo}"

    def _salvar_conta(self):
        """Salva os detalhes da conta em um arquivo JSON."""
        dados_conta = {
            "titular": self._titular,
            "saldo": self._saldo
        }

        with open("conta_bancaria.json", "w") as arquivo:
            json.dump(dados_conta, arquivo, indent=4)


# Exemplo de uso:
if __name__ == "__main__":
    titular = input("Digite o nome do titular da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    
    conta = ContaBancaria(titular, saldo_inicial)

    while True:
        print("\nEscolha uma opção:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Consultar saldo")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            valor_deposito = float(input("Digite o valor a depositar: "))
            conta.depositar(valor_deposito)
        elif opcao == "2":
            valor_saque = float(input("Digite o valor a sacar: "))
            conta.sacar(valor_saque)
        elif opcao == "3":
            print(conta.consultar_saldo())
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")