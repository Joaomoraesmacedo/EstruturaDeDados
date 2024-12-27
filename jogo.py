from pilhas import Pilha
from random import randint

def add_pilhas(n, lista_total):
    lista_util = []
    for i in range(n + 2):
        lista_util.append(lista_total[i])
    return lista_util


def Insere_num(x, p:Pilha):
    if not p.pilha_cheia():
        p.empilha(x)

def Verifica_x(x: int, Lista:list[Pilha]):
    contador = 0
    for i in Lista:
        for j in range(i.topo+1):
            if x == i.elem[j]:
                contador += 1
    if contador == 4:
        return False
    else:
        return True

def Cria_Pilhas_Aleatórias(n: int, pilha:Pilha, Lista: list[Pilha]):
    while not pilha.pilha_cheia():
        x = randint(1, n)
        while not Verifica_x(x,Lista) == True:
            x = randint(1, n)
        Insere_num(x, pilha)


def Troca_Pilha(P_Origem: Pilha, P_Destino: Pilha):
    if not P_Origem.pilha_vazia() and not P_Destino.pilha_cheia():   
        if  P_Destino.pilha_vazia() or P_Origem.elemento_do_topo() == P_Destino.elemento_do_topo():    
            x = P_Origem.desempilha(P_Origem.elem[P_Origem.elemento_do_topo()])
            P_Destino.empilha(x)
        else:
            print("Troca inválida !!")
    else:
        print("Troca inválida !!")

def Verifica_pilha(P_verificada: Pilha):
    if P_verificada.pilha_vazia():
        return True
    elif P_verificada.pilha_cheia():
        elemento = P_verificada.elemento_do_topo()
        for i in range(P_verificada.topo + 1):
            if P_verificada.elem[i] != elemento:
                return False
    else: 
        return False
    return True

def Verifica_todas_pilhas(Lista: list[Pilha]) -> bool:
    for pilha in Lista:
        if Verifica_pilha(pilha) == False:  # Usa a função existente
            return False
    return True



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

    Lista_de_pilhas_total = [p1, p2, p3, p4, p5, p6, p7, p8, p9] #Pode usar lista?
    n = int(input("Digite o numero de pilhas:  "))
    Lista = add_pilhas(n, Lista_de_pilhas_total)
    
    contador = 0
    while contador != n:
        Cria_Pilhas_Aleatórias(n, Lista[contador],Lista)
        contador = contador + 1
   
    for i, pilha in enumerate(Lista):
        print(f"Pilha {i + 1}: {pilha.elem}")
    
    while Verifica_todas_pilhas(Lista) == False:
        p_desempilha = int(input("Digite o número da pilha que deseja desempilhar: "))
        p_empilha = int(input("Digite o número da pilha que deseja empilhar: "))
        Troca_Pilha(Lista[p_desempilha - 1], Lista[p_empilha - 1])
        for i, pilha in enumerate(Lista):
            print(f"Pilha {i + 1}: {pilha.elem}")

 
if __name__ == '__main__':
    main()
