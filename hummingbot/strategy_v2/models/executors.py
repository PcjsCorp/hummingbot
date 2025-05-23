from decimal import Decimal
from enum import Enum
from typing import Optional

from hummingbot.core.data_type.in_flight_order import InFlightOrder


class CloseType(Enum):
    TIME_LIMIT = 1
    STOP_LOSS = 2
    TAKE_PROFIT = 3
    EXPIRED = 4
    EARLY_STOP = 5
    TRAILING_STOP = 6
    INSUFFICIENT_BALANCE = 7
    FAILED = 8
    COMPLETED = 9
    POSITION_HOLD = 10


class TrackedOrder:
    def __init__(self, order_id: Optional[str] = None):
        self._order_id = order_id
        self._order = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id: str):
        self._order_id = order_id

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, order: InFlightOrder):
        self._order = order

    @property
    def creation_timestamp(self):
        if self.order:
            return self.order.creation_timestamp
        else:
            return None

    @property
    def price(self):
        if self.order:
            return self.order.price
        else:
            return None

    @property
    def last_update_timestamp(self):
        if self.order:
            return self.order.last_update_timestamp
        else:
            return None

    @property
    def average_executed_price(self):
        if self.order:
            return self.order.average_executed_price or self.order.price
        else:
            return Decimal("0")

    @property
    def executed_amount_base(self):
        if self.order:
            return self.order.executed_amount_base
        else:
            return Decimal("0")

    @property
    def executed_amount_quote(self):
        if self.order:
            return self.order.executed_amount_quote
        else:
            return Decimal("0")

    @property
    def fee_asset(self):
        if self.order and len(self.order.order_fills) > 0:
            return list(self.order.order_fills.values())[0].fee_asset
        else:
            return None

    @property
    def cum_fees_base(self):
        if self.order:
            return self.order.cumulative_fee_paid(token=self.order.base_asset)
        else:
            return Decimal("0")

    @property
    def cum_fees_quote(self):
        if self.order:
            return self.order.cumulative_fee_paid(token=self.order.quote_asset)
        else:
            return Decimal("0")

    @property
    def is_done(self):
        if self.order:
            return self.order.is_done
        else:
            return False

    @property
    def is_open(self):
        if self.order:
            return self.order.is_open
        else:
            return False

    @property
    def is_filled(self):
        if self.order:
            return self.order.is_filled
        else:
            return False
