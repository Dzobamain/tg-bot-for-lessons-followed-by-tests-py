<div style="text-align: center;">
  <h1>Telegram bot for conducting lessons and reinforcing the material with a test</h1>
</div>

After completing the lesson, reinforce the material with a test on the topic

## How to use the app

There are a few rules for working with the program:

- The first line in the lesson+test file must be a link to the lesson.
- Lesson+test filenames in levels should be specified with numbers, for example: 1.txt. 1 is the lesson number within this level. .txt is a mandatory file extension.
- You can add new levels or change their names, but you need to specify the changes (path and level name) in the config.py file.
- At the moment, there must be 4 answer options for each test.

To run the bot, you need to create a .env file and add the following line:
```TELEGRAM_API_TOKEN=YOUR_TOKEN```

The test can be available only after subscribing to a channel. To enable this, add the following line in .env:
```TELEGRAM_CHANNEL_ID=YOUR_CHANNEL_ID```

Replace id with your channel's ID where the subscription needs to be checked. But before that, make sure to add the bot as a member of this channel.
If you don't need subscription verification, just leave it empty in .env:
```TELEGRAM_CHANNEL_ID=```

## Install Guide

### This guide is for running locally (on your PC). If you need to run it on a server, skip step 3!

Follow these steps to install and run the Telegram bot:

Items 1, 4(1,2) are websites:
<div style="text-align: center;">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Download_Python-3.9+-blue" alt="Download Python">
  </a>
  <a href="https://pypi.org/project/pyTelegramBotAPI/">
    <img src="https://img.shields.io/badge/Install_pyTelegramBotAPI-pip%20install%20pyTelegramBotAPI-blue" alt="Install pyTelegramBotAPI">
  </a>
  <a href="https://pypi.org/project/python-dotenv/">
    <img src="https://img.shields.io/badge/Install_python--dotenv-pip%20install%20python--dotenv-blue" alt="Install python-dotenv">
  </a>
</div>

1. **Install Python**
   - Make sure Python is installed on your system.
   - Recommended version: Python 3.9 or higher.
   - You can download Python from the official website: https://www.python.org/downloads/

2. **Clone the bot's source code**
   - ```git clone https://github.com/Dzobamain/youtube-comment-analyzer-gpt```

3. **Create a virtual environment (optional but recommended)**
   - On Windows:
    ```
    venv\Scripts\activate
    ```
   - On macOS/Linux:
    ```
    source venv/bin/activate
    ```
4. **Install the required libraries**

   - ```pip install pyTelegramBotAPI```
   - ```pip install python-dotenv```

5. **Create a `.env` file in the root directory of the project**
   - ```TELEGRAM_API_TOKEN=YOUR_BOT_TOKEN```
   - if you need:
       - ```TELEGRAM_CHANNEL_ID=YOUR_CHANNEL_ID```
   - else
     - ```TELEGRAM_CHANNEL_ID=```

## How to run

Open the console and compile the code:

```
python main.py
```
