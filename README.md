# ScenAIrio

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

Run `install.bat`.
This will install the Python packages needed for the bot to run, and will initialise a `secrets.py` file for you to use.

### Scenario

Include your scenario information in `scenario.txt`.

### Rules

Include rules in `rules.txt` for the AI to try and follow. 
One rule per line.

### Keys and Tokens

In `secret.py`, you will store your API token:

|           Key | Value                                              |  Type  |
| ------------: | :------------------------------------------------- | :-----: |
| `openaikey` | Your API key for OpenAI (obtained on your Profile) | `str` |

## Running

Once everything is installed and set up properly, double-clicking `main.py` should work.
If it brings up a "no program to run this" message, you can Browse for Python from there and then say "always use this program".
