# funcion sin parametros 
def nombrefuncion():
    print("mensaje")
    nombrefuncion()

    #funcion con parametro
    def nombrefuncionConParametro(parametro):
     print("este es el parametro" + parametro)
    nombrefuncionConParametro("este es  el argumento del parametro")

    #Funcion con multoples parametros
    def nombreFuncionConMultiplesParametros(parametro1,parametro2):
        print("estos son los valores de los multiples parametros:" + parametro1,parametro2)
        nombreFuncionConMultiplesParametros("este es el argumento1 ", "este es el argumento2")

