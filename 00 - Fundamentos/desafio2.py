import textwrap


def menu():
    menu = """\n
-----------------   menu -------------------
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair

=> """
return input(textwrap.dedent(menu))

 def depositar(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print('\nDepósito realizado com sucesso!')
        else:
            print("Operação falhou! O valor informado é inválido.")

        return saldo, extrato


def lista_contas(contas):
    for conta in contas:

        linha = f***\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['bo']}
        ***
        print('n ' = 100)
        print(textwrap.dedent(linha))





def main():
LIMITE_SAQUES = 5
AGENCIA = "0001"

saldo = 0
limite = 700
extrato = ""
numero_saques = 0
usuarios = []
contas = []


while True:

    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(saldo,valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saque,
            limite_saque=LIMITE_SAQUES;
        )
def sacar(*, saldo, valor, extrato, limite, numero_saques, limites_saques):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > limite_saques
    
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
             print("\n@@@ Saque realizado com sucesso! @@@")

        else:
            print("\n@@@Operação falhou! O valor informado é inválido. @@@")

        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

def criar_usuário(usuarios):
        cpf = imput("Informe o cpf (somente números): ")
        usuario = filtrar_usuário(cpf, usuários)

        if usuario:
            print("\n@@@ já existe usuário com esse CPF! @@@")
            return
        
        nome = imput("Informe o nome completo: ")
        data_nascimento = imput("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = imput("Informe o endereço (logradouro, nro - bairro - cidade/ sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
        print("@@@ U/suário criado com sucesso! @@@")


def filtrar_usuario(cpf, usuarios):
        usuarios_filtrados = [usuario for usuario in usuario if usuario ["cpf"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None
    
     elif opcao == "Nu":
        criar_usuário(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "lc":
                    

    elif opcao == "q":
        break 

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
