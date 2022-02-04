import numpy as np 

#ver definición en la linea 167 de vocabulario.txt

class Model:
    def __init__(self,a,b,t,M):
        self.a = a      #int
        self.t = t      #array columnas
        self.b = b      #array filas
        
        bloquesM = len(M)
        tratamientosM = len(M[0])
        
        if (bloquesM == len(b)) and (tratamientosM == len(t)):
            self.M = M  #matrix
        else:
            print("Dimensiones de M deben corresponder a las dimensiones de tratamientos y bloques. Se requiere: \n#columnas de M == longitud de t \n#filas de M == longitud de b")
  
          
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
        else:
            print("Argumentos Invalidos")
            return       
         
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
        
        #retorna todos los datos del tratamiento t-esimo
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
            return

    

#Ejemplos

#modelo = Model(1,[0,1,8],[7,5],[[9,8,1],[7,6]])
#modeloz = Model (a,b,t,M)
#modeloZ = Model(4.7,[-7.4,1.2],[5.4,-9.2,3],[[[15.9,-4.0,66.1],[-6.1,3.9],[4.2,-1.3,12.4,5.8]],[[23.8],[4.5,3.6,-0.5],[2.2,-5.6]]])
#print(len(modeloZ.M[0]))

#print(modeloZ.operationNum(".","."))
#print(modeloZ.operationNum(".",1))
#print(modeloZ.operationSet(0,"."))
#print(modeloZ.operationSet(".",2))



