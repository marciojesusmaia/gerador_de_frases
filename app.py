from random import choice
import PySimpleGUI as sg

f = []
with open('frases.txt', 'r') as arquivo:
    a = arquivo.readlines()
    for l in a:
        f.append(l.replace(',\n',''))


sg.theme('LightBlue2')

layout = [
    [sg.Text('A frase do dia é:')],
    [sg.Output(size=(50,5),key='saida')],
    # [sg.Text('',text_color='blue',font=20,key='saida')],
    [sg.Button('Gerar Frase', key='gerar')]

]

window = sg.Window('Melhore o seu dia com uma frase!!', layout=layout, finalize=True)

while True:

    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    
    elif event == 'gerar':
        window['saida'].update(choice(f))
