import requests
import traceback

CURRENCY_API = "eace0dc0-7665-11ec-9c39-813e50af74bf"

def currencyExchange(target_currency, currency_to_convert):
    try:
        tc = currency_to_convert
        URL= f"https://freecurrencyapi.net/api/v2/latest?apikey={CURRENCY_API}&base_currency={target_currency}"

        r = requests.get(URL)
        data = r.json()
        
        
        d = data['data']
        keys = list(d.items())
        target = d.get(tc)
        
        if target == None:
            raise Exception("Target currency not valid")

        else:
            print(f"1 {target_currency} is equal to: {target} {tc}")
            

    except Exception as f:
        print("Either your target currency or your currency to convert is NOT A VALID CURRENCY, please check spelling and enter using all capital letters")
        

target = input("Enter your target currency")
cc = input("Enter the currency you wish to convert to the target currency")
currencyExchange(target, cc)