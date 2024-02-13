from webex_bot.models.command import Command
import requests
import json

class BenficaWatcher(Command):
    def __init__(self):
        super().__init__(
            command_keyword="game"
            help_message="Get benfica result."
        )
