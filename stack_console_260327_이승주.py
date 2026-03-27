# 메뉴
def print_menu():
    print("=" * 50)
    print("\t1.Push\t2.Pop\t3.Peek\t0.Exit")
    print("=" * 50)

# 스택에 값 추가
def stack_push(stack):
    if stack_IsFull(stack):
        return
    else:
        number = int(input("> 데이터 입력 : "))
        stack.append(number)
        print(f"> 현재 스택 상태 {stack}")

# 스택에서 값 뽑기
def stack_pop(stack):
    if stack_IsEmpty(stack):
        return
    else:
        data = stack.pop()
        print(f"> 가져온 데이터 : {data}")
        print(f"> 현재 스택 상태 {stack}")

# 스택의 top의 값 보기
def stack_peek(stack):
    if stack_IsEmpty(stack):
        return
    else:
        data = stack[-1]
        print(f"> 가져온 데이터 : {data}")
        print(f"> 현재 스택 상태 {stack}")

# 스택이 비었는지 확인
def stack_IsEmpty(stack):
    if len(stack) == 0:
        print("> Stack이 비어 있습니다.")
        print(f"> 현재 스택 상태 {stack}")
        return True
    else:
        return False

# 스택이 가득 차있는지 확인
def stack_IsFull(stack):
    if len(stack) == 5:
        print("> Stack이 차 있어서 더 이상 추가할 수 없습니다.")
        print(f"> 현재 스택 상태 {stack}")
        return True
    else:
        return False

stack = []

while True:
    print_menu()
    choice = int(input("> 메뉴 선택 : "))
    match choice:
        case 1:
            stack_push(stack)
            print()
        case 2:
            stack_pop(stack)
            print()
        case 3:
            stack_peek(stack)
            print()
        case 0:
            break
        case _:
            print("메뉴를 다시 선택해 주세요.")
            print()