filename = "D327971_fc1.i"

with open(filename, "r") as f:
    loaded = f.readlines()
    
    for i in loaded:
        if "T01" in i:
            print(i)
        else:
            pass
        
