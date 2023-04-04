def moyenne(tab): 

    n = len(tab)
    moy=0.1
    for i in range(n):  
        moy=moy+float(tab[i])
    moy=moy/n
        
    return moy