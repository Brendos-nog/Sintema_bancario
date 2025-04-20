from datetime import datetime

class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.limite_saque = 500
        self.saques_realizados = 0
        self.limite_saques_diarios = 3
        self.limite_transacoes_diarias = 10
        self.transacoes_realizadas = 0
        self.extrato = []

    def depositar(self, valor):
        if self.transacoes_realizadas >= self.limite_transacoes_diarias:
            print("Limite diário de transações atingido.")
            return

        if valor > 0:
            self.saldo += valor
            self.extrato.append(TrazaçoesDiarias("Depósito", valor))
            self.transacoes_realizadas += 1
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.transacoes_realizadas >= self.limite_transacoes_diarias:
            print("Limite diário de transações atingido.")
            return

        if self.saques_realizados >= self.limite_saques_diarios:
            print("Limite diário de saques atingido.")
        elif valor > self.limite_saque:
            print(f"Valor excede o limite de saque diário de R${self.limite_saque:.2f}.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor <= 0:
            print("Valor inválido para saque.")
        else:
            self.saldo -= valor
            self.saques_realizados += 1
            self.transacoes_realizadas += 1
            self.extrato.append(TrazaçoesDiarias("Saque", valor))
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        print("\n--- Extrato ---")
        if not self.extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for operacao in self.extrato:
                print(operacao)
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("----------------\n")


class TrazaçoesDiarias:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.data_hora = datetime.now()

    def __str__(self):
        return f"{self.data_hora.strftime('%d/%m/%Y %H:%M:%S')} - {self.tipo}: R${self.valor:.2f}"


# Exemplo de uso
banco = SistemaBancario()

while True:
    print("\n=== Bem-vindo ao Sistema Bancário ===")
    print("Escolha uma das opções abaixo:")
    print("[1] Depositar Dinheiro")
    print("[2] Sacar Dinheiro")
    print("[3] Ver Extrato")
    print("[4] Sair")
    print("=====================================")
    opcao = input("Digite o número da sua escolha: ")

    if opcao == "1":
        valor = float(input("Digite o valor para depósito: "))
        banco.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor para saque: "))
        banco.sacar(valor)
    elif opcao == "3":
        banco.exibir_extrato()
    elif opcao == "4":
        print("Obrigado por usar o Sistema Bancário. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
