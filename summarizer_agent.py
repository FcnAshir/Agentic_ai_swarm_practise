from swarm import agent

@agent(name="Summarizer")
def run(conversation):
    text = conversation.latest_user_message()
    summary = f"Summary: {text[:50]}..."  # Placeholder summary logic
    return conversation.reply(summary, name="Summarizer")
