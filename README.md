# 📅 Narada - Integrated Discord-Calendar Agent

Narada is a powerful Discord bot that seamlessly integrates with Google Calendar to manage your events effortlessly. Users can create, update, and delete events directly through Discord commands, with all events automatically adjusted to their local timezone.

## 🌟 Features

- **Event-Sync-Snap**: Instantly sync events with your Google Calendar.
- **Timezone-Adapt-Control**: Automatically adjusts events to your local timezone.
- **Calendar-Swift-Updates**: Create, update, and delete events swiftly.
- **Cal-Cord Clean Sweep**: Clean up and manage your calendar events from Discord.
- **Dynamic Event Handling**: Detects and processes event timings dynamically from user inputs.

## 🛠️ Requirements

   To run Narada, make sure you have the following dependencies installed:<br>

   crewai<br>
   langchain_google_genai<br>
   composio_crewai<br>
   discord.py<br>
   python-dotenv

## 🚀 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/narada.git
   cd narada
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
3. **Setup Environment Variables**:
   Create a .env file in the root directory and add your Discord bot token and Google API credentials.
   ```env
   DISCORD_TOKEN=your_discord_bot_token
   GOOGLE_API_CREDENTIALS=your_google_api_credentials

## 🎮 Usage

1. **Run the Bot**:
   ```bash
   python bot.py
2. **Interact with the Bot**:
   Mention the bot in your Discord server with event commands.<br>
   Example: @Narada Create an Event 'Meeting' From 2pm to 4pm on 29th June, 2024, Timezone is Indian Timezone.


## 🌐 Landing Page
   Here are some screenshots of Narada in action:<br>
   Page 1-
   ![Screenshot 2024-06-30 001426](https://github.com/arnabpal2022/narada-bot/assets/119407936/9eec43df-5270-420a-a775-d442be96fd3a)
   Page 2-
   ![Screenshot 2024-06-30 000301](https://github.com/arnabpal2022/narada-bot/assets/119407936/7fc1d9e2-00ce-46ff-ba6a-c73411b29217)


## 📄 Code Overview

`bot.py`
This script sets up the Discord bot and handles incoming messages. It utilizes the `discord.py` library and integrates with the main logic to process commands.
`main.py`
This script contains the main logic for interacting with the Google Calendar using the `crewai` and `langchain_google_genai` libraries.

## 🤝 Contributing

We welcome contributions! Please see our Contributing Guidelines for more details.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📧 Contact


Feel free to replace the placeholders like `yourusername`, `your_discord_bot_token`, `your_google_api_credentials`, and `your_email@example.com` with the actual values relevant to your project.


