import PySimpleGUI as sg
import currency_api as ca

currency = ca.currency

input_column = [
    [sg.Text('Currency'), sg.Combo(currency, size=(5, 1), key='-INCUR-')],
    [sg.Text('Amount'), sg.In(size=(10, 1), key='-INVAL-')]
]

output_column = [
    [sg.Text('Currency'), sg.Combo(currency, size=(5, 1), key='-OUTCUR-')],
    [sg.Text('Amount'), sg.In(size=(10, 1), key='-OUTVAL-', readonly = True)]
]

cr_buttons = [
    [sg.Button('Convert'), sg.Button('Swap'), sg.Button('Reset')]
]

layout = [
    [
        [sg.Frame('Current Currency', [[sg.Column(input_column)]]),
            sg.Frame('New Currency', [[sg.Column(output_column)]])],
        [cr_buttons],
    ]
]

window = sg.Window("Currency Converter", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Convert':
        if values['-INCUR-'] == '' or values['-INVAL-'] == '' or values['-OUTCUR-'] == '':
            sg.popup('ERROR\nA value is missing!\nMake sure the appropriate boxes have been filled.', title="ERROR")
        elif values['-INCUR-'] == values['-OUTCUR-']:
            sg.popup("ERROR\nYou can't convert a currency into itself!", title="ERROR")
        else:
            try:
                #Convert INVAL to GBP
                money_mult = float(ca.repo_dicts[values['-INCUR-']])
                money_gbp = float(values['-INVAL-']) / money_mult
                #Convert to chosen currency.
                new_money_mult = float(ca.repo_dicts[values['-OUTCUR-']])
                new_money = money_gbp * new_money_mult
                #Update OUTVAL
                window['-OUTVAL-'].update(new_money)
            except:
                sg.popup("ERROR\nCurrency values must be in integer format!", title="ERROR")
    if event == 'Swap':
        incur, outcur = values['-INCUR-'], values['-OUTCUR-']
        window['-INCUR-'].update(outcur)
        window['-OUTCUR-'].update(incur)
    if event == 'Reset':
        window['-INCUR-'].update('')
        window['-INVAL-'].update('')
        window['-OUTCUR-'].update('')
        window['-OUTVAL-'].update('')
            
window.close()