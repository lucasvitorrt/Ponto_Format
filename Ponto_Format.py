# ------ Ponto Format -----
# Adição de 'Ponto e Vírgula' e 'Aspas e Vírgula'
# em um conjunto de caracteres copiados do excel
# ou de alguma grade de bando de dados.
#
# By @Lucas Vitor.
#
import PySimpleGUI as sg
import subprocess as sp

# Comando para fechar o cmd assim que abrir o executavel!
sp.Popen('cmd', shell=True)

# Tema da janela
sg.theme('BrownBlue')

# Layout da janela
layout = [
    [sg.Frame(layout=[
        [sg.Checkbox('Aspas e Vírgula', key='aspas_virgula'), sg.T(' ' * 86),
         sg.Checkbox('Ponto e Vírgula', key='ponto_virgula')]],
        title='Opções de Formatação', title_color='Orange', relief=sg.RELIEF_SUNKEN,
        tooltip='Marque a caixa para escolher', font=('', 9, 'italic'))],
    [sg.Multiline(size=(85, 15), key='entrada', font=('', 9))],
    [sg.Button('Processar'), sg.Button('Limpar'), sg.T(' ' * 108), sg.Button('Sair')],
    [sg.Output(size=(85, 15), key='output', font=('', 9))],
    [sg.Text('Developed by: Lucas Vitor', size=(23, 1), font=('', 7, 'italic'), text_color='Orange')]
]
# Criação da janela principal
window = sg.Window('Ponto Format', layout, icon=('C:\icon.ico'), disable_close=True)

# Vetores para o tratamento de informação
vet = []
vet2 = []

# Função para o tratamento dos valores da entrada.
def read_enter(values, vet, vet2):
    final = ''
    vet2.clear()
    vet.clear()
    for i in values['entrada']:
        if i == '\n':
            vet.append(final)
            final = ''
        final += i
    for i in vet:
        vet2.append(i.replace('\n', ''))

# Função de execução principal.
def begin(window):
    while True:
        event, values = window.Read()
        window.FindElement('output').Update('')
        read_enter(values, vet, vet2)
        if event == 'Sair':
            break
        if event == 'Limpar':
            window.FindElement('output').Update('')
            window.FindElement('entrada').Update('')
        else:
            if event == 'Processar' and values['aspas_virgula'] is True and values['ponto_virgula'] is False:
                if str(vet2[0]) != '':
                    j = 0
                    for i in vet2:
                        if j == len(vet2) - 1:
                            print('\'{}\''.format(i))
                        else:
                            print('\'{}\','.format(i))
                        j += 1
            elif event == 'Processar' and values['ponto_virgula'] is True and values['aspas_virgula'] is False:
                j = 0
                for i in vet2:
                    if j == len(vet2) - 1:
                        print('{}'.format(i), end='')
                    else:
                        print('{};'.format(i), end='')
                    j += 1
            else:
                sg.PopupOK('Selecione uma opção \n     de formatação.', icon=('C:\icon.ico'))


begin(window)

