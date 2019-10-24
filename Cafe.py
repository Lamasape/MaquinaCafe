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

import json
with open('Dictionario.json') as js:
    DICTIONARIO = json.load(js)
    ENTRADAS = DICTIONARIO.get('entradas')
    SALIDAS = DICTIONARIO.get('salidas')
    VARIABLES = DICTIONARIO.get('variables')

# %% Clase principal

class Cafe :

    def __init__ (self,entradas,salidas,variables):
        self.entradas=entradas    # list of String
        self.salidas=salidas      # list of String
        self.variables=variables  # dict
        dim=[]
        for e in entradas :
            dim.append(len(variables[e]["labels"]))
        self.matrizProba = np.zeros(dim)

    def run(self):
        self.pedirUsuario()
        self.fuzzificar()
        self.llenarMatriz()
        print("\n*******   SU CAFE CONTIENE   *******")
        print("14 g de cafe puro Colombiano")
        for key in self.salidas :
            d=self.etiquetaSalida(key)
            self.variables[key]["salida"] += self.defuzzificar(key,d)
            print("{} {} de {}.".format(self.variables[key]["salida"], 
                  self.variables[key]["unidad"], key))

    def pedirUsuario(self):
        print("*******   BIENVENIDO   *******")
        for key in self.entradas :
            ok=False;
            mini=self.variables[key]["escala"][0]
            maxi=self.variables[key]["escala"][1]
            print("Que tan {} le gustaria su cafe?".format(key))
            while ok==False :
                try:
                    res=int(input("Escriba un valor entre {} y {} : ".format(mini,maxi)))
                    if res<mini or res>maxi :
                        print("Su numero no cumple las condiciones...")
                        ok=False
                    else : ok=True
                except ValueError :
                    print("Escribe un numero porfavor")
            self.variables[key]["entrada"]=res

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
        for key in self.entradas :
            ax=plt.subplot(2,1,dim,title="Que tan {} ?".format(key))
            plt.grid()
            labels=self.variables[key]["labels"]
            scale=self.variables[key]["escala"]
            nbSplit=len(labels)
            n=int((scale[1]-scale[0])/(nbSplit-1))
            sigma=n/3
            for i in range(0,nbSplit):
                promedio=scale[0]+i*n
                self.addGauss(ax,scale[0],scale[1],promedio,sigma,labels[i])
                mu=round(norm.pdf(self.variables[key]["entrada"],promedio,sigma)/norm.pdf(promedio,promedio,sigma),2)
                self.variables[key]["valuesMu"][i]=mu
            ax.axvline(self.variables[key]["entrada"],color="Crimson")
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
    coffee = Cafe(ENTRADAS,SALIDAS,VARIABLES)
    print(coffee.matrizProba)
    coffee.run()
    print(coffee.matrizProba)
