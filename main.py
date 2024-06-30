import json
import re
from datetime import date, datetime

from crewai import Agent, Task
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
# executed_value = None

from composio_crewai import Action, App, ComposioToolSet

composio_toolset = ComposioToolSet()
tools = composio_toolset.get_tools(apps=[App.GOOGLECALENDAR])


def run_crew(msg):

    todo = "Detect Start Datetime and End Datetime and Convert them to RFC3339 Format, Then take the input as the format"

    crewai_agent = Agent(
        role="Google Calendar Agent",
        goal="""You take action on Google Calendar using Google Calendar APIs""",
        backstory=(
            """You are an AI agent responsible for taking actions on Google Calendar on users' behalf. 
            You need to take action on Calendar using Google Calendar APIs. Use correct tools to run APIs from the given tool-set. If you think the task is complete then exit the program.
            The default timezone is India Standard Time (IST) and the default calendar is primary. 
            Use default timezone if timezone is not provided in the input.
            if told to delete find the event id of said name and use the acquired id to delete the event.
            if told to update find the event id of said name and use the acquired id to update the event.
            """
            # """You are an AI agent responsible for taking actions on Google Calendar on users' behalf.
            # You need to take action on Calendar using Google Calendar APIs. Use correct tools to run APIs from the given tool-set.
            # If no date is specified then calculate everything in reference to 30/06/2024, Sunday,
            # timezone is Indian Standard Time    !important."""
        ),
        verbose=True,
        tools=tools,
        llm=llm,
        memory=True,
    )

    task = Task(
        description=msg + todo,
        agent=crewai_agent,
        expected_output="if Event is Created",
        allow_delegation=False,
    )

    try:
        res = task.execute()

        # Use regex to extract the value of 'executed'
        # pattern = re.compile(r"'executed':\s*(True|False)")
        # match = pattern.search(res)

        if res is not None:
            # global executed_value
            # executed_value = match.group(1)
            # print(f"executed: {executed_value}")
            return res
        else:
            print("No match found.")
            res_dict = {}

            # Ensure that res is a string representation of JSON
            if isinstance(res, str):
                # If res is already in dictionary format, skip json.loads
                if res.startswith("{") and res.endswith("}"):
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


# Example usage
# run_crew("Create an Event 'Meeting' From 2pm to 4pm. The Date is 29th June, 2024, Timezone is Indian Timezone.")

# # Save executed_value to a file for use in another script
# if executed_value is not None:
#     with open('executed_value.txt', 'w') as file:
#         file.write(executed_value)
