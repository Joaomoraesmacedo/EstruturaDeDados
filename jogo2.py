from pilhas import Pilha
from random import randint

def add_pilhas(n:int, lista_total: list[Pilha]):
    "Fazer explicação e testes - João"
    lista_util: list = []
    for i in range(n + 2):
        lista_util.append(lista_total[i])
    return lista_util


def Insere_num(x:int, p:Pilha):
    "blablabla"
    if not p.pilha_cheia():
        p.empilha(x)

def Arruma_pilha(p_inicial: Pilha, p_final:Pilha):
    while not p_inicial.pilha_vazia():
                    y = p_inicial.desempilha()
                    p_final.empilha(y)

def Verifica_x(x: int, Lista:list[Pilha]): #Usar pilha aux: João
    contador = 0 #N 
    for pilha in Lista: #N 
        for j in range(pilha.topo+1): #Usar o arruma pilha 
            if x == pilha.elem[j]:
                contador += 1 # N 
    if contador == (pilha.TamMax + 1): #nn
        return False
    else:
        return True

def Cria_Pilhas_Aleatórias(n: int, pilha:Pilha, Lista: list[Pilha]):
    while not pilha.pilha_cheia():
        x: int = randint(1, n)
        while not Verifica_x(x,Lista) == True:
            x = randint(1, n)
        Insere_num(x, pilha)


def Troca_Pilha(P_Origem: Pilha, P_Destino: Pilha): 
    if not P_Origem.pilha_vazia():
        if not P_Destino.pilha_cheia():   
            if  P_Destino.pilha_vazia() or P_Origem.elemento_do_topo() == P_Destino.elemento_do_topo():    
                x = P_Origem.desempilha()
                P_Destino.empilha(x)
            else:
                print("Troca inválida:O elemento do topo da pilha de origem é diferende do topo da pilha de destino!")
        else:
            print("Troca inválida: A pilha de destino está cheia!")
    else:
        print("Troca inválida: A pilha de origem está vazia!")

def Ultimo_elem(P: Pilha):
    "blabla"
    pAux = Pilha()
    Aux = int
    topo = P.topo
    Aux = P.topo   
    while Aux != 0:
        x = P.desempilha()
        pAux.empilha(x)
        Aux = Aux - 1
    y = P.elemento_do_topo()
    while Aux != topo:
        x = pAux.desempilha()
        P.empilha(x)
        Aux = Aux + 1

    return y

def Verifica_pilha(P_verificar: Pilha):
    "blabla"
    if  P_verificar.pilha_vazia(): #Pilha_Vazia -> correto
        return True
    p_Armazenador = Pilha()
    num_pilha = Ultimo_elem(P_verificar)
    if P_verificar.pilha_cheia():
        for i in range(0, P_verificar.TamMax + 1):
            if num_pilha == P_verificar.elemento_do_topo():
                y = P_verificar.desempilha()
                p_Armazenador.empilha(y)
            else: 
                Arruma_pilha(p_Armazenador, P_verificar)
                return False
        Arruma_pilha(p_Armazenador, P_verificar)
    else:
        return False
    return True

def Verifica_todas_pilhas(Lista: list[Pilha]) -> bool:
    for pilha in Lista:
        if Verifica_pilha(pilha) == False:  # Usa a função existente
            return False
    return True

"""def imprime_lista(Lista: list[Pilha],n):
    num: int = n-1
    aux = Pilha()
    for pilha in Lista:
        while not pilha.pilha_vazia():
            print(pilha.elemento_do_topo())
            x = pilha.desempilha()
            aux.empilha(x)
        print(f"P{n-num}")
        num -= 1
        Arruma_pilha(aux, pilha)"""
        

        
def main():
    p1 = Pilha()
    p2 = Pilha()
    p3 = Pilha()
    p4 = Pilha()
    p5 = Pilha()
    p6 = Pilha()
    p7 = Pilha()
    p8 = Pilha()
    p9 = Pilha()

    Lista_de_pilhas_total: list = [p1, p2, p3, p4, p5, p6, p7, p8, p9] 
    n: int = int(input("Digite o numero de pilhas:  "))
    Lista:list = add_pilhas(n, Lista_de_pilhas_total)
    
    #Gera todas as pilhas com números 
    contador:int = 0
    while contador != n:
        Cria_Pilhas_Aleatórias(n, Lista[contador],Lista)
        contador = contador + 1
    
    #Printa todas as pilhas na lista de pilhas 
    #Printar em vertical: Eduarda 
    """imprime_lista(Lista, n)"""""
    for i, pilha in enumerate(Lista):
        print(f"Pilha {i + 1}: {pilha.elem}")

    #Verifica a quantidade de trocas necessárias para vencer o jogo 
    cont: int = 0
    #BLABLABLA
    while Verifica_todas_pilhas(Lista) == False:
        p_desempilha = int(input("Digite o número da pilha de origem: "))
        p_empilha = int(input("Digite o número da pilha de destino: "))
        Troca_Pilha(Lista[p_desempilha - 1], Lista[p_empilha - 1])
        cont +=1
        for i, pilha in enumerate(Lista): #printar na vertical
            print(f"Pilha {i + 1}: {pilha.elem}")
    
    print("Você venceu o jogo após:", cont, "trocas")

 
if __name__ == '__main__':
    main()