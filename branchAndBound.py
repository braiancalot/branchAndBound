class No: #criação da classe que será usada para representar cada ponto(x,y) na matriz, e seu custo
    def __init__(self, posicao, pai):
        self.posicao = posicao
        self.pai = pai
        self.g = 0
        self.h = 0
        self.f = 0

def getF(no): # função para permitir a ordenação da lista aberta de acordo com os custo de cada no
    return no.f

def bnb(mat, start, goal): # implementação do branch-and-bound
    numCol = len(mat[0])
    numLin = len(mat)
    listaAberta = []
    listaFechada = []

    noStart = No(start, None)
    noGoal = No(goal, None)

    listaAberta.append(noStart)

    while(len(listaAberta)) > 0:
        
        listaAberta.sort(key=getF)

        noAtual = listaAberta.pop(0)

        listaFechada.append(noAtual)

        if(noAtual.posicao == noGoal.posicao):
            caminho = []
            while(noAtual.posicao != noStart.posicao):
                caminho.append(noAtual.posicao)
                noAtual = noAtual.pai
            caminho.append(noStart.posicao)
            return caminho
        
        x = noAtual.posicao[0]
        y = noAtual.posicao[1]

        proximos = [(x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1)]

        for proximo in proximos:
            if(proximo[0] < 0 or proximo[1] < 0):
               continue

            if(proximo[0] >= numLin or proximo[1] >= numCol):
                continue

            if(mat[proximo[0]][proximo[1]] < 1):
                continue

            noProximo = No(proximo, noAtual)

            if(noProximo in listaFechada):
                continue 

            noProximo.g = calcularDistancia(noProximo, noStart)
            noProximo.h = calcularDistancia(noProximo, noGoal)
            noProximo.f = noProximo.g + noProximo.h + mat[proximo[0]][proximo[1]] + noProximo.pai.f

            if(addListaAberta(listaAberta, listaFechada, noProximo) == True):
                listaAberta.append(noProximo)

    return None

def calcularDistancia(noOrigem, noDestino): # calcular a distancia entre duas celulas, levando em conta a possibilidade da movimentação na diagonal
    distX = abs(noOrigem.posicao[0] - noDestino.posicao[0])
    distY = abs(noOrigem.posicao[1] - noDestino.posicao[1])

    if(distX >= distY):
        return distX
    else:
        return distY

def addListaAberta(listaAberta, listaFechada, noProximo): # verificar se o no atual já se encontra na lista aberta, e caso contrario, adiciona-lo 
    for no in listaAberta:
        if(noProximo.posicao == no.posicao):
            return False
    
    for no in listaFechada:
        if(noProximo.posicao == no.posicao):
            return False
    return True


# definição das matrizes pré-determinadas
mat1 = [[1, 0], 
        [0, 1]]

mat2 = [[1, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 0],
        [1, 1, 1, 0]] 

mat3 = [[1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]]

mat4 = [[0, 1, 0, 0, 0],
        [0, 1, -1, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, -1, -1, 1, 0]]
        
mat5 =  [[0, 5, 0, 0, 0],
         [0, 2, 3, 3, 0],
         [1, 0, 2, 0, 7],
         [0, 4, 0, 6, 0],
         [0, 1, 2, 1, 2],
         [0, 1, 1, 3, 0]]

mat6 =  [[1, 0, 1],
         [0, 4, 0],
         [2, 0, 2],
         [0, 3, 0]]

mat7 =  [[1, 0, 0, 1, 0, 1],
         [1, 1, 0, 0, 0, 0],
         [1, 0, 1, 1, 1, 1],
         [0, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [1, 1, 0, 1, 0, 1],
         [0, 0, 1, 0, 1, 1],
         [0, 1, 0, 0, 1, 1],
         [1, 0, 0, 0, 1, 1]]      

mat8 =  [[1, 0, 0, 4, 0, 1],
         [2, 3, 0, 0, 0, 0],
         [8, 0, 2, 1, 2, -1],
         [0, 6, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, -1],
         [1, 2, 0, 1, 0, 1],
         [0, 0, 1, 0, 1, -1],
         [0, 1, 0, 0, 1, 1],
         [5, 0, 0, 0, 1, -1]]
        

def imprimirMatriz(mat): # imprimir matriz formatada
    lin = len(mat)
    col = len(mat[0])

    for linha in mat:
        for num in linha:
            print(f'{num:>3}', end=" ")
        print()

def verificarEntradas(mat, start, goal): # verificar se as coordenadas do START e GOAL são validas
    lin = len(mat)
    col = len(mat[0])

    if((start[0] < 0 or start[1] < 0) or (goal[0] < 0 or goal[1] < 0)):
        return False

    if((start[0] >= lin or start[1] >= col) or (goal[0] >= lin or goal[1] >= col)):
        return False

    if(mat[start[0]][start[1]] == 0 or mat[goal[0]][goal[1]] == 0):
        return False

    return True

def verificarInput(input): # verificar se o input do usuario é valido
    try:
        int(input)
        return True
    except ValueError:
        return False




################################################################################################################
#-------------------------------------------------MENU---------------------------------------------------------#
################################################################################################################

op = None
while op != 0:
    
    print("\n-----===Menu===-----")
    print("1. Matrizes Exemplo")
    print("2. Criar Matriz")
    print("0. Sair")
    print("--------------------")
    op = input("Digite a opção: ")
    while(verificarInput(op) == False):
        op = input("Opção incorreta, digite novamente: ")
    
    op = int(op)

    if op == 1:        
        print("\nMatriz 1:\n")
        imprimirMatriz(mat1)
        print("\nMatriz 2:\n")
        imprimirMatriz(mat2)
        print("\nMatriz 3:\n")
        imprimirMatriz(mat3)
        print("\nMatriz 4:\n")
        imprimirMatriz(mat4)
        print("\nMatriz 5:\n")
        imprimirMatriz(mat5)
        print("\nMatriz 6:\n")
        imprimirMatriz(mat6)
        print("\nMatriz 7:\n")
        imprimirMatriz(mat7)
        print("\nMatriz 8:\n")
        imprimirMatriz(mat8)

        
        op2 = input("\nDigite o número da matriz que deseja trabalhar: ")
        while(verificarInput(op2) == False or int(op2) < 1 or int(op2) > 8):
            print("Entrada inválida, digite novamente.")
            op2 = input("Digite o número da matriz que deseja trabalhar: ")
        op2 = int(op2)    

        sair = True
        while(sair):
            print("Digite as coordenadas do START e GOAL, lembre-se: Só é possível começar e terminar em uma célula cujo o valor é igual ou maior que 1")
            
            startX = input("\nDigite a linha do START: ")
            while(verificarInput(startX) == False):
                print("Entrada inválida")
                startX = input("Digite a linha do START: ")
            startX = int(startX)

            startY = input("Digite a coluna do START: ")
            while(verificarInput(startY) == False):
                print("Entrada inválida")
                startY = input("Digite a coluna do START: ")
            startY = int(startY)

            goalX = input("Digite a linha do GOAL: ")
            while(verificarInput(goalX) == False):
                print("Entrada inválida")
                goalX = input("Digite a linha do GOAL: ")
            goalX = int(goalX)

            goalY = input("Digite a coluna do GOAL: ")
            while(verificarInput(goalY) == False):
                print("Entrada inválida")
                goalY = input("Digite a coluna do GOAL: ")
            goalY = int(goalY)
            
            start = (startX, startY)
            goal = (goalX, goalY)   
        
            if op2 == 1:
                if(verificarEntradas(mat1, start, goal)):
                    path = bnb(mat1, start, goal)
                    if(path == None):
                        print("\nCaminho não encontrado", end="")
                    else:
                        print("\nMelhor caminho encontrado: \n")
                        for i in range(len(path)-1, -1, -1):
                            print(path[i], end='\t')

                    print()
                else:
                    print("Informações inválidas! Tente novamente.")  

            elif op2 == 2:
                if(verificarEntradas(mat2, start, goal)):
                    path = bnb(mat2, start, goal)
                    if(path == None):
                        print("\nCaminho não encontrado", end="")
                    else:
                        print("\nMelhor caminho encontrado: \n")
                        for i in range(len(path)-1, -1, -1):
                            print(path[i], end='\t')

                    print()
                else:
                    print("Informações inválidas! Tente novamente.")

            elif op2 == 3:
                if(verificarEntradas(mat3, start, goal)):
                    path = bnb(mat3, start, goal)
                    if(path == None):
                        print("\nCaminho não encontrado", end="")
                    else:
                        print("\nMelhor caminho encontrado: \n")
                        for i in range(len(path)-1, -1, -1):
                            print(path[i], end='\t')

                    print()
                else:
                    print("Informações inválidas! Tente novamente.")  

            elif op2 == 4:
                if(verificarEntradas(mat4, start, goal)):
                    path = bnb(mat4, start, goal)
                    if(path == None):
                        print("\nCaminho não encontrado", end="")
                    else:
                        print("\nMelhor caminho encontrado: \n")
                        for i in range(len(path)-1, -1, -1):
                            print(path[i], end='\t')

                    print()
                else:
                    print("Informações inválidas! Tente novamente.")

            elif op2 == 5:
                if(verificarEntradas(mat5, start, goal)):
                    path = bnb(mat5, start, goal)
                    if(path == None):
                        print("\nCaminho não encontrado", end="")
                    else:
                        print("\nMelhor caminho encontrado: \n")
                        for i in range(len(path)-1, -1, -1):
                            print(path[i], end='\t')

                    print()
                else:
                    print("Informações inválidas! Tente novamente.")

            elif op2 == 6:
                if(verificarEntradas(mat6, start, goal)):
                    path = bnb(mat6, start, goal)
                    if(path == None):
                        print("\nCaminho não encontrado", end="")
                    else:
                        print("\nMelhor caminho encontrado: \n")
                        for i in range(len(path)-1, -1, -1):
                            print(path[i], end='\t')

                    print()
                else:
                    print("Informações inválidas! Tente novamente.")

            elif op2 == 7:
                if(verificarEntradas(mat7, start, goal)):
                    path = bnb(mat7, start, goal)
                    if(path == None):
                        print("\nCaminho não encontrado", end="")
                    else:
                        print("\nMelhor caminho encontrado: \n")
                        for i in range(len(path)-1, -1, -1):
                            print(path[i], end='\t')

                    print()
                else:
                    print("Informações inválidas! Tente novamente.")

            elif op2 == 8:
                if(verificarEntradas(mat8, start, goal)):
                    path = bnb(mat8, start, goal)
                    if(path == None):
                        print("\nCaminho não encontrado", end="")
                    else:
                        print("\nMelhor caminho encontrado: \n")
                        for i in range(len(path)-1, -1, -1):
                            print(path[i], end='\t')

                    print()
                else:
                    print("Informações inválidas! Tente novamente.")

            else:
                print("Informações inválidas! Tente novamente.")

            escolha = input("\nDeseja tentar novamente com a mesma matrz? (S/N): ")
            if(escolha == "N" or escolha == "n"):
                sair = False
                break
    
    elif op == 2:
        qtLin = input("Digite a quantidade de linhas: ")
        while(verificarInput(qtLin) == False):
            print("Entrada inválida, digite novamente.")
            qtLin = input("Digite a quantidade de linhas: ")
        qtLin = int(qtLin)
        
        qtCol = input("Digite a quantidade de colunas: ")
        while(verificarInput(qtCol) == False):
            print("Entrada inválida, digite novamente: ")
            qtCol = input("Digite a quantidade de colunas: ")
        qtCol = int(qtCol)  

        print("\nPreencha a matriz: (Lembre-se: 0 ou -1 = não da pra passar por essa célula, 1 ou maior = é possível passar e o custo para passar por essa célula\n")
      
        matCriada = []
        for i in range(qtLin):
            linha = []
            for j in range(qtCol):
                num = input("Digite o elemento[" + str(i) + "][" + str(j) + "]: ")
                while(verificarInput(num) == False):
                    print("Entrada inválida, digite novamente. ")
                    num = input("Digite o elemento[" + str(i) + "][" + str(j) + "]: ")
                num = int(num)
                linha.append(num)
            matCriada.append(linha)

        print("\nMatriz criada:\n ")
        imprimirMatriz(matCriada)  

        sair = True
        while(sair):
            print("\nDigite as coordenadas do START e GOAL, lembre-se: Só é possível começar e terminar em uma célula cujo o valor é igual ou maior que 1")
            
            startX = input("\nDigite a linha do START: ")
            while(verificarInput(startX) == False):
                print("Opção Inválida")
                startX = input("Digite a linha do START: ")
            startX = int(startX)

            startY = input("Digite a coluna do START: ")
            while(verificarInput(startY) == False):
                print("Opção Inválida")
                startY = input("Digite a coluna do START: ")
            startY = int(startY)

            goalX = input("Digite a linha do GOAL: ")
            while(verificarInput(goalX) == False):
                print("Opção Inválida")
                goalX = input("Digite a linha do GOAL: ")
            goalX = int(goalX)

            goalY = input("Digite a coluna do GOAL: ")
            while(verificarInput(goalY) == False):
                print("Opção Inválida")
                goalY = input("Digite a coluna do GOAL: ")
            goalY = int(goalY) 
            
            start = (startX, startY)
            goal = (goalX, goalY)

            if(verificarEntradas(matCriada, start, goal)):
                path = bnb(matCriada, start, goal)
                if(path == None):
                    print("\nCaminho não encontrado", end="")
                else:
                    print("\nMelhor caminho encontrado: \n")
                    for i in range(len(path)-1, -1, -1):
                        print(path[i], end='\t')

                print()
            else:
                print("\nInformações inválidas! Tente novamente.")

            
            escolha = input("\nDeseja tentar novamente com a mesma matrz? (S/N): ")   
            if(escolha == "N" or escolha == "n"):
                sair = False    
    
    elif op == 0:
       print("Saindo...") 
    
    elif(op > 2 or sair != False):
        print("\nOpção inválida! Tente novamente.")
