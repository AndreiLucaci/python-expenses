from src.models import expenses
from src.util.validationTypes import ValidationTypes
from src.util.validator import Validator


class Appartment:
    def __init__(self, number):
        self._number = number
        self._expenses = {
            expenses.Expenses.gas: 0,
            expenses.Expenses.heating: 0,
            expenses.Expenses.sewer: 0,
            expenses.Expenses.water: 0,
            expenses.Expenses.other: 0
        }

    def set_payment(self, expense, value):
        if not Validator.validate_input(expense, ValidationTypes.expense) \
                or not Validator.validate_input(value, ValidationTypes.number):
            return False

        self._expenses[expense] = value
        return True

    def unset_payment(self, expense):
        if not Validator.validate_input(expense, ValidationTypes.expense):
            return False

        self.__reset_expense(expense)
        return True

    def __reset_expense(self, expense):
        self._expenses[expense] = 0
