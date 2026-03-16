# main.py
import asyncio
from models.player import Player
from game.turtle_soup_game import TurtleSoupGame
from config.models_config import MODELS

async def main():
    print("🧠 初始化四人海龟汤游戏...\n")

    players = []
    for i, model_info in enumerate(MODELS):
        player = Player(
            player_id=i + 1,
            name=model_info["name"],
            model_type=model_info["type"],
            config=model_info["config"],
            role="player"  # 如果你还没有用角色字段，这里也可以省略
        )
        players.append(player)

    game = TurtleSoupGame(players)
    await game.run_game()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n游戏被用户中断")
    except Exception as e:
        print(f"\n游戏运行出错: {e}")
