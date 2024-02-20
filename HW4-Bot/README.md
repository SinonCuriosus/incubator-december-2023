## README for Webex Bot
### Issue Resolution:

- We faced difficulties running the bot using the method suggested by Tumul. To resolve this, Sandro and I raised a ticket [here](https://github.com/fbradyirl/webex_bot/issues/48). Additionally, Gerard reached out to Tumul to seek further assistance.

### Homework Assignment:

To interact with the bot, you will need to follow these steps:

1. **Two Shell Sessions:** Open two shell sessions.

2. **First Shell:** Run ngrok to expose port 4111:
    ```
    ngrok http 4111
    ```

3. **Second Shell:** Start the Webex bot:
    ```
    python webex-bot-ngrok.py
    ```

4. **Webex Search:** Search for `benficafan@webex.bot` on Webex and initiate a conversation.

### Bot Behavior:

The bot behaves as follows:

- **Greeting:** If a person greets the bot with "Hello" (capitalization doesn't matter), the bot responds with a greeting and explains its functionality, asking the person to name a club.

- **Correct Club Name:** If the person mentions the name of the club correctly (e.g., "Benfica"), the bot responds with the last result and details about the match (e.g., who won and where the match was played).

- **Incorrect Input:** If the person's input does not match the expected club name, the bot explains its purpose (e.g. just try saying Yahoo).

### Bot Conversation:

![Bot Conversation](<https://github.com/SinonCuriosus/incubator-december-2023/blob/cf79a76f5997e61b47d2b0e0c2eedacb8995fe4e/HW4-Bot/BotConversation.png>)
