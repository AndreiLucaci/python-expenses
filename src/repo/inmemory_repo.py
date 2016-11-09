from src.models.apartment import Apartment
from src.repo.base_repo import Repository
from src.util.imports import xrange
from src.util.validator import Validator
from src.util.validator_types import ValidatorTypes


class InMemoryRepository(Repository):
    def __init__(self, initial_appartments=10):
        # apartments start form 1
        self._apartments = [Apartment(i + 1) for i in xrange(initial_appartments)]

    def set_expense(self, appartment_number, expense, value):
        if self.__validate_apartment_number(appartment_number) and \
                self._validate_expense(expense) and \
                self.__validate_number_value(value):
            self._apartments[appartment_number - 1].set_expense(expense, value)

    def get_expenses(self, expense):
        pass

    def get_apartments_with_expenses_over(self, given_amount):
        pass

    def unset_expense(self, appartment_number, expense):
        if self.__validate_apartment_number(appartment_number) and \
                self._validate_expense(expense):
            self._apartments

    def unset_expense_for_type(self, exepnse):
        pass

    def __validate_apartment_number(self, appartment_number):
        if not Validator.validate_input(appartment_number, ValidatorTypes.number):
            raise ValueError('Appartment number should be a number', appartment_number)

        if appartment_number >= len(self._apartments) or appartment_number < 1:
            raise ValueError('Invalid appartment number provided', appartment_number)

        return True

    @staticmethod
    def __validate_expense(expense):
        if not Validator.validate_input(expense, ValidatorTypes.expense):
            raise ValueError('Invalid expense provided', expense)

        return True

    @staticmethod
    def __validate_number_value(value):
        if not Validator.validate_input(value, ValidatorTypes.number):
            raise ValueError('Provided input should be a number', value)

        return True
