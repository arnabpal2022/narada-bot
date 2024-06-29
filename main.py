from dotenv import load_dotenv
from datetime import datetime, date
from crewai import Agent, Task
from langchain_google_genai import ChatGoogleGenerativeAI
import json
import re
from events.create_event_prompt import create_event

llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
# executed_value = None

from composio_crewai import ComposioToolSet, Action, App

composio_toolset = ComposioToolSet()
tools = composio_toolset.get_tools(apps=[App.GOOGLECALENDAR])

def run_crew(msg):

    todo = "Detect Start Datetime and End Datetime from the input without using any actions and Convert them to RFC3339 Format, Then take the input as the format"

    crewai_agent = Agent(
        role="Google Calendar Agent",
        goal="""You take action on Google Calendar using Google Calendar APIs""",
        backstory=(
            """You are an AI agent responsible for taking actions on Google Calendar on users' behalf. 
            You need to take action on Calendar using Google Calendar APIs. Use correct tools to run APIs from the given tool-set.And if you think the task is complete then exit the program.
            the default timezone is India Standard Time (IST) and the default calendar is primary.
            """
        ),
        verbose=True,
        tools=tools,
        llm=llm,
    )

    task = Task(
        description=msg + todo,
        agent=crewai_agent,
        expected_output="if Event is Created"
    )

    
    try:
        res = task.execute()
        
        # Use regex to extract the value of 'executed'
        pattern = re.compile(r"'executed':\s*(True|False)")
        match = pattern.search(res)

        if match:
            # global executed_value
            executed_value = match.group(1)
            print(f"executed: {executed_value}")
            return executed_value
        else:
            print("No match found.")
            res_dict = {}
            
            # Ensure that res is a string representation of JSON
            if isinstance(res, str):
                # If res is already in dictionary format, skip json.loads
                if res.startswith('{') and res.endswith('}'):
                    res_dict = json.loads(res)
                else:
                    raise ValueError("Response is not a valid JSON string")
            else:
                raise ValueError("Response is not a string")
        
            print(res_dict.get("executed", "No 'executed' key found"))
            # Additional processing of res_dict as needed

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Response content: {res}")  # Print the actual content for debugging
    except Exception as ex:
        print(f"An error occurred: {ex}")
        # Handle other exceptions
