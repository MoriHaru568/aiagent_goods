from crewai import Agent

def makeAgent(role_agent,gole_agent,backstory_agent,llm_agent):
    agent = Agent(
    role=role_agent,
    goal=gole_agent,
    backstory=backstory_agent,
    tools = [],
    llm=llm_agent
    )

    return agent
