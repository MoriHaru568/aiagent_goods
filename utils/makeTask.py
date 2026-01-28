from crewai import Task
def makeTask(description_agent,expected_output_agent,use_agent):
    task = Task(
    description=description_agent,
    expected_output=expected_output_agent,
    agent=use_agent
    )
    return task