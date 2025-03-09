from random import choice
from game_data import instagram_followers_millions
import art


def has_more_followers(page1, page2):
    """
    :param page1: Primeira página a ser verificada
    :param page2: Segunda página a ser verificada
    :return: True ou False, dependendo da página que contém mais seguidores
    """
    return page1[1] > page2[1]


def get_user_choice():
    """
    :return: 'a' ou 'b', dependendo da página que o usuário escolher
    """
    pick = input("Who has more followers? Type 'A' or 'B':  ").lower()
    while pick not in ('a', 'b'):
        print("\nPlease, choose 'A' or 'B'")
        pick = input("Who has more followers? Type 'A' or 'B':  ").lower()
    return pick


def get_unique_page(dictionary, used_pages):
    """
    :param dictionary: Dicionário com todas as páginas
    :param used_pages: Lista com as páginas que já foram escolhidas
    :return: Uma página aleatória que ainda não tenha sido escolhida
    """
    available_pages = [p for p in dictionary.items() if p not in used_pages]
    return choice(available_pages)


def game(dictionary):
    """
    Higher Lower Game - Adivinhe quem tem mais seguidores
    :param dictionary: Dicionário que contém todas as páginas
    """
    # Seleciona a primeira página aleatória dentro do dicionário instagram_followers_millions e retorna uma tupla
    p1 = choice(list(dictionary.items()))
    score = 0
    # Variável criada para armazenar os resultados selecionados e evitar repetições
    selected_pages = [p1]

    # Enquanto o usuário acertar, o loop abaixo será verdadeiro, a menos que ele acerte todas.
    # Nesse caso, o loop se encerrará e será mostrada uma mensagem informando que o usuário ganhou.
    while True:
        # Seleciona a segunda página aleatória que não tenha sido sorteada ainda.
        p2 = get_unique_page(instagram_followers_millions, selected_pages)
        selected_pages.append(p2)

        #print(selected_pages)

        print(art.logo)

        # Se o score for maior que 0, será exibido na tela
        if score > 0:
            print(f"You're right! Current score: {score}")

        # Exibe as páginas sorteadas para o usuário
        print(f"Compare A: {p1[0]}")
        print(art.vs)
        print(f"Against B: {p2[0]}")

        # Pergunta ao usuário a resposta; se ele digitar errado, a pergunta será feita novamente
        a_or_b = get_user_choice()

        # Verifica se o usuário acertou
        if has_more_followers(p1, p2) and a_or_b == "a" or not has_more_followers(p1, p2) and a_or_b == "b":

            # Se a segunda página for a maior, a variável p1 recebe o valor de p2
            # e a variável p2 recebe um novo valor quando o loop for reiniciado
            if a_or_b == "b":
                p1 = p2
            # Soma ao score do usuário
            score += 1

            # Caso o usuário acerte todas as respostas, o jogo acaba e é exibida uma mensagem informando a vitória
            if len(instagram_followers_millions) == len(selected_pages):
                print(art.logo)
                print(f"Congratulations, You win!")
                print(f"Your score was {score}")
                break

        # Caso o usuário erre, a condição abaixo se torna verdadeira.
        # Será exibida uma mensagem de fim de jogo, juntamente com o score, e o loop será encerrado.
        else:
            print(art.logo)
            if score == 0:
                print("Better luck next time!")
            elif score < 5:
                print(f"Nice try! Your score was {score}.")
            elif score < 10:
                print(f"Great job! You scored {score} points!")
            else:
                print(f"Amazing! You got {score} points!")
            break


while True:
    game(instagram_followers_millions)
    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again != 'y':
        break
