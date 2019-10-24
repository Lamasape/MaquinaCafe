#-------------------------------------------------------------------------------
# Intro IA - Proyecto 3
#
#             ***   Logica Difusa : MAQUINA DE CAFE   ***
#
#
# Authors:     Laura SANCHEZ & Elise JACQUEMET 
# Created:     23/10/2019
#-------------------------------------------------------------------------------

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# %% Clase principal

class Cafe :

    def __init__ (self):
        self.labels={"dulce" : [["PURO",0],["AMARGO",0],["SUAVE",0],["DULCE",0],["DEMASIADO",0]], 
                    "fuerte" : [["SUBTIL",0],["LIGERO",0],["AMARGO",0],["FUERTE",0]], 
                    "agua" : [["POQUITO",0],["POCO",0],["BASTANTE",0],["MUCHO",0]], 
                    "azucar" : [["POQUITO",0],["POCO",0],["BASTANTE",0],["MUCHO",0]]}   # variable : list[clase, valor de mu]
        self.matrices = {"agua":np.array([["BASTANTE","BASTANTE","MUCHO","MUCHO","MUCHO"],
                                        ["POCO","POCO","BASTANTE","BASTANTE","MUCHO"],
                                        ["POQUITO","POQUITO","POCO","POCO","BASTANTE"],
                                        ["POQUITO","POQUITO","POQUITO","POCO","POCO"]]),
                        "azucar":np.array([["POCO","POCO","BASTANTE","MUCHO","MUCHO"],
                                        ["POQUITO","POCO","BASTANTE","MUCHO","MUCHO"],
                                        ["POQUITO","POQUITO","POCO","BASTANTE","MUCHO"],
                                        ["POQUITO","POQUITO","POCO","BASTANTE","BASTANTE"]])}
        self.escalas = {"dulce" : [0,100], "fuerte" : [0,100], "agua" : [0,240], "azucar" : [0,100]}    # variable : start,end
        self.entradas = {"dulce" : [0,5], "fuerte" : [0,4]}   # variable : valor,splits
        self.salidas = {"agua" : [40,"mL"], "azucar" : [0,"g"]} # variable : valor,unidad
        self.matrizProba = np.zeros([4,5])

    def run(self):
        self.pedirUsuario()
        self.fuzzificar()
        self.llenarMatriz()
        print("\n*******   SU CAFE CONTIENE   *******")
        print("14 g de cafe puro Colombiano")
        for key, value in self.salidas.items() :
            d = self.etiquetaSalida(key)
            value[0] += self.defuzzificar(key, d)
            print("{} {} de {}.".format(value[0], value[1], key))

    def pedirUsuario(self):
        print("*******   BIENVENIDO   *******")
        for key,value in self.entradas.items() :
            ok=False;
            mini=self.escalas[key][0]
            maxi=self.escalas[key][1]
            print("Que tan {} le gustaria su cafe?".format(key))
            while ok==False :
                try:
                    res=int(input("Escriba un valor entre {} y {} : ".format(mini,maxi)))
                    ok=True
                    if res<mini or res>maxi :
                        print("Su numero no cumple las condiciones...")
                        ok=False
                except ValueError :
                    print("Escribe un numero porfavor")
            self.entradas[key][0]=res

        print("Listo! Empezamos la preparacion :-)")

    def addGauss(self,ax,xmin,xmax,promedio,sigma,label):
        x = np.linspace(xmin, xmax, 100)
        y = norm.pdf(x,promedio,sigma)/norm.pdf(promedio,promedio,sigma)
        ax.plot(x,y,color="lightblue")
        ax.text(promedio-3, 0.6, label, fontsize=9)
        
    def fuzzificar(self):
        plt.figure(figsize=(15,10))
        plt.suptitle("FUZZIFICACION",fontsize=16)
        dim=1
        for key, value in self.entradas.items() :
            ax=plt.subplot(2,1,dim,title="Que tan {} ?".format(key))
            plt.grid()
            labels=self.labels[key]
            scale=self.escalas[key]
            nbSplit=value[1]
            n=int((scale[1]-scale[0])/(nbSplit-1))
            sigma=n/3
            for i in range(0,nbSplit):
                promedio=scale[0]+i*n
                self.addGauss(ax,scale[0],scale[1],promedio,sigma,labels[i][0])
                self.labels[key][i][1]=round(norm.pdf(value[0],promedio,sigma)/norm.pdf(promedio,promedio,sigma),2)
            ax.axvline(value[0],color="Crimson")
            dim+=1
        plt.show()
        plt.savefig("Fuzzificacion")

    def llenarMatriz(self):
        print("llenarMatriz() not implemented yet")
    
    def etiquetaSalida(self, salida):
        result = dict()
        # LLENAR DICTIONARIO
        print("etiquetaSalida() not implemented yet")
        return result
        
    def defuzzificar(self, salida, etiquetas):
        result=0
        # defuzzificar variable de salida
        print("defuzzificar() not implemented yet")
        return result
    
# %% Ejecucion
if __name__ == '__main__':
    coffee = Cafe()
    coffee.run()
