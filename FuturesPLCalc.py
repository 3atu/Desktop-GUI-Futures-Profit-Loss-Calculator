import PySimpleGUI as sg

def calculate(values):
    ticker = ticker_list[[values[("Ticker", i)] for i in range(len(tickers))].index(1)]
    tick_size, contract_amount = tickers[ticker]
    position = "Long" if values[("Position", 0)] else "Short"
    purchase_price = float(values['Entry'])
    selling_price  = float(values['Exit'])
    contract_size  = float(values['Contract'])

    tick_value = (((purchase_price - selling_price)*contract_size)/tick_size)
    dollar_value = (tick_value*contract_amount)
    
    if position == "Long":
        tick_value = abs(tick_value)
        dollar_value = abs(dollar_value)
    return tick_value, dollar_value

#dictionary [key:value] of ticker (key) and list (value)
tickers = {
    'ES' : (0.25, 12.50),
    'NQ' : (0.25,  5.00),
    'RTY': (0.10,  5.00),
    'YM' : (1.00,  5.00),
    'GC' : (0.10, 10.00),
    'CL' : (0.01, 10.00),
}
ticker_list = list(tickers.keys())
positions = ['Long', 'Short']

keys = {
    'Entry':'Entry price',
    'Exit':'Exit price',
    'Contract':'Contract size',
}

sg.theme('Dark')
sg.set_options(font=('Helvetica', 10))

layout = [
    [sg.Text("Ticker:",   size=10)] + [sg.Radio(tick, "Radio 1", key=("Ticker", i)) for i, tick in enumerate(tickers)],
    [sg.Text("Position:", size=10)] + [sg.Radio(pos,  "Radio 2", key=("Position", i)) for i, pos in enumerate(positions)]] + [
    [sg.Text(text, size=10), sg.InputText(size=10, expand_x=True, key=key)] for key, text in keys.items()] + [
    [sg.Text("Result"), sg.Text(text_color="white", key="Output")],
    [sg.Push(), sg.Button("Reset"), sg.Button("Calculate", button_color=('white', '#007339'))],
]

window = sg.Window('Futures Profit/Loss Calculator', layout=layout)

while True:

    event, values = window.read()
    #print(event, values)

    if event == sg.WIN_CLOSED:
        break

    elif event == "Calculate":
        tick_value, dollar_value = calculate(values)
        result = f"ticks: {tick_value} | profit/loss: ${dollar_value}"
        window['Output'].update(result)

    elif event == "Reset":
        for key in keys:
            window[key].update('')

window.close()