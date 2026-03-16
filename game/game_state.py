# game/game_state.py

from collections import defaultdict


class GameState:
    def __init__(self, players):
        self.players = players  # 所有玩家
        self.question_counts = {player.id: 0 for player in players}
        self.correct_guessed = False
        self.winner = None

        # 游戏记录
        self.history = defaultdict(list)

    def increase_question_count(self, player_id):
        """增加某玩家的提问次数，并判断是否淘汰"""
        self.question_counts[player_id] += 1
        count = self.question_counts[player_id]

        if count >= 5:
            player = self.get_player_by_id(player_id)
            if player and player.is_alive:
                player.eliminate()

    def get_player_by_id(self, player_id):
        return next((p for p in self.players if p.id == player_id), None)

    def get_alive_players(self):
        return [p for p in self.players if p.is_alive]

    def get_dead_players(self):
        return [p for p in self.players if not p.is_alive]

    def is_game_over(self):
        """游戏是否结束：猜中 或 全部淘汰"""
        return self.correct_guessed or len(self.get_alive_players()) == 0

    def set_game_winner(self, player):
        self.correct_guessed = True
        self.winner = player

    def conversation_history(self, round, player, question,response):
        self.history[round].append({
            "player_id": player.id,
            "name": player.name,
            "question": question,
            "response": response
        })

    def print_player_status(self):
        """打印当前所有玩家状态"""
        print("\n 当前玩家状态：")
        for p in self.players:
            status = "存活" if p.is_alive else "淘汰"
            print(f" - {p.name}（ID: {p.id}）: {status}, 已提问 {self.question_counts[p.id]} 次")
