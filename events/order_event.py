from events.event import Event


class OrderEvent(Event):

    def __init__(self, symbol, order_type, quantity, direction, stop_loss=None, take_profit=None, price=None,
                 note=None, trade_id_related_to=None, trade_to_exit_direction=None):
        """
        Initialises the order type, setting whether it is
        a Market order ('MKT'), Limit order ('LMT'), Stop order ('STP') or Exit ('EXIT'), has
        a quantity (integral) and its direction ('BUY' or 'SELL').

        Parameters:
        symbol - The instrument to trade.
        order_type - 'MKT', 'LMT', 'STP' for Market, Limit, Stop or Exit.
        quantity - Non-negative integer for quantity.
        direction - 'BUY' or 'SELL' for long or short.
        stop_loss - The price where the order is closed at market automatically with loss.
        take_profit - The price where the order is closed at market automatically with profit.
        price - The price for stop or limit orders
        note
        trade_id_related_to
        trade_to_exit_direction
        """
        super().__init__('ORDER', symbol)

        self.order_type = order_type
        self.quantity = quantity
        self.direction = direction
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.price = price
        self.note = note
        self.trade_id_related_to = trade_id_related_to
        self.trade_to_exit_direction = trade_to_exit_direction

    def get_as_string(self) -> str:
        return 'Order: Symbol=%s, Type=%s, Quantity=%s, Direction=%s, StopLoss=%f, TakeProfit=%f, Price=%f, ' \
               'Note=%s, TradeIdRelatedTo=%d, TradeToExitDirection=%s' % \
               (self.symbol, self.order_type, self.quantity, self.direction,
                self.get_default_value_if_none_or_value(self.stop_loss, 0),
                self.get_default_value_if_none_or_value(self.take_profit, 0),
                self.get_default_value_if_none_or_value(self.price, 0),
                self.get_default_value_if_none_or_value(self.note, ''),
                self.get_default_value_if_none_or_value(self.trade_id_related_to, 0),
                self.get_default_value_if_none_or_value(self.trade_to_exit_direction, ''))

    def get_default_value_if_none_or_value(self, value, default_value):
        if value is None:
            return default_value
        else:
            return value
