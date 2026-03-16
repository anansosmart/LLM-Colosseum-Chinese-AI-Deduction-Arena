# story.py
def story_description():
    return "一个男人走进一家餐馆，点了一碗海龟汤，吃了一口后自杀了。为什么？"

# 正确故事描述（用于判断猜中）
ground_truth = "他在海边出过事故，以为吃到的不是海龟肉，确认后失望至极自杀"

def is_correct_guess(guess: str) -> bool:
    # 可用更复杂的语义匹配算法，这里简化为关键词匹配
    keywords = ["海龟", "事故", "幸存", "回忆", "认出", "自杀"]
    return all(word in guess for word in keywords)

