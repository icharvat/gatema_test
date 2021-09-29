
#načtení souboru souřadnic 
filename = "D327971_fc1.i"

with open(filename, "r") as f:
    loaded = f.readlines()
    for i in loaded:
        #rozdělení textu od čísel
        try:
            x, y = i.split("X")[1].split("Y")
            x = float(x)
            try:
                y = float(y)
            except ValueError:
                y = y.split("T")[1]
                y= float(y)
            #přidání hodnoty k Y, pokud je x>50
            if x > 50:
                y = y +10
            x = str(x)
            y = str(y)
            print(x, y)
            #ignorování prvních pár řádků bez souřadnic
        except IndexError:
            pass

