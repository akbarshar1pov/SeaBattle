from SeaBattle import Player
from SeaBattle import Game
from SeaBattle import FieldPart


if __name__ == '__main__':
    print("Морской бой")
    player_name = input("Введите имя игрока: ")
    # здесь делаем список из двух игроков и задаем им основные параметры
    players = []
    players.append(Player(name=player_name, is_ai=False, auto_ship=True, skill=1))
    players.append(Player(name='Bot', is_ai=True, auto_ship=True, skill=1))

    # создаем саму игру и погнали в бесконечном цикле
    game = Game()

    while True:
        # каждое начало хода проверяем статус и дальше уже действуем исходя из статуса игры
        game.status_check()

        if game.status == 'prepare':
            game.add_player(players.pop(0))

        if game.status == 'in game':
            # в основной части игры мы очищаем экран добавляем сообщение для текущего игрока и отрисовываем игру
            Game.clear_screen()
            game.current_player.message.append("Ждём приказа: ")
            game.draw()
            # очищаем список сообщений для игрока. В следующий ход он уже получит новый список сообщений
            game.current_player.message.clear()
            # ждём результата выстрела на основе выстрела текущего игрока в следующего
            shot_result = game.current_player.make_shot(game.next_player)
            # в зависимости от результата накидываем сообщений и текущему игроку и следующему
            # ну и если промазал - передаем ход следующему игроку.
            if shot_result == 'miss':
                game.next_player.message.append('На этот раз {}, промахнулся! '.format(game.current_player.name))
                game.next_player.message.append('Ваш ход {}!'.format(game.next_player.name))
                game.switch_players()
                continue
            elif shot_result == 'retry':
                game.current_player.message.append('Попробуйте еще раз!')
                continue
            elif shot_result == 'get':
                game.current_player.message.append('Отличный выстрел, продолжайте!')
                game.next_player.message.append('Наш корабль попал под обстрел!')
                continue
            elif shot_result == 'kill':
                game.current_player.message.append('Корабль противника уничтожен!')
                game.next_player.message.append('Плохие новости, наш корабль был уничтожен :(')
                continue

        if game.status == 'game over':
            Game.clear_screen()
            game.next_player.field.draw_field(FieldPart.main)
            game.current_player.field.draw_field(FieldPart.main)
            print('Это был последний корабль {}'.format(game.next_player.name))
            print('{} выиграл матч! Поздравления!'.format(game.current_player.name))
            break

    print('Спасибо за игру!')
    input('')
