## README for Webex Bot

### Setup Instructions:

To run the bot without issues, follow these steps:

1. Download and install ngrok from [https://ngrok.com/download](https://ngrok.com/download).

2. Run ngrok to expose your local server to the internet:
    ```
    ngrok http 4111
    ```

3. Start the Webex bot using the following command:
    ```
    python webex-bot-ngrok.py
    ```

4. Search for `benficafan@webex.bot` on Webex and start a conversation.

### Issue Resolution:

If you encounter any issues running the bot, please refer to the following:

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

- **Incorrect Input:** If the person's input does not match the expected club name, the bot explains its purpose (e.g., similar to Yahoo).

### Bot Conversation:

![Bot Conversation](<IMAGE_URL>)
