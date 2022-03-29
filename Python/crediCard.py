from datetime import date
from attr import dataclass
from payment import Payment


class crediCard(Payment):
    number = int
    cuv = int
    date = date

    def __init__(self, id, number, cuv, date):
        super(crediCard, self).__init__(id)
        self.number = number
        self.cuv = cuv
        self.date = date
