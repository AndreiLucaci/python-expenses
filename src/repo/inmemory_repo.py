from src.models.apartment import Apartment
from src.models.expenses import Expenses
from src.repo.base_repo import Repository
from src.util.imports import range
from src.util.validator import Validator
from src.util.validator_types import ValidatorTypes


class InMemoryRepository(Repository):
    def __init__(self, initial_appartments=10):
        # apartments start form 1
        self.__apartments = [Apartment(i + 1) for i in range(initial_appartments)]
        self.apartments = self.__apartments

    def set_expense(self, apartment_number, expense, value):
        if self.__validate_apartment_number_list(apartment_number):
            [self.__set_expense_for_one(i, expense, value) for i in apartment_number]
        else:
            self.__set_expense_for_one(apartment_number, expense, value)

    def __set_expense_for_one(self, apartment_number, expense, value):
        if self.__validate_apartment_number(apartment_number) and \
                self.__validate_expense(expense) and \
                self.__validate_number_value(value):
            self.__apartments[apartment_number - 1].set_expense(expense, value)

    def filber_by(self, filter_type, expense, asc=True):
        if self.__validate_filter_by(filter_type) and self.__validate_expense(expense):
            result = self.__apartments[:]
            result.sort(key=lambda apartment: apartment.get_expense(expense), reverse=not asc)
            return result

    def get_expense(self, apartment_number, expense=None):
        if self.__validate_apartment_number(apartment_number) and ((not expense == None and
                                                                           self.__validate_expense(expense)) or True):
            return self.__apartments[apartment_number].get_expense(expense)

    def get_expenses(self, expense):
        return [i.get_expense(expense) for i in self.__apartments]

    def get_apartments_with_expenses_over(self, given_amount):
        return [i for i in self.__apartments if i.get_expense() > given_amount]

    def unset_expense(self, apartment_number, expense):
        if self.__validate_apartment_number_list(apartment_number):
            [self.__unset_expense_for_one(i, expense) for i in apartment_number]
        else:
            self.__unset_expense_for_one(apartment_number, expense)

    def __unset_expense_for_one(self, apartment_number, expense):
        if self.__validate_apartment_number(apartment_number) and \
                self.__validate_expense(expense):
            self.__apartments[apartment_number].unset_expense(expense)

    def unset_expense_for_type(self, expense):
        if self.__validate_expense(expense):
            [i.unset_expense(expense) for i in self.__apartments]

    def unset_expense_lower_than(self, value):
        if self.__validate_number_value(value):
            [i.unset_expense(j) for i in self.__apartments if i.get_expense(j) < value for j in Expenses]

    def unset_range(self, start, stop, expense):
        if self.__validate_range(start, stop):
            self.unset_expense(range(start, stop + 1), expense)

    def __validate_apartment_number(self, appartment_number):
        if not Validator.validate_input(appartment_number, ValidatorTypes.number):
            raise ValueError('Appartment number should be a number', appartment_number)
        if appartment_number >= len(self.__apartments) or appartment_number < 1:
            raise ValueError('Invalid appartment number provided', appartment_number)
        return True

    def __validate_apartment_number_list(self, apartment_number):
        result = True
        if Validator.validate_input(apartment_number, ValidatorTypes.list):
            result = all(self.__validate_apartment_number(i) for i in apartment_number)
        return result

    def __validate_range(self, start, stop):
        if self.__validate_number_value(start) and self.__validate_number_value(stop) and start > stop:
            raise ValueError('Start should be lower or equal than stop', start, stop)
        return True

    def __validate_filter_by(self, filter_by):
        if not Validator.validate_input(filter_by, ValidatorTypes.filter):
            raise ValueError('Provided filter is unrecognized', filter_by)
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
