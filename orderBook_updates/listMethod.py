class OrderBook:
    def __init__(self):
        self.bids = []  # List to store buy orders
        self.asks = []  # List to store sell orders

    def add_order(self, side, price, quantity):
        if side == "BUY":
            self.bids.append((price, quantity))
        elif side == "SELL":
            self.asks.append((price, quantity))
        else:
            raise ValueError("Side must be 'BUY' or 'SELL'.")

    def remove_order(self, side, price, quantity):
        if side == "BUY":
            self.bids.remove((price, quantity))
        elif side == "SELL":
            self.asks.remove((price, quantity))
        else:
            raise ValueError("Side must be 'BUY' or 'SELL'.")

"""not sure how to even implement this in the market"""
    def print_order_book(self):
          print("Order Book:")
          print("Bids:")
          for bid in self.bids:
              print(f"Price: {bid[0]}, Quantity: {bid[1]}")

          print("Asks:")
          for ask in self.asks:
              print(f"Price: {ask[0]}, Quantity: {ask[1]}")
