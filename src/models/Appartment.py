from src.models import Expenses

class Appartment:
    def __init__(self, number):
        self._number = number
        self._knownExpenses = {
            Expenses.Expenses.gas: 0,
            Expenses.Expenses.heating: 0,
            Expenses.Expenses.sewer: 0,
            Expenses.Expenses.water: 0,
            Expenses.Expenses.other: 0
        }

    def

