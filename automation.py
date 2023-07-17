import csv

# Abrir o arquivo CSV para leitura
with open('entrada.csv', 'r') as csv_file:
    # Ler o arquivo CSV
    csv_reader = csv.reader(csv_file, delimiter=';')
    
    # Pular o cabeçalho
    next(csv_reader)
    
    # Criar listas para armazenar os dados transformados
    variaveis = []
    padroes_caracteres = []
    padroes_formato = []
    indice_range = 1
    
    # Iterar sobre as linhas do arquivo CSV
    for row in csv_reader:
        # Extrair os valores da linha
        nome = row[0].strip()
        nu_caracteres = row[1].strip()
        
        # Transformar os nomes das variáveis
        palavras = nome.split(' ')
        nome_variavel = palavras[0].lower() + ''.join(palavra.title() for palavra in palavras[1:])
        
        # Criar a linha no novo formato
        variaveis.append(f'private String {nome_variavel};  // X({nu_caracteres})')

        # Criar o padrão de formato
        padroes_formato.append(f'"{nome_variavel};$-{nu_caracteres}s" // X({nu_caracteres})')
        
        # Criar o padrão de caracteres
        fim_range = indice_range + int(nu_caracteres) - 1
        padroes_caracteres.append(f'new Range({indice_range}, {fim_range});  // {nome_variavel};$-{nu_caracteres}s" X({nu_caracteres})')
        indice_range = fim_range + 1
        

variaveis.append(" ")
padroes_formato.append(" ")
        
# Abrir o arquivo TXT para escrita
with open('seu_arquivo.txt', 'w') as txt_file:
    # Escrever as variáveis no arquivo TXT
    for linha in variaveis:
        txt_file.write(linha + '\n')

    # Escrever os padrões de formato no arquivo TXT
    for linha in padroes_formato:
        txt_file.write(linha + '\n')
    
    # Escrever os padrões de caracteres no arquivo TXT
    for linha in padroes_caracteres:
        txt_file.write(linha + '\n')
