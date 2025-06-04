import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.isLogin = False
        self.id = None
        self.password = None

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

    def login(self, id, password):
        if self.id == id and self.password == password:
            self.isLogin = True
            return True
        return False
    
    def register(self, id, passsword):
        if self.isLogin:
            return False
        else:
            self.id = id
            self.password = passsword
            return True
    
    def is_login(self):
        return self.isLogin
        
        


