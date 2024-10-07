### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
tot_quantidade = 52
tot_preco = 1200

if tot_quantidade > 0:
    print("Quantidade válida")
else:
    print("Quantidade inválida. Inseririr um valor positivo.")

if tot_preco > 0:
    print("Preço válido")
else:
    print("Preço inválido. Inseririr um valor positivo.")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
temps = [-1,6,15,25,29,33,38,42]
for temp in temps:
    if temp < 18:
        print(f'temperatura {temp} e classificada como baixa')
    elif temp >= 18 and temp <= 26:
        print(f'temperatura {temp} e classificada normal')
    else:
        print(f'temperatura {temp} e classificada como alta')

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == 'ERROR':
    print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
entrada_idade = 25
entrada_email = 'exemplo@examplo.com'

if entrada_idade >= 18 and entrada_idade <= 65:
    print("Idade do usuário válida")
else:
    print("Usuario nao possui idade recomendada")    

if '@' in entrada_email:
    print("Email OK")
else:
    print("Email invalido")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000:
    if transacao['hora'] < 9 or transacao['hora'] > 18:
        print("Transacao suspeita")
else:
    print("Transacao OK")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
texto = "O rato roeu a roupa do rei de roma."
for caractere in texto:
    if caractere == ',':
        texto = texto.replace(',', '')
    if caractere == '.':
        texto = texto.replace('.', '')
    if  caractere == '!':
        texto = texto.replace('!', '')
    if  caractere == '?':
        texto = texto.replace('?', '')
    if  caractere == ';':
        texto = texto.replace(';', '')
    if  caractere == ':':
        texto = texto.replace(':', '')
print(f'caracteres removidos: {texto}')
separa = texto.split()
contagem = {}

for palavra in separa:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
numeros = [9, 15, 33, 47, 59]
min = min(numeros)
print(min)
max = max(numeros)
print(max)
normal = [(x - min) / (max - min) for x in numeros]

print(normal)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
users = [{"nome": "Joaquim", "idade": 25, "email": "joaquim@joaquim"},
         {"nome": "Rapahael", "idade": None, "email": "rp@raphael"},
         {"nome": "Ana", "idade": 18, "email": "an@ana"}]

idade_vazia = []
for user in users:
    if user["idade"] == None or user["idade"] == "":
        idade_vazia.append(user)
print(idade_vazia)


### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(f'Numeros pares: {pares}')


### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
vendas = [
        {"categoria": "celular", "preco": 1500},
        {"categoria": "notebook", "preco": 3000},
        {"categoria": "tablet", "preco": 2000},
        {"categoria": "celular", "preco": 1500},
        {"categoria": "notebook", "preco": 3000},
        {"categoria": "tablet", "preco": 2000}
]

agg_categoria = {}

for venda in vendas:
    if venda['categoria'] in agg_categoria:
        agg_categoria[venda['categoria']] += venda['preco']
    else:
        agg_categoria[venda['categoria']] = venda['preco']

print(agg_categoria)


### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.