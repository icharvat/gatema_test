
#načtení souboru souřadnic 
filename = "D327971_fc1.i"

with open(filename, "r") as f:
    loaded = f.readlines()
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
            #ignorování prvních pár řádků bez souřadnic
        except IndexError:
            pass

