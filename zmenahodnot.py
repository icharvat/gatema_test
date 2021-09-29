
#načtení souboru souřadnic 
filename = "D327971_fc1.i"

with open(filename, "r") as f:
    loaded = f.readlines()
    
    #zapsání upravených souřadnic do jiného souboru
    with open("test3.txt", "w") as g:
            for i in loaded:
                #rozdělení textu od čísel
                try:
                    x, y = i.split("X")[1].split("Y")
                    x = float(x)
                    y = float(y)
                    #přidání hodnoty k Y, pokud je x>50
                    if x > 50:
                        y = y +10
                    x = str(x)
                    y = str(y)
                    g.write(x + y)
                #ignorování prvních pár řádků bez souřadnic
                except IndexError:
                        pass

