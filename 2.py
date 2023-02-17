# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

# Вариант игры с ботом

import random
def player_takes(player_p, turn_p, candy_p, bot_p, player_turn):
    k = int(input('Введите количество конфет, которое хотите забрать\n'))
    if k > 28: player_takes(player_p, turn_p, candy_p, bot_p, player_turn)
    candy_p -= k
    player_p += k
    turn_p += 1
    player_turn += 1
    print(f'Вы взяли {k} конфет! Теперь у Вас в стопке {player_p}. На столе осталось {candy_p}.')
    if candy_p > 0: bot_takes(bot_p, turn_p, candy_p, player_p, player_turn)
    else: 
        print(f'Ура! Вы победили и забрали все конфеты у бота. \n Количество общих ходов: {turn_p}, из них Ваших: {player_turn}')
        return

def bot_takes(bot_b, turn_b, candy_b, player_b, player_turn):
    k = random.randrange(1, 29)
    candy_b -= k
    bot_b += k
    turn_b += 1
    print(f'Бот взял {k} конфет! Теперь у него в стопке {bot_b}. На столе осталось {candy_b}')
    if candy_b > 0: player_takes(player_b, turn_b, candy_b, bot_b, player_turn)
    else: 
        print(f'О нет! Бот победил и забрал все Ваши кофеты... \n Количество общих ходов: {turn_b}, из них Ваших: {player_turn}')
        return

player_counter = 0
bot_counter = 0
turn_counter = 0
player_turn_counter = 0
candy_counter = int(input('Введите количество конфет на столе \n'))
turn_choice = random.randrange(0,2)
if turn_choice == 0: 
    print('Вы ходите первыми')
    player_takes(player_counter, turn_counter, candy_counter, bot_counter, player_turn_counter)
else:
    print('Первым ходит бот')
    bot_takes(bot_counter, turn_counter, candy_counter, player_counter, player_turn_counter)
