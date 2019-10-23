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

class Cafe :

    def __init__ (self):
        self.matrizProba = np.empty([6,5])
        self.matrices = {"agua":np.array([["BASTANTE","BASTANTE","MUCHO","MUCHO","MUCHO"],
                                        ["POCO","POCO","BASTANTE","BASTANTE","MUCHO"],
                                        ["POQUITO","POQUITO","POCO","POCO","BASTANTE"],
                                        ["POQUITO","POQUITO","POQUITO","POCO","POCO"]]),
                        "azucar":np.array([["POCO","POCO","BASTANTE","MUCHO","MUCHO"],
                                        ["POQUITO","POCO","BASTANTE","MUCHO","MUCHO"],
                                        ["POQUITO","POQUITO","POCO","BASTANTE","MUCHO"],
                                        ["POQUITO","POQUITO","POCO","BASTANTE","BASTANTE"]])}
        self.escalas = {"entrada" : [0,100], "agua" : [0,240], "azucar" : [0,100]}
        self.entradas = {"dulce" : 0, "fuerte" : 0}
        self.salidas = {"agua" : [40," mL"], "azucar" : [0," g"]}

    def run(self):
        self.pedirUsuario()
        self.fuzzificar()
        self.llenarMatriz()
        print("*******   SU CAFE CONTIENE   *******")
        print("14 g de cafe puro Colombiano")
        for key, value in salidas :
            d = self.etiquetaSalida(key)
            value[0] += self.defuzzificar(key, d)
            print(value[0]+[1]+" de "+key)

    def pedirUsuario(self):
        print("*******   BIENVENIDO   *******")
        numeric=False;
        print("¿Que tan dulce le gustaria su cafe?")
        while numeric==False :
            try:
                res=int(raw_input("Escriba un valor entre 0 y 100 : "))
                numeric=True
            except ValueError :
                print("Escribe un numero porfavor")
        self.entradas["dulce"]=res

        numeric=False;
        print("¿Que tan fuerte le gustaria su cafe?")
        while numeric==False :
            try:
                res=int(raw_input("Escriba un valor entre 0 y 100 : "))
                numeric=True
            except ValueError :
                print("Escribe un numero porfavor")
        self.entradas["fuerte"]=res

        print("¡Listo! Empezamos la preparacion :-)")

    def fuzzificar(self, variables, escala):
        # fuzzificar cada variable sgun su escala
        #for v in variables :
        print("Not implemented yet")


    def llenarMatriz(self):
        print("Not implemented yet")

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
