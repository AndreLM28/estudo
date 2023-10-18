import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3 # É UMA CONSTANTE

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}" #concatenando a strirg Depósito:R$ com a variável valor formatando em 2 casas. Atribuido tudo isso na variável extrato

        else:
            print("Operação falhou! O valor informado é inválido: ")

    elif opcao == "s":
      valor = float(input("Informe o valor do saque: "))

      excedeu_saldo = valor > saldo

      excedeu_limite = valor > limite

      excedeu_saque = numero_saques >= LIMITE_SAQUE


      if excedeu_saldo:
         print("Operação falhou! Saldo insuficiente.")

      elif excedeu_limite:
         print("Operação falhou! Limite excedido.")
      
      elif excedeu_saque:  
         print("Operação falhou! Excedido o máximo de saque.")

      elif valor > 0:
         saldo -= valor
         extrato= f"Saque: R$ {valor: .2f}"
         numero_saques += 1

      else:
         print("Operação falhou! Valor informado é inválido.")       

    elif opcao == "e":
       # Obtenha a data e hora atuais
       data_hora_atual = datetime.datetime.now()
       # Formate a data e a hora
       data_formatada = data_hora_atual.strftime("%d/%m/%Y")
       hora_formatada = data_hora_atual.strftime("%H:%M:%S")
       print("\n======================= EXTRATO =======================")
       print(f"Extrato bancário em {data_formatada} às {hora_formatada} :\n\n")
       print("Não foram realizadas movimentações." if not extrato else extrato)   
       print(f"\nSaldo: R$ {saldo:.2f}")
       print("========================================================")     

    elif opcao == "q":
       break

    else:
        print("Operação inválida, por favor selecionar novamente a operação desejada.")
