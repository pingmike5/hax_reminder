import os
import requests
import json

def send_message_to_telegram(message, button_text='想反馈问题❓反馈个锤子，哪有人给你维护!', button_url='https://www.google.com'):
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')

    if not telegram_bot_token or not telegram_chat_id:
        print("Error: telegram必要参数未设置")
        return

    url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
    payload = {
        'chat_id': telegram_chat_id,
        'text': message,
        'reply_markup': json.dumps({
            'inline_keyboard': [[{'text': button_text, 'url': button_url}]]
        })
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # 检查请求是否成功
    except requests.exceptions.RequestException as e:
        print(f"Error: 发送消息失败: {e}")
        return

    return response.json()

if __name__ == "__main__":
    # 从环境变量获取自定义消息
    custom_message = os.getenv('CUSTOM_MESSAGE')
    
    if not custom_message:
        print("Error: 提醒内容未设置！")
        exit(1)  # 使用 exit(1) 替代 return

    # 添加前缀
    final_message = f"自动化提醒脚本运行开始:\n-----------------------------------\n\n {custom_message}"
    
    response = send_message_to_telegram(final_message)
    
    print("脚本执行结束~~~~")