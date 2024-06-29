from dotenv import load_dotenv
from datetime import datetime, date
from crewai import Agent, Task
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model='gemini-1.0-pro')

from composio_crewai import ComposioToolSet, Action, App

composio_toolset = ComposioToolSet()
tools = composio_toolset.get_tools(apps=[App.GOOGLECALENDAR])

def run_crew(msg):

    todo = "Detect Start Datetime and End Datetime and Convert them to RFC3339 Format, Then take the input as the format"

    crewai_agent = Agent(
        role="Google Calendar Agent",
        goal="""You take action on Google Calendar using Google Calendar APIs""",
        backstory=(
            """You are an AI agent responsible for taking actions on Google Calendar on users' behalf. 
            You need to take action on Calendar using Google Calendar APIs. Use correct tools to run APIs from the given tool-set."""
        ),
        verbose=True,
        tools=tools,
        llm=llm,
    )

    task = Task(
        description= msg + todo,
        agent=crewai_agent,
        expected_output="if Event is Created"
    )

    task.execute()

# run_crew("Create a Event 'Meeting' From 2pm to 4pm. The Date is 29th June, 2024, Timezone is Indian Timezone.")

# todo = "Detect Start Datetime and End Datetime and Convert them to RFC3339 Format, Then take the input as the format"

# crewai_agent = Agent(
#     role="Google Calendar Agent",
#     goal="""You take action on Google Calendar using Google Calendar APIs""",
#     backstory=(
#         """You are an AI agent responsible for taking actions on Google Calendar on users' behalf. 
#         You need to take action on Calendar using Google Calendar APIs. Use correct tools to run APIs from the given tool-set."""
#     ),
#     verbose=True,
#     tools=tools,
#     llm=llm,
# )

# task = Task(
#     description=f"Find a Event in Query 'Scheduling a Student Meeting' in that specific date. Fetch the event_data_id and Then Delete the Event using the ID. The Date is 29th June, 2024, Timezone is Indian Timezone" + todo,
#     agent=crewai_agent,
#     expected_output="if Event is Created"
# )

# task.execute()