from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        print("5. 로그인")
        print("6. 회원가입")
        choice = input("선택 > ")

        if choice == "1":
            if not budget.is_login():
                print("로그인 먼저 진행해주세요.\n")
                continue

            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            if not budget.is_login():
                print("로그인 먼저 진행해주세요.\n")
                continue
            budget.list_expenses()

        elif choice == "3":
            if not budget.is_login():
                print("로그인 먼저 진행해주세요.\n")
                continue
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        elif choice == "5":
            if budget.is_login():
                print("이미 로그인 중입니다!\n")
                continue

            print("로그인을 진행합니다.\n")
            id = input("아이디 입력: ")
            password = input("비밀번호 입력: ")
            if budget.login(id, password):
                print("로그인 성공!")
            else:
                print("로그인 실패!")

        elif choice == "6":
            print("회원가입을 진행합니다.\n")
            id = input("아이디 입력: ")
            password = input("비밀번호 입력: ")

            if budget.register(id, password):
                print("회원가입 완료!")
            else:
                print("이미 계정이 존재합니다.")

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
