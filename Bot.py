
import time
import random
import os
import sys


mapa = [
"###############",
"#        X    #",
"#     #       #",
"#             #",
"###############"
]

class Robo:
    def __init__(self):
     self.x = 1
     self.y = 1
     self.nome = "José"
     self.memoria = []
     self.fome = 0

     self.energia = 100
     self.vida = 100
     self.dinheiro = 0

    def atualizar(self):
     self.fome += 1

     print("Fome:", self.fome)

    def andar(self, direcao):
        self.memoria.append((self.x, self.y))

        novo_x = self.x
        novo_y = self.y

        if direcao == "cima":
            novo_y -= 1

        elif direcao == "baixo":
            novo_y += 1

        elif direcao == "esquerda":
            novo_x -= 1

        elif direcao == "direita":
            novo_x += 1


        if mapa[novo_y][novo_x] != "#":
            self.x = novo_x
            self.y = novo_y


    def ver(self):
        print("Estou em:", self.x, self.y)

    def olhar(self):

     visao = {}

     visao["cima"] = mapa[self.y-1][self.x]
     visao["baixo"] = mapa[self.y+1][self.x]
     visao["esquerda"] = mapa[self.y][self.x-1]
     visao["direita"] = mapa[self.y][self.x+1]

     return visao
     

    valores = {
        "❤️": +10,
        "💵": +50,
        "X":+1000,
    }
     
    def comer(self):

     if mapa[self.y][self.x] == "🍎":
        self.fome = 0
        print("🤖 Comi! Fome zerada!")

     robo.andar(decisao)
     robo.comer()

    def pensar(self):

        movimentos = [
            "cima",
            "baixo",
            "esquerda",
            "direita"
        ]

        melhores = []

        for movimento in movimentos:

            x = self.x
            y = self.y

            if movimento == "cima":
                y -= 1
            elif movimento == "baixo":
                y += 1
            elif movimento == "esquerda":
                x -= 1
            elif movimento == "direita":
                x += 1

            if mapa[y][x] != "#":

             if mapa[self.y][self.x] == "X":
                print("WIN!")
                time.sleep(1)
                print("criado por carnagem(eu)")
                time.sleep(1)
                print("sistema Linux")
                time.sleep(1)
                print("criado em Python")
                time.sleep(1)
                print("demorou 1 semana para criar este bot")
                time.sleep(1)
                print("Obrigado por jogar!")
                sys.exit(0)

                if (x, y) not in self.memoria:
                    melhores.append(movimento)


        if melhores:
            return random.choice(melhores)

        return random.choice(movimentos)
    
robo = Robo()




while True:

    robo.atualizar()

    decisao = robo.pensar()
    robo.andar(decisao)



    print("\nMapa:")

    for y, linha in enumerate(mapa):
        linha_nova = ""

        for x, bloco in enumerate(linha):

            if x == robo.x and y == robo.y:
                linha_nova += "🤖"
            else:
                linha_nova += bloco

        print(linha_nova)

    decisao = robo.pensar()

    print("Pensando:", decisao)

    robo.andar(decisao)

    robo.ver()

    time.sleep(1)
