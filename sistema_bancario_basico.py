#VARIÁVEIS GLOBAIS
#saldo: armazena o saldo atual do usuário
#transacoes: lista que armazena todas as transações
#saque_diario: conta o número de saques realizados no dia
#max_saques_diários: limite máximo de saques diários
#limite_saque_diário: limite de valor para cada saque

saldo = 0.0
transacoes = []
saques_diarios = 0
MAX_SAQUES_DIARIOS = 3
limite_saque_diario = 500.0

#FUNÇÃO DE DEPÓSITO
#def depositar(valor): define uma função chamada "depositar" que recebe um parâmetro "valor"
#global saldo: permite que a função modifique a função global "saldo"
#if valor > 0: verifica se o valor do depósito é positivo
#saldo += valor adiciona o valor do depósito ao saldo
#transacores.append(f"Depósito: +R${valor:.2f}"): adiciona uma descrição da transição à lista "transacoes". O "f"{valor:.2f}"" formata o valor em float com duas casas decimais
#print(...): Exibe uma mensagem de confimação. Se o valor for inválido (menor ou igual À zero), exibe uma mensagem de erro.
def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        transacoes.append(f"Depósito: +R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")

#FUNÇÃO PARA SAQUE
#global saldo, saques_diarios: permite que a função modifique as variáveis globais 'saldo' e 'saques_diarios'
#if...elif...else: verifica várias condições para validar o saque
# - saques_diarios >=MAX_SAQUES_DIARIOS: verifica se o limmite de saques diários foi atingido
# - valor > 

def sacar(valor):
    global saldos, saques_diarios
    if saques_diarios >= MAX_SAQUES_DIARIOS:
        print("Número máximo de saques diários atingido.")
    elif valor > limite_saque_diario:
        print(f"Valor do saque diário excede o limite de R${limite_saque_diario:.2f} por saque.")
    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor <=0:
        print("Valor de saque inválido.")
    else:
        saldo -= valor
        saques_diarios += 1
        transacoes.append(f"Saque: -R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso")
        
#FUNÇÃO PARA EXTRATO
def extrato():
    print("\nExtrato:")
    if not transacoes:
        print("Não foram realizadas transações.")
    else:
        for transacao in transacoes:
            print(transacao)
    print(f"\nSaldo atual: R${saldo:.2f}")
    print()
    
#FUNÇÃO PARA EXIBIR O MENU E PROCESSAR AS OPERAÇÕES DO USUÁRIO
def menu():
    while True:
        print("\nBem-vindo ao PaulBank! Escolha uma operação:")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            valor = float(input("Digite o valor do depósito: R$"))
            depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: R$"))
            sacar(valor)
        elif opcao == "3":
            extrato()
        elif opcao == "4":
            print("Obrigado por usar o PaulBank, aquele que te fode atrás e te fode na frente. Volte sempre!")
            break
        else:
            print("Opção inválida. Por favor, digite uma opção válida!")
    
    menu()