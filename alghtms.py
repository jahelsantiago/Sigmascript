#import pandas as pd 
#import numpy as np 





class Model:
    def __init__(self,a,b,t,M):
        self.a = a          #int
        self.t = t      #array columnas
        self.b = b      #array filas
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.symbolsList = []
        
        
        bloquesM = len(M)
        tratamientosM = len(M[0])
        
        if (bloquesM == len(b)) and (tratamientosM == len(t)):
            self.M = M     #matrix
        else:
            print("Dimensiones de M corresponden a las dimensiones de tratamientos y bloques. Se requiere: \n#columnas de M == longitud de t \n#filas de M == longitud de b")
  
  
        #crear simbolos, maximo 23 bloques alfabeto
        
        for i in range(tratamientosM):
            self.symbolsList.append(self.alphabet[i])
  
          
    def operationNum(self,b,t):
        count = 0
        
        #recuento de todos los datos del Modelo
        if(b == "." and t == "."):
            for i in range(len(self.M)):
                for j in range(len(self.M[i])): 
                    for k in range(len(self.M[i][j])):
                        count += 1
            return count
                    
        #recuento de todos los datos del bloque b-esimo
        elif((type(b) is int) and t == "."):
            if(b <= len(self.b)-1):
                for i in range(len(self.M[b])):
                    for j in range(len(self.M[b][i])):
                            count += 1
                return count
            else:
                print("El bloque numero " + str(b) + " no existe, recuerde que la numeración comienza en 0")
        
        #recuento de todos los datos del tratamiento t-esimo
        elif(b == "." and (type(t) is int)):
            if(t <= len(self.t)-1):
                for i in range(len(self.M)):
                    for j in range(len(self.M[i][t])):
                        count += 1
                return count
            else:
                print("El tratamiento numero " + str(t) + " no existe, recuerde que la numeración comienza en 0")
     
         
    def operationSet(self,b,t):
        
        templist = []
        
        #retorna todos los elementos de modelo en un arreglo
        if(b == "." and t == "."):
            for i in range(len(self.M)):
                for j in range(len(self.M[i])): 
                    for k in range(len(self.M[i][j])):
                        templist.append(self.M[i][j][k])
            return templist
   
        #retorna todos los datos del bloque b-esimo
        elif((type(b) is int) and t == "."):
            if(b <= len(self.b)-1):
                for i in range(len(self.M[b])):
                    for j in range(len(self.M[b][i])):
                        templist.append(self.M[b][i][j])
                return templist
            else:
                print("El bloque numero " + str(b) + " no existe, recuerde que la numeración comienza en 0")
                return templist
        
            
        
        
        elif(b == "." and (type(t) is int)):
            if(t <= len(self.t)-1):
                for i in range(len(self.M)):
                    for j in range(len(self.M[i][t])):
                        templist.append(self.M[i][t][j])
                return templist
            else:
                print("El tratamiento numero " + str(t) + " no existe, recuerde que la numeración comienza en 0")
                return templist
        else:
            print("Argumentos Invalidos")
            return templist
            
            
    def findElementSymbol(self,element): #retorna simbolo relacionado al tratamiento que pertenece
        
        for i in range(len(self.M)):
            for j in range(len(self.M[i])): 
                for k in range(len(self.M[i][j])):
                    if element == self.M[i][j][k]:
                        #encontrado
                        symbol = self.symbolsList[j]
                        #print(symbol)
                        return symbol

        
    def multicotomize(self, numberList): #multicotomiza el bloque i-esimo, retorna chain

        chainList = []
        str = ""
        
        for i in range(len(numberList)):
            #buscar numberList[i] en model y retornar simbolo relacionado al tratamiento
            symbol = self.findElementSymbol(numberList[i])
            
            if symbol == "":
                print("error de multicotomización")
            else:
                chainList.append(symbol) 

        for e in chainList: 
            str += e

        return Chain(str)
        
        
   
    def toSteakModel(self): #algortimo de multicomozación del modelo de 2 vias
    
        self.Z = self.M #crea modelo de rachas Z con las dimenciones de M
    #para cada bloque del modelo   
        for i in range(len(self.M)):
            
            count = 0
            
            #extraer bloque i-esimo
            b = self.operationSet(i,".") #recursive
            #ordenar bloque i-esimo (ascendente)
            #print(b)
            
            b.sort()
            
            #guarda bloque original paraa comparar
            bOrigin = self.operationSet(i,".")
       
            #calcular cadena multicotomizada de bloque i-esimo
            chain = self.multicotomize(b)
            #caluclar numero de rachas de la cadena multicotomizada i-esima
            NumberofSteaks = chain.numberOfSteaks()
            #asigna al Z el numero encontrado
    
            #print(chain.chainArray)
            #chain.chainArray
            
            #El arreglo orginal se busca en el ordenado y retorna la posicion donde quedó en el ordenado
            positionsList = []
            
            for e in range(len(bOrigin)):
                #print(bOrigin[e])
                positionsList.append(b.index(bOrigin[e]))
            
            #print(positionsList)
            
            
            #for i in range(len(self.M)):
            for j in range(len(self.M[i])): 
                for k in range(len(self.M[i][j])):
                    if(positionsList[count] < len(chain.chainArray) - 1):
                        #print(positionsList[count])
                        self.Z[i][j][k] = chain.numberOfSteaksUntilIndex(positionsList[count])
                        #print(self.Z[i][j])
                        count += 1
                    else:
                        
                        count += 1
                        self.Z[i][j][k] = chain.numberOfSteaks()
                       # print(self.Z[i][j])
        return self.Z
            
    
    
    def SteakOperationNum(self,b,t): #operaciones sobre modelo de rachas, 9 operaciones
        count = 0
        
        #recuento de todos los datos del Modelo
        if(b == "." and t == "."):
            for i in range(len(self.M)):
                for j in range(len(self.M[i])): 
                    for k in range(len(self.M[i][j])):
                        count += 1
            return count
                    
        #recuento de todos los datos del bloque b-esimo
        elif((type(b) is int) and t == "."):
            if(b <= len(self.b)-1):
                for i in range(len(self.M[b])):
                    for j in range(len(self.M[b][i])):
                            count += 1
                return count
            else:
                print("El bloque numero " + str(b) + " no existe, recuerde que la numeración comienza en 0")
        
        #recuento de todos los datos del tratamiento t-esimo
        elif(b == "." and (type(t) is int)):
            if(t <= len(self.t)-1):
                for i in range(len(self.M)):
                    for j in range(len(self.M[i][t])):
                        count += 1
                return count
            else:
                print("El tratamiento numero " + str(t) + " no existe, recuerde que la numeración comienza en 0")
     

    
#modelo = Model(1,[0,1,8],[7,5],[[9,8,1],[7,6]])

#modeloz = Model (a,b,t,M)
modeloZ = Model(4.7,[-7.4,1.2],[5.4,-9.2,3],[[[15.9,-4.0,66.1],[-6.1,3.9],[4.2,-1.3,12.4,5.8]],[[23.8],[4.5,3.6,-0.5],[2.2,-5.6]]])

#print(len(modeloZ.M[0]))

#print(modeloZ.operationNum(".",2))

#print(modeloZ.operationSet(".",1))


class Chain:
    def __init__(self, chain):   
        if chain == "":
            print("Cadena vacia")
        else:  
            self.chain = chain                #string
            self.chainArray = list(chain)     #array of strings


    def numberOfSteaks(self):
        if self.chain == "":
            print("Cadena vacia")
            return 0
        else:
            counter = 1
    
            for i in range(len(self.chainArray) - 1):
                if self.chainArray[i] != (self.chainArray[i + 1]):
                    counter += 1
            return counter    
    
    def numberOfSteaksUntilIndex(self,index):
        
        if self.chain == "":
            print("Cadena vacia")
            return 0
        elif (index < 0) or (index >= len(self.chainArray) - 1):
            print("indice fuera de rango")
            return 0
        else:
            counter = 1
    
            for i in range(index + 1):
                if self.chainArray[i] != (self.chainArray[i + 1]):
                    if i < index:
                        counter += 1
            return counter    
        
            

#s = Chain("aabccc")
#print(s.chain)
#print(s.chainArray)

#print(s.numberOfSteaks())

modelodeRachas = modeloZ.toSteakModel()

print(modelodeRachas)


#numbers = modeloZ.operationSet(0,".")

#cadena = modeloZ.multicotomize(numbers)

#print(cadena.chainArray)

#print(cadena.numberOfSteaksUntilIndex(8))