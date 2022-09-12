import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [
    [sg.Text('1º Bimestre'), sg.Input(key='bimestre1')],
    [sg.Text('2º Bimestre'), sg.Input(key='bimestre2')],
    [sg.Text('3º Bimestre'), sg.Input(key='bimestre3')],
    [sg.Text('4º Bimestre'), sg.Input(key='bimestre4')],
    [sg.Button('MEDIAS')]
]

window = sg.Window('Média Bolsa Família', layout, element_justification='center')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
            break
    if event == 'MEDIAS':
            b1 = values['bimestre1']
            if b1 != "":
                b1 = float(b1)
                if b1 == 0.0:
                    b1 = 100.0
            else:
                b1 = 0.0
            b2 = values['bimestre2']
            if b2 != "":
                b2 = float(b2)
                if b2 == 0.0:
                    b2 = 100.0
            else:
                b2 = 0.0
            b3 = values['bimestre3']
            if b3 != "":
                b3 = float(b3)
                if b3 == 0.0:
                    b3 = 100.0
            else:
                b3 = 0.0
            b4 = values['bimestre4']
            if b4 != "":
                b4 = float(b4)
                if b4 == 0.0:
                    b4 = 100.0
            else:
                b4 = 0
            if b1 != 0.0 and b1 != 100:
                b1 = 100 - b1
            if b2 != 0.0 and b2 != 100:
                b2 = 100 - b2
            if b3 != 0.0 and b3 != 100:
                b3 = 100 - b3
            if b4 != 0.0 and b4 != 100:
                b4 = 100 - b4
            media = []
            if b1 != 0.0:
                media.append(b1)
            if b2 != 0.0:
                media.append(b2)
            if b3 != 0.0:
                media.append(b3)
            if b4 != 0.0:
                media.append(b4)
            media = sum(media)/len(media)
            sg.Popup(f'FEVEREIRO: {b1:.2f}\nMARÇO: {b1:.2f}\nABRIL: {b2:.2f}\nMAIO: {b2:.2f}\nJUNHO: {b2:.2f}\nJULHO: {b3:.2f}\nAGOSTO: {b3:.2f}\nSETEMBRO: {b3:.2f}\nOUTUBRO: {b4:.2f}\nNOVEMBRO: {b4:.2f}\nDEZEMBRO: {b4:.2f}\n\nMÉDIA GERAL: {media:.2f}')

window.close()
