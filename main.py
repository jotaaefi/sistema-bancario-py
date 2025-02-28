from datetime import datetime

class Conta:
    def __init__(self, saldo):
        self.saldo = saldo
        self.historico = {}
        self.contagem = 0
        self.data_ultimo_saque = None
        self.LIMITE_SAQUES = 3  
        
    

    def depositar(self, v):
        if v <= 0:
            raise Exception("O valor inválido, digite um valor acima de R$0.00")
        
        self.saldo += v
        data_hora = self.getHoraDeposito()
        self.historico[data_hora] = self.saldo
        
        print(f"Depósito de R$ {v:.2f} realizado com sucesso!")

    def extrato(self):
        if not self.historico:
            print("Nenhuma operação registrada.")
        else:
            for data_hora, saldo in self.historico.items():
                print(f"Data: {data_hora} | Saldo: R$ {saldo:.2f}")

    def sacar(self, valor):
        dataAtual = datetime.now().date()  

        if self.data_ultimo_saque and self.data_ultimo_saque.date() != dataAtual:
            self.contagem = 0  

        if self.contagem < self.LIMITE_SAQUES:
            if valor <= 0:
               print("Não pode sacar um valor menor ou igual a zero")
            if valor > 500:
                print("O limite de saque é R$ 500.")
            if valor > self.saldo:
                raise Exception("Saldo insuficiente.")
            
            self.saldo -= valor
            data_hora = self.getHoraDeposito()
            self.historico[data_hora] = self.saldo  # Registrando o saque no histórico 
            self.data_ultimo_saque = datetime.now()  
            self.contagem += 1  
        
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Você atingiu o limite de 3 saques diários.")

    def getHoraDeposito(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    

minha_conta = Conta(100)

# Menu de opções
menu = """
Escolha uma operação:
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair
> """

while True:
    opcao = input(menu).strip().upper()  # Converte entrada para maiúscula e remove espaços

    if opcao == "D":
        deposito = float(input("Informe o valor do depósito: "))
        minha_conta.depositar(deposito)

    elif opcao == "S":
        saque = float(input("Informe o valor do saque: "))
        minha_conta.sacar(saque)  # Corrigido, antes chamava `depositar()`

    elif opcao == "E":
        minha_conta.extrato()

    elif opcao == "Q":
        print("Saindo do sistema. Obrigado!")
        break

    else:
        print("Opção inválida, tente novamente.")
