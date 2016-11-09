from src.models import expenses
from src.util.validationTypes import ValidationTypes


class Validator:
    @staticmethod
    def validate_input(original_input, original_type):
        if original_type == ValidationTypes.expense:
            return isinstance(original_input, expenses.Expenses)
        if original_type == ValidationTypes.number:
            return isinstance(original_input, (int, float, complex))
