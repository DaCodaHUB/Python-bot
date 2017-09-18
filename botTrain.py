# -*- coding: utf-8 -*-
from chatterbot import ChatBot


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    "Sakura",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="database.db",
    trainer="chatterbot.trainers.ChatterBotCorpusTrainer"
#    trainer="chatterbot.trainers.ListTrainer"
)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

#bot.train(conversation)
bot.train(
    "chatterbot.corpus.english.botprofile",
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.emotion",
    "chatterbot.corpus.english.food",
    "chatterbot.corpus.english.humor",
    "chatterbot.corpus.english.movies"
)

bot.logger.info('Trained database generated successfully!')
print("Done")
