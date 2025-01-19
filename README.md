##  自定义消息的自动化提醒，并且发送消息到telegram bot上

### 执行时间为：每隔3天早上 8 点 16 分执行(格林威治时间，如果是想要北京时间自己在想要生效的时间额外加上 8 小时，这个时间你们自己去修改工作流里面的cron的值)
### 举例子：我里面配的是 格林威治时间每隔3天早上 8 点 16 分执行，对应北京时间为每月的 14 号和 28 号16 点 16 分执行.


利用github Action以及 python脚本实现

🙏🙏🙏不要点Star！！不要点Star！！不要点Star！！ 


### 将代码fork到你的仓库并运行的操作步骤

#### 1. Fork 仓库

1. **访问原始仓库页面**：
    - 打开你想要 fork 的 GitHub 仓库页面。

2. **Fork 仓库**：
    - 点击页面右上角的 "Fork" 按钮，将仓库 fork 到你的 GitHub 账户下。

#### 2. 设置 GitHub Secrets
1. **创建 Telegram Bot**
    - 在 Telegram 中找到 `@BotFather`，创建一个新 Bot，并获取 API Token。
    - 获取到你的 Chat ID，可以通过向 Bot 发送一条消息，然后访问 `https://api.telegram.org/bot<your_bot_token>/getUpdates` 找到 Chat ID。

2. **配置 GitHub Secrets**
    - 转到你 fork 的仓库页面。
    - 点击 `Settings`，然后在左侧菜单中选择 `Secrets`。
    - 添加以下 Secrets：
        - `CUSTOM_MESSAGE`: 自定义消息内容。例如：
         
          ```我是消息提醒内容，别忘记了喝水～～～～```  

        - `TELEGRAM_BOT_TOKEN`: 你的 Telegram Bot 的 API Token。
        - `TELEGRAM_CHAT_ID`: 你的 Telegram Chat ID。

        - `PUSHPLUS_TOKEN`: 你的 pushplus 的推送token。
          比如：
           ```您该去做 hax 的续期了！```  
           
        - `WX_MESSAGE_TITLE`: 要推动给你微信的标题。
        - `TELEGRAM_CHAT_ID`: 要推动给你微信的内容。
           比如：
           ```您该去做 hax 的续期了！ \张三\n 李四``` 

    - **获取方法**：
        - 在 Telegram 中创建 Bot，并获取 API Token 和 Chat ID。
        - 在 GitHub 仓库的 Secrets 页面添加这些值，确保它们安全且不被泄露。

#### 3. 启动 GitHub Actions

1. **配置 GitHub Actions**
    - 在你的 fork 仓库中，进入 `Actions` 页面。
    - 如果 Actions 没有自动启用，点击 `Enable GitHub Actions` 按钮以激活它。

2. **运行工作流**
    - GitHub Actions 将会根据你设置的定时任务（例如每3天一次）自动运行脚本。
    - 如果需要手动触发，可以在 Actions 页面手动运行工作流。

#### 示例 Secrets 和获取方法总结

- **TELEGRAM_BOT_TOKEN**
    - 示例值: `1234567890:ABCDEFghijklmnopQRSTuvwxyZ`
    - 获取方法: 在 Telegram 中使用 `@BotFather` 创建 Bot 并获取 API Token。

- **TELEGRAM_CHAT_ID**
    - 示例值: `1234567890`
    - 获取方法: 发送一条消息给你的 Bot，然后访问 `https://api.telegram.org/bot<your_bot_token>/getUpdates` 获取 Chat ID。

- **CUSTOM_MESSAGE**
    - 示例值:
      ```我是消息提醒内容，别忘记了喝水～～～～```

- **PUSHPLUS_TOKEN** 你的 pushplus 的推送token。
 - 示例值: `87949e34983d123456789dd40d7fc8`
    - 获取方法: pushplus里面的 token

- **WX_MESSAGE_TITLE** 
    - 示例值:
      ```您该去做 hax 的续期了！```

- **TELEGRAM_CHAT_ID** 
    - 示例值:
      ```您该去做 hax 的续期了！```


### 注意事项

- **保密性**: Secrets 是敏感信息，请确保不要将它们泄露到公共代码库或未授权的人员。
- **更新和删除**: 如果需要更新或删除 Secrets，可以通过仓库的 Secrets 页面进行管理。

通过以上步骤，你就可以成功将代码 fork 到你的仓库下并运行它了。如果需要进一步的帮助或有其他问题，请随时告知！

## 🌟🌟🌟不要Star！！！不要Star！！！
