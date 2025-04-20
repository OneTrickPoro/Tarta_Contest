import pyxel
import random
import time

#num = int(input('Inserire il numero di partecipanti: '))
num = 15

'''
spawno tra 20 e 320 quindi ho 260 pixel da spartire,
con y iniziale 180
'''
x_space = int(300/(num-1))

class Tarta:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y
        self.numX = random.randint(0,3)
        self.numY = random.randint(0,1)
        self.gara = True
        self.w = 8
        self.h = 8

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8*self.numX, 8*self.numY, self.w, self.h, colkey=7)
        
class App:
    def __init__(self):
        pyxel.init(330, 210, 'Volontari cercarsi', fps=60)
        pyxel.load('/assets/res.pyxres')
        self.concorrenti = []
        self.tarta_arrivo = []  
        for i in range(num):
            self.concorrenti.append(Tarta(20+i*x_space, 180))
        self.concorrenti_pos = [0]*num
        self.endgara = False
        self.finito = False
        self.annuncio = False
        self.c1 = 0
        self.c2 = 0
        pyxel.run(self.update, self.draw)   

    def update(self):
        if not self.finito:
            self.c1 +=1
            if self.c1 > num-1:
                self.finito = True
                self.annuncio = True
                time.sleep(1)
        elif self.annuncio:
            self.c2 +=1
            time.sleep(0.4)
            if self.c2 > 4:
                self.finito = True
                self.annuncio = False
                time.sleep(0.2)
        else:
            if all(self.concorrenti_pos) and not self.endgara:
                print("Ordine di arrivo:", self.tarta_arrivo)  
                self.endgara = True
            for i in self.concorrenti:
                if i.y <= 25:
                    i.y = 25
                    if self.concorrenti_pos[self.concorrenti.index(i)] == 0:
                        self.concorrenti_pos[self.concorrenti.index(i)] = 1
                        self.tarta_arrivo.append(self.concorrenti.index(i) + 1)
                else:
                    step = random.randint(2, 30)/50
                    i.y -= step

    def draw(self):
        if self.endgara:
            text_fin = "Il fortunato vincitore e' il numero..."
            text_num = str(self.tarta_arrivo[0])
            pyxel.text(70,100, text_fin,0)
            pyxel.text(130,130, text_num,0)
        elif not  self.finito:
            pyxel.cls(6)
            for i in range(min(self.c1+1, num)):
                self.concorrenti[i].draw()
                pyxel.text(self.concorrenti[i].x, 190, str(i+1) , 0)
            time.sleep(0.3)
        elif self.annuncio:
            pyxel.cls(6)
            for i in range(20):
                pyxel.blt(5+16*i, 35, 0, 32, 0, 16, 8)
            pyxel.line(10, 175, 320 ,175 ,0)
            for i in self.concorrenti:
                i.draw()
                pyxel.text(i.x, 190, str(self.concorrenti.index(i)+1) , 0)
            if self.c2 == 1:
                pyxel.text(160,100, 'READY...',0)
            elif self.c2 == 2:
                pyxel.text(160,100, '..SET...',0)
            elif self.c2 == 3:
                pyxel.text(160,100, '...GO!!!!',0)
        else:
            pyxel.cls(6)
            for i in range(20):
                pyxel.blt(5+16*i, 35, 0, 32, 0, 16, 8)
            pyxel.line(10, 175, 320 ,175 ,0)
            for i in self.concorrenti:
                i.draw()
                pyxel.text(i.x, 190, str(self.concorrenti.index(i)+1) , 0)
                pyxel.text(i.x, 15, str(self.concorrenti.index(i)+1) , 0)

App()
