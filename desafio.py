BONUS_2024 = 1000

#variaveis de controle loop
nome_valido = False
salario_valido = False
bonus_percent_valido = False



#Tratamento erros nome
#Loop nome
while not nome_valido:
    try:
        nome = input("Digite seu nome: ")
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        if any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)    

#Traramento erros salario
#Loop salario
while not salario_valido:
    try:
        salario = float(input("Qual seu salario? "))
        if salario < 0:
            raise ValueError("Salário inválido. digite apenas valores positivos.")
        else:
            print("Salário válido:", salario)
            salario_valido = True
    except ValueError:
        print("Salário inválido. digite apenas numeros.")


#Tratamento erros bonus
#Loop bonus
while not bonus_percent_valido:
    try:
        bonus_percent = float(input("Qual o valor do bonus recebido? "))
        if bonus_percent < 0:
            print("Bonus inválido. digite apenas valores positivos.")
        else:
            print("Bonus válido:", bonus_percent)
            bonus_percent_valido = True
    except ValueError:
        print("Bonus inválido. digite apenas numeros.")

total_bonus = (salario * bonus_percent) + BONUS_2024
print(f"{nome}, seu bonus sera de: {total_bonus}")