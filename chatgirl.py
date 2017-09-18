# -*- coding: utf-8 -*-
from chatterbot import ChatBot

# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

def speak(arg):
    import pyttsx
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-5)
    engine.setProperty('voice', 'english+f3')
    engine.say(arg)
    engine.say("   ")
    engine.runAndWait()


# Create a new instance of a ChatBot
bot = ChatBot(
    "Sakura",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
#        "chatterbot.logic.MathematicalEvaluation",
#        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="database.db"
)

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)
	speak(bot_input)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
