# ScenAIrio
```
   ▄   ▄                                          
  ▄██▄▄██▄          ┏┓      ┏┓┳  •   █            
  ███▀██▀██         ┗┓┏━┏┓┏┓┣┫┃┏┓┓┏┓ █            
  ▀███████▀         ┗┛┗━┗━┛┗┛┗┻┛•┗┗┛ █ by Bane    
    ▀███████▄▄      ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀          
     ██████████▄                                  
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀
```

Scenario? AI?
I'm funny.

## About

A useful tool for generating interactive scenario interviews based on provided information.

Can also be used as a weird AI-based way to glean information from a dataset, but that gets rather expensive rather quickly...

## Requirements

1. A paid [OpenAI](https://platform.openai.com/) account
2. Python download: https://www.python.org/downloads/

## Setup

### Install

Run `INSTALL.bat`.
This will install the Python packages needed for the bot to run, and will initialise a `secrets.py` file for you to use.

### Scenario

Include your scenario information in a text file and place it into the `scenarios` folder.  

For instance: 

```
scenarios
├── Assessment 1 Scenario.txt
├── Business X SLA.txt
├── SystemRequirements.txt
├── Interview Information.txt
¦
└── untitled_scenario.txt
```

These will be listed when the program starts up.

### Rules

Include rules in `rules.txt` for the AI to try and follow.
One rule per line.

### Keys and Tokens

In `secret.py`, you will store your API token:

|           Key | Value                                              |  Type  |
| ------------: | :------------------------------------------------- | :-----: |
| `openaikey` | Your API key for OpenAI (obtained on your Profile) | `str` |

## Running

Once everything is installed and set up properly, double-clicking `main.py` or `RUN.bat` should work.  
If it brings up a "no program to run this" message, you can Browse for Python from there and then say "always use this program".
