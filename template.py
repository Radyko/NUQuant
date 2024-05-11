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
        self.delta_volume = None
        self.current_balance = 100000
        self.buy_price = None
        self.sell_price = None
        self.buy_greater_ctr = 0
        self.buy_lesser_ctr = 0
        self.sell_greater_ctr = 0
        self.sell_lesser_ctr = 0

    # def execute_trade(self, delta_volume):
    #     if delta_volume > 0:
    #         if self.buy_price is not None:
    #             place_market_order("BUY", "ETH", 1, self.buy_price)
    #         else:
    #             print("Error: Cannot execute trade. Buy price is not available.")
    #     elif delta_volume < 0:
    #         if self.sell_price is not None:
    #             place_market_order("SELL", "ETH", 1, self.sell_price)
    #         else:
    #             print("Error: Cannot execute trade. Sell price is not available.")

    def on_trade_update(self, ticker: str, side: str, price: float, quantity: float) -> None:
        total_eth_volume = 0
        total_eth_sell_volume = 0
        total_eth_buy_volume = 0
        self.delta_volume = 0

        print(f"Python Trade update: {ticker} {side} {price} {quantity}")

        total_eth_volume += 1

        if side == "SELL":
            total_eth_sell_volume += 1
        elif side == "BUY":
            total_eth_buy_volume += 1

        self.delta_volume = ((total_eth_buy_volume - total_eth_sell_volume) / total_eth_volume)

        # self.execute_trade(delta_volume)
        
        print(self.buy_lesser_ctr)
        print(self.buy_greater_ctr)
        print(self.sell_lesser_ctr)
        print(self.sell_greater_ctr)

    def on_orderbook_update(self, ticker: str, side: str, price: float, quantity: float) -> None:
        if ticker == "ETH" and self.delta_volume is not None:
            if side == "BUY" and self.delta_volume > 0:
                self.buy_greater_ctr += 1
            if side == "BUY" and self.delta_volume < 0:
                self.buy_lesser_ctr += 1
            if side == "SELL" and self.delta_volume > 0:
                self.sell_greater_ctr += 1
            if side == "SELL" and self.delta_volume < 0:
                self.sell_lesser_ctr += 1


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
