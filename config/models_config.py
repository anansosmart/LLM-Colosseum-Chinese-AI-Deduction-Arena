# 豆包模型配置
DOUBAO_CONFIG = {
    "base_url": "https://ark.cn-beijing.volces.com/api/v3",
    "api_key": "95a05f04-7e27-4d5d-83f2-f246a8382142",  
    "model": "doubao-seed-1-6-250615"
}

# DEEPSEEK模型配置
DEEPSEEK_CONFIG = {
    "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "api_key": "sk-eb5dfb995e384c43841622f1859b0131",
    "model": "deepseek-r1"
}

# 百度千帆配置
ERNIE_CONFIG = {
    "base_url": "https://qianfan.baidubce.com/v2",
    "api_key": "bce-v3/ALTAK-W668E2fxYwfqvoj9SheB7/f140f146972dffc1bd1ae4e2d4bc33ed5261b74e",
    "model": "ernie-3.5-8k"
}

# 通义千问配置
QWEN_CONFIG = {
    "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "api_key": "sk-3be08469d15a42c98049236cb3448793",
    "model": "qwen-plus"
}

# Kimi 模型配置
KIMI_CONFIG = {
    "base_url": "https://api.moonshot.cn/v1",  
    "api_key": "sk-QYAJc7DWkTWvQ8uRQjW1toywY5tAWRCAzhVimCBTWvMYXcx4",
    "model": "moonshot-v1-8k"  
}

# 模型列表
MODELS = [
    {"name": "豆包", "type": "doubao", "config": DOUBAO_CONFIG},
    {"name": "Deepseek", "type": "deepseek", "config": DEEPSEEK_CONFIG},
    {"name": "文心一言", "type": "ernie", "config": ERNIE_CONFIG},
    {"name": "通义千问", "type": "qwen", "config": QWEN_CONFIG},
    {"name": "Kimi", "type": "kimi", "config": KIMI_CONFIG} 
]

