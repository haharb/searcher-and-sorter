def splitText(title):
    f = open(title + ".txt", encoding="utf-8")
    #print(f.read())
    weartch = []
    meng = f.read()
    tmp = ""
    for txt in meng:
        if txt == "▪" :
            weartch.append(tmp)
            tmp = ""
        else:
            tmp+= txt
    return weartch

