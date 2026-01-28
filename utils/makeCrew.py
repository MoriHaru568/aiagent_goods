from crewai import Crew

def makeCrew(agents_crew,tasks_crew):
    crew = Crew(
    agents=agents_crew,
    tasks=tasks_crew
    )
    return crew