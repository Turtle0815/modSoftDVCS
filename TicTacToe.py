# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:37:51 2023

@author: schla
"""
import random
import time

print ('Dörte Binder')
print ('OSMI Master')
print ('Moderne Softrwareentwicklung Wintersemester 2023/24')
print ('Übung Clean Code')
print()
print ('Tic-Tac-Toe')
print()
print('Die Regeln:')
print ('Tic-Tac-Toe wird von zwei Spielern auf einem 3x3 - Spielfeld gespiel.')
print ('Die Spieler kennzeichnen abwechselnd ein Feld auf dem Spielfeld mit dem Ziel, als erster Drei Felder in einer Reihe, Spalte oder Diagonale zu kennzeichnen.')
print()
print ('Deine Züge werden mit x gekennzeichnet und meine mit o.')
print ('Gib bitte immer das Feld ein, das du belegen möchtest. (z.B. x1)')
print()
input ('Alles klar? Weiter mit "Enter"!')
print()

print('Lass uns spielen!')
spieler_1 = (random.randint(1,2))
print ('Würfeln wir erst einmal aus, wer zuerst am Zug ist. Ich mache das über meinen Zufallsgenerator.')
print() 
time.sleep(3) 
a = 0
while a < 10:
    print ('.', end = '')
    time.sleep(0.3)
    a = a + 1

    
Felder = ['x1', 'x2', 'x3', 'y1', 'y2', 'y3', 'z1', 'z2', 'z3']
Felder_hilf = ['x1', 'x2', 'x3', 'y1', 'y2', 'y3', 'z1', 'z2', 'z3']
Belegung = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',] 
Sieg = [0, 0, 0, 0, 0, 0, 0, 0, 0]
Sieger = 0


print()
print ('Unser Spielfeld:')
print()
print ('     x      y      z')
print()
print ('1  ', (Belegung[0]), '   ', (Belegung[3]), '   ', (Belegung[6]))
print()
print ('2  ', (Belegung[1]), '   ', (Belegung[4]), '   ', (Belegung[7]))
print()
print ('3  ', (Belegung[2]), '   ', (Belegung[5]), '   ', (Belegung[8]))
print()

 
a = 0
while a < 8:                                            # Spielschleife für max. 9-malige Durchlauf (9 Felder auf dem Spielbrett)
    b = len(Felder_hilf)
    while b == len(Felder_hilf):             
        if spieler_1 == 1:
            ZugS = input ('Dein Zug: ')
            dS = 0
            while dS < len(Felder):                     # Festlegung der Kennzeichnung der bespielten Felder
                if Felder[dS] == ZugS:
                    Belegung[dS] = 'x' 
                    Sieg[dS] = 1
                dS = dS + 1
            cS = 0
            while cS < len(Felder_hilf):                # nimmt die bereits gespielten Felder aus dem Spiel
                if ZugS == Felder_hilf[cS]:
                    dS = 0
                    del Felder_hilf[cS]
                cS = cS + 1                  
            print()
            print ('Unser Spielfeld:')
            print()
            print ('    x      y      z')
            print()
            print ('1  ', (Belegung[0]), '   ', (Belegung[3]), '   ', (Belegung[6]))
            print()
            print ('2  ', (Belegung[1]), '   ', (Belegung[4]), '   ', (Belegung[7]))
            print()
            print ('3  ', (Belegung[2]), '   ', (Belegung[5]), '   ', (Belegung[8]))
            print()
            ZugC = random.choice(Felder_hilf)
            dC = 0
            while dC < len(Felder):
                if Felder[dC] == ZugC:
                    Belegung[dC] = 'o'
                    Sieg[dC] = 4
                dC = dC + 1
            print ('Mein Zug:', ZugC)
            cC = 0
            while cC < len(Felder_hilf):
                if ZugC == Felder_hilf[cC]:
                    print (Belegung)
                    del Felder_hilf[cC]
                cC = cC + 1                   
            print()
            print ('Unser Spielfeld:')
            print()
            print ('    x      y      z')
            print()
            print ('1  ', (Belegung[0]), '   ', (Belegung[3]), '   ', (Belegung[6]))
            print()
            print ('2  ', (Belegung[1]), '   ', (Belegung[4]), '   ', (Belegung[7]))
            print()
            print ('3  ', (Belegung[2]), '   ', (Belegung[5]), '   ', (Belegung[8]))
            print()
        else:
            ZugC = random.choice(Felder_hilf)
            dC = 0
            while dC < len(Felder):
                if Felder[dC] == ZugC:
                    Belegung[dC] = 'o' 
                    Sieg[dC] = 4
                dC = dC + 1
            print ('Mein Zug:', ZugC)                
            cC = 0
            while cC < len(Felder_hilf):
                if ZugC == Felder_hilf[cC]:                                                
                    del Felder_hilf[cC]                   
                cC = cC + 1                     
            print (Belegung)
            print()
            print ('Unser Spielfeld:')
            print()
            print ('    x      y      z')
            print()
            print ('1  ', (Belegung[0]), '   ', (Belegung[3]), '   ', (Belegung[6]))
            print()
            print ('2  ', (Belegung[1]), '   ', (Belegung[4]), '   ', (Belegung[7]))
            print()
            print ('3  ', (Belegung[2]), '   ', (Belegung[5]), '   ', (Belegung[8]))
            print()
            ZugS = input ('Dein Zug: ')
            dS = 0 
            while dS < len(Felder):
                if Felder[dS] == ZugS:
                    Belegung[dS] = 'x' 
                    Sieg[dS] = 1
                dS = dS + 1
            cS = 0
            while cS < len(Felder_hilf):
                if ZugS == Felder_hilf[cS]:                        
                    del Felder_hilf[cS]
                cS = cS + 1                   
            print (Belegung)
            print()
            print ('Unser Spielfeld:')
            print()
            print ('    x      y      z')
            print()
            print ('1  ', (Belegung[0]), '   ', (Belegung[3]), '   ', (Belegung[6]))
            print()
            print ('2  ', (Belegung[1]), '   ', (Belegung[4]), '   ', (Belegung[7]))
            print()
            print ('3  ', (Belegung[2]), '   ', (Belegung[5]), '   ', (Belegung[8]))
            print()
        if sum(Sieg[0:3]) == 3 or sum(Sieg[3:6]) == 3 or sum(Sieg[6: :]) == 3 or sum(Sieg[0: :4]) == 3 or sum(Sieg[2:8:2]) == 3 or sum(Sieg[0:8:3]) == 3 or sum(Sieg[1:8:3]) == 3 or sum(Sieg[2: :3]) == 3:
            Sieger = 1
            a = 8
        if sum(Sieg[0:3]) == 12 or sum(Sieg[3:6]) == 12 or sum(Sieg[6: :]) == 12 or sum(Sieg[0: :4]) == 12 or sum(Sieg[2:8:2]) == 12 or sum(Sieg[0:8:3]) == 12 or sum(Sieg[1:8:3]) == 12 or sum(Sieg[2: :3]) == 12:
            Sieger = 2
            a = 8
        if Sieger == 1:
                print ('Herzlichen Glückwunsch. Du hast gewonnen.')
        else:
            if Sieger == 2:
                print ('Ich habe gewonnen. Danke für das nette Spiel.')
    a = a + 1
    if a == 8:
        print ('Unentschieden. Danke für das nette Spiel.')


    
        
        
        
    
        