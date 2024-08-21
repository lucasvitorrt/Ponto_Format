# ------ Ponto Format -----
# Adição de 'Ponto e Vírgula', 'Aspas e Vírgula' e
# Busca de uma META(Valor específico) através de variação de soma
# em um conjunto de caracteres copiados do excel
# ou de alguma grade de bando de dados.
#
# By @Lucas Vitor.
#
import PySimpleGUI as sg
import subprocess as sp
import functions as f

var = []
reset = 0

# Comando para fechar o cmd assim que abrir o executavel!
sp.Popen('cmd', shell=True)

# Tema da janela
sg.theme('BrownBlue')

# Layout da janela
layout = [
    [sg.Frame(layout=[
        [sg.Checkbox('Aspas e Vírgula', key='aspas_virgula'), sg.T(' ' * 12),
         sg.Checkbox('Ponto e Vírgula', key='ponto_virgula'), sg.T(' ' * 12),
         sg.Checkbox('Soma Meta', key='soma_meta'), sg.T('   Meta:'),
         sg.Input(size=(8, 1), key='entrada_meta', font=('', 9))]],
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
        k = i.replace(',', '.')
        vet2.append(k.replace('\n', ''))


# Função de execução principal.
def begin(window, reseto):
    global test
    test = 1
    while True:
        event, values = window.Read()
        window.FindElement('output').Update('')
        read_enter(values, vet, vet2)
        if event == 'Sair':
            break
        if event == 'Limpar':
            window.FindElement('output').Update('')
            window.FindElement('entrada').Update('')
            window.FindElement('entrada_meta').Update('')
            reseto = 1
            break
        else:
            #ASPAS E VÍRGULA
            if event == 'Processar' and values['aspas_virgula'] is True and values['ponto_virgula'] is False:
                if str(vet2[0]) != '':
                    j = 0
                    for i in vet2:
                        if j == len(vet2) - 1:
                            print('\'{}\''.format(i))
                        else:
                            print('\'{}\','.format(i))
                        j += 1
            #
            #PONTO E VÍRGULA
            elif event == 'Processar' and values['ponto_virgula'] is True and values['aspas_virgula'] is False:
                j = 0
                for i in vet2:
                    if j == len(vet2) - 1:
                        print('{}'.format(i), end='')
                    else:
                        print('{};'.format(i), end='')
                    j += 1
            #
            #BUSCA META
            elif event == 'Processar' and values['soma_meta'] is True and (values['aspas_virgula'] or values['ponto_virgula']) is False:
                meta = str(values['entrada_meta']).replace(',', '.')
                if meta == '':
                    print('Adicione um valor como META')
                else:
                    meta = float(meta)
                    n = int(len(vet2))
                    ##matriz de análise através de vetor.
                    if n == 1 and vet2[0] == '':
                        print('Sem valores de entrada!')
                    else:
                        array = f.matriz(n, 2)
                        for i in range(0, n):
                            if vet2[i] != '':
                                array[i][1] = float(vet2[i])
                            else:
                                vet2.pop(i)
                        n = int(len(vet2))
                        for i in range(0, n):
                            var.append(pow(2, i))
                        x = sum(var)
                        total = format(x, "b")
                        for i in range(0, x + 1):
                            soma = 0.0
                            f.serializa(format(i, "b"), total)
                            for j in range(0, n):
                                array[j][0] = f.ajst[j]
                            for k in range(0, n):
                                soma = float(soma) + float(array[k][0]) * float(array[k][1])
                            if round(soma, 2) == meta:
                                test = 0
                                tes = []
                                for p in range(0, n):
                                    if float(array[p][0]) * float(array[p][1]) != 0.0:
                                        tes.append(float(array[p][0]) * float(array[p][1]))
                                for m in tes:
                                    print(str(m).replace('.', ','))
                                n = 0
                                break
                        array.clear()
                        if test:
                            print('Nenhum Valor encontrado')
            #
            else:
                sg.PopupOK('Selecione uma opção \n     de formatação.', icon=('C:\icon.ico'))
    return reseto


while True:
    loop = begin(window, reset)
    if loop == 1:
        reset = 0
        begin(window, reset)
    else:
        break
