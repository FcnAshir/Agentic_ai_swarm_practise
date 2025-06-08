from swarm import run
from agents import summarizer_agent, sentiment_agent

if __name__ == "__main__":
    run(
        agents=[
            summarizer_agent.run,
            sentiment_agent.run
        ]
    )
