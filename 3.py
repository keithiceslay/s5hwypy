# Создайте программу для игры в ""Крестики-нолики"".

def ttt_play(table, i):
    if i % 2 == 0:
        player_choice = int(input('На какое место вы ходите поставить o?'))
        for k in range(len(table)):
            for j in range(len(table[k])): 
                if player_choice == table[k][j]: table[k][j] = 'o'
    if i % 2 == 1: 
        player_choice = int(input('На какое место вы ходите поставить х?'))
        for k in range(len(table)):
            for j in range(len(table[k])): 
                if player_choice == table[k][j]: table[k][j] = 'x'
    for k in table: print(k)
    win_check(table, i)

def win_check(table, i):
    check_table = False
    for k in table:
        for a in k:
            if str(a) in '123456789': 
                check_table = True
                break
    if check_table:
        for k in range(len(table)):
            if table[k][0] == table[k][1] == table[k][2]: 
                print(f'Урааа! Победил {table[k][0]}')
                return
        if table[0][0] == table [1][1] == table[2][2]:
            print(f'Урааа! Победил {table[0][0]}')
            return
        if table[0][2] == table[1][1] == table[2][0]:
            print(f'Урааа! Победил {table[2][0]}')
            return
        for j in range(3):
            if table[0][j] == table[1][j] == table[2][j]:
                print(f'Урааа! Победил {table[0][j]}')
                return
        else:
            i += 1
            ttt_play(table, i)
            return
    else: 
        print('Победила дружба...')
        return

ttt_table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in ttt_table: print(i)
i = int(1)
ttt_play(ttt_table, i)
