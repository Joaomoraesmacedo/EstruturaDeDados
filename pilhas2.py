from random import randint
class Pilha:
    def __init__(self):
        self.TamMax = 3
        self.topo = -1
        self.elem = [""] * (self.TamMax + 1)
    
    def inicializa_pilha(self): #não sei se é necessária
        self.topo = -1

    def pilha_vazia(self):
        return self.topo == -1
    
    def pilha_cheia(self):
        return self.topo == self.TamMax
    
    def empilha(self, valor):
        if not self.pilha_cheia():
            self.topo += 1
            self.elem[self.topo] = valor
        else:
            print("A pilha está cheia!")

    def desempilha(self):
        if not self.pilha_vazia():
            valor = self.elem[self.topo]
            self.topo -= 1
            return valor
        else:
            print("A pilha está vazia!")
            return None
    
    def elemento_do_topo(self):
        if not self.pilha_vazia():
            return self.elem[self.topo]
        else:
            print("A pilha está vazia!")
            return None

p1 = Pilha()
p2 = Pilha()
p3 = Pilha()
p4 = Pilha()
p5 = Pilha()
p6 = Pilha()
p7 = Pilha()
p8 = Pilha()
p9 = Pilha()

Lista_de_pilhas_total = [p1.elem, p2.elem, p3.elem, p4.elem, p5.elem, p6.elem, p7.elem, p8.elem, p9.elem] #Pode usar lista?

def add_pilhas(n, lista_total):
    lista_util = []
    for i in range(n + 2):
        lista_util.append(lista_total[i])
    return lista_util


def Insere_num(x, p:Pilha):
    contador = 0
    if contador != p.TamMax + 1:
        p.empilha(x)
        contador = contador + 1




def Cria_Pilhas_Aleatórias(p1:Pilha, p2:Pilha , p3:Pilha ):

    while not p1.pilha_cheia():
        x = randint(1, 3)
        Insere_num(x, p1)
    while not p2.pilha_cheia():
        y = randint(1, 3)
        Insere_num(x, p1)        



def Troca_Pilha(P_Origem: Pilha, P_Destino: Pilha):
    x = int
    if not P_Origem.pilha_vazia() and not P_Destino.pilha_cheia():   
        if P_Origem.topo == P_Destino:    
            P_Origem.desempilha(x)
            P_Destino.empilha(x)
    else:
        print("Troca inválida !!")

def Verifica_pilha(P_verificada: Pilha):
    if  P_verificada.pilha_vazia():
        return True
    for i in P_verificada.elem: #Fazer com pilha auxiliar dps
        if i != P_verificada.elemento_do_topo():
            return False
    return True 



def main():
    n = int(input("Digite o numero de pilhas:  "))
    print(p1.empilha(4))
    print(add_pilhas(n, Lista_de_pilhas_total))
    





 
if __name__ == '__main__':
    main()

