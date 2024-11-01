import argparse

# Definição dos argumentos da linha de comando
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url-file", help="Caminho para o arquivo com as URLs")
parser.add_argument("-p", "--param-file", help="Caminho para o arquivo com os parâmetros")
args = parser.parse_args()

# Leitura dos arquivos de entrada
with open(args.url_file, "r") as url_file:
    urls = url_file.read().splitlines()

with open(args.param_file, "r") as param_file:
    params = param_file.read().splitlines()

# Geração das combinações de URLs e parâmetros
combinations = []
for url in urls:
    for param in params:
        combinations.append(url + "/" + param)

# Impressão dos resultados
for combination in combinations:
    print(combination)
