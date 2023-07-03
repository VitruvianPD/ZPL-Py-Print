import PySimpleGUI as sg    
import shutil
import socket  
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")
copias = [i for i in range(1, 100)]
loop = 0

target = "\\"+"\\"+(socket.gethostname())+"\\ZDesigner"

s1 = sg.Spin(copias, initial_value=1, readonly=True, size=3, enable_events=True, key='copy')
sg.theme('Reddit')  

layout = [[sg.Text('Insira o Texto a ser impresso')],
          [sg.Text('Modelo',size=(7, 1)),sg.Input(key='-IN-')],
          [sg.Text('Data', size=(7, 1)), sg.InputText(key='data',default_text = d1, size=(11,1)),sg.Text('Qtd', size=(3,1)),s1], 
          [sg.Button('Imprimir')]]      

window = sg.Window('Impressão de Codigo de Barras', layout)      

while True:                             
    event, values = window.read() 
    print(event, values) 
       
    with open("C:\Temp\impressao.prn","w") as file:
        file.write("^XA^MD27^MD20~SD25^FO80,15 ^FT30,30^AAN,18,10^FH^FDData:\n")
        file.write(values['data'])
        file.write("^FS^FX ^BY1,2,30 ^FO60,80 ^BC,50,N^FD\n")
        file.write(values['-IN-'])
        file.write("^FS ^FT80,150^AAN,18,10^FH^FD\n")
        file.write(values['-IN-'])
        file.write("^FS ^XZ\n")
        loop_len = (values['copy'])  

    if event == 'Imprimir':      
        
        while loop != loop_len:
           shutil.copyfile("C:\Temp\impressao.prn", target)
           loop = loop + 1     
           print(loop) 
        break    

    if event == sg.WIN_CLOSED or event == 'Exit':
     break

window.close()   
    ##if event == sg.WIN_CLOSED or event == 'Exit':
   