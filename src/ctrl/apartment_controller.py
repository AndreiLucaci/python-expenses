from src.models.expenses import Expenses
from src.models.filter_types import FilterTypes
from src.repo.base_repo import Repository
from src.util.validator import Validator
from src.util.validator_types import ValidatorTypes


class ApartmentController:
    def __init__(self, repository: Repository):
        if not Validator.validate_input(repository, ValidatorTypes.repository):
            raise ValueError('repository should be of type Repository')
        self.repo = repository

    def add_expense(self, apartment_number, expense, value):
        self.repo.set_expense(apartment_number, expense, value)

    def update_expense(self, apartment_number, expense, value):
        self.repo.set_expense(apartment_number, expense, value)

    def remove_expense(self, apartment_number):
        [self.repo.unset_expense(apartment_number, expense) for expense in Expenses]

    def remove_exepense_range(self, start, stop):
        [self.repo.unset_range(start, stop, expense) for expense in Expenses]

    def remove_expenses(self, expense):
        self.repo.unset_expense_for_type(expense)

    def get_aparment_with_expense_greater_than(self, value):
        return self.repo.get_apartments_with_expenses_over(value)

    def get_expenses(self, expense):
        return self.repo.get_expenses(expense)

    def get_total_expense(self, expense):
        return sum(self.get_expenses(expense))

    def sort_apartments_by_expense(self, expense, asc=True):
        return self.repo.filber_by(FilterTypes.expense, expense, asc)

    def get_total_expense_for_apartment(self, apartment_number):
        return self.repo.get_expense(apartment_number, None)

    def remove_expense_lower_than(self, value):
        self.repo.unset_expense_lower_than(value)


