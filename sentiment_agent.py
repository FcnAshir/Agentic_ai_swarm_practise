from swarm import agent

@agent(name="SentimentAnalyzer")
def run(conversation):
    text = conversation.latest_user_message()
    sentiment = "Positive" if "good" in text.lower() else "Negative"
    return conversation.reply(f"Sentiment: {sentiment}", name="SentimentAnalyzer")
