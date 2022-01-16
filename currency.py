import requests
import traceback
import asyncio

CURRENCY_API = "eace0dc0-7665-11ec-9c39-813e50af74bf"

def currencyExchange():
    try:
        URL= f"https://freecurrencyapi.net/api/v2/latest?apikey={CURRENCY_API}&base_currency=CAD"

        r = requests.get(URL)
        data = r.json()
        
        d = data['data']
        keys = list(d.items())
        print(f"As of the latest currency exchange rate update, 1 CAD is equal to: ")
        i = 0

        while i < len(d):
            k = list(keys[i])

            print(f"{k[1]} {k[0]}")
            i+=1
       

    except Exception as f:
        print(f)
        traceback.print_exc()

currencyExchange()