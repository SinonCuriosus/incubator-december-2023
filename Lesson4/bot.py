'''from webex_bot.webex_bot import WebexBot
import os

webex_token = "ODZiYmE5NjktMjk5MC00M2IxLTkwNjEtOGYwYWFiMjE2NmY4NTk0ZWFiNTMtMjI4_P0A1_db9ced2e-7d22-4ed1-9efc-08b3b5cb317c"
#os.environ["WEBEX_TOKEN"]
bot =  WebexBot(webex_token)

bot.run()
'''

import logging
import os

from webex_bot.webex_bot import WebexBot
from webexteamssdk import WebexTeamsAPI
log = logging.getLogger(__name__)
webex_token = "ODZiYmE5NjktMjk5MC00M2IxLTkwNjEtOGYwYWFiMjE2NmY4NTk0ZWFiNTMtMjI4_P0A1_db9ced2e-7d22-4ed1-9efc-08b3b5cb317c"

# Create a Bot Object
bot = WebexBot(teams_bot_token=webex_token,
               include_demo_commands=True)

webex_api = WebexTeamsAPI(access_token=webex_token)

bot.run()

