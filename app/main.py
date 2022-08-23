"""
Demo project

Simplest project you can imagine:
- sets the project
- receives messages from slack
- gets an AI response
- gets an AI response
- posts back to slack
"""
from ai.ai import ai
from ai.message import Message

APP_NAME = 'demo-agent'
ai.init(APP_NAME)


async def handle_message(msg: Message):
    if msg.channel == 'slack':
        if APP_NAME in msg.body.text:
            query = msg.body.text[8:]
            response = ai.get_model('openai/gpt-3').query(query)
            text = response['choices'][0]['text']
            ai.channel_interfaces['slack'].send_message(text)


if __name__ == "__main__":
    ai.start(handle_message)
