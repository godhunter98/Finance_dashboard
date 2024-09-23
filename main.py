from Fetch_prices import fetch_price

portfolio = ['HDFC Bank','ICICI Bank','zomato','ICICI Securities','Kotak Mahindra Bank']

for stock in portfolio:
    print(f"{stock}: {fetch_price(stock)}")