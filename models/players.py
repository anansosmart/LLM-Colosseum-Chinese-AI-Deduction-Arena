# models/player.py

import asyncio
from models.ai_client import AIClient
from game.game_state import GameState


class Player:
    def __init__(self, player_id, name, model_type, config, role="player"):
        self.id = player_id
        self.name = name
        self.model_type = model_type
        #self.role = role
        self.ai_client = AIClient(model_type, config)
        self.votes_received = 0  # 如果未来加入投票环节可以用到
        self.is_alive = True

    async def ask_question(self, game_state, story_description):
        """
        让 AI 提一个与故事相关的问题，用于揭示真相
        """
        # 构造系统提示词
        system_prompt = self._generate_system_prompt(game_state)


        # 构造 user 消息
        user_prompt = (
                f"你正在参与一个名为「海龟汤」的推理游戏。\n"
                f"故事是：{story_description}\n"
                "请你提出一个揭示真相的【是非问题】，问题应清晰、合逻辑，一次只问一个。\n"
                "可以参考下面的历史问题和回答去思考，避免问重复问题，浪费机会。\n"
                )

        user_prompt+="历史问题和回答\n"
        for round_num, speeches in game_state.history.items():
            user_prompt+=f"第{round_num}轮:\n"
            for s in speeches:
                user_prompt+=f"{s['name']}: {s['question']}, {s['response']}\n"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        # 向模型发送消息获取问题
        response = await self.ai_client.send_message(messages, system_prompt)
        question = response.strip()

        # 保存到对话历史
        '''self.conversation_history.append({
            "story": story_description,
            "question": question
        })'''

        print(f"🗣️ {self.name} 提问：{question}")
        return question, None  # 返回问题文本（主游戏会处理裁判回答）

    def _generate_system_prompt(self, game_state):
        """
        系统提示词，定义模型行为：只提问题，不猜答案，不解释
        """
        return (
            "你是一个逻辑推理专家，正在参与一个名为「海龟汤」的问答游戏。\n"
            "你每次只能提一个「是/否」问题来揭示故事背后的真相。\n"
            "不要直接猜答案，也不要解释问题，只提出关键问题。"
        )

    def eliminate(self):
        """标记该玩家已被淘汰"""
        self.is_alive = False
        print(f"☠️ 玩家 {self.name} 被淘汰（5次提问未命中）")
