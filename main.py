import tkinter as tk
from tkinter import ttk
import requests
from config import API_KEY

def main():
    window = tk.Tk()
    window.title('BTC Price in Local Currency')
    window.geometry('300x200')

    label_currency = tk.Label(window, text='Select currency:')
    label_currency.pack()

    currencies = ['USD', 'EUR', 'GBP', 'CNY', 'JPY']
    combo_currency = ttk.Combobox(window, values=currencies)
    combo_currency.pack()

    label_result = tk.Label(window, text='')
    label_result.pack()

    def show_btc_price():
        def fetch_btc_price(selected_currency):
            api_key = API_KEY
            base_url = 'https://rest.coinapi.io/v1/exchangerate/BTC'
            headers = {'X-CoinAPI-Key': api_key}
            response = requests.get(f'{base_url}/{selected_currency}', headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                return data['rate']
            else:
                print(f"Error: {response.status_code} - {response.text}")
                return None

        selected_currency = combo_currency.get()
        btc_price = fetch_btc_price(selected_currency)
        if btc_price:
            label_result.config(text=f'BTC price in {selected_currency}: {btc_price}')
        else:
            label_result.config(text='Error fetching BTC price')

    btn_fetch = tk.Button(window, text='Fetch BTC Price', command=show_btc_price)
    btn_fetch.pack()

    window.mainloop()

if __name__ == '__main__':
    main()
