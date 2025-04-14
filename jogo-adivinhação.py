from random import randint

# Variável que armazena quantos acertos o usuário conseguiu
acertos = 0

# Loop de 15 rodadas
for num in range(1, 16):
    print(f'Jogada {num}')
    
    # Gera número aleatório entre 1 e 50
    bot = randint(1, 50)
    
    # Usuário insere um número
    escolha_usuario = int(input('Digite um número entre 1-50: '))
    
    # Verifica se o número está dentro do intervalo permitido
    if escolha_usuario in range(1, 51):
        
        # Compara o número do usuário com o número aleatório
        if escolha_usuario > bot:
            print('Você digitou um número maior que o aleatório.')
            print(f'Número Aleatório: {bot}')
            
        elif escolha_usuario < bot:
            print('Você digitou um número menor que o aleatório.')
            print(f'Número Aleatório: {bot}')
            
        else:
            print('Você acertou!')
            acertos += 1
    else:
        print('Número fora do intervalo permitido. Encerrando o jogo.')
        break

# Exibe o total de acertos
print(f'\nNúmero de acertos: {acertos}')
print('Obrigado por jogar!')
