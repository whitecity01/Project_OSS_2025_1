from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        print("5. 카테고리 추가")
        print("6. 카테고리 목록")
        choice = input("선택 > ")

        if choice == "1":
            if budget.is_catecory_empty():
                print("경고: 현재 등록된 카테고리가 없습니다. 5번을 통해 카테고리를 추가해주십시오.\n")
                continue
            
            budget.print_category_list()
            category = input("카테고리 선택: ")
            if not budget.is_category_contain(category):
                print("경고: 존재하지 않는 카테고리입니다.\n")
                continue

            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        elif choice == "5":
            category = input("추가할 카테고리: ")
            budget.add_category(category)
            
        elif choice == "6":
            budget.print_category_list()

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
