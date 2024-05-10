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

        self.orderbook_update_LTC_sell_count = 0
        self.orderbook_update_LTC_buy_count = 0
        self.orderbook_update_ETH_sell_count = 0
        self.orderbook_update_ETH_buy_count = 0
        self.orderbook_update_BTC_sell_count = 0
        self.orderbook_update_BTC_buy_count = 0

    def on_trade_update(self, ticker: str, side: str, price: float, quantity: float) -> None:
        """Called whenever two orders match. Could be one of your orders, or two other people's orders.

        Parameters
        ----------
        ticker
            Ticker of orders that were matched ("ETH", "BTC", or "LTC")
        side
            Side of orders that were matched ("BUY" or "SELL")
        price
            Price that trade was executed at
        quantity
            Volume traded
        """
        print(f"Python Trade update: {ticker} {side} {price} {quantity}")

    def on_orderbook_update(
            self, ticker: str, side: str, price: float, quantity: float
    ) -> None:
        """Called whenever the orderbook changes. This could be because of a trade, or because of a new order, or both.
        Returns the total quantity available at the given level

        Parameters
        ----------
        ticker
            Ticker that has an orderbook update ("ETH", "BTC", or "LTC")
        side
            Which orderbook was updated ("BUY" or "SELL")
        price
            Price of orderbook that has an update
        quantity
            Volume placed into orderbook
        """

        print(f"Python Orderbook update: {ticker} {side} {price} {quantity}")
        if ticker == "LTC" and side == "SELL":
            price_ltc = price
            self.orderbook_update_LTC_sell_count += 1
            if self.orderbook_update_LTC_sell_count >= 30:
                # Stop collecting after 30 updates
                print("Collected 30 Litecoin sell prices. Stopping collection.")
                place_market_order("SELL", "ETH", 1, price_ltc)
            print(self.orderbook_update_LTC_sell_count)



        if ticker == "LTC" and side == "BUY":
            price_ltc = price
            self.orderbook_update_LTC_buy_count += 1
            if self.orderbook_update_LTC_buy_count >= 30:
                print("Collected 30 Litecoin sell prices. Stopping collection.")
                place_market_order("BUY", "ETH", 1, price_ltc)
            print(self.orderbook_update_LTC_buy_count)


        if ticker == "ETH" and side == "SELL":
            price_eth = price
            self.orderbook_update_ETH_sell_count += 1
            if self.orderbook_update_ETH_sell_count >= 30:
                # Stop collecting after 30 updates
                print("Collected 30 Etherium sell prices. Stopping collection.")
                place_market_order("SELL", "ETH", 1, price_eth)
            print(self.orderbook_update_ETH_sell_count)


        if ticker == "ETH" and side == "BUY":
            price_eth = price
            self.orderbook_update_ETH_buy_count += 1
            if self.orderbook_update_ETH_buy_count >= 30:
                print("Collected 30 Etherium sell prices. Stopping collection.")
                place_market_order("BUY", "ETH", 1, price_eth)
            print(self.orderbook_update_ETH_buy_count)


        if ticker == "BTC" and side == "SELL":
            price_btc = price
            self.orderbook_update_BTC_sell_count += 1
            if self.orderbook_update_BTC_sell_count >= 30:
                # Stop collecting after 30 updates
                print("Collected 30 Bitcoin sell prices. Stopping collection.")
                place_market_order("SELL", "BTC", 1, price_btc)
            print(self.orderbook_update_BTC_sell_count)


        if ticker == "BTC" and side == "BUY":
            price_btc = price
            self.orderbook_update_BTC_buy_count += 1
            if self.orderbook_update_BTC_buy_count >= 30:
                print("Collected 30 Bitcoin sell prices. Stopping collection.")
                place_market_order("BUY", "BTC", 1, price_btc)
            print(self.orderbook_update_BTC_buy_count)






    def on_account_update(
            self,
            ticker: str,
            side: str,
            price: float,
            quantity: float,
            capital_remaining: float,

    ) -> None:
        """Called whenever one of your orders is filled.

        Parameters
        ----------
        ticker
            Ticker of order that was fulfilled ("ETH", "BTC", or "LTC")
        side
            Side of order that was fulfilled ("BUY" or "SELL")
        price
            Price that order was fulfilled at
        quantity
            Volume of order that was fulfilled
        capital_remaining
            Amount of capital after fulfilling order
        """
        print(
            f"Python Account update: {ticker} {side} {price} {quantity} {capital_remaining}"
        )
