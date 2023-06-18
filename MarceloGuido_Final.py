import serial
import time
from datetime import datetime
import tkinter as tk

# Configurações da porta serial
porta_serial = serial.Serial('COM3', 9600)  # Substitua 'COM3' pela porta serial correta

# Variáveis de intensidade das cores
intensidade_hora = '00'
intensidade_minuto = '00'
intensidade_segundo = '00'


def enviar_hora_computador():
    now = datetime.now()
    hora = now.hour
    minuto = now.minute
    segundo = now.second
    enviar_hora(hora, minuto, segundo)


def simular_variacao_tempo():
    botao_simular.config(state=tk.DISABLED)  # Desabilita o botão de simulação
    botao_parar.config(state=tk.NORMAL)  # Habilita o botão de parar
    global parar_simulacao
    parar_simulacao = False  # Define a flag para False antes de iniciar a simulação
    for hora in range(24):
        for minuto in range(60):
            for segundo in range(0,60,10):
                enviar_hora(hora, minuto, segundo)
                horario = f"{hora:02d}:{minuto:02d}:{segundo:02d}"
                campo_horario.config(text=horario)
                campo_horario.update()
                if parar_simulacao:
                    botao_simular.config(state=tk.NORMAL)  # Habilita o botão de simulação
                    botao_parar.config(state=tk.DISABLED)  # Desabilita o botão de parar
                    return
    botao_simular.config(state=tk.NORMAL)  # Habilita o botão de simulação
    botao_parar.config(state=tk.DISABLED)  # Desabilita o botão de parar
    return




def parar_simulacao():
    global parar_simulacao
    parar_simulacao = True


def enviar_hora(hora, minuto, segundo):
    global intensidade_hora, intensidade_minuto, intensidade_segundo
    hora_str = str(hora).zfill(2)
    minuto_str = str(minuto).zfill(2)
    segundo_str = str(segundo).zfill(2)
    horario = f"{hora_str} {minuto_str} {segundo_str}"
    campo_horario.config(text=horario)
    campo_horario.update()

    # Enviar valores para a serial
    dados_serial = f"{hora} {minuto} {segundo}\n"
    porta_serial.write(dados_serial.encode('utf-8'))

    # Ler valores da serial
    leitura_serial = porta_serial.readline().decode('utf-8').strip()
    valores = leitura_serial.split(' ')
    if len(valores) == 3:
        intensidade_hora = valores[0]
        intensidade_minuto = valores[1]
        intensidade_segundo = valores[2]

    atualizar_cores()


def atualizar_cores():
    cor_hora = f"#00{intensidade_hora}00"
    cor_minuto = f"#{intensidade_minuto}{intensidade_minuto}00"
    cor_segundo = f'#0000{intensidade_segundo}'
    bola_hora.config(text=cor_hora, bg=cor_hora)
    bola_minuto.config(text=cor_minuto, bg=cor_minuto)
    bola_segundo.config(text=cor_segundo, bg=cor_segundo)
    root.update()


# Interface gráfica do Tkinter
root = tk.Tk()
root.title("Envio de Horário")

# Campo para mostrar o horário sendo enviado
campo_horario = tk.Label(root, font=("Arial", 24), width=10, background="light blue")
campo_horario.place(x=145,y=50)

# Bola para representar a intensidade da cor da hora
bola_hora = tk.Label(root, width=10, height=5, bd=2, relief=tk.RAISED)
bola_hora.place(x=100,y=300)

# Bola para representar a intensidade da cor do minuto
bola_minuto = tk.Label(root, width=10, height=5, bd=2, relief=tk.RAISED)
bola_minuto.place(x=200,y=300)

# Bola para representar a intensidade da cor do segundo
bola_segundo = tk.Label(root, width=10, height=5, bd=2, relief=tk.RAISED)
bola_segundo.place(x=300,y=300)

# Botão para enviar a hora do computador
botao_hora_computador = tk.Button(root, width=25, text="Enviar Hora do Computador", command=enviar_hora_computador)
botao_hora_computador.place(x=145,y=150)

# Botão para simular a variação de tempo
botao_simular = tk.Button(root, width=25, text="Simular Variação de Tempo", command=simular_variacao_tempo)
botao_simular.place(x=145,y=200)

# Botão para parar a simulação
botao_parar = tk.Button(root, width=25, text="Parar Simulação", command=parar_simulacao, state=tk.DISABLED)
botao_parar.place(x=145,y=250)

root.geometry("450x450+0+0")
root.configure(background="light blue")

root.mainloop()
