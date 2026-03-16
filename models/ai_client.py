"""
AI客户端统一接口
支持不同大模型的API调用
"""
import json
from openai import OpenAI
from urllib.parse import urlparse, urlencode
from time import mktime



class AIClient:
    def __init__(self, model_type, config):
        self.model_type = model_type
        self.config = config
        self.client = None
        self._init_client()

    def _init_client(self):
        """初始化不同类型的客户端"""
        self.client = OpenAI(
            api_key=self.config["api_key"],
            base_url=self.config["base_url"]
        )

    async def send_message(self, messages, system_prompt=""):
        """发送消息并获取回复"""
        try:
            return await self._send_openai_message(messages, system_prompt)
        except Exception as e:
            print(f"模型 {self.model_type} 调用失败: {e}")
            return "抱歉，我现在无法回应。"

    async def _send_openai_message(self, messages, system_prompt):
        """使用OpenAI兼容接口发送消息"""
        formatted_messages = []
        if system_prompt:
            formatted_messages.append({"role": "system", "content": system_prompt})

        for msg in messages:
            formatted_messages.append(msg)

        completion = self.client.chat.completions.create(
            model=self.config["model"],
            messages=formatted_messages,
            temperature=0.7,
            max_tokens=500
        )

        return completion.choices[0].message.content
