import random

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
def exibir_tabuleiro():
   print("\n")
   i = 0
   for linha in tabuleiro:
       print(" | ".join(linha))
       print("--" * 5) if i < len(tabuleiro)-1 else print("")
       i+=1

def verificar_vitoria():
   
   for i in range(3):
       if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
           return True
       if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
           return True
   
   if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
       return True
   if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
       return True
   return False

def verificar_empate():
   for linha in tabuleiro:
       if " " in linha:
           return False
   return True

def menu():
    print("JOGO DA VELHA\n\n1 jogaodor (1)\n2 Jogadores (2)\nSair (3)")
    try:
        quantidade_jogadores = int(input("Entre com a quantidade de jogadores: "))
        if quantidade_jogadores not in (1, 2, 3):
            print("Entrada inválida. Digite 1, 2 ou 3.")
            return None
        return quantidade_jogadores
    except:
        print("Entrada invalida. Digite apenas números.")
        return None



def jogar():
   jogador_atual = "X"
   jogadores = menu()

   while True:
       
       if jogadores == None:
           continue
       if jogadores == 1:
            exibir_tabuleiro()
            if jogador_atual == "X":
                print("Sua vez!")
                try:
                    linha = int(input("Escolha a linha(1-3): ")) - 1
                    coluna = int(input("Escolha a coluna(1-3): ")) - 1

                    if tabuleiro[linha][coluna] == " ":
                        tabuleiro[linha][coluna] = jogador_atual

                        if verificar_vitoria():
                            exibir_tabuleiro()
                            print(f"Jogador {jogador_atual} Venceu!")
                            break
                        elif verificar_empate():
                            exibir_tabuleiro()
                            print("Empate!")
                            break
                        jogador_atual = "O" if jogador_atual == "X" else "X"

                    else:
                        print("Posição já ocupada. tente novamente.")

                except (IndexError, ValueError):
                    print("Entrada inválida. Escolha números entre 1 e 3.")

            if jogador_atual == "O":
                linha = random.randint(0, 2)
                coluna = random.randint(0, 2)
                while tabuleiro[linha][coluna] != " ":
                    linha = random.randint(0, 2)
                    coluna = random.randint(0, 2)

                print(f"A maquina escolheu a {linha+1}ª linha, {coluna+1}ª coluna")
                tabuleiro[linha][coluna] = jogador_atual
                if verificar_vitoria():
                    exibir_tabuleiro()
                    print(f"Jogador {jogador_atual} Venceu!")
                    break
                elif verificar_empate():
                    exibir_tabuleiro()
                    print("Empate!")
                    break
                jogador_atual = "O" if jogador_atual == "X" else "X"
                           

       if jogadores == 2:
           exibir_tabuleiro()

           print(f"Vez do jogador {jogador_atual}")
           try:
               linha = int(input("Escolha a linha(1-3): ")) - 1
               coluna = int(input("Escolha a coluna(1-3): ")) - 1

               if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = jogador_atual

                    if verificar_vitoria():
                        exibir_tabuleiro()
                        print(f"Jogador {jogador_atual} Venceu!")
                        break
                    elif verificar_empate():
                        exibir_tabuleiro()
                        print("Empate!")
                        break
                    jogador_atual = "O" if jogador_atual == "X" else "X"

               else:
                   print("Posição já ocupada. tente novamente.")

           except (IndexError, ValueError):
               print("Entrada inválida. Escolha números entre 1 e 3.")

           
       

jogar()
