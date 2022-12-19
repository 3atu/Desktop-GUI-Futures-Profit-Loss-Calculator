
from user_input import ticker, position, purchase_price, selling_price, contract_size

"""
- User selects a futures contract
- User selects position
- User enters purchase price
- User enters selling price
- Print profit/loss, ticks, contract size
"""

while True:
   
    def futures_calc(ticker):
        #ES - 0.25 index points = $12.50
        if ticker == "es":
            tick_size = 0.25
            contract_amount = 12.50

            if position == "l":
                tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = abs(tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")
            else:
                tick_value = (((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = (tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")

        #NQ - 0.25 index points = $5.00
        elif ticker == "nq":
            tick_size = 0.25
            contract_amount = 5.00

            if position == "l":
                tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = abs(tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")
            else:
                tick_value = (((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = (tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")            

        #RTY - 0.10 index points = $5.00
        elif ticker == "rty":
            tick_size = 0.10
            contract_amount = 5.00

            if position == "l":
                tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = abs(tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")
            else:
                tick_value = (((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = (tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")      

        #YM - 1.0 index points = $5.00
        elif ticker == 'ym':
            tick_size = 1.00
            contract_amount = 5.00

            if position == "l":
                tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = abs(tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")
            else:
                tick_value = (((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = (tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")      

        #GC - 0.10 per troy ounce = $10.00
        elif ticker == 'gc':
            tick_size = 0.10
            contract_amount = 10.00

            if position == "l":
                tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = abs(tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")
            else:
                tick_value = (((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = (tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")      

        #CL - 0.01 per barrel = $10.00
        elif ticker == 'cl':
            tick_size = 0.01
            contract_amount = 10.00

            if position == "l":
                tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = abs(tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")
            else:
                tick_value = (((purchase_price - selling_price)*contract_size)/tick_size)
                dollar_value = (tick_value*contract_amount)
                return(f"ticks: {tick_value} | profit/loss: ${dollar_value}")      
        
    break


if __name__ == "__main__":
    print(futures_calc(ticker))
