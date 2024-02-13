from webex_bot.webex_bot import WebexBot
import os

webex_token = "ODZiYmE5NjktMjk5MC00M2IxLTkwNjEtOGYwYWFiMjE2NmY4NTk0ZWFiNTMtMjI4_P0A1_db9ced2e-7d22-4ed1-9efc-08b3b5cb317c"
#os.environ["WEBEX_TOKEN"]
bot =  WebexBot(webex_token)

bot.run()


