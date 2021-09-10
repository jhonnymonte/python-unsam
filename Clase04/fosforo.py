#autor jonatan montenegro
#mrmontenegro@gmail.com

def propagar(fosforos):
    l=len(fosforos)-1
    for n,i in enumerate(fosforos):
        if i == 1 and n < l:
            if fosforos[n-1]==0:
                fosforos[n-1] = 1
                if fosforos[n-2] ==0:
                    z=n-1
                    for i in fosforos:
                        if fosforos[z] == 0 and z>=0:
                            fosforos[z] = 1
                        
                        z-=1
            if fosforos[n+1] == -1:
                fosforos[n+1] = -1
            if fosforos[n+1] == 0:
                fosforos[n+1] = 1
        return(fosforos)
                

