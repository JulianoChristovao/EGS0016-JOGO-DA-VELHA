import random  # importa a biblioteca para fazer o sorteio da palavra

def sortear_palavra_misteriosa():#função para sortear uma palavra para o jogo
    with open('plv_misteriosa.txt', 'r') as arquivo: #Abre o arquivo plv_misteriosa
        plv_misteriosa = arquivo.read().splitlines()  # Abre o arquivo e lê todas as palavras que estão nele
    return random.choice(plv_misteriosa)  # Sorteia uma das palavras do arquivo

def salvar_partida_parcial(letras_acertadas, tentativas, letras_consumidas):# Função para salvar a partida a cada jogada para o HTML
    with open('partidas.txt', 'w') as arquivo:# Sobescreve o arquivo com os dados atualizados
        arquivo.write(f"Palavra misteriosa: {''.join(letras_acertadas)}\n")#Função join = junta todas as letras que estão em lista e foma a palavra no arquivo
        arquivo.write(f"Letras consumidas: {', '.join(letras_consumidas)}\n")# Esvreve no arquivo
        arquivo.write(f"Tentativas restantes: {tentativas}\n")#Escreve no arquivo
        match tentativas: # Desenha o enforcado conforme for sendo mutilado
            case 0:
                arquivo.write("....___\n")
                arquivo.write("....|.....|\n")
                arquivo.write("...   ....|\n")
                arquivo.write("...   ....|\n")
                arquivo.write("...   ....|\n")
                arquivo.write("..........|\n")
                arquivo.write(".=========\n")
            case 1:
                arquivo.write("....___\n")
                arquivo.write("....|.....|\n")
                arquivo.write("...O....|\n")
                arquivo.write("...   ....|\n")
                arquivo.write("...   ....|\n")
                arquivo.write("..........|\n")
                arquivo.write(".=========\n")
            case 2:
                arquivo.write("....___\n")
                arquivo.write("....|.....|\n")
                arquivo.write("...O....|\n")
                arquivo.write("... | ....|\n")
                arquivo.write("...   ....|\n")
                arquivo.write("..........|\n")
                arquivo.write(".=========\n")
            case 3:
                arquivo.write("....___\n")
                arquivo.write("....|.....|\n")
                arquivo.write("...O....|\n")
                arquivo.write(".../| ....|\n")
                arquivo.write("...   ....|\n")
                arquivo.write("..........|\n")
                arquivo.write(".=========\n")
            case 4:
                arquivo.write("....___\n")
                arquivo.write("....|.....|\n")
                arquivo.write("...O....|\n")
                arquivo.write(".../|\....|\n")
                arquivo.write("...   ....|\n")
                arquivo.write("..........|\n")
                arquivo.write(".=========\n")
            case 5:
                arquivo.write("....___\n")
                arquivo.write("....|.....|\n")
                arquivo.write("...O....|\n")
                arquivo.write(".../|\....|\n")
                arquivo.write(".../  ....|\n")
                arquivo.write("..........|\n")
                arquivo.write(".=========\n")
            case 6:
                arquivo.write("....___\n")
                arquivo.write("....|.....|\n")
                arquivo.write("...O....|\n")
                arquivo.write(".../|\....|\n")
                arquivo.write(".../ \....|\n")
                arquivo.write("..........|\n")
                arquivo.write(".=========\n")


    roda_html() # Chama a funçã para atualizar o html com a ultima jogada

def salvar_partida(resultado, palavra_misteriosa): #Função para salvar a partida apontando o resultado de venceu ou perdeu
    with open('partidas.txt', 'a') as arquivo:#Abre o arquivo partidas.txt
        arquivo.write(f"\nO jogo acabou!!!\n\nA palavra era: {palavra_misteriosa}\n\nVocê {resultado}!!!") # Escreve no arquivo partidas.txt o resultado e revela a palavra misteriosa

def roda_html():#Função para criar o HTML
    with open('partidas.txt', 'r') as arquivo: # Abre o arquivo para ler e imprimir no HTML
        ultimas_partidas = arquivo.read().splitlines() # Função .splitlines() divide o arquivo linha por linha

    with open('IHM.html', 'w') as arquivo: # Abre o arquivo do HTML para escrever "sobrescreve o arquivo a cada chamada da função"
        html = """<!DOCTYPE html>
<html>
<head>
    <title>Jogo da Forca - Versão EGS0016</title>
    <style>
        pre { font-family: Arial, sans-serif; font-size: 14px; }
    </style>
</head>
<body>
    <h4>Escola: Uniasselvi Indaial</h4>
    <h4>Materia: Algoritimos e lógica de Programação</h4>
    <h4>Professor: Rodrigo Michalovski Szatkowski</h4>
    <h4>Nome: Juliano Christovão</h4>
    <h4>Turma: EGS0016 - 2</h4>
    <h4>__________________________________________</h4>
    <h1>Jogo da Forca</h1>
    <h4>__________________________________________</h4>
    <pre>
"""
        for linha in ultimas_partidas: 
            html += f"{linha.strip()}\n" #adiciona o conteúdo formatado da linha (agora sem espaços extras) à variável html | .strip() remove qualquer espaço em branco no início e no final de linha
        html += """</pre> # Fecha a tag pre e 
</body>
</html>"""
        arquivo.write(html) # escreve o HTML

def jogo_principal():#Função principal do jogo.   
    palavra_misteriosa = sortear_palavra_misteriosa().upper()  # Chama a função para selecionar aleatoriamente uma palavra do arquivo
    letras_acertadas = ['_' for letra in palavra_misteriosa]  # Monta as letras da palavra com '_' para ficar oculto
    tentativas = 6  # Define 6 tentativas
    letras_consumidas = set()  # Define conjunto vazio para adicionar as letras utilizadas

    while tentativas > 0 and '_' in letras_acertadas:  # Verifica se ainda existem letras não reveladas na palavra secreta
        print('Palavra:', ' '.join(letras_acertadas))  # Imprime o estado atual da palavra com letras reveladas e ocultas
        print('Chances restantes:', tentativas)# Imprime as chances restantes
        palpite = input('Digite uma letra: ').upper() # Digite um palpite de letra

        if palpite in letras_consumidas: # Se palpite já foi citado anteriormente
            print('Letra já utilizada!')
        else: # Se palpite é novo
            letras_consumidas.add(palpite)  # Adiciona a letra chutada ao conjunto de letras usadas
            if palpite in palavra_misteriosa:  # Verifica se a letra está na palavra secreta
                for i in range(len(palavra_misteriosa)):  # Substitui '_' pela letra correta nos índices correspondentes
                    if palavra_misteriosa[i] == palpite: # quando o loop chegar na posição correta da letra
                        letras_acertadas[i] = palpite # Adiciona a letra na posição que deu match
            else:
                tentativas -= 1  # Decrementa as tentativas em caso de erro
                print('Letra digitada incorreta, digite novamente!')

        salvar_partida_parcial(letras_acertadas, tentativas, letras_consumidas)  # Atualiza o HTML a cada jogada

    if '_' not in letras_acertadas:  # Caso não haja mais letras ocultas, jogador vence
        print('lol, venci!!!')
        resultado = 'Venceu'
    else:
        print('Ah, perdi, era pra ser:', palavra_misteriosa)
        resultado = 'Perdeu'

    return resultado, palavra_misteriosa  # Retorna o resultado e a palavra misteriosa ao final do jogo

def limpar_IHM(): # Função para limpar a IHM para começão um novo jogo
    with open('partidas.txt', 'w') as arquivo:
        arquivo.write("Vamos iniciar a jogada\n")
    roda_html()

# Bloco principal
while True:
    limpar_IHM()
    resultado, palavra_misteriosa = jogo_principal()  # Chama a função principal e armazena o resultado
    salvar_partida(resultado, palavra_misteriosa)  # Salva o resultado da partida
    roda_html()  # Gera o HTML final com o histórico
    print("Fim de jogo")
    jogo = input("Deseja iniciar nova jogada? S ou N:").upper() # Solicita se quer fazer uma nova jogada ou parar
    if jogo == "S":
        continue
    else:
        print("Você saiu do jogo")
        break