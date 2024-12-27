
from pilhas import Pilha


p1 = Pilha()
p2 = Pilha()
p3 = Pilha()
p4 = Pilha()
p5 = Pilha()
p6 = Pilha()
p7 = Pilha()
p8 = Pilha()
p9 = Pilha()
pAux = Pilha()

p1.empilha(11)
p1.empilha(11)
p1.empilha(11)
p1.empilha(11)


def Ultimo_elem(P: Pilha):
    pAux = Pilha()
    Aux = int
    topo = P.topo
    Aux = P.topo
    x = int    
    while Aux != 0:
        x = P.desempilha()
        pAux.empilha(x)
        Aux = Aux - 1
    y = P.elemento_do_topo()
    while Aux != topo:
        x= pAux.desempilha()
        P.empilha(x)
        Aux = Aux + 1

    return y

def Verifica_pilha(P_verificar: Pilha):
    if  P_verificar.pilha_vazia(): #Pilha_Vazia -> correto
        return True
    p_Armazenador = Pilha()
    y = int
    num_pilha = int
    num_pilha = Ultimo_elem(P_verificar)
    if P_verificar.pilha_cheia():
        for i in range(0, 4):
            if num_pilha == P_verificar.elemento_do_topo():
                y = P_verificar.desempilha()
                p_Armazenador.empilha(y)
            else: 
                return False
    else:
        return False
    return True

print(Verifica_pilha(p1))