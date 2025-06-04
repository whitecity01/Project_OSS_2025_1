import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

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
    
    # 카테고리에 해당하고 max_amount보다 작거나 같은 지출 목록 반환
    def get_list_by_category_and_under_amount(self, category, max_amount):
        category_list = self.get_category_list(category)
        under_amount_list = self.get_list_under_amount(category_list, max_amount)

        if not under_amount_list:
            print("해당하는 조건의 지출 기록이 없습니다.")
        else:
            print(f"{category}에 해당하고 {max_amount} 이하의 지출 내역:\n")
            for idx, e in enumerate(under_amount_list, 1):
                print(f"{idx}. {e}")

    def get_category_list(self, category):
        return [e for e in self.expenses if e.category == category]
    
    def get_list_under_amount(self, category_list, max_amount):
        return [e for e in category_list if e.amount <= max_amount]

