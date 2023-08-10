x=True
while(True):
    while(True):
        try:
            nonb=int(input("Antre tab ou bezwen an , ant 0 a 10\n"))
            break
        except ValueError:
            print("Nonb enkorek, eseye anko")
    while(nonb<0 or nonb>10):
        print("Nonb enkorek, eseye anko")
        nonb=int(input("Antre tab ou bezwen an , ant 0 a 10\n"))
    for i in range(0,10):
        print(str(nonb)+ " X "+ str(i)+" = "+str(nonb*i))
    chwa=input("Eske ou vle jenere on lot tab W|N\n")
    if(chwa=="W" or chwa=="w"):
        True
    elif(chwa=="n" or chwa=="N"):
        
        break
    else:
        while (True):
            chwa=input("chwa enkorek, peze 'W' pou kontinye, 'N' pou kite program lan\n")
            if(chwa=="w" or chwa=="W" or chwa=="n" or chwa=="N"):
                break
        if(chwa=="W" or chwa=="w"):
            x=True
        elif(chwa=="n" or chwa=="N"):
            x=False
            break
                

