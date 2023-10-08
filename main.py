import os
import math
import random


# 화면을 클리어하는 ㅎ마수
def clear_screen():
    os.system('cls')
    return


# 플레이어에게 계단의 개수를 입력 받은 값을 바탕으로 계단을 만드는 함수
def create_stair(row, col):
    s_matrix = [[" " for i in range(col)] for j in range(row)]
    s_matrix[0][0] = "○"
    s_matrix[0][col - 1] = "●"
    space = col - 1

    for i in range(1, row):
        for j in range(i):
            s_matrix[i][j] = "▨"

        for k in range(space + i - 1, col):
            s_matrix[i][k] = "▨"
        space -= 2

    return s_matrix


# 묵찌빠 결과에 따라 계단을 업데이트하는 함수
def update_stair(s_matrix, winner, step):
    global p_row_prev
    global p_col_prev
    global c_row_prev
    global c_col_prev

    # 먼저 전에 있던 플레이어와 컴퓨터의 위치를 빈 칸으로 초기화한다
    s_matrix[p_row_prev][p_col_prev] = " "
    s_matrix[c_row_prev][c_col_prev] = " "

    # 플레이어와 컴퓨터 중 승자를 확인하고, step의 값에 따라 승자가 이동해야 하는 칸을 각 row와 col에 업데이트 한다
    if winner == "플레이어":                                # 플레이어가 묵찌빠를 이겼을 때
        if num_stairs % 2 == 0:                           # 계단 개수가 짝수일 때
            if p_col_prev + step <= COL // 2:
                p_row_prev += step
                p_col_prev += step
            else:
                p_row_prev = COL - (p_col_prev + step) - 1
                p_col_prev += step
        else:                                             # 계단 개수가 홀수일 때
            if p_col_prev + step < COL // 2:
                p_row_prev += step
                p_col_prev += step
            else:
                p_row_prev = COL - (p_col_prev + step) - 1
                p_col_prev += step
    else:                                                 # 컴퓨터가 묵찌빠를 이겼을 때
        if num_stairs % 2 == 0:                           # 계단 개수가 짝수일 때
            if c_col_prev - step >= COL // 2:
                c_row_prev += step
                c_col_prev -= step
            else:
                c_row_prev = c_col_prev - step
                c_col_prev -= step
        else:                                             # 계단 개수가 홀수일 때
            if c_col_prev - step >= COL // 2:
                c_row_prev += step
                c_col_prev -= step
            else:
                c_row_prev = c_col_prev - step
                c_col_prev -= step

    # 업데이트한 플레이어와 컴퓨터의 row와 col을 바탕으로 s_matrix에 그림값을 넣어준다.
    if p_row_prev == c_row_prev and p_col_prev == c_col_prev:               # 플레이어와 컴퓨터가 같은 위치에 있는 상황
        s_matrix[p_row_prev][p_col_prev] = "◑"
    else:     # 플레이어나 컴퓨터가 승리 했을 때 s_matrix의 값을 벗어나는 경우가 있기 때문에 예외 처리를 하면서 각자의 위치에 그림을 넣어준다.
        if p_col_prev >= COL:
            p_col_prev = COL - 1
            p_row_prev = 0
        if c_col_prev < 0:
            c_col_prev = 0
            c_row_prev = 0
        s_matrix[p_row_prev][p_col_prev] = "○"
        s_matrix[c_row_prev][c_col_prev] = "●"


# 화면에 계단과 플레이어들을 출력하는 함수
def print_stairs(s_matrix):
    row = len(s_matrix)
    col = len(s_matrix[0])

    # 이중 for문을 사용하여
    for x in range(row):
        for y in range(col):
            print(s_matrix[x][y], end=" ")
        print()


# 화면에 게임 현황과 계단을 보여주는 함수
def print_display():
    clear_screen()
    print(f"총 계단 수: {num_stairs}")
    print(f"PLAYER:   ○  <{min(player_step, num_stairs):2d}>")
    print(f"COMPUTER: ●  <{min(com_step, num_stairs):2d}>")
    print_stairs(S_MATRIX)


# random 모듈을 활용하여 무작위로 가위, 바위, 보 중 하나를 반환하는 함수
def computer_choice():
    return random.choice(["가위", "바위", "보"])


# 플레이어가 올바른 입력값을 입력할 때까지 input을 받는 함수
def player_choice():
    player = ""
    while player not in ["가위", "바위", "보"]:
        player = input("가위, 바위, 보 중 하나 선택:")
    return player


# 플레이어와 컴퓨터의 가위바위보 결과가 돌려주는 함수
# 0이면 플레이어 승리, 1이면 무승부, 2이면 컴퓨터 승리
def check_result(p_choice, c_choice):
    if p_choice == c_choice:                  # 플레이어와 컴퓨터가 같은 것을 냈을 때
        return 1
    if p_choice == rock:
        if c_choice == paper:
            return 2
        return 0
    elif p_choice == paper:
        if c_choice == scissor:
            return 2
        return 0
    else:
        if c_choice == rock:
            return 2
        return 0


# 화면에 바위를 출력하는 함수
def print_rock():
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)


# 화면에 보를 출력하는 함수
def print_paper():
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)


# 화면에 가위를 출력하는 함수
def print_scissors():
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)


if __name__ == "__main__":

    rock = "바위"
    paper = "보"
    scissor = "가위"

    num_stairs = 0
    while num_stairs < 10 or num_stairs > 30:
        num_stairs = int(input("게임을 위한 계단의 개수를 입력해주세요. <10 ~ 30>"))

    # 화면 초기화
    clear_screen()

    # 입력된 계단의 수에서 row와 col을 계산한다
    ROW = math.ceil(num_stairs / 2) + 1
    COL = num_stairs + 1

    # player 값들 초기화
    p_row = 0
    p_col = 0
    player_step = 0

    # computer 값들 초기화
    c_row = 0
    c_col = COL
    com_step = 0

    # row와 col을 이용해서 stair matrix를 만든다
    S_MATRIX = create_stair(ROW, COL)

    p_row_prev = p_row
    p_col_prev = p_col
    c_row_prev = c_row
    c_col_prev = c_col - 1

    while True:
        # stair matrix를 출력한다
        print_display()
        input("\n계속하려면 엔터를 눌러주세요...")

        ################## 공격권 결정 가위바위보 #######################
        turn = ""     # 공격권
        while True:
            clear_screen()
            print(["공격권 결정 가위바위보"])

            # 이동 칸 수 초기화
            step = 1

            # 플레이어가 올바른 입력값을 입력할 때까지 input을 받는다
            player = player_choice()

            # 컴퓨터 무작위로 가위바위보 중 하나 선택
            com = computer_choice()
            
            # 컴퓨터 선택 출력
            print("[컴퓨터 선택]")
            if com == rock:
                print_rock()
            elif com == paper:
                print_paper()
            else:
                print_scissors()

            # 플레이어 선택 출력
            print("\n[플레이어 선택]")
            if player == rock:
                print_rock()
            elif player == paper:
                print_paper()
            else:
                print_scissors()

            # 게임 결과를 계산하고 result에 담는다
            result = check_result(player, com)
            if result == 0:
                turn = "player"
                print("[결과] 플레이어 공격, 컴퓨터 수비입니다.")
                input("\n계속하려면 엔터를 눌러주세요...")
                break
            elif result == 2:
                turn = "com"
                print("[결과] 컴퓨터 공격, 플레이어 수비입니다.")
                input("\n계속하려면 엔터를 눌러주세요...")
                break
            else:
                print("[결과] 무승부입니다")
                input("\n계속하려면 엔터를 눌러주세요...")

        ###################################################################

        ########################### 묵찌빠 #################################
        while True:
            clear_screen()
            print("[묵찌빠]")
            print(f"승리 시 이동 칸 수: {step}")

            # 플레이어가 올바른 입력값을 입력할 때까지 input을 받는다
            player = player_choice()

            # 컴퓨터 무작위로 가위바위보 중 하나 선택
            com = computer_choice()
            
            # 컴퓨터 선택 출력
            print("\n[컴퓨터 선택]")
            if com == rock:
                print_rock()
            elif com == paper:
                print_paper()
            else:
                print_scissors()

            # 플레이어 선택 출력
            print("[플레이어 선택]")
            if player == rock:
                print_rock()
            elif player == paper:
                print_paper()
            else:
                print_scissors()

            # 게임 결과를 계산하고 result에 담는다
            result = check_result(player, com)
            if result == 0:
                turn = "player"
                print("[결과] 플레이어 공격, 컴퓨터 수비입니다.")
            elif result == 2:
                turn = "com"
                print("[결과] 컴퓨터 공격, 플레이어 수비입니다.")
            else:
                print("[결과] 묵찌빠 종료")
                winner = "플레이어" if turn == "player" else "컴퓨터"

                update_stair(S_MATRIX, winner, step)
                if winner == "플레이어":
                    player_step += step
                else:
                    com_step += step

                print(f"{winner} 승, {step}칸 이동합니다")
                input("\n계속하려면 엔터를 눌러주세요...")
                clear_screen()
                break

            # 승부가 결정나지 않아 이동 칸 수를 하나 증가시킨다
            step += 1
            input("\n계속하려면 엔터를 눌러주세요...")
        ###################################################################

        # 승자가 있는지 확인하는 if문
        if player_step >= num_stairs:
            print_display()
            print()
            print("▨ " * COL)
            print(" " * (num_stairs - 10) + "플레이어 최종 승리!!!")
            print("▨ " * COL)
            print("\n게임을 종료합니다...")
            break
        elif com_step >= num_stairs:
            print_display()
            print()
            print("▨ " * COL)
            print(" " * (num_stairs - 9) + "컴퓨터 최종 승리!!!")
            print("▨ " * COL)
            print("\n게임을 종료합니다...")
            break




