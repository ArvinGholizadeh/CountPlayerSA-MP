# SA-MP Player Count Discord Bot

This Discord bot displays the current player count of a San Andreas Multiplayer (SA-MP) server as its status.

## Features

*   Connects to a specified SA-MP server.
*   Regularly updates its Discord presence to show "Watching: Players: X/Y", where X is the current number of players and Y is the maximum player capacity.

## Configuration

To use this bot, you'll need to configure the following:

1.  **Server IP Address (`NeedIP`)**: The IP address of the SA-MP server you want to monitor.
2.  **Server Port (`NeedPort`)**: The port of the SA-MP server (default is usually 7777).
3.  **Discord Bot Token (`TokenBot`)**: Your Discord bot's token.

**Important:** It is strongly recommended to use environment variables or a configuration file to store your bot token and other sensitive information, rather than hardcoding them directly in the script. This will be addressed in future code improvements.

## Setup and Usage

1.  **Prerequisites:**
    *   Python 3.x
    *   `discord.py` library (`pip install -U discord.py`)
    *   `samp-client` library (`pip install -U samp-client`)

2.  **Configure the Bot:**
    *   Open the Python script (currently `Untitled-1.py`).
    *   Locate the following lines at the beginning of the script:
        ```python
        NeedIP = ' ' # IP Server
        NeedPort = 7777 # Port Server
        TokenBot = ' ' # Token Bot
        ```
    *   Replace the placeholder values with your actual server IP, port, and bot token.

3.  **Run the Bot:**
    ```bash
    python Untitled-1.py
    ```
    (Note: The script name will likely be changed to something more descriptive like `samp_discord_status_bot.py` in future updates.)

4.  Once the bot is running and connected to Discord, it will automatically update its status every 60 seconds to show the SA-MP server's player count.

## Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, please feel free to open an issue or submit a pull request.