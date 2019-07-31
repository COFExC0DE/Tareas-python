import sys
sys.setrecursionlimit(10000)

#     # #   # #  ##### ##### 
#     # #   # #    #     #   
##   ## #   # #    #     #  
# # # # #   # #    #     #   
#  #  # ##### ###  #   #####
def multi(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1+multi(num1, num2-1)
    
##### #   # #       # #### #### ##### ##### ####
  #   ##  #  #     #  #    #  #   #     #   #  #
  #   # # #   #   #   #### ####   #     #   ####
  #   #  ##    # #    #    ##     #     #   ##
##### #   #     #     #### # #    #   ##### # #

def invertir(num):
    if num == 0:
        return ''
    else:
        return int(str(num%10)+str(invertir(num//10)))

#     # #   # #  #####   # ##### #####
#     # #   # #    #     #   #   #
##   ## #   # #    #  ####   #   #  ##
# # # # #   # #    #  #  #   #   #   #
#  #  # ##### ###  #  #### ##### #####
def multdig(num1, num2):
    if num1 == 0:
        return ''
    else:
        multi = (num1%10)*(num2%10)
        if multi > 9:
            pri_numero = multi // 10
            segun_numero = multi%10
            if segun_numero>pri_numero:
                multi = segun_numero
                print(multi)
            else:
                multi =pri_numero
                print(multi)
        
        return int(str(multdig(num1//10,num2//10))+str(multi))
    
##### ##### #####    #
  #   # # #   #     ##
  #   #   #   #    #  #
  #   #   #   #   #####
##### #####   #  #     #

def iota(num):
    i=0
    guar = []
    lista = []
    lista = iota_aux(num,i,guar)
    return lista

def iota_aux(num,i,guar):

    if num == i:
        return[]
    else:
        guar += [i]
        iota_aux(num,i+1,guar)
    return guar

#   # ##### #####   #
##  # # # #   #    # #
# # # #   #   #   #####
#  ## #####   #  #     #

def notas(lista):

    paso1 = paso(lista,0,1,1)
    return paso1
    
def paso(lista,cont,nota,uno):

    if cont == len(lista):
        return 0
    else:
        if lista[cont]>=70:
                
        paso(lista, cont+1,nota,uno)    
    




          
def ultimo_par(lista):
    
    ulti_par = par(lista,0,[])
    return ulti_par
def par(lista,cont,guard):

    if cont ==len(lista):
        return 0
    if ((lista[cont])%2)==0:

        return par(lista,cont+1,lista[cont])















    
