
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


def send_message_to_weixin():
    pushplus_token = os.getenv('PUSHPLUS_TOKEN')
    title = os.getenv('WX_MESSAGE_TITLE')
    content = os.getenv('WX_MESSAGE_CONTENT')

    if  pushplus_token:
        print("Error: vx消息推送的 pushplus token未设置,停止微信消息发送")
        return

    if not pushplus_token:
      if not telegram_bot_token or not telegram_chat_id:
         print("Error: vx消息推送的标题和内容未设置,停止微信消息发送！")
         return


    url = 'http://www.pushplus.plus/send'
    data = {
        "token":pushplus_token,
        "title":title,
        "content":content
    }
    body=json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type':'application/json'}

    try:
        response = requests.post(url,data=body,headers=headers)
        response.raise_for_status()  # 检查请求是否成功
    except requests.exceptions.RequestException as e:
        print(f"Error: 发送微信消息失败: {e}")
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
    send_message_to_weixin()
    
    print("脚本执行结束~~~~")
