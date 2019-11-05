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
from scipy.integrate import simps
import matplotlib.pyplot as plt

import json
with open('DictionarioRobot.json') as js:
    DICTIONARIO = json.load(js)
    ENTRADAS = DICTIONARIO.get('entradas')
    SALIDAS = DICTIONARIO.get('salidas')
    VARIABLES = DICTIONARIO.get('variables')

# %% Clase principal

class Robot :

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
        print("\n*******   El angulo buscado es   *******")
      #  print("14 g de cafe puro Colombiano")
        self.etiquetaSalida()
        self.defuzzificar()
        for key in self.salidas :
            print("{} {} de {}.".format(self.variables[key]["salida"], 
                  self.variables[key]["unidad"], key))

    def pedirUsuario(self):
        print("*******   BIENVENIDO   *******")
        for key in self.entradas :
            ok=False;
            mini=self.variables[key]["escala"][0]
            maxi=self.variables[key]["escala"][1]
            print("Qué angulo {} ?".format(key))
            while ok==False :
                try:
                    res=int(input("Escriba un valor entre {} y {} : ".format(mini,maxi)))
                    if res<mini or res>maxi :
                        print("Su angulo no cumple las condiciones...")
                        ok=False
                    else : ok=True
                except ValueError :
                    print("Escribe un angulo porfavor")
            self.variables[key]["entrada"]=res

        print("Listo! :-)")

    def addGauss(self,ax,xmin,xmax,promedio,sigma,label):
        x = np.linspace(xmin, xmax, 1000)
        y = norm.pdf(x,promedio,sigma)/norm.pdf(promedio,promedio,sigma)
        ax.plot(x,y,color="lightblue")
        ax.text(promedio-3, 0.6, label, fontsize=9)
        
    def addGaussDefuzz(self,ax,xmin,xmax,promedio,sigma,label,mu):
        x = np.linspace(xmin, xmax, 1000)
        y = norm.pdf(x,promedio,sigma)/norm.pdf(promedio,promedio,sigma)
        g = np.linspace(mu, mu, 1000)
        
        intersect = np.argwhere(np.diff(np.sign(y - g)) != 0).reshape(-1) + 0
        idx=np.argwhere(g<y).reshape(-1) + 0
        
        area = simps(y, dx=5)-simps(y[idx], dx=5)+simps(g[idx], dx=5)
        if len(idx>1): centro=promedio
        elif promedio>idx[0] : centro=idx[0]+(promedio-idx[0])/2
        else : centro=promedio+(idx[0]-promedio)/2
        ax.plot(x,y,color="lightblue")
        ax.plot(x[idx],g[idx],color="purple",linestyle="--")
        #ax.fill_between(x,y,color="lavender")
        ax.fill_between(x, y, where=y < g, facecolor='lavender')
        ax.fill_between(x, g, where=y > g, facecolor='lavender')
        plt.plot(x[intersect], y[intersect], 'x',color="purple")
        ax.text(promedio-3, 0.6, label, fontsize=9)
        return (area,centro)
        
    def fuzzificar(self):
        plt.figure(figsize=(15,10))
        plt.suptitle("FUZZIFICACION",fontsize=16)
        dim=1
        for key in self.entradas :
            ax=plt.subplot(2,1,dim,title="Angulo {} ?".format(key))
            plt.grid()
            labels=self.variables[key]["labels"]
            scale=self.variables[key]["escala"]
            nbSplit=len(labels)
            #n=int((scale[1]-scale[0])/(nbSplit-1))
            #sigma=n/3
            for i in range(0,nbSplit):
                sigma=self.variables[key]["std"][i]
                promedio=self.variables[key]["promedios"][i]
                #promedio=scale[0]+i*n
                self.addGauss(ax,scale[0],scale[1],promedio,sigma,labels[i])
                mu=round(norm.pdf(self.variables[key]["entrada"],promedio,sigma)/norm.pdf(promedio,promedio,sigma),2)
                self.variables[key]["valuesMu"][i]=mu
            ax.axvline(self.variables[key]["entrada"],color="Crimson")
            dim+=1
        plt.show()
        plt.savefig("Fuzzificacion")

    def llenarMatriz(self):
        beta=self.variables["beta"]["valuesMu"]
        alpha=self.variables["alpha"]["valuesMu"]
        for i in range(len(beta)):
            for j in range(len(alpha)):
                self.matrizProba[i][j]=min(beta[i],alpha[j])
    
    def etiquetaSalida(self):
        lineas, columnas = self.matrizProba.shape
        for key in self.salidas :
            result = dict()
            for lab in self.variables[key]["labels"]:
                result[lab]=[]
                
            for i in range(lineas):
                for j in range(columnas):
                    lab=self.variables[key]["matriz"][i][j]
                    val=self.matrizProba[i][j]
                    result[lab].append(val)
            
            for k in range(len(self.variables[key]["labels"])):
                self.variables[key]["valuesMu"][k]=max(result[self.variables[key]["labels"][k]])
        
    def defuzzificar(self):
        plt.figure(figsize=(15,10))
        plt.suptitle("DEFUZZIFICACION",fontsize=16)
        dim=1
        for key in self.salidas :
            ax=plt.subplot(2,1,dim,title="Angulo {} ?".format(key))
            plt.grid()
            labels=self.variables[key]["labels"]
            scale=self.variables[key]["escala"]
            nbSplit=len(labels)
            #n=int((scale[1]-scale[0])/(nbSplit-1))
            #sigma=n/3
            sumArea=0
            sumAreaCentro=0
            for i in range(0,nbSplit): 
                sigma=self.variables[key]["std"][i]
                promedio=self.variables[key]["promedios"][i]
                #promedio=scale[0]+i*n
                mu=self.variables[key]["valuesMu"][i]
                if mu>0 :
                    area, centro=self.addGaussDefuzz(ax,scale[0],scale[1],promedio,sigma,labels[i],mu)
                    sumArea+=area
                    sumAreaCentro+=area*centro
                else:
                    self.addGauss(ax,scale[0],scale[1],promedio,sigma,labels[i])
            self.variables[key]["salida"]=round(sumAreaCentro/sumArea,2)
            ax.axvline(self.variables[key]["salida"],color="Crimson")
            dim+=1
        plt.show()
        plt.savefig("Defuzzificacion")
    
# %% Ejecucion
if __name__ == '__main__':
    robot = Robot(ENTRADAS,SALIDAS,VARIABLES)
    robot.run()
