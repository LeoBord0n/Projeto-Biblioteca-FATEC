import PySimpleGUI as sg 
import sqlite3
biblioteca = sqlite3.connect('biblioteca.db')
cursor = biblioteca.cursor()


sg.theme ('LightBlue7')
# layout do login
layoutp = [
    [sg.Text('Usuário')],

    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha', password_char = '*')],
    [sg.Button('Login'), sg.Button('Sair')],
    [sg.Text(key='Mensagem')]
]
#Layout da plataforma principal
layp = [
    [sg.Text('Digitar nome do aluno'), sg.Input(key='aluno')],
    [sg.Button('Pesquisar'), sg.Button('Adicionar novo')],
    [sg.Button('Editar dado de aluno')],
    [sg.Button('Sair')],
    [sg.Listbox(values=[], size=(40,10), key='aluno_list')]
]

adn = [
    [sg.Text('Nome do aluno:      '), sg.Input(key='cadastro')],
    [sg.Text('CPF do aluno:       '), sg.Input(key='cpf')],
    [sg.Text('Email do aluno'), sg.Input(key='email')],
    [sg.Text('Livro alocado:      '), sg.Input(key='livro')],
    [sg.Text('Data de devolução DD/MM/AA:  '), sg.Input(key='idade')],
    [sg.Button('Adicionar aluno'), sg.Button('Sair')]
]
def janela4(values4):
    deseja = [
    sg.Text('Deseja adicionar um novo aluno?'),
    sg.Button('Sim'), sg.Button('Não')
]
    window4 = sg.Window('Adicionar novo aluno?', layout=deseja)
    while True:
        event, values4 = window4.read()

#Sistema de close window
def login(values):
    if event == 'Login':
        uc = ''
        sc = ''
        usuario = values['usuario']
        senha = values['senha']
        if usuario == uc and senha == sc:
            window['Mensagem'].update('Login feito com sucesso')
            sg.popup('Usuario logado!', title = 'Login')
            janela2(values)
            window.close()
        else:
            window['Mensagem'].update('Usuário ou senha inválidos')
            sg.popup('Erro no Login', title = 'Erro')

            #Janela principal da biblioteca
def janela2 (values):            
    window2 = sg.Window('Biblioteca FATEC', layout=layp)
    while True:
        event, values2 = window2.read()
        if event == sg.WIN_CLOSED or event == 'Sair':
            break
        #Sistema de adicionar novo aluno vinculado ao commit()
        if event == 'Adicionar novo':
            janela3(values2)
def janela3(values):
    window3 = sg.Window('Adicionar aluno', layout=adn)
    while True:
        event3, values3 = window3.read()
        if event3 == sg.WIN_CLOSED or event3 == 'Sair':
            break
        elif event3 == 'Adicionar aluno':
            nome = values3['cadastro']
            cpf = values3['cpf']
            email = values3['email']
            livro = values3['livro']
            dev = values3['idade']
            while True:
                if len(nome) <3 or len(cpf) <3 or len(email) <3 or len(livro) <3 or len(dev) <3:
                    sg.popup('Nenhum dado pode ter menos de 3 carácteres. ')
                else:
                    cursor.execute("INSERT INTO aluno VALUES (?,?,?,?,?)",(nome,cpf,email,livro,dev))
                    biblioteca.commit()
                    biblioteca.close()
            
            sg.popup('Aluno adicionado com sucesso! ')
            janela4(values3)



            


window = sg.Window('Login biblioteca FATEC', layout=layoutp)
while True:
    event,values = window.read()
    if event == 'Sair' or event == sg.WIN_CLOSED:
        break
    elif event == 'Login':
        login(values)





       

       


        

    












