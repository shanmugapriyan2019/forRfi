print("Github RFI exploited")
import requests
import pdb

res = requests.get("https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&symbols=AAPL&fields=regularMarketPrice")
# If you need to work around SSL issues, set the verify kw arg to False. For example:
# requests.get("URL_HERE", verify=False)

stock_data = res.json()
price = stock_data['quoteResponse']['result'][0]['regularMarketPrice']
print(price)
