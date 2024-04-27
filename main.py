from tkinter import * #Importação da tkinter para a execução de uma interface

root = Tk() #Criação da janela principal


class funcoes(): #Classe para organizar as funções que serão utilizadas no sistema

    def limpar_tela(self): #função que limpa os dados dos inputs
        self.decimal_entry.delete(0, END)
        self.binario_entry.delete(0, END)
        self.octal_entry.delete(0, END)
        self.hexadecimal_entry.delete(0, END)      
   
    # 1. Implementação computacional com funções 
    #Funções para realizar as conversões sem utilizando bibliotecas do python, essão são as funções que efetivamente estão implementadas no sistema        
    def converter_decimal(self, event=None): #função que converte o número decimal nas demais opções
             
            decimal = int(self.decimal_entry.get()) # Coletando o número do input decimal
            binario = bin(decimal)[2:] # convertendo o número para binario
            octal = oct(decimal)[2:] # convertendo o número para octal 
            hexadecimal = hex(decimal)[2:].upper() # convertendo o número para hexadecimal,
            self.binario_entry.delete(0, END) #limpar os dados do input binário
            self.binario_entry.insert(END, binario), #inseri o resultado no input binário
            self.octal_entry.delete(0, END) #limpar os dados do input octal
            self.octal_entry.insert(END, octal) #inseri o resultado no input octal
            self.hexadecimal_entry.delete(0, END) #limpar os dados do input hexadecimal
            self.hexadecimal_entry.insert(END, hexadecimal) #inseri o resultado no input hexadecimal
       
    def converter_binario(self, event=None): #função que converte o número binário nas demais opções
        
            binario = self.binario_entry.get() # Coletando o número do input binário
            decimal = int(binario, 2) # convertendo o número para decimal
            octal = oct(decimal)[2:] # convertendo o número para octal
            hexadecimal = hex(decimal)[2:].upper() # convertendo o número para hexadecimal
            self.decimal_entry.delete(0, END) #limpar os dados do input decimal
            self.decimal_entry.insert(END, decimal) #inseri o resultado no input decimal
            self.octal_entry.delete(0, END) #limpar os dados do input octal
            self.octal_entry.insert(END, octal) #inseri o resultado no input octal
            self.hexadecimal_entry.delete(0, END) #limpar os dados do input hexadecimal
            self.hexadecimal_entry.insert(END, hexadecimal)  #inseri o resultado no input hexadecimal

    def converter_octal(self, event=None): #função que converte o número octal nas demais opções
       
            octal = self.octal_entry.get() # Coletando o número do input octal
            decimal = int(octal, 8) # convertendo o número para decimal
            binario = bin(decimal)[2:] # convertendo o número para binario
            hexadecimal = hex(decimal)[2:].upper() # convertendo o número para hexadecimal
            self.decimal_entry.delete(0, END)
            self.decimal_entry.insert(END, decimal)
            self.binario_entry.delete(0, END)
            self.binario_entry.insert(END, binario)
            self.hexadecimal_entry.delete(0, END)
            self.hexadecimal_entry.insert(END, hexadecimal)
       
    def converter_hexadecimal(self, event=None): #função que converte o número hexadecimal nas demais opções
        
            hexadecimal = self.hexadecimal_entry.get() # Coletando o número do input hexadecimal
            decimal = int(hexadecimal, 16) # convertendo o número para decimal
            binario = bin(decimal)[2:] # convertendo o número para binario
            octal = oct(decimal)[2:].upper() # convertendo o número para octal
            self.decimal_entry.delete(0, END)
            self.decimal_entry.insert(END, decimal)
            self.binario_entry.delete(0, END)
            self.binario_entry.insert(END, binario)
            self.octal_entry.delete(0, END)
            self.octal_entry.insert(END, octal) 
            
    #3.	Implementação computacional manual         
    #Funções para realizar as conversões sem utilizar bibliotecas do python    
    def decimal_para_binario(self, decimal):
        binary = ""
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal = decimal // 2
        return binary if binary else "0"

    def decimal_para_octal(self, decimal):
        octal = ""
        while decimal > 0:
            octal = str(decimal % 8) + octal
            decimal = decimal // 8
        return octal if octal else "0"

    def decimal_para_hexadecimal(self, decimal):
        hex_chars = "0123456789ABCDEF"
        hexadecimal = ""
        while decimal > 0:
            hexadecimal = hex_chars[decimal % 16] + hexadecimal
            decimal = decimal // 16
        return hexadecimal if hexadecimal else "0"

    def binario_para_decimal(self, binary):
        decimal = 0
        binary = binary[::-1]  # invertendo a string binária
        for i in range(len(binary)):
            if binary[i] == '1':
                decimal += 2 ** i
        return decimal

    def octal_para_decimal(self, octal):
        decimal = 0
        octal = octal[::-1]  # invertendo a string octal
        for i in range(len(octal)):
            decimal += int(octal[i]) * (8 ** i)
        return decimal

    def hexadecimal_para_decimal(self, hexadecimal):
        hex_chars = "0123456789ABCDEF"
        decimal = 0
        hexadecimal = hexadecimal[::-1]  # invertendo a string hexadecimal
        for i in range(len(hexadecimal)):
            decimal += hex_chars.index(hexadecimal[i]) * (16 ** i)
        return decimal        

class Application(funcoes): #criação de uma classe para organizar os itens gráficos da janela
   
    def __init__(self): #função para iniciar a janela

        self.root = root #Como a várivel root é global, é preciso informar que a várival root global é a mesma que a de dentro da função
        self.tela() #Chama a função tela que está as configurações gráficas
        self.frames_da_tela() #Chama o frame/container
        self.widgets_frame1() #Chama os widgets/objetos
        root.mainloop() #Executa a tela

    def tela(self): # função para configurar as determinações da janela

        self.root.title('Calculadora') #Alteração do título da janela
        self.root.configure(background='DarkGray') #Alteração do cor de background
        self.root.geometry('600x500') #Definição do tamanho inicial da janela
        self.root.resizable(True, True) #Definindo que a janela seja responsiva, o 1º True é de horizontal e o 2º de vertical
        self.root.maxsize(width=800, height=600) #Definição da altura e largura máxima que a janela pode ter
        self.root.minsize(width=400, height=300) #Definição da altura e largura mínima que a janela pode ter

    def frames_da_tela(self): #função que cria os frames/Containers
        self.frame_1 = Frame(self.root, bd = 8, bg= 'lightGray', highlightbackground='lightblue', highlightthickness=3) #Cria um container na tela
        self.frame_1.place(relx= 0.010, rely= 0.01, relwidth = 0.98, relheight = 0.98) #Posicionamento do container na tela 

    def widgets_frame1(self): #função para criar todos os widgets/objetos da telas

        ###Criação dos botões
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=3, bg='#7791B6', font=('verdana', 10, 'bold'), command=self.limpar_tela )#Cria o botão que irá limpar os dados após a conversão
        self.bt_limpar.place(relx =0.25, rely=0.65, relwidth=0.48, relheight=0.10) #Posicionamento do botão na tela

        ###Criando as labels
        self.lb_decimal = Label(self.frame_1, text="Decimal", bg= 'lightGray', font=('verdana', 10, 'bold')) #Cria a label decimal
        self.lb_decimal.place(relx=0.015, rely=0.02, relwidth=0.97) #Posiciona a label na tela

        self.lb_binario = Label(self.frame_1, text="Binário", bg= 'lightGray', font=('verdana', 10, 'bold')) #Cria a label binário
        self.lb_binario.place(relx=0.015, rely=0.18, relwidth=0.97) #Posiciona a label na tela

        self.lb_octal = Label(self.frame_1, text="Octal", bg= 'lightGray', font=('verdana', 10, 'bold')) #Cria a label octal
        self.lb_octal.place(relx=0.015, rely=0.34, relwidth=0.97) #Posiciona a label na tela

        self.lb_hexadecimal = Label(self.frame_1, text="Hexadecimal", bg= 'lightGray', font=('verdana', 10, 'bold')) #Cria a label hexadecimal
        self.lb_hexadecimal.place(relx=0.015, rely=0.5, relwidth=0.97) #Posiciona a label na tela

        ###Criando os inputs/entry
        self.decimal_entry = Entry(self.frame_1) #Cria o input/entry decimal
        self.decimal_entry.place(relx=0.015, rely=0.08, relwidth=0.97)  #Posiciona o input/entry na tela
        self.decimal_entry.bind("<KeyRelease>", self.converter_decimal)
        
        self.binario_entry = Entry(self.frame_1) #Cria o input/entry  binário
        self.binario_entry.place(relx=0.015, rely=0.24, relwidth=0.97) #Posiciona o input/entry na tela
        self.binario_entry.bind("<KeyRelease>", self.converter_binario)

        self.octal_entry = Entry(self.frame_1) #Cria o input/entry octal
        self.octal_entry.place(relx=0.015, rely=0.40, relwidth=0.97) #Posiciona o input/entry na tela
        self.octal_entry.bind("<KeyRelease>", self.converter_octal)

        self.hexadecimal_entry = Entry(self.frame_1) #Cria o input/entry hexadecimal
        self.hexadecimal_entry.place(relx=0.015, rely=0.56, relwidth=0.97) #Posiciona o input/entry na tela
        self.hexadecimal_entry.bind("<KeyRelease>", self.converter_hexadecimal)
      
Application()