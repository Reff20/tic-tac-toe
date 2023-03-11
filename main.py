import tkinter
from tkinter import *
from tkinter import ttk

# cores

co0 = "#FFFFFF"  # Branco
co1 = "#333333"  # Preto
co2 = "#FCC058"  # Laranja
co3 = "#38576B"  # Azul "Turquesa"
co4 = "#3297A8"  # Azul
co5 = "#FFF873"  # Amarelo
co6 = co2  # Laranja
co7 = "#E85151"  # Vermelho
co8 = co4  # Azul
fundo = "#3B3B3B"

# Janela
janela = Tk()
janela.title("")
janela.geometry("260x450")
janela.configure(bg=fundo)

frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)


# Lógica
jogador_1 = "X"
jogador_2 = "O"
score_1 = 0
score_2 = 0

table = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

jogando = "X"
joga = ''
contador = 0


jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]

jogando = 'X'
joga =''
contador = 0
contador_de_rodada = 0


def init():
    b_jogar.place(x=800, y=350)
    # pra controlar o jogo
    def controlar(i):
        global jogando
        global contador
        global jogar

        # comparando o valor recebido
        if i==str(1):
            # verificando se aquela posicao esta vazia ou nao
            if b_0['text']=='':
                # verificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[0][0]= jogando

                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                # incrementar o contador para proxima rodada
                contador+=1

        if i==str(2):
            # verificando se aquela posicao esta vazia ou nao
            if b_1['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][1] = jogando

                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                # incrementar o contador para proxima rodada
                contador+=1

        if i==str(3):
            # verificando se aquela posicao esta vazia ou nao
            if b_2['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][2]= jogando

                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                # incrementar o contador para proxima rodada
                contador+=1   

        if i==str(4):
            # verificando se aquela posicao esta vazia ou nao
            if b_3['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[1][0] = jogando

                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                # incrementar o contador para proxima rodada
                contador+=1

        if i==str(5):
            # verificando se aquela posicao esta vazia ou nao
            if b_4['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][1] = jogando

                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                # incrementar o contador para proxima rodada
                contador+=1

        if i==str(6):
            # verificando se aquela posicao esta vazia ou nao
            if b_5['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][2] = jogando

                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                # incrementar o contador para proxima rodada
                contador+=1   

        if i==str(7):
            # verificando se aquela posicao esta vazia ou nao
            if b_6['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[2][0] = jogando

                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                # incrementar o contador para proxima rodada
                contador+=1

        if i==str(8):
            # verificando se aquela posicao esta vazia ou nao
            if b_7['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][1] = jogando

                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                # incrementar o contador para proxima rodada
                contador+=1      

        if i==str(9):
            # verificando se aquela posicao esta vazia ou nao
            if b_8['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][2] = jogando

                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                # incrementar o contador para proxima rodada
                contador+=1

        # Apos o contador ser maior ou igual a 5, 
        # verifica se ouve algum vencedor de acordo 
        # com os padroes seguintes dentro da tabela
        if contador>=5:
            # linhas
            if tabela[0][0]==tabela[0][1]==tabela[0][2]!="":
                vencedor(jogando)
            elif tabela[1][0] == tabela[1][1]==tabela[1][2]!="":
                vencedor(jogando)
            elif tabela[2][0] == tabela[2][1]==tabela[2][2]!="":
                vencedor(jogando)

            # colunas
            if tabela[0][0] == tabela[1][0]==tabela[2][0]!="":
                vencedor(jogando)
            elif tabela[0][1] == tabela[1][1]==tabela[2][1]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][2]==tabela[2][2]!="":
                vencedor(jogando)


            # diagonais
            if tabela[0][0] == tabela[1][1]==tabela[2][2]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][1]==tabela[2][0]!="":
                vencedor(jogando)

            # Empate 
            if contador>=9:
                vencedor('Foi empate') 


    # pra decidir o vencedor
    def vencedor(i):
        global tabela
        global score_1
        global score_2
        global contador_de_rodada
        global contador

        # bloqueando os botoes
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'

        app_vencedor = Label(frame_baixo, text='', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2 )
        app_vencedor.place(x=40, y=220)

        if i =='X':
            score_2+=1
            app_vencedor['text'] = 'Joagador 2 venceu'
            app_o_pontos['text'] =score_2

        if i =='O':
            score_1+=1
            app_vencedor['text'] = 'Joagador 1 venceu'
            app_x_pontos['text'] =score_1

        if i=='Foi empate':
            app_vencedor['text'] = 'Foi um empate'

        def start():
            # limpando os botoes
            b_0['text']=''
            b_1['text']=''
            b_2['text']=''
            b_3['text']=''
            b_4['text']=''
            b_5['text']=''
            b_6['text']=''
            b_7['text']=''
            b_8['text']=''

            b_0['state']='normal'
            b_1['state']='normal'
            b_2['state']='normal'
            b_3['state']='normal'
            b_4['state']='normal'
            b_5['state']='normal'
            b_6['state']='normal'
            b_7['state']='normal'
            b_8['state']='normal'

            app_vencedor.destroy()
            b_jogar.destroy()

        # Botao jogar
        b_jogar = Button(frame_baixo, command=start, text='Proxima rodada', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
        b_jogar.place(x=70, y=250)


        def jogo_acabou():
            b_jogar.destroy()
            app_vencedor.destroy()

            terminar()

        if contador_de_rodada>=5:
            jogo_acabou()
        else:
            contador_de_rodada+=1
            # reiniciando a tabela
            tabela = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]
            contador = 0



    # pra terminar o jogo atual
    def terminar():
        global tabela
        global contador_de_rodada
        global score_1
        global score_2
        global contador

        tabela = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]
        contador_de_rodada = 0
        score_1 = 0
        score_2 = 0
        contador = 0

        # bloqueando os botoes
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'

        app_fim = Label(frame_baixo, text='Jogo Acabou', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2 )
        app_fim.place(x=40, y=220)

        # jogar de novo

        def jogar_denovo():
            app_x_pontos['text'] = '0'
            app_o_pontos['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()

            # chamando a funcao iniciar o jogo
            init()

        # Botao jogar denovo
        b_jogar = Button(frame_baixo, command=jogar_denovo, text='Jogar de novo', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
        b_jogar.place(x=77, y=250)

    app_vert = Label(
        frame_baixo,
        text="",
        height=28,
        width=1,
        relief="flat",
        pady=5,
        anchor="center",
        font=("Ivy 5 bold"),
        bg=co0,
        fg=co7,
    )


    app_vert.place(x=90, y=15)
    app_vert = Label(
        frame_baixo,
        text="",
        height=28,
        width=1,
        relief="flat",
        pady=5,
        anchor="center",
        font=("Ivy 5 bold"),
        bg=co0,
        fg=co7,
    )
    app_vert.place(x=160, y=15)

    app_horz = Label(
        frame_baixo,
        text="",
        width=185,
        height=2,
        relief="flat",
        padx=5,
        anchor="center",
        font=("Ivy 1"),
        bg=co0,
        fg=co7,
    )
    app_horz.place(x=30, y=80)
    app_horz = Label(
        frame_baixo,
        text="",
        width=185,
        height=2,
        relief="flat",
        padx=5,
        anchor="center",
        font=("Ivy 1"),
        bg=co0,
        fg=co7,
    )
    app_horz.place(x=30, y=150)

    # Linha 0
    b_0 = Button(
        frame_baixo,
        command=lambda:controlar('1'),
        text="",
        width=3,
        font=("Ivy 20"),
        relief="flat",
        overrelief=RIDGE,
        bg=fundo,
        fg=co7,
    )
    b_0.place(x=31, y=23)
    b_1 = Button(
        frame_baixo,
        command=lambda:controlar('2'),
        text="",
        width=3,
        font=("Ivy 20"),
        relief="flat",
        overrelief=RIDGE,
        bg=fundo,
        fg=co7,
    )
    b_1.place(x=101, y=23)
    b_2 = Button(
        frame_baixo,
        command=lambda:controlar('3'),
        text="",
        width=3,
        font=("Ivy 20"),
        relief="flat",
        overrelief=RIDGE,
        bg=fundo,
        fg=co7,
    )
    b_2.place(x=170, y=23)

    b_3 = Button(
        frame_baixo,
        command=lambda:controlar('4'),
        text="",
        width=3,
        font=("Ivy 20"),
        relief="flat",
        overrelief=RIDGE,
        bg=fundo,
        fg=co7,
    )
    b_3.place(x=31, y=92)
    b_4 = Button(
        frame_baixo,
        command=lambda:controlar('5'),
        text="",
        width=3,
        font=("Ivy 20"),
        relief="flat",
        overrelief=RIDGE,
        bg=fundo,
        fg=co7,
    )
    b_4.place(x=101, y=92)
    b_5 = Button(
        frame_baixo,
        command=lambda:controlar('6'),
        text="",
        width=3,
        font=("Ivy 20"),
        relief="flat",
        overrelief=RIDGE,
        bg=fundo,
        fg=co7,
    )
    b_5.place(x=170, y=92)

    b_6 = Button(
        frame_baixo,
        command=lambda:controlar('7'),
        text="",
        width=3,
        font=("Ivy 20"),
        relief="flat",
        overrelief=RIDGE,
        bg=fundo,
        fg=co7,
    )
    b_6.place(x=31, y=162)
    b_7 = Button(
        frame_baixo,
        command=lambda:controlar('8'),
        text="",
        width=3,
        font=("Ivy 20"),
        relief="flat",
        overrelief=RIDGE,
        bg=fundo,
        fg=co7,
    )
    b_7.place(x=101, y=162)
    b_8 = Button(
        frame_baixo,
        command=lambda:controlar('9'),
        text="",
        width=3,
        font=("Ivy 20"),
        relief="flat",
        overrelief=RIDGE,
        bg=fundo,
        fg=co7,
    )
    b_8.place(x=170, y=162)


app_x = Label(
    frame_cima,
    text="X",
    height=1,
    relief="flat",
    anchor="center",
    font=("Ivy 40 bold"),
    bg=co1,
    fg=co7,
)
app_x.place(x=25, y=10)
app_x = Label(
    frame_cima,
    text="Jogador 1",
    height=1,
    relief="flat",
    anchor="center",
    font=("Ivy 8 bold"),
    bg=co1,
    fg=co0,
)
app_x.place(x=17, y=70)
app_x_pontos = Label(
    frame_cima,
    text="0",
    height=1,
    relief="flat",
    anchor="center",
    font=("Ivy 30 bold"),
    bg=co1,
    fg=co0,
)
app_x_pontos.place(x=75, y=18)

app_separador = Label(
    frame_cima,
    text=":",
    height=1,
    relief="flat",
    anchor="center",
    font=("Ivy 30 bold"),
    bg=co1,
    fg=co0,
)
app_separador.place(x=110, y=15)

app_o = Label(
    frame_cima,
    text="O",
    height=1,
    relief="flat",
    anchor="center",
    font=("Ivy 40 bold"),
    bg=co1,
    fg=co4,
)
app_o.place(x=173, y=10)
app_o = Label(
    frame_cima,
    text="Jogador 2",
    height=1,
    relief="flat",
    anchor="center",
    font=("Ivy 8 bold"),
    bg=co1,
    fg=co0,
)
app_o.place(x=165, y=70)
app_o_pontos = Label(
    frame_cima,
    text="0",
    height=1,
    relief="flat",
    anchor="center",
    font=("Ivy 30 bold"),
    bg=co1,
    fg=co0,
)
app_o_pontos.place(x=134, y=18)


b_jogar = Button(
    frame_baixo,
    text="Jogar",
    command=init,
    width=10,
    height=1,
    font=("Ivy 10 bold"),
    relief="raised",
    overrelief=RIDGE,
    bg=fundo,
    fg=co0,
)
b_jogar.place(x=84, y=250)



janela.mainloop()
