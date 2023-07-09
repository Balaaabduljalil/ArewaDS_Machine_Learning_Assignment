Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
... from nltk.sentiment import SentimentIntensityAnalyzer
... from nltk.tokenize import word_tokenize
... 
... def bot_response(user_input):
...     if user_input.lower() == 'bye':
...         return 'Goodbye!'
...     else:
...         # Tokenize user input
...         tokens = word_tokenize(user_input)
...         
...         # Check for specific triggers
...         if 'why' in tokens:
...             return 'That is an interesting question. Could you provide more context?'
...         elif 'how' in tokens:
...             return 'It depends on the situation. Can you be more specific?'
...         
...         # Use sentiment analysis to generate a response
...         sentiment_score = SentimentIntensityAnalyzer().polarity_scores(user_input)['compound']
...         
...         if sentiment_score >= 0.2:
...             return 'I'm glad you feel that way!'
...         elif sentiment_score <= -0.2:
...             return 'I'm sorry if you're feeling down. Is there anything I can do to help?'
...         else:
...             responses = ['That's interesting. Tell me more.', 'I'm not sure about that.', 'Could you rephrase your question?', 'I'm here to assist you. What else would you like to know?']
...             return random.choice(responses)
...         
... # Test the bot
... while True:
...     user_input = input("User: ")
...     response = bot_response(user_input)
...     print("Bot:", response)
...     if response == 'Goodbye!':
...         break
