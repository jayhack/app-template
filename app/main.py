"""
App template
- Update your APP_NAME
- Set your URL appropriately
"""
from ai.ai import ai
from ai.utils.message import Message

APP_NAME = 'debug-app'
ai.init(APP_NAME, url='https://8c17-73-241-110-178.ngrok.io')


async def handle_message(msg: Message):
    if msg.channel == 'slack':
        if APP_NAME in msg.body.text:
            query = msg.body.text[8:]
            response = ai.get_model('openai/gpt-3').query(query)
            text = response['choices'][0]['text']
            ai.channel_interfaces['slack'].send_message(text)


if __name__ == "__main__":
    ai.start(handle_message)

