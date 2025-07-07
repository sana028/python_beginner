
selling_stocks={}
buyed_stocks={}
stocks = {
    "AA123":{
        "stock_name": "Apple Inc.",
        "price": 150.00,
        "quantity": 10
    },
}

def sell_stocks():
    stock_name = input("Enter the stock name you want to sell: ")
    stock_quantity = int(input(f"Enter the quantity of {stock_name} stocks you want to sell: "))
    stock_price = float(input(f"Enter the selling price of {stock_name} stocks: "))
    user_id = input("Enter your ID: ")
    
    if stock_name and user_id not in stocks:
       raise ValueError(f"{stock_name} is not available in your portfolio.")
    
    selling_stocks[user_id] = {
        "quantity": stock_quantity, 
        "price": stock_price,
        "stock_name": stock_name
    } 
    
    