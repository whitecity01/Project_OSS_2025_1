import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.categories = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")
    
    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)
            print(f"카테고리에 [{category}]가 추가되었습니다!\n")
        else:
            print("경고: 이미 존재하는 카테고리입니다.\n")

    def print_category_list(self):
        print(f"현재 존재하는 카테고리: {', '.join(self.categories)}\n")
    
    def is_category_contain(self, category):
        if category not in self.categories:
            return False
        return True
    
    def is_catecory_empty(self):
        if not self.categories:
            return True
        return False
