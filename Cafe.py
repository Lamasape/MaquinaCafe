#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Laura Mambo
#
# Created:     23/10/2019
# Copyright:   (c) Laura Mambo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from scipy.stats import norm
from scipy.integrate import quad
import matplotlib.pyplot as plt


class Cafe :

    def __init__ (self):
        self.matrizProba = np.zeros([4,5])
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
        self.entradas = {"dulce" : [54,5], "fuerte" : [89,4]}   # variable : valor,splits
        self.salidas = {"agua" : [40,"mL"], "azucar" : [0,"g"]} # variable : valor,unidad

    def run(self):
        #self.pedirUsuario()
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
        numeric=False;
        print("Que tan dulce le gustaria su cafe?")
        while numeric==False :
            try:
                res=int(raw_input("Escriba un valor entre 0 y 100 : "))
                numeric=True
            except ValueError :
                print("Escribe un numero porfavor")
        self.entradas["dulce"][0]=res

        numeric=False;
        print("Que tan fuerte le gustaria su cafe?")
        while numeric==False :
            try:
                res=int(raw_input("Escriba un valor entre 0 y 100 : "))
                numeric=True
            except ValueError :
                print("Escribe un numero porfavor")
        self.entradas["fuerte"][0]=res

        print("Listo! Empezamos la preparacion :-)")

    def addGauss(self,ax,xmin,xmax,promedio,sigma,label):
        x = np.linspace(xmin, xmax, 100)
        y = norm.pdf(x,promedio,sigma)
        ax.plot(x,y,color="lightblue")
        ax.text(promedio-3, 0.01, label, fontsize=9)
        
    def fuzzificar(self):
        fig1=plt.figure(figsize=(15,10))
        plt.suptitle("FUZZIFICACION",fontsize=16)
        dim=1
        for key, value in self.entradas.items() :
            ax=plt.subplot(2,1,dim,title=key)
            plt.grid()
            labels=self.labels[key]
            scale=self.escalas[key] # 0-100
            nbSplit=value[1] # 5
            n=int((scale[1]-scale[0])/(nbSplit-1)) # 25
            sigma=n/(nbSplit-1)
            for i in range(0,nbSplit):
                promedio=scale[0]+i*n
                self.addGauss(ax,scale[0],scale[1],promedio,sigma,labels[i][0])
            ax.axvline(value[0],color="Crimson")
            dim+=1
        plt.show()

    def llenarMatriz(self):
        print("llenarMatriz not implemented yet")
    
    def etiquetaSalida(self, salida):
        result = dict()
        # LLENAR DICTIONARIO
        print("Not implemented yet")
        return result
        
    def defuzzificar(self, salida, etiquetas):
        result=0
        # defuzzificar variable de salida
        print("Not implemented yet")
        return result

if __name__ == '__main__':
    coffee = Cafe()
    coffee.run()
