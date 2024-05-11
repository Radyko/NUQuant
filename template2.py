def place_market_order(side: str, ticker: str, quantity: float, price: float) -> bool:
    """Place a market order - DO NOT MODIFY

    Parameters
    ----------
    side
        Side of order to place ("BUY" or "SELL")
    ticker
        Ticker of order to place ("ETH", "BTC", or "LTC")
    quantity
        Volume of order to place
    price
        Price of order to place

    Returns
    -------
    True if order succeeded, False if order failed due to rate limiting
    """
class Strategy:
    def __init__(self) -> None:
        self.current_balance = 100000
        self.eth_prices = []  # List to store Ethereum prices
        self.window_size = 3  # Moving average window size
        self.buy_price = None
        self.sell_price = None

    def calculate_moving_average(self):
        if len(self.eth_prices) >= self.window_size:
            return sum(self.eth_prices[-self.window_size:]) / self.window_size
        else:
            return None

    def generate_signals(self):
        moving_avg = self.calculate_moving_average()
        if moving_avg is not None:
            if self.eth_prices[-1] > moving_avg:
                return "BUY"
            elif self.eth_prices[-1] < moving_avg:
                return "SELL"
        return None

    def execute_trade(self, signal):
        if signal == "BUY":
            if self.buy_price is not None:
                place_market_order("BUY", "ETH", 1, self.buy_price)
            else:
                print("Error: Cannot execute trade. Buy price is not available.")
        elif signal == "SELL":
            if self.sell_price is not None:
                place_market_order("SELL", "ETH", 1, self.sell_price)
            else:
                print("Error: Cannot execute trade. Sell price is not available.")

    def on_trade_update(self, ticker: str, side: str, price: float, quantity: float) -> None:
        self.eth_prices.append(price)
        signal = self.generate_signals()
        if signal is not None:
            self.execute_trade(signal)

    def on_orderbook_update(self, ticker: str, side: str, price: float, quantity: float) -> None:
        if ticker == "ETH":
            if side == "BUY":
                self.buy_price = price  # Update buy price
            elif side == "SELL":
                self.sell_price = price  # Update sell price

    def update_balance(self, amount: float) -> None:
        self.current_balance += amount
        print(f"Balance updated. Current balance: {self.current_balance}")

    def on_account_update(
            self,
            ticker: str,
            side: str,
            price: float,
            quantity: float,
            capital_remaining: float,
    ) -> None:
        print(
            f"Python Account update: {ticker} {side} {price} {quantity} {capital_remaining}"
        )
