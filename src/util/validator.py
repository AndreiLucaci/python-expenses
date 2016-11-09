from src.models import expenses
from src.models.filter_types import FilterTypes
from src.util.validator_types import ValidatorTypes


class Validator:
    @staticmethod
    def validate_input(original_input, original_type):
        if original_type == ValidatorTypes.expense:
            return isinstance(original_input, expenses.Expenses)
        if original_type == ValidatorTypes.number:
            return isinstance(original_input, (int, float, complex))
        if original_type == ValidatorTypes.list:
            return isinstance(original_input, list)
        if original_type == ValidatorTypes.filter:
            return isinstance(original_input, FilterTypes)