import PySimpleGUI as sg

sg.theme('DarkGreen3')


layout = [
  [sg.Text('Massa'), sg.InputText(key='kg')],
  [sg.Text('Altura'), sg.InputText(key='alt')],
  [sg.Push(), sg.Button('Calcular'), sg.Button('Sair'),sg.Push()]
  ]
  
window = sg.Window('Calculadora de Energia Potencial', layout)

while True:
  event, values = window.read()
  
  if event == sg.WINDOW_CLOSED or event == 'Sair':
    break
  
  elif event == 'Calcular':
    try:
      massa = float(values['kg'])
      altura = float(values['alt'])
      gravidade = 10 
      ep = massa * altura * gravidade
      sg.Popup (f'O resultado eh {ep:.2f} J')
    except:
      sg.Popup (f'Insira os valores!')

window.close()
