from stocks import StockExceptions



selling_stocks={
    "AA123":{
        "stock_name": "Apple Inc",
        "price": 170.00,
        "quantity": 10,
    }
}
buyed_stocks={}
stocks = {
    "AA123":{
        "stock_name": "Apple Inc",
        "price": 150.00,
        "quantity": 10,
        "status": "new"
    },
}



def add_new_stocks():
    try:
        stock_name = input("Enter the stock name you want to sell: ")
        stock_quantity = int(input(f"Enter the quantity of {stock_name} stocks you want to sell: "))
        stock_price = float(input(f"Enter the selling price of {stock_name} stocks: "))
        user_id = input("Enter your ID: ")

        if stock_name and stock_quantity and stock_price and user_id is not None:
           stocks[user_id] = {
            "quantity": stock_quantity, 
            "price": stock_price,
            "stock_name": stock_name,
            "status":"new"
        }
           print("added new stock to portfolio")
        else:
           raise StockExceptions("Enter the name,quantity,price correctly") 
        

    except ValueError as e:
       print(e)
    except StockExceptions as e:
       print(e)
       
       



def sell_stocks():
    stock_name = input("Enter the new stock name : ")
    stock_quantity = int(input(f"Enter the quantity of {stock_name} stocks : "))
    stock_price = float(input(f"Enter the price of {stock_name} stocks: "))
    user_id = input("Enter your ID: ")
    
    
    try:
        if user_id not in stocks:
         raise StockExceptions(f"{user_id} is not available in your portfolio stocks to sell.")
        elif stock_name not in stocks[user_id]:
         raise StockExceptions(f"{stock_name} not present in the user_id")
        selling_stocks[user_id] = {
            "quantity": stock_quantity, 
            "price": stock_price,
            "stock_name": stock_name
        } 

        stocks[user_id]["status"] = "sell"
        print("stock added in selling stocks")
    except StockExceptions as e:
        print(e)

def buy_stocks():
     
    if len(selling_stocks) == 0:
       raise StockExceptions("No stocks available to buy wait for the selling start")
    else:
     for items in selling_stocks.items():
         print(items)
        

     stock_name = input("Enter stock_name from the selling list: ")
     stock_quantity = int(input("Enter the quantity of stocks which need to buy: "))    
     try:
         found = None
         id= None
         for user_id , stock_info in selling_stocks.items():
             if stock_info["stock_name"].lower() == stock_name.lower():
                 found = {user_id : stock_info}
                 id = user_id
                 break
         if found is None:
             raise StockExceptions("The stock_name that entered is not available for sell")
         elif found[id]["quantity"] < stock_quantity:
             raise StockExceptions("The stocks quantity is more than the avilable to sell")
         else:
            stocks[id]["status"] = "sold"
            print("The stocks is sold")
     except StockExceptions as e:
         print(e)


def stocks_exchange():

    print("===== Do you want buy or sell the stocks =====")
    try:
     sell_buy = int(input("if you want for buy enter 0 or if you want sell enter 1 or if you want add new stock enter 2:"))
     if sell_buy == 1:
         sell_stocks()
     elif sell_buy == 2:
        add_new_stocks()
     elif sell_buy == 0:
         buy_stocks()
     else:
        raise StockExceptions("Enter the number which are provided only")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except StockExceptions as e:
       print(e)

stocks_exchange()


         








    
    