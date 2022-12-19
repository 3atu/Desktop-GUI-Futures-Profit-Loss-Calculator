ticker = input("Enter ticker: ")
purchase_price = float(input("Enter purchase price: "))
selling_price = float(input("Enter selling price: "))
contract_size = float(input("Enter contract size: "))

match ticker:
#ES - 0.25 index points = $12.50
    case 'es':
        tick_size = 0.25
        contract_amount = 12.50
        tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
        dollar_value = abs(tick_value*contract_amount)
        print(f"ticks: {tick_value} | profit/loss: ${dollar_value}")

#NQ - 0.25 index points = $5.00
    case 'nq':
        tick_size = 0.25
        contract_amount = 5.00
        tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
        dollar_value = abs(tick_value*contract_amount)
        print(f"ticks: {tick_value} | profit/loss: ${dollar_value}")

#RTY - 0.10 index points = $5.00
    case 'rty':
        tick_size = 0.10
        contract_amount = 5.00
        tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
        dollar_value = abs(tick_value*contract_amount)
        print(f"ticks: {tick_value} | profit/loss: ${dollar_value}")

#YM - 1.0 index points = $5.00
    case 'ym':
        tick_size = 1.00
        contract_amount = 5.00
        tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
        dollar_value = abs(tick_value*contract_amount)
        print(f"ticks: {tick_value} | profit/loss: ${dollar_value}")

#GC - 0.10 per troy ounce = $10.00
    case 'gc':
        tick_size = 0.10
        contract_amount = 10.00
        tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
        dollar_value = abs(tick_value*contract_amount)
        print(f"ticks: {tick_value} | profit/loss: ${dollar_value}")

#CL - 0.01 per barrel = $10.00
    case 'cl':
        tick_size = 0.01
        contract_amount = 10.00
        tick_value = abs(((purchase_price - selling_price)*contract_size)/tick_size)
        dollar_value = abs(tick_value*contract_amount)
        print(f"ticks: {tick_value} | profit/loss: ${dollar_value}")