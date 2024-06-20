from tkinter import *
'''
essa classe nada mais do que a interface da calculadora, junto com as fucionalidades de outras classe de outro modulos
'''
class InterFaceGrafica():

    calculo = '' # a variavel que irar pegar o digito e entre para class que é responsavel em fazer a conta


    def __init__(self):
        self.gui()


    def gui(self):
        #cores que sao utilizadas no projeto
        cor_fundo = '#323232'
        font_botao = 'Arial 11 bold'
        cor_botoesDi = '#505050'
        cor_operadores = '#0D0F14'

        self.janela = Tk()
        self.janela.title('Calculadora Simples')
        self.janela.geometry('385x475')
        self.janela.config(bg=cor_fundo)

        """
        **Interface Gráfica com Tkinter:**
        - Criar uma janela principal (`Tk()`) e configurar o título.
        - Utilizar um `Entry` para exibir a expressão atual e o resultado.
        - Criar botões para os dígitos de 0 a 9, operadores (+, -, *, /), botão de igual (=) e botão de limpar (C).
        """
        #botoes da calculadora, na caso as numerções de 0 a 9
        # ainda nao sei oq botar


        self.botao_apagar = Button(self.janela, width = 9 , height = 3 , text = '#' , font = font_botao , bg  = cor_botoesDi , fg = 'white' , relief = 'flat' , command = self.Apagar)
        self.botao_apagar.place(x = 5 ,y = 402)

        #botao que terar o valor de zero na calculado
        self.botao_0 = Button(self.janela , width  = 9 , height = 3 , text = '0', font = font_botao , bg = cor_botoesDi , fg = 'white' , relief='flat' , command=self.Digitar0)
        self.botao_0.place(x = 100 , y =402)

        # o botao que terar o valor de virgular
        self.botao_virgula = Button(self.janela , width=9 ,height= 3 , text = ',' , font = font_botao , bg = cor_botoesDi , fg = 'white' , relief='flat' , command = self.Digitar_virgula)
        self.botao_virgula.place(x = 195  , y = 402)

        # o botao que terar o valor de 1
        self.botao_1 = Button(self.janela , width = 9 , height = 3 , text = '1' , font = font_botao , bg = cor_botoesDi , fg = 'white' , relief='flat' , command=self.Digitar1)
        self.botao_1.place(x = 5, y = 330)

        #o botao que terar o valor de 2
        self.botao_2 = Button(self.janela , width = 9 , height = 3 ,  text = '2', font = font_botao , bg =  cor_botoesDi , fg = 'white' , relief='flat' , command= self.Digitar2)
        self.botao_2.place(x = 100 , y = 330)
        
        #botao que terar o valor 3
        self.botao_3 = Button(self.janela , width = 9 , height = 3 , text = '3' , font= font_botao , bg = cor_botoesDi , fg = 'white' , relief = 'flat' , command=self.Digitar3)
        self.botao_3.place(x = 195 , y = 330)

        #botao que terar o valor de 4
        self.botao_4 = Button(self.janela, width = 9 , height = 3 , text = '4' , font = font_botao , bg = cor_botoesDi , fg = 'white' , relief = 'flat' , command = self.Digitar4)
        self.botao_4.place(x = 5 , y = 258)

        #botao que terar o valor de 5
        self.botao_5 = Button(self.janela , width = 9 , height = 3 ,text = '5' , font = font_botao , bg = cor_botoesDi , fg = 'white' , relief= 'flat' , command = self.Digitar5)
        self.botao_5.place(x = 100 , y = 258)

        #botao que terar o valor de 6
        self.botao_6 = Button(self.janela , width = 9 , height = 3 , text = '6' , font = font_botao , bg = cor_botoesDi , fg = 'white' , relief = 'flat' , command = self.Digitar6)
        self.botao_6.place(x = 195 , y = 258)

        #botao que terar o valor de 7
        self.botao_7 = Button(self.janela , width = 9 , height = 3 , text = '7' , font = font_botao , bg = cor_botoesDi , fg = 'white' , relief = 'flat' , command = self.Digitar7)
        self.botao_7.place(x = 5 , y = 186)

        #botao que terar o valor de 8
        self.botao_8 = Button(self.janela , width= 9 , height = 3 , text = '8' , font = font_botao , bg = cor_botoesDi , fg = 'white' , relief = 'flat' , command = self.Digitar8)
        self.botao_8.place(x = 100 , y = 186)

        #botao que terar o valor de 9
        self.botao_9 = Button(self.janela , width = 9 , height = 3 , text = '9' , font = font_botao , bg = cor_botoesDi , fg = 'white' , relief = 'flat' ,command= self.Digitar9)
        self.botao_9.place(x = 195 , y = 186)

        #operadores
        #aqui sera o sinal de igual parar somar os numero digitados
        self.sinal_igual = Button(self.janela , width= 9 , height = 3 , text = '=' , font= font_botao , bg = '#16878C' , fg = 'white' , relief = 'flat' , command=self.Calcular)
        self.sinal_igual.place(x = 290  , y = 402)

        # o sinal de adição(+)
        self.sinal_mais = Button(self.janela , width = 9 , height= 3 , text = '+' , font= font_botao , bg = cor_operadores , fg = 'white' , relief = 'flat' , command = self.Digitar_adicao , state = 'disabled')
        self.sinal_mais.place(x = 290 , y = 330)

        #sinal de subtração(-)
        self.sinal_sub = Button(self.janela , width = 9 , height = 3 , text = '-' , font = font_botao , bg = cor_operadores , fg = 'white' , relief = 'flat' , command = self.Digitar_sub , state = 'disabled')
        self.sinal_sub.place(x = 290 , y = 258)

        #sinal de multiplicação(x)
        self.sinal_multi = Button(self.janela , width = 9 , height = 3 ,text = 'x' , font = font_botao , bg = cor_operadores , fg = 'white' , relief = 'flat' , command = self.Digitar_multi , state = 'disabled')
        self.sinal_multi.place(x = 290 , y = 186)

        #sinal de divisao(/)
        self.sinal_divi = Button(self.janela , width = 9 , height = 3 , text = '÷' , font = font_botao , bg = cor_operadores , fg = 'white' , relief = 'flat' , command = self.Digitar_divi , state = 'disabled')
        self.sinal_divi.place(x = 290 , y =114)

        # o ²√x é raiz de X ao quadrado
        self.raiz_quadrado = Button(self.janela , width = 9 , height = 3 , text = '²√x' , font= font_botao , bg = cor_operadores , fg = 'white',  relief = 'flat' , command= self.RaizAoQuadrado)
        self.raiz_quadrado.place(x = 195  , y = 114)

        #²X é x vez ele mesmo
        self.aoquadrado = Button(self.janela , width = 9 , height = 3 , text = '²x' , font = font_botao , bg = cor_operadores , fg = 'white' , relief = 'flat' , command = self.AoQuadrado)
        self.aoquadrado.place(x = 100 , y = 114)

        self.limpar_calcu = Button(self.janela , width = 9 , height = 3 , text = 'C' , font = font_botao , bg = cor_operadores , fg = 'white' , relief = 'flat' , command= self.Limpar_C)
        self.limpar_calcu.place(x = 5 , y = 114)

        #frames ondem vai fica a conta
        self.frame_calcu = Frame(self.janela , width = 400 , height= 110 , bg = '#1D1D1D')
        self.frame_calcu.place(x = 0 , y = 0)

        #label que serao o exbido da conta
        self.label_calcular = Label(self.janela , width = 18 , height = 0 , text = '0' , font = 'Arial 25 bold' , bg = '#1D1D1D' , fg = 'white' , relief = 'flat' , anchor='e')
        self.label_calcular.place(x = 0 , y = 30)


        self.janela.mainloop()

    # as funcoes que da o poder de digitar na calculadora, sao funcao simples.

    def Digitar0(self):
        self.calculo += '0'
        self.exbir_calculo()
        self.sinal_mais['state'] = 'normal'
        self.sinal_divi['state'] = 'normal'
        self.sinal_multi['state'] = 'normal'
        self.sinal_sub['state'] = 'normal'


    def Digitar1(self):
        self.calculo += '1'
        self.exbir_calculo()
        self.sinal_mais['state'] = 'normal'
        self.sinal_sub['state'] = 'normal'
        self.sinal_divi['state']  = 'normal'
        self.sinal_multi['state'] = 'normal'


    def Digitar2(self):
        self.calculo += '2'
        self.exbir_calculo()
        self.sinal_mais['state'] = 'normal'
        self.sinal_divi['state'] = 'normal'
        self.sinal_sub['state'] = 'normal'
        self.sinal_multi['state'] = 'normal'
        


    def Digitar3(self):
        self.calculo += '3'
        self.exbir_calculo()
        self.sinal_mais['state'] = 'normal'
        self.sinal_divi['state'] = 'normal'
        self.sinal_multi['state'] = 'normal'
        self.sinal_sub['state'] = 'normal'


    def Digitar4(self):
        self.calculo += '4'
        self.exbir_calculo()
        self.sinal_mais['state'] = 'normal'
        self.sinal_sub['state'] = 'normal'
        self.sinal_divi['state'] = 'normal'
        self.sinal_multi['state'] = 'normal'


    def Digitar5(self):
        self.calculo += '5'
        self.exbir_calculo()
        self.sinal_mais['state'] = 'normal'
        self.sinal_sub['state'] = 'normal'
        self.sinal_divi['state'] = 'normal'
        self.sinal_multi['state'] = 'normal'


    def Digitar6(self):
        self.calculo += '6'
        self.exbir_calculo()
        self.sinal_mais['state'] = 'normal'
        self.sinal_sub['state'] = 'normal'
        self.sinal_divi['state'] = 'normal'
        self.sinal_multi['state'] = 'normal'

    def Digitar7(self):
        self.calculo += '7'
        self.exbir_calculo()
        self.sinal_mais['state'] = 'normal'
        self.sinal_sub['state'] = 'normal'
        self.sinal_divi['state'] = 'normal'
        self.sinal_multi['state'] = 'normal'


    def Digitar8(self):
        self.calculo += '8'
        self.exbir_calculo()
        self.sinal_mais['state'] = 'normal'
        self.sinal_sub['state'] = 'normal'
        self.sinal_divi['state'] = 'normal'
        self.sinal_multi['state'] = 'normal'


    def Digitar9(self):
        self.calculo += '9'
        self.exbir_calculo()
        self.sinal_mais['state'] = 'normal'
        self.sinal_sub['state'] = 'normal'
        self.sinal_divi['state'] = 'normal'
        self.sinal_multi['state'] = 'normal'


    def Digitar_virgula(self):
        self.calculo += ','
        self.exbir_calculo()
        self.sinal_mais['state'] = 'normal'
        self.sinal_sub['state'] = 'normal'
        self.sinal_divi['state'] = 'normal'
        self.sinal_multi['state'] = 'normal'



    def Digitar_multi(self):
        self.calculo += 'x'
        self.exbir_calculo()
        self.sinal_divi['state'] = 'disabled'
        self.sinal_mais['state'] = 'disabled'
        self.sinal_sub['state'] = 'disabled'
        self.sinal_multi['state'] = 'disabled'


    def Digitar_sub(self):
        self.calculo += '-'
        self.exbir_calculo()
        self.sinal_divi['state'] = 'disabled'
        self.sinal_mais['state'] = 'disabled'
        self.sinal_sub['state'] = 'disabled'
        self.sinal_multi['state'] = 'disabled'


    def Digitar_adicao(self):
        self.calculo += '+'
        self.exbir_calculo()
        self.sinal_divi['state'] = 'disabled'
        self.sinal_mais['state'] = 'disabled'
        self.sinal_sub['state'] = 'disabled'
        self.sinal_multi['state'] = 'disabled'


    def Digitar_divi(self):
        self.calculo += '÷'
        self.exbir_calculo()
        self.sinal_divi['state'] = 'disabled'
        self.sinal_mais['state'] = 'disabled'
        self.sinal_sub['state'] = 'disabled'
        self.sinal_multi['state'] = 'disabled'


    #Funcoes que terar contato com calculo

    #Serve para atualizar o label que exbir os numero e operadores.
    def exbir_calculo(self):
        self.label_calcular['text'] = str(self.calculo)
        self.calculo = str(self.calculo).replace(',','.')
        self.label_calcular.update()

    
    def Limpar_C(self):
        self.label_calcular['text'] = '0'
        self.calculo = ''
        self.sinal_mais['state'] = 'disabled'
        self.sinal_sub['state'] = 'disabled'
        self.sinal_divi['state'] = 'disabled'
        self.sinal_multi['state'] = 'disabled'
        self.label_calcular.update()


    def Apagar(self):
        valor = ''
        if len(self.calculo) > 0:
            for indice , valores in enumerate(self.calculo):
                if indice != len(self.calculo)-1:
                    valor += valores

        self.calculo = valor
        self.label_calcular['text'] = self.calculo

        if len(self.calculo) == 0:
            self.label_calcular['text'] = '0'
        

        try:
            if self.calculo[len(self.calculo)-1] not in ('-','x','+','÷'):
                self.sinal_mais['state'] = 'normal'
                self.sinal_sub['state'] = 'normal'
                self.sinal_divi['state'] = 'normal'
                self.sinal_multi['state'] = 'normal'
        except IndexError:
            print('\033[1;31mNao tem nada aqui\033[m')


    def AoQuadrado(self):
        from .calculador import Calculadora
        ultimo = len(self.calculo)
        print(ultimo)
        TemOperadorEnd = False

        try:
            if self.calculo[len(self.calculo)-1] == '+' or self.calculo[len(self.calculo)-1] == 'x' or self.calculo[len(self.calculo)-1] == '÷' or self.calculo[len(self.calculo)-1] == '-':
                TemOperadorEnd = True
        except IndexError:
            print('\033[1;31mNao tem nada aqui\033[m')

        if not TemOperadorEnd:
            conta = Calculadora(self.calculo)
            self.calculo = conta.AoQuadrado2()
            self.exbir_calculo()


    def RaizAoQuadrado(self):
        from .calculador import Calculadora

        TemOperadorEnd = False

        try:    
            if self.calculo[len(self.calculo)-1] == '+' or self.calculo[len(self.calculo)-1] == 'x' or self.calculo[len(self.calculo)-1] == '÷' or self.calculo[len(self.calculo)-1] == '-':
                TemOperadorEnd = True
        except IndexError:
            print('\033[1;31mNao tem nada aqui\033[m')

        if not TemOperadorEnd:
            conta = Calculadora(self.calculo)
            self.calculo = conta.RaizAoquadrado()
            self.exbir_calculo()
                

    def Calcular(self):
        error = False

        if self.calculo == '':
            error = True

        else:

            # vai ver se tem operadores
            TemOperador = False

            for valor in self.calculo: 
                if valor == 'x' or valor == '+' or valor ==  '-' or valor ==  '÷':
                        TemOperador = True

            if not TemOperador:
                error = True

            else:
                #se o tem algum valor depois de um operador
                for indice , valor in enumerate(self.calculo):
                    if indice+1 == len(self.calculo):
                        if valor == 'x' or valor == '+' or valor == '-' or valor == '÷':
                            error = True

        if not error:
            from .calculador import Calculadora
            cal = Calculadora(self.calculo)
            self.label_calcular['text'] = str(cal.Calcular())
            self.calculo = str(cal.Calcular())


        else:
            print('Não valido')


if __name__ == '__main__':
    InterFaceGrafica()