coords = "D327971_fc1.i"
xvalues = []
yvalues = []

with open(coords, "r") as f:
    loaded = f.readlines()
    
    for i in loaded:
        try:
            x, y = i.split("X")[1].split("Y")
            xvalues.append(x)
            yvalues.append(y)
        #přeskočení pár prvních linek, kde nejsou souřadnice
        except IndexError:
            pass

#seřazení hodnot v listech 
xvalues.sort()
yvalues.sort()


#výstup nejnižších/nejvyšších hodnot
print(xvalues[0], "|", xvalues[-1], "|",
 yvalues[0].strip(), "|", yvalues[-1].strip())

