def create_event(msg):
    return """
    Create Googlecalendar create event action configuration JSON with the following structure:
    - Schema: {_*schema*_}
    - Example:
        {
            "start_datetime": "2024-04-09T10:00:00",
            "end_datetime": "2024-04-09T12:00:00",
            "description": "Description of the event. Can contain HTML. Optional.",
            "eventType": "default",
            "create_meeting_room": null,
            "guestsCanSeeOtherGuests": null,
            "guestsCanInviteOthers": null,
            "location": null,
            "summary": "Summary of the event. Title of the event.",
            "transparency": null,
            "visibility": null,
            "recurrence": null,
            "timezone": "Asia/Kolkata",
            "attendees": [
                "abc@xyz.com",
                "foo@bar.baz"
            ],
            "send_updates": null,
            "guests_can_modify": false,
            "calendar_id": "primary"
        }

        Task:
        - Learn the schema of the Google Calendar API event creation action.
        - Understand the structure of the JSON payload required to create a Google Calendar event.
        - Create a Google Calendar event JSON payload based on user message as follows: "{_*message*_}"
        - Return the JSON payload as stringified JSON object.
        
        Note: Do not send any additional information other than the JSON payload.
        The output must be aligned with the output schema:
        {"properties":{"event":{"description":"Event Details","title":"Event","type":"string"}},"required":["event"],
        "title":"CreateEventResponse","type":"object"}
        """