from src.ctrl.apartment_controller import ApartmentController
from src.models.expenses import Expenses
from src.repo.inmemory_repo import InMemoryRepository

repo = InMemoryRepository(2)
ctrl = ApartmentController(repo)

ctrl.add_expense(1, Expenses.water, 200)

result = ctrl.get_aparment_with_expense_greater_than(100)

print(result[0])

print(ctrl.repo.apartments[0])