# Dm-all-server-member
Discord Bot - Send Message to All Members
This is a Python script that uses the discord.py library to send a message to all members of a Discord server via a Discord bot.

Prerequisites
Before running this script, you need to:

Create a Discord bot and invite it to your server. Follow the instructions in the official Discord API documentation to do that: https://discord.com/developers/docs/intro

Install the discord.py library using pip in your Python environment. You can do that with the following command:

Copy code
pip install discord.py
Usage
To use this script:

Clone this repository or download the send_message_to_all_members.py file.

Open the send_message_to_all_members.py file in a text editor.

Replace <TOKEN> with your bot's token, <SERVER_ID> with your server's ID, and <YOUR_MESSAGE> with the message you want to send.

Save the file.

Open a terminal or command prompt and navigate to the directory where the file is located.

Run the script with the following command:

Copy code
python send_message_to_all_members.py
The script will log in to the Discord API using your bot's token, get the server object by ID, and iterate over all members to send the message to each one. If a member has blocked DMs from the bot, or the bot doesn't have permission to send messages to that member, it will print an error message.

Contributing
If you find any issues with the script or want to suggest improvements, feel free to submit an issue or pull request.

License
This code is released under the MIT License.
