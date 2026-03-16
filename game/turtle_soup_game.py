# game/turtle_soup_game.py

import asyncio
from colorama import Fore, Style
from game.game_state import GameState
from game.story import story_description, is_correct_guess
from game.judge import judge_answer


class TurtleSoupGame:
    def __init__(self, players):
        self.players = players
        self.state = GameState(players)
        self.story = story_description

    async def run_game(self):
        print(f"\n本次海龟汤故事：\n{self.story}\n")

        round_num = 1
        while not self.state.is_game_over():
            print(f"\n-------- 第 {round_num} 轮提问 --------")

            for player in self.state.get_alive_players():  # 拷贝一份避免在循环中修改列表
                print(f"\n {player.name} 开始提问...")
                try:
                    question, _ = await player.ask_question(self.state, self.story)
                except Exception as e:
                    print(Fore.RED + f"{player.name} 提问出错：{e}" + Style.RESET_ALL)
                    continue

                # 裁判判断是否猜中真相
                if is_correct_guess(question):
                    self.state.set_game_winner(player)
                    print(Fore.GREEN + f"\n{player.name} 猜中真相，赢得了游戏！" + Style.RESET_ALL)
                    return

                response = judge_answer(question)
                self.state.conversation_history(round_num,player,question,response)
                print(f"{response}\n")

                self.state.increase_question_count(player.id)

            round_num += 1

        # 游戏结束：无人猜中
        if not self.state.correct_guessed:
            print(Fore.YELLOW + "\n所有AI都未能猜中真相，游戏结束，无人获胜。" + Style.RESET_ALL)
