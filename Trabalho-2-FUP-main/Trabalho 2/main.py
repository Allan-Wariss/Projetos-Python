#---imports do gerador de tela Tkinter----
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

account = { #Cria dicionario de conta, ele possui um usuario e uma senha
    "user": '',
    "password":''
}

# -----------Configs de elementos das Telas---------- #
_script = sys.argv[0]
_location = os.path.dirname(_script)

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40'  # X11 color: #666666
_ana1color = '#c3c3c3'  # Closest X11 color: 'gray76'
_ana2color = 'beige'  # X11 color: #f5f5dc
_tabfg1 = 'black'
_tabfg2 = 'black'
_tabbg1 = 'grey75'
_tabbg2 = 'grey89'
_bgmode = 'light'


class LoginWindow: #Crias classe para a primeira tela: LOGIN
    def __init__(self):

        #----- CONFIGS TELA LOGIN ----- #
        self.top = tk.Tk()
        self.top.geometry("621x488+327+117")
        self.top.minsize(120, 1)
        self.top.maxsize(1370, 749)
        self.top.resizable(1, 1)
        self.top.title("LOGIN - AGRO É TOP!")
        self.top.configure(background="#2e2625")

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.167, rely=0.068, relheight=0.877
                          , relwidth=0.691)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#0f1011")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.42, rely=0.093, height=61, width=84)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#0f1011")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Times New Roman} -size 18")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Login''')

        self.userLabel = tk.Label(self.Frame1)
        self.userLabel.place(relx=0.21, rely=0.28, height=41, width=94)
        self.userLabel.configure(activebackground="#f9f9f9")
        self.userLabel.configure(anchor='w')
        self.userLabel.configure(background="#0f1011")
        self.userLabel.configure(compound='left')
        self.userLabel.configure(disabledforeground="#a3a3a3")
        self.userLabel.configure(font="-family {Times New Roman} -size 14")
        self.userLabel.configure(foreground="#ffffff")
        self.userLabel.configure(highlightbackground="#d9d9d9")
        self.userLabel.configure(highlightcolor="black")
        self.userLabel.configure(text='''Usuario:''')

        self.userEntry = tk.Entry(self.Frame1)
        self.userEntry.place(relx=0.21, rely=0.374, height=20, relwidth=0.592)
        self.userEntry.configure(background="white")
        self.userEntry.configure(disabledforeground="#a3a3a3")
        self.userEntry.configure(font="TkFixedFont")
        self.userEntry.configure(foreground="#000000")
        self.userEntry.configure(insertbackground="black")

        self.passwordLabel = tk.Label(self.Frame1)
        self.passwordLabel.place(relx=0.21, rely=0.467, height=41, width=94)
        self.passwordLabel.configure(activebackground="#f9f9f9")
        self.passwordLabel.configure(anchor='w')
        self.passwordLabel.configure(background="#0f1011")
        self.passwordLabel.configure(compound='left')
        self.passwordLabel.configure(disabledforeground="#a3a3a3")
        self.passwordLabel.configure(font="-family {Times New Roman} -size 14")
        self.passwordLabel.configure(foreground="#ffffff")
        self.passwordLabel.configure(highlightbackground="#d9d9d9")
        self.passwordLabel.configure(highlightcolor="black")
        self.passwordLabel.configure(text='''Senha:''')

        self.passwordEntry = tk.Entry(self.Frame1)
        self.passwordEntry.place(relx=0.21, rely=0.561, height=20
                                 , relwidth=0.592)
        self.passwordEntry.configure(background="white", show='*')
        self.passwordEntry.configure(disabledforeground="#a3a3a3")
        self.passwordEntry.configure(font="TkFixedFont")
        self.passwordEntry.configure(foreground="#000000")
        self.passwordEntry.configure(highlightbackground="#d9d9d9")
        self.passwordEntry.configure(highlightcolor="black")
        self.passwordEntry.configure(insertbackground="black")
        self.passwordEntry.configure(selectbackground="#c4c4c4")
        self.passwordEntry.configure(selectforeground="black")

        self.buttonLogin = tk.Button(self.Frame1, command=self.login)
        self.buttonLogin.place(relx=0.35, rely=0.678, height=44, width=137)
        self.buttonLogin.configure(activebackground="beige")
        self.buttonLogin.configure(activeforeground="black")
        self.buttonLogin.configure(background="#00b700")
        self.buttonLogin.configure(compound='left')
        self.buttonLogin.configure(disabledforeground="#a3a3a3")
        self.buttonLogin.configure(font="-family {Segoe UI} -size 18")
        self.buttonLogin.configure(foreground="#000000")
        self.buttonLogin.configure(highlightbackground="#d9d9d9")
        self.buttonLogin.configure(highlightcolor="black")
        self.buttonLogin.configure(pady="0")
        self.buttonLogin.configure(text='''Login''')

        self.buttonRegister = tk.Button(self.Frame1, command=self.RegisterWindow)
        self.buttonRegister.place(relx=0.35, rely=0.841, height=44, width=137)
        self.buttonRegister.configure(activebackground="beige")
        self.buttonRegister.configure(activeforeground="black")
        self.buttonRegister.configure(background="#5b5b91")
        self.buttonRegister.configure(compound='left')
        self.buttonRegister.configure(disabledforeground="#a3a3a3")
        self.buttonRegister.configure(font="-family {Segoe UI} -size 18")
        self.buttonRegister.configure(foreground="#000000")
        self.buttonRegister.configure(highlightbackground="#d9d9d9")
        self.buttonRegister.configure(highlightcolor="black")
        self.buttonRegister.configure(pady="0")
        self.buttonRegister.configure(text='''Cadastrar''')
        self.top.mainloop()
    
    # ------- CONFIGS TELA CADASTRO --------#
    def RegisterWindow(self):
        self.topR = tk.Tk()
        self.topR.geometry("621x488+327+117")
        self.topR.minsize(120, 1)
        self.topR.maxsize(1370, 749)
        self.topR.resizable(1, 1)
        self.topR.title("CADASTRO - AGRO É TOP!")
        self.topR.configure(background="#2e2625")

        self.Frame1R = tk.Frame(self.topR)
        self.Frame1R.place(relx=0.167, rely=0.068, relheight=0.877, relwidth=0.691)
        self.Frame1R.configure(relief='groove')
        self.Frame1R.configure(borderwidth="2")
        self.Frame1R.configure(relief="groove")
        self.Frame1R.configure(background="#0f1011")

        self.Label1R = tk.Label(self.Frame1R)
        self.Label1R.place(relx=0.35, rely=0.093, height=61, width=184)
        self.Label1R.configure(anchor='w')
        self.Label1R.configure(background="#0f1011")
        self.Label1R.configure(compound='left')
        self.Label1R.configure(disabledforeground="#a3a3a3")
        self.Label1R.configure(font="-family {Times New Roman} -size 18")
        self.Label1R.configure(foreground="#ffffff")
        self.Label1R.configure(text='''CADASTRO''')
        self.userLabelR = tk.Label(self.Frame1R)
        self.userLabelR.place(relx=0.21, rely=0.28, height=41, width=94)
        self.userLabelR.configure(activebackground="#f9f9f9")
        self.userLabelR.configure(anchor='w')
        self.userLabelR.configure(background="#0f1011")
        self.userLabelR.configure(compound='left')
        self.userLabelR.configure(disabledforeground="#a3a3a3")
        self.userLabelR.configure(font="-family {Times New Roman} -size 14")
        self.userLabelR.configure(foreground="#ffffff")
        self.userLabelR.configure(highlightbackground="#d9d9d9")
        self.userLabelR.configure(highlightcolor="black")
        self.userLabelR.configure(text='''Usuario:''')
        self.userEntryR = tk.Entry(self.Frame1R)
        self.userEntryR.place(relx=0.21, rely=0.374, height=20, relwidth=0.592)
        self.userEntryR.configure(background="white")
        self.userEntryR.configure(disabledforeground="#a3a3a3")
        self.userEntryR.configure(font="TkFixedFont")
        self.userEntryR.configure(foreground="#000000")
        self.userEntryR.configure(insertbackground="black")

        self.passwordLabelR = tk.Label(self.Frame1R)
        self.passwordLabelR.place(relx=0.21, rely=0.467, height=41, width=94)
        self.passwordLabelR.configure(activebackground="#f9f9f9")
        self.passwordLabelR.configure(anchor='w')
        self.passwordLabelR.configure(background="#0f1011")
        self.passwordLabelR.configure(compound='left')
        self.passwordLabelR.configure(disabledforeground="#a3a3a3")
        self.passwordLabelR.configure(font="-family {Times New Roman} -size 14")
        self.passwordLabelR.configure(foreground="#ffffff")
        self.passwordLabelR.configure(highlightbackground="#d9d9d9")
        self.passwordLabelR.configure(highlightcolor="black")
        self.passwordLabelR.configure(text='''Senha:''')
        self.passwordEntryR = tk.Entry(self.Frame1R)
        self.passwordEntryR.place(relx=0.21, rely=0.561, height=20, relwidth=0.592)
        self.passwordEntryR.configure(background="white", show='*')
        self.passwordEntryR.configure(disabledforeground="#a3a3a3")
        self.passwordEntryR.configure(font="TkFixedFont")
        self.passwordEntryR.configure(foreground="#000000")
        self.passwordEntryR.configure(highlightbackground="#d9d9d9")
        self.passwordEntryR.configure(highlightcolor="black")
        self.passwordEntryR.configure(insertbackground="black")
        self.passwordEntryR.configure(selectbackground="#c4c4c4")
        self.passwordEntryR.configure(selectforeground="black")

        self.passwordLabelR2 = tk.Label(self.Frame1R)
        self.passwordLabelR2.place(relx=0.21, rely=0.667, height=41, width=200)
        self.passwordLabelR2.configure(activebackground="#f9f9f9")
        self.passwordLabelR2.configure(anchor='w')
        self.passwordLabelR2.configure(background="#0f1011")
        self.passwordLabelR2.configure(compound='left')
        self.passwordLabelR2.configure(disabledforeground="#a3a3a3")
        self.passwordLabelR2.configure(font="-family {Times New Roman} -size 14")
        self.passwordLabelR2.configure(foreground="#ffffff")
        self.passwordLabelR2.configure(highlightbackground="#d9d9d9")
        self.passwordLabelR2.configure(highlightcolor="black")
        self.passwordLabelR2.configure(text='''Confirmar Senha:''')
        self.passwordEntryR2 = tk.Entry(self.Frame1R)
        self.passwordEntryR2.place(relx=0.21, rely=0.761, height=20, relwidth=0.592)
        self.passwordEntryR2.configure(background="white", show='*')
        self.passwordEntryR2.configure(disabledforeground="#a3a3a3")
        self.passwordEntryR2.configure(font="TkFixedFont")
        self.passwordEntryR2.configure(foreground="#000000")
        self.passwordEntryR2.configure(highlightbackground="#d9d9d9")
        self.passwordEntryR2.configure(highlightcolor="black")
        self.passwordEntryR2.configure(insertbackground="black")
        self.passwordEntryR2.configure(selectbackground="#c4c4c4")
        self.passwordEntryR2.configure(selectforeground="black")

        self.buttonRegisterR = tk.Button(self.Frame1R)
        self.buttonRegisterR.place(relx=0.35, rely=0.878, height=44, width=137)
        self.buttonRegisterR.configure(activebackground="beige", command= self.register)
        self.buttonRegisterR.configure(activeforeground="black")
        self.buttonRegisterR.configure(background="#5b5b91")
        self.buttonRegisterR.configure(compound='left')
        self.buttonRegisterR.configure(disabledforeground="#a3a3a3")
        self.buttonRegisterR.configure(font="-family {Segoe UI} -size 18")
        self.buttonRegisterR.configure(foreground="#000000")
        self.buttonRegisterR.configure(highlightbackground="#d9d9d9")
        self.buttonRegisterR.configure(highlightcolor="black")
        self.buttonRegisterR.configure(pady="0")
        self.buttonRegisterR.configure(text='''Cadastrar''')
        self.topR.mainloop()

    def wrongpassword(self): # Tela Senha invalida
        self.topW = tk.Tk()
        self.topW.geometry("500x70+390+317")
        self.topW.minsize(120, 1)
        self.topW.resizable(1, 1)
        self.topW.title("INVALIDO!!!")

        self.Label1W = tk.Label(self.topW)
        self.Label1W.place(relx=0.36, rely=0.093, height=61, width=884)
        self.Label1W.configure(anchor='w')
        
        self.Label1W.configure(disabledforeground="#a3a3a3")
        self.Label1W.configure(font="-family {Times New Roman} -size 13")
        self.Label1W.configure(foreground="#000000")
        self.Label1W.configure(text='''SENHAS DIFERENTES!''')



#------------------------------------------------Main------------------------------------------------#
    def main(self): #Essa função será chamada quando o usuario estiver LOGADO

    # ------------------------------Funções------------------------------------ #

        # FUNÇÕES de Leituras Tarefa 1, Chamadas em prints
        def readUserSeg1():
            with open ('irrigação/segunda/segunda_registro.txt', 'r') as Seg1:
                names = Seg1.readlines()
                names = list(map(lambda x: x.replace('\n', ''), names)) #Tirar o \n da LEITURA
                print(names)
        def readUserTer1():
            with open ('irrigação/terca/terca_registro.txt', 'r') as Ter1:
                names = Ter1.readlines()
                names = list(map(lambda x: x.replace('\n', ''), names)) #Tirar o \n da LEITURA
                print(names)
        def readUserQua1():
            with open ('irrigação/quarta/quarta_registro.txt', 'r') as Qua1:
                names = Qua1.readlines()
                names = list(map(lambda x: x.replace('\n', ''), names)) #Tirar o \n da LEITURA
                print(names)
        def readUserQui1():
            with open ('irrigação/quinta/quinta_registro.txt', 'r') as Qui1:
                names = Qui1.readlines()
                names = list(map(lambda x: x.replace('\n', ''), names)) #Tirar o \n da LEITURA
                print(names)
        def readUserSex1():
            with open ('irrigação/sexta/sexta_registro.txt', 'r') as Sex1:
                names = Sex1.readlines()
                names = list(map(lambda x: x.replace('\n', ''), names)) #Tirar o \n da LEITURA
                print(names)

        #FUNÇÕES de Leituras Tarefa 2, Chamadas em prints
        def readUserSeg2():
            with open ('colheita/segunda/segunda_registro.txt', 'r') as Seg2:
                names = Seg2.readlines()
                names = list(map(lambda x: x.replace('\n', ''), names)) #Tirar o \n da LEITURA
                print(names)
        def readUserTer2():
            with open ('colheita/terca/terca_registro.txt', 'r') as Ter2:
                names = Ter2.readlines()
                names = list(map(lambda x: x.replace('\n', ''), names)) #Tirar o \n da LEITURA
                print(names)
        def readUserQua2():
            with open ('colheita/quarta/quarta_registro.txt', 'r') as Qua2:
                names = Qua2.readlines()
                names = list(map(lambda x: x.replace('\n', ''), names)) #Tirar o \n da LEITURA
                print(names)
        def readUserQui2():
            with open ('colheita/quinta/quinta_registro.txt', 'r') as Qui2:
                names = Qui2.readlines()
                names = list(map(lambda x: x.replace('\n', ''), names)) #Tirar o \n da LEITURA
                print(names)
        def readUserSex2():
            with open ('colheita/sexta/sexta_registro.txt', 'r') as Sex2:
                names = Sex2.readlines()
                names = list(map(lambda x: x.replace('\n', ''), names)) #Tirar o \n da LEITURA
                print(names)


    # -----------------------------Funções MAIN------------------------------------ #

        #--------------------------------------------------------------------#
        #ADICIONAR USUARIOS DOS DIAS TAREFA 1
        def addUserSeg1():
            global account
            with open ('irrigação/segunda/segunda_registro.txt', 'a') as regSeg1:
                regSeg1.write(account["user"] + '\n')
        def addUserTer1():
            global account
            with open ('irrigação/terca/terca_registro.txt', 'a') as regTer1:
                regTer1.write(account["user"] + '\n')
        def addUserQua1():
            global account
            with open ('irrigação/quarta/quarta_registro.txt', 'a') as regQua1:
                regQua1.write(account["user"] + '\n')
        def addUserQui1():
            global account
            with open ('irrigação/quinta/quinta_registro.txt', 'a') as regQui1:
                regQui1.write(account["user"] + '\n')
        def addUserSex1():
            global account
            with open ('irrigação/sexta/sexta_registro.txt', 'a') as regSex1:
                regSex1.write(account["user"] + '\n')

        #ADICIONAR USUARIOS DOS DIAS TAREFA 2
        def addUserSeg2():
            global account
            with open ('colheita/segunda/segunda_registro.txt', 'a') as regSeg2:
                regSeg2.write(account["user"] + '\n')
        def addUserTer2():
            global account
            with open ('colheita/terca/terca_registro.txt', 'a') as regTer2:
                regTer2.write(account["user"] + '\n')
        def addUserQua2():
            global account
            with open ('colheita/quarta/quarta_registro.txt', 'a') as regQua2:
                regQua2.write(account["user"] + '\n')
        def addUserQui2():
            global account
            with open ('colheita/quinta/quinta_registro.txt', 'a') as regQui2:
                regQui2.write(account["user"] + '\n')
        def addUserSex2():
            global account
            with open ('colheita/sexta/sexta_registro.txt', 'a') as regSex2:
                regSex2.write(account["user"] + '\n')

        # -------------DELETAR INFORMAÇÕES DE TODAS AS LISTAS------------- #
        def deleteALL():
            #Leitura Tarefa 2 para usar em tuplas
            Seg1 = open ('irrigação/segunda/segunda_registro.txt', 'w')
            Ter1 = open ('irrigação/terca/terca_registro.txt', 'w')
            Qua1 = open('irrigação/quarta/quarta_registro.txt', 'w')
            Qui1 = open ('irrigação/quinta/quinta_registro.txt', 'w')
            Sex1 = open ('irrigação/sexta/sexta_registro.txt', 'w')


            #Leitura Tarefa 2 para usar em tuplas
            Seg2 = open ('colheita/segunda/segunda_registro.txt', 'w')
            Ter2 = open ('colheita/terca/terca_registro.txt', 'w')
            Qua2 = open('colheita/quarta/quarta_registro.txt', 'w')
            Qui2 = open ('colheita/quinta/quinta_registro.txt', 'w')
            Sex2 = open ('colheita/sexta/sexta_registro.txt', 'w')

        # -------------------------Lista e Tuplas--------------------------- #
            #Organização de tarefas e seus dias
            irrigacao = (Seg1, Ter1, Qua1, Qui1, Sex1)
            colheita = (Seg2, Ter2, Qua2, Qui2, Sex2)
            tasks = [irrigacao, colheita]

            #FUNÇÕES DE RESETAR LISTAS TAREFA 1
            global account
            for i in range (5):
                irrigacao[i].write('')
                irrigacao[i].close() #Fechando Arquivos


            #FUNÇÕES DE RESETAR LISTAS TAREFA 2
            for i in range (5):
                colheita[i].write('')
                irrigacao[i].close() #Fechando Arquivos

        #-----------------------------TESTE DE CONSOLE MAIN------------------------------------#

        # TAREFA 1
        print('Registre que dia você vai fazer a irrigação: ')
        print('2 - Seg\n3 - Ter\n4 - Qua\n5 - Qui\n6 - Sex\n0 - Sair\ndel - deletar todas as listas')
        choose = input()
        if choose == '2':
            addUserSeg1()
            readUserSeg1()
        elif choose == '3':
            addUserTer1()
            readUserTer1()
        elif choose == '4':
            addUserQua1()
            readUserQua1()
        elif choose == '5':
            addUserQui1()
            readUserQui1()
        elif choose == '6':
            addUserSex1()
            readUserSex1()
        elif choose == '0':
            pass
        elif choose == 'del':
            deleteALL()
        else:
            print('Opção inválida.')

        # TAREFA 2
        print('Registre que dia você vai fazer a COLHEITA: ')
        print('2 - Seg\n3 - Ter\n4 - Qua\n5 - Qui\n6 - Sex\n0 - Sair\ndel - deletar todas as listas')
        choose = input()
        if choose == '2':
            addUserSeg2()
            readUserSeg2()
        elif choose == '3':
            addUserTer2()
            readUserTer2()
        elif choose == '4':
            addUserQua2()
            readUserQua2()
        elif choose == '5':
            addUserQui2()
            readUserQui2()
        elif choose == '6':
            addUserSex2()
            readUserSex2()
        elif choose == '0':
            pass
        elif choose == 'del':
            deleteALL()
        else:
            print('Opção inválida.')

#--------------------Funções Regsitro e Login------------------#
    def register(self): #Registrar novo usuário
        global account
        account["user"] = self.userEntryR.get()

        # ------- Verifica se senha está vazia ou igual -------- # 
        password = self.passwordEntryR.get()
        passwordConfirm = self.passwordEntryR2.get()
        if password == '' or passwordConfirm == '' or password != passwordConfirm:
            self.wrongpassword()
        elif password == passwordConfirm:
            account["password"] = self.passwordEntryR.get()
            self.topR.destroy() #Sai da tela de CADASTRO ao terminar o CADASTRO

            # Se senha forem compativeis CADASTRA o Usuário e a Senha
            with open('users.txt', 'a') as archiveUsers:
                archiveUsers.write(account["user"] + '\n')
            with open('passwords.txt', 'a') as archivePasswords:
                archivePasswords.write(account["password"] + '\n')  

    def login(self): #Logar com conta e senha correspondentes
        global account
        with open('users.txt', 'r') as archiveUsers:
            users = archiveUsers.readlines() #Lê linhas de usuarios
        with open('passwords.txt', 'r') as archivePasswords:
            passwords = archivePasswords.readlines() #Lê linhas das senhas

        users = list(map(lambda x: x.replace('\n', ''), users))         #Tira \n da verificação
        passwords = list(map(lambda x: x.replace('\n', ''), passwords)) #Tira \n da verificação

        account["user"] = self.userEntry.get()
        account["password"] = self.passwordEntry.get()
        logged = False

        for i in range(len(users)):
            if account["user"] == users[i] and account["password"] == passwords[i]: #Verifica se usuario linha[i] equvale a senha linha[i]
                logged = True
                print('usuário logado')
                self.top.destroy() #Terminar o LOGIN a tela é fechada
                self.main() #Usuario logado, a main inicia
        if not logged:
            print('usuário inválido')

    #-----------------------------TESTE DE CONSOLE INICIO------------------------------------#
    '''while True:
        print('(1)Logar ou (2)Cadastrar? - (0) SAIR')
        choose = input()
        if choose == "1":
            account["user"] = input('Escreva seu usuario: ')  #Nome do usuario
            account["password"] = input('Escreva sua senha: ')#Senha do usuario
            login() #Tenta logar
        elif choose == "2":
            account["user"] = input('Escreva seu usuario: ')  #Nome do usuario para registrar
            account["password"] = input('Escreva sua senha: ')#Senha do usuario para registrar
            register() #Registra
        elif choose == "0" or choose == "sair" :
            break
        else:
            print('Opção invalida') #Se o usuario escrever ABSURDOS'''
LoginWindow()