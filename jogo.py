from pilhas import Pilha
from random import randint

def add_pilhas(n:int, lista_total: list[Pilha]) -> list[Pilha]:
    '''
    Adiciona as pilhas necessárias para o jogo, que estão na *lista_total*, em outra lista, contendo a quantidade de pilhas escolhidas pelo usuário *n*,
    com mais 2 pilhas vazias para a manipulação dos números.

    >>> add_pilhas(4, [p1, p2, p3, p4, p5, p6, p7, p8, p9] )
    [p1, p2, p3, p4, p5, p6]
    '''
    lista_util: list = []
    for i in range(n + 2):
        lista_util.append(lista_total[i])
    return lista_util


def Insere_num(x:int, p:Pilha) -> Pilha:
    '''
    Insere o número no topo *x*, na pilha *p*, se ela não estiver cheia.

    >>> p = [1, 2, '', '']
    >>> Insere_num(3, p)
    >>> p
    [1, 2, 3, '']

    >>> p = [1, 2, 3, 4]
    >>> Insere_num(5, p)
    >>> p
    [1, 2, 3, 4]

    >>> p = ['', '', '', '']
    >>> Insere_num(3, p)
    >>> p
    [3, '', '', '']
    '''
    if not p.pilha_cheia():
        p.empilha(x)

def Arruma_pilha(p_inicial: Pilha, p_final:Pilha) -> Pilha:
    '''
    Transfere todos os elementos da *p_inicial* na *p_final*

    >>> P_final = [1, '', '', '']
    >>> P_inicial = [4, 3, 2, '']
    >>> Arruma_pilha(P_inicial, P_final)
    >>> P_final
    [1, 2, 3, 4]
    >>> P_inicial
    ['', '', '', '']
    '''

    while not p_inicial.pilha_vazia():
                    y = p_inicial.desempilha()
                    p_final.empilha(y)

def Verifica_x(x: int, Lista:list[Pilha]) -> bool: 
    '''
    Retorna False caso já tenha aparecido o número já tenha sido adicionado na lista de pilhas *Lista* o máximo de vezes possíveis 
    >>> p1 = [1, 2, 2, 1]
    >>> p1 = [2, 2, '', '']
    >>> p1 = ['', '', '', '']
    >>> p1 = ['', '', '', '']
    >>> Lista = [p1, p2, p3, p4]
    >>> x = 2
    >>> Verifica_x(x, Lista)
    False
    >>> p1 = [1, 2, 2, 2]
    >>> p1 = [1, 2, '', '']
    >>> p1 = ['', '', '', '']
    >>> p1 = ['', '', '', '']
    >>> Lista = [p1, p2, p3, p4]
    >>> x = 1
    >>> Verifica_x(x, Lista)
    True    
            '''
    contador = 0 
    aux = Pilha()
    for pilha in Lista: 
        while not pilha.pilha_vazia():
            j = pilha.desempilha()
            aux.empilha(j)
            if x == j:
                contador += 1
        Arruma_pilha(aux, pilha)
    if contador == (pilha.TamMax + 1):
        return False
    else:
        return True

def Cria_Pilhas_Aleatórias(n: int, pilha:Pilha, Lista: list[Pilha]) -> Pilha:
    '''
    Cria uma pilha com números aleatórios que estão entre 1 e *n*

    >>> p = ['', '', '', '']
    >>> n = 3
    >>> Lista = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
    >>> Cria_Pilhas_Aleatórias(n, p, Lista)
    >>> p
    [3, 2, 2, 1] 
    '''
    while not pilha.pilha_cheia():
        x: int = randint(1, n)
        while not Verifica_x(x,Lista) == True:
            x = randint(1, n)
        Insere_num(x, pilha)


def Troca_Pilha(P_Origem: Pilha, P_Destino: Pilha) -> Pilha: 
    '''
    Transfere o elemento do topo da *P_Origem* para o topo da *P_Destino*, porém, a *P_Destino* não pode estar cheia,
    a *P_Origem* não pode estar vazia, e o elemento do topo da *P_Origem* deve ser igual ao elemento do topo da *P_Destino*
    >>> p = [2, 3, '', '']
    >>> p1 = [1, 3, '', '']
    >>> Troca_Pilha(p, p1)
    >>> p
    [2, '', '', '']
    >>> p1
    [1, 3, 3, '']
    '''
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

def Ultimo_elem(P: Pilha) -> int:
    '''
    Encontra o último elemento da pilha *P*

    >>> p = [1, 4, 3, 2]
    >>> Ultimo_elem(p)
    1
    '''
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

def Verifica_pilha(P_verificar: Pilha) -> bool:
    '''
    Retorna True se *P_verificar* está cheia com todos os elementos iguais ou se a pilha está vazia, 
    caso contrário retorna False

    >>> p = [3, 3, 3, 3]
    >>> Verifica_pilha(p)
    True
    >>> p1 = ['', '', '', '']
    >>> Verifica_pilha(p1)
    True
    >>> p2 = [3, 3, 3, '']
    >>> Verifica_pilha(p2)
    False
    >>> p3 = [3, 1, 3, 2]
    >>> Verifica_pilha(p3)
    False    
    '''
    if  P_verificar.pilha_vazia(): 
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
    '''
    Retorna True se todas as pilhas da *Lista* está cheia com todos os elementos iguais ou se a pilha está vazia, 
    caso contrário retorna False
    >>> p = [[3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1], ['', '', '', ''], ['', '', '', '']]
    >>> Verifica_todas_pilhas(p)
    True
    >>> p1 = [[3, 3, 2, 3], [2, 2, 1, 2], [1, 1, 3, 1], ['', '', '', ''], ['', '', '', '']]
    >>> Verifica_todas_pilhas(p1)
    False
    >>> p2 = [[3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, ''], [2, '', '', ''], ['', '', '', '']]
    >>> Verifica_todas_pilhas(p1)
    False
    '''
    for pilha in Lista:
        if Verifica_pilha(pilha) == False:  # Usa a função existente
            return False
    return True

def imprime_lista(Lista: list[Pilha],n): #FAZER SE SOBRAR TEMPO e o Franklin quiser MUITOOO
    '''
    Pedir ajuda pro meu amor
    '''
    num: int = n-1
    aux = Pilha()
    for pilha in Lista:
        while not pilha.pilha_vazia():
            print(pilha.elemento_do_topo())
            x = pilha.desempilha()
            aux.empilha(x)
        print(f"P{n-num}")
        num -= 1
        Arruma_pilha(aux, pilha)
        

        
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
    
    #Gera n pilhas com números de 1 até n
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
    #Interface do jogo, interação com o usuário e verificação da conclusão do jogo
    while Verifica_todas_pilhas(Lista) == False:
        p_desempilha = int(input("Digite o número da pilha de origem: "))
        p_empilha = int(input("Digite o número da pilha de destino: "))
        Troca_Pilha(Lista[p_desempilha - 1], Lista[p_empilha - 1])
        cont +=1
        for i, pilha in enumerate(Lista): #printar na vertical
            print(f"Pilha {i + 1}: {pilha.elem}")
    #Mensagem da conclusão do jogo
    print("Você venceu o jogo após:", cont, "trocas")

 
if __name__ == '__main__':
    main()