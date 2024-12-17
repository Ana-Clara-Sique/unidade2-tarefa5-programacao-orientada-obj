class Contador:

    contador = 0

    @staticmethod
    def aumentar():
      
        Contador.contador += 1

    @staticmethod
    def diminuir():
      if Contador.contador > 0:
         Contador.contador -= 1
      else:
         print("O contador não pode ser negativo.")   

    @staticmethod
    def zerar():
       Contador.contador = 0

    @staticmethod
    def mostrar():
       print(f"Valor do contador: {Contador.contador}")        


Contador.aumentar()
Contador.aumentar()
Contador.mostrar()
Contador.diminuir()
Contador.mostrar()
Contador.zerar()
Contador.mostrar()
