# Stock Portfolio Tracker

# Predefined stock prices (you can update these manually)
stock_prices = {
    "AAPL": 180,    # Apple
    "GOOGL": 135,   # Alphabet
    "TSLA": 250,    # Tesla
    "MSFT": 330,    # Microsoft
    "AMZN": 140     # Amazon
}

# Your stock holdings (quantity of each stock)
portfolio = {
    "AAPL": 10,
    "GOOGL": 5,
    "TSLA": 8,
    "MSFT": 12,
    "AMZN": 6
}

# Function to calculate total investment
def calculate_portfolio_value(prices, holdings):
    total_value = 0
    print("Your Portfolio Value:")
    print("---------------------")
    for stock, qty in holdings.items():
        if stock in prices:
            value = prices[stock] * qty
            total_value += value
            print(f"{stock} - {qty} shares × ${prices[stock]} = ${value}")
    print("---------------------")
    print(f"Total Investment Value: ${total_value}")

# Run portfolio tracker
calculate_portfolio_value(stock_prices, portfolio)