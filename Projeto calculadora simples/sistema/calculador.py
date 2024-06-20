
class Calculadora():
    def __init__(self , conta):
        self.conta = conta


    def Calcular(self):
        conta_tratada = self.conta
        if 'x' in conta_tratada:
            conta_tratada = conta_tratada.replace('x','*')

        if '÷' in conta_tratada:
            conta_tratada = conta_tratada.replace('÷','/')

        return eval(conta_tratada)
    

    def AoQuadrado2(self):
        if len(self.conta) > 0:
            print(self.conta)
            conta_tratada = self.conta
            if 'x' in conta_tratada:
                conta_tratada = conta_tratada.replace('x','*')

            if '÷' in conta_tratada:
                conta_tratada = conta_tratada.replace('÷','/')

            aoQuadrado = eval(conta_tratada)*eval(conta_tratada)
            return str(aoQuadrado)
            
    
    def RaizAoquadrado(self):
        from math import sqrt
        if len(self.conta) > 0:
            raiz = sqrt(float(self.conta))
            return raiz
 


if __name__ == '__main__':
    conta = Calculadora('8')
    conta.RaizAoquadrado()