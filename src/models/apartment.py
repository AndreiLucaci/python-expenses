from src.models import expenses
from src.util.validator_types import ValidatorTypes
from src.util.validator import Validator


class Apartment:
    def __init__(self, number):
        self.__number = number
        self.__expenses = {
            expenses.Expenses.gas: 0,
            expenses.Expenses.heating: 0,
            expenses.Expenses.sewer: 0,
            expenses.Expenses.water: 0,
            expenses.Expenses.other: 0
        }

    def set_expense(self, expense, value):
        if not Validator.validate_input(expense, ValidatorTypes.expense) \
                or not Validator.validate_input(value, ValidatorTypes.number):
            return False

        self.__expenses[expense] = value
        return True

    def unset_expense(self, expense):
        if not Validator.validate_input(expense, ValidatorTypes.expense):
            return False

        self.__reset_expense(expense)
        return True

    def get_expense(self, expense=None):
        if expense is None:
            return sum(self.__expenses.values())

        if not Validator.validate_input(expense, ValidatorTypes.expense):
            return -1

        return self.__expenses[expense]

    def __reset_expense(self, expense):
        self.__expenses[expense] = 0
