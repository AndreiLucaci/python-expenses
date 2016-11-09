from src.models import expenses
from src.util.validator_types import ValidatorTypes


class Validator:
    @staticmethod
    def validate_input(original_input, original_type):
        if original_type == ValidatorTypes.expense:
            return isinstance(original_input, expenses.Expenses)
        if original_type == ValidatorTypes.number:
            return isinstance(original_input, (int, float, complex))
