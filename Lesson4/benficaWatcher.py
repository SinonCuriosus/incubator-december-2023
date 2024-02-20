from webex_bot.models.command import Command
import requests
import json

class WeatherByCity(Command):
    def __init__(self):
        super().__init__(
            command_keyword ="weather"
            help_message = "Get weather by City name."
        )

    def execute(self ,message, attacgment_actions, activity):
        OpenWeather_Key=""
        url=""

        response = request.get(url)

        weather = response.json()

        city = weather['name']
        temporatura = weather['main']['temp']

        response_message = 

