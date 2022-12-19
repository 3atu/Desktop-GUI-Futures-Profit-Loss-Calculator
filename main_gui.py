import PySimpleGUI as sg
import functions


ticker_options = ['ES', 'NQ', 'RTY', 'YM', 'GC', 'CL']
position_options = ['Long', 'Short']



while True:
   
    def futures_calc(ticker):
        #ES - 0.25 index points = $12.50
        if ticker == "ES":
            tick_size = 0.25
            contract_amount = 12.50

            if position == "Long":
                tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = abs(tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")
            else:
                tick_value = (((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = (tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")

        #NQ - 0.25 index points = $5.00
        elif ticker == "NQ":
            tick_size = 0.25
            contract_amount = 5.00

            if position == "Long":
                tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = abs(tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")
            else:
                tick_value = (((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = (tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")            

        #RTY - 0.10 index points = $5.00
        elif ticker == "RTY":
            tick_size = 0.10
            contract_amount = 5.00

            if position == "Long":
                tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = abs(tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")
            else:
                tick_value = (((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = (tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")      

        #YM - 1.0 index points = $5.00
        elif ticker == 'YM':
            tick_size = 1.00
            contract_amount = 5.00

            if position == "Long":
                tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = abs(tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")
            else:
                tick_value = (((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = (tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")      

        #GC - 0.10 per troy ounce = $10.00
        elif ticker == 'GC':
            tick_size = 0.10
            contract_amount = 10.00

            if position == "Long":
                tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = abs(tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")
            else:
                tick_value = (((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = (tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")      

        #CL - 0.01 per barrel = $10.00
        elif ticker == 'CL':
            tick_size = 0.01
            contract_amount = 10.00

            if position == "Long":
                tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = abs(tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")
            else:
                tick_value = (((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = (tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")      
        
    break


###


sg.theme('Dark')

label1 = sg.Text("Ticker:")
ticker_buttons = [[sg.Radio(tick,1) for tick in ticker_options]]
"""
radio_ticker1 =sg.Radio('ES', "RADIO", default=False, key='es')
radio_ticker2 =sg.Radio('NQ', "RADIO", default=False, key='nq')
radio_ticker3 =sg.Radio('RTY', "RADIO", default=False, key='rty')
radio_ticker4 =sg.Radio('YM', "RADIO", default=False, key='ym')
radio_ticker5 =sg.Radio('GC', "RADIO", default=False, key='gc')
radio_ticker6 =sg.Radio('CL', "RADIO", default=False, key='cl')
"""

label2 = sg.Text("Position:")
position_buttons = [[sg.Radio(pos,2) for pos in position_options]]
"""
radio_position1 =sg.Radio('Long', "RADIO2", default=False, key='long')
radio_position2 =sg.Radio('Short', "RADIO2", default=False, key='short')
"""
label3 = sg.Text("Entry price:")
input_box3 = sg.InputText(size =(10, 1), key="entry")

label4 = sg.Text("Exit price:")
input_box4 = sg.InputText(size =(10, 1), key="exit")

label5 = sg.Text("Contract size:")
input_box5 = sg.InputText(size =(10, 1), key="contract")

label6 = sg.Text("Result:")
output_label = sg.Text(key="output", text_color="white")

calculate_button = sg.Button("Calculate", key='calculate', button_color=('white', '#007339'))
reset_button = sg.Button("Reset", key='reset'),


layout_GUI = [[label1],
                [ticker_buttons],
                [label2],
                [position_buttons],
                 [label3],
                 [input_box3],
                [label4],
                 [input_box4],
                [label5],
                [input_box5],
                [label6],
                [output_label],
                [calculate_button],
                [reset_button]]

#window
window = sg.Window('Futures Profit/Loss Calculator', 
                    layout=layout_GUI, 
                    font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "calculate":
            window.perform_long_operation(futures_calc, '-FUNCTION COMPLETED-')
            tick_value = values['entry']
            dollar_value = values['exit']
            contract_size = values['contract']
            #calc = futures_calc(values[''])

            es= values[0] 
            nq= values[1]           
            rty= values[2]          
            ym= values[3] 
            gc=values[4] 
            cl= values[5]

            l = values[6]
            s = values[7]

            print(type(tick_value))
            result = f"ticks: {tick_value} | profit/loss: ${dollar_value}"
            window['output'].update(result)

        case "reset":
            window['entry'].update('')
            window['exit'].update('')
            window['contract'].update('')
            window['output'].update('')

        case sg.WIN_CLOSED:
            break

window.close()