from abc import ABCMeta, abstractmethod


class Repository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_expense(self, appartment_number, expense, value):
        raise NotImplementedError()

    @abstractmethod
    def unset_expense(self, appartment_number, expense):
        raise NotImplementedError()

    @abstractmethod
    def unset_range(self, start, stop, expense):
        raise NotADirectoryError()

    @abstractmethod
    def unset_expense_for_type(self, exepnse):
        raise NotImplementedError()

    @abstractmethod
    def unset_expense_lower_than(self, value):
        raise NotImplementedError()

    @abstractmethod
    def get_apartments_with_expenses_over(self, given_amount):
        raise NotImplementedError()

    @abstractmethod
    def get_expenses(self, expense):
        raise NotImplementedError()

    @abstractmethod
    def filber_by(self, filter_type, expense, asc=True):
        raise NotImplementedError()

    @abstractmethod
    def get_expense(self, apartment_number, expense):
        raise NotImplementedError()
