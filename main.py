import os
import sys
import openai

import secret

openai.api_key = secret.openaikey


quit_commands = ["quit", "exit", "stop", "end", "q"]
restart_commands = ["restart", "reset", "reboot", "reload", "re", "r"]

# Helper Functions
def wrap(string: str, width: int = 80, indent: int = 0) -> str:
    """Wraps a string to a specified width and adds an indent to the beginning of each line.\n
    Returns the wrapped string, with each line separated by a newline character.

    Arguments:
        `string`: The string to wrap.\n
        `width`: The width to wrap the string to.\n
        `indent`: The number of spaces to indent the beginning of each line.
    """

    width = width - indent

    # split the string into paragraphs
    paragraphs = string.split("\n")

    lines = []
    for paragraph in paragraphs:
        # set the last character so that it can be targeted later
        paragraph += "←"

        # split the paragraph into words
        words = paragraph.split()

        current_line = ""
        for word in words:
            # if the line isn't too long, add the word to the current line
            if len(current_line) + len(word) + 1 <= width:
                # add the word to the current line if it is not the first word, otherwise set the current line to the current word
                current_line = current_line + " " + word if current_line else word
            else:
                # if the line is too long, add the current line to the list of lines and set the current line to the current word
                lines.append(current_line)
                current_line = word

        # if the current line is not empty, add it to the list of lines
        if current_line:
            lines.append(current_line)

    output_lines = []
    for i, line in enumerate(lines):
        # remove the targeting character to make the paragraphs work again
        line = line.replace("←", "\n")

        # if this line is a repeat, a new line, a space, or empty, skip it
        if line == lines[i - 1] or line == "\n" or line == " " or line == "":
            continue

        line = f"{' ' * indent}{line}"

        output_lines.append(line)

    return "\n".join(output_lines)


# AI Support Functions
def create_context(scenario: str = "", rules: list = None, preface: str = None) -> str:
    """Creates a context string from the scenario, rules, and preface.\n
    Returns the context string.

    Arguments:
        `scenario`: The scenario to use.\n
        `rules`: A list of rules to use.\n
        `preface`: A preface to use.
    """

    context = preface
    if rules:
        context += "\n\Please adhere to the following rules:"
        for rule in rules:
            context += f"\n- {rule}"

    context += f"\n\n{scenario}\n\n"

    return context


# AI Functions
# no API access for account information yet, here's the URL instead
# https://platform.openai.com/account/usage


def generate_chat(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """Very simple chatbot function. Takes a prompt and returns a response.\n
    May fail if the prompt is too long or the response is too long.

    Args:
        prompt (str): The prompt to use.
        model (str, optional): The GPT model to use. Defaults to "gpt-3.5-turbo".

    Returns:
        str: The response from the AI.
    """

    if len(prompt) < 1:
        return "Invalid prompt."

    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1800,
    )

    return response["choices"][0]["message"]["content"]


def print_header():
    header = "\
   ▄   ▄                                          \n\
  ▄██▄▄██▄          ┏┓      ┏┓┳  •   █            \n\
  ███▀██▀██         ┗┓┏━┏┓┏┓┣┫┃┏┓┓┏┓ █            \n\
  ▀███████▀         ┗┛┗━┗━┛┗┛┗┻┛•┗┗┛ █ by Bane    \n\
    ▀███████▄▄      ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀          \n\
     ██████████▄                                  \n\
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▀"

    print(header)


def display_scenarios(scenarios, columns=3):
    print("Please select a scenario:")
    for i, scenario in enumerate(scenarios):
        print(f"{i + 1}. {scenario.replace('.txt', '')}", end="\t\t")
        if (i + 1) % columns == 0:
            print()     # print a newline
    print()             # to end the \t


def auto_wrap_scenarios(scenarios, console_width):
    print("Please select a scenario:")
    lines = []
    line = ""
    for i, scenario in enumerate(scenarios):
        num = i + 1
        
        scenario_text = scenario.replace('.txt', '')
        scenario_text = f"{num}. {scenario_text}"
        
        # add to the line. If the line is larger than the console width, add it to the list of lines and reset the line
        if len(line) + len(f"{scenario_text}") > (console_width - 20):
            lines.append(line)
            line = f"{scenario_text}\t\t"
        else:
            line += f"{scenario_text}\t\t"
            
    # add the last line to the list of lines
    lines.append(line)
    
    # print the lines
    for line in lines:
        print(line)

def print_repeat(char, times, end="\n", suffix=""):
    """Prints a character a specified number of times.\n
    `end` and `suffix` are passed to the print function.
    
    Arguments:
        char: The character to print.\n
        times: The number of times to print the character.\n
        end: The end parameter for the print function.\n
        suffix: A suffix to add to the end of the string.
    """
    print((char * times) + suffix, end=end)


if __name__ == "__main__":
    # clear the console
    os.system("cls" if os.name == "nt" else "clear")

    print_header()

    try:
        # open the scenarios folder and put all the .txt files in a list
        scenarios = os.listdir("scenarios")
        
        # get size of terminal
        columns, rows = os.get_terminal_size()
        print(f"Terminal size: {columns}x{rows}")

        # list comprehension to remove all non .txt files
        scenarios = [scenario for scenario in scenarios if scenario.endswith(".txt")]
        # display_scenarios(scenarios, columns=2)
        auto_wrap_scenarios(scenarios, columns)
        
        # get the user's input
        choice = input("> ")
        choice = choice.strip().lower()
        
        if choice in quit_commands:
            exit()
        
        choice = int(choice)

        with open(f"scenarios/{scenarios[choice - 1]}", "r") as f:
            print(f"Loading scenario: {scenarios[choice - 1]}")
            scenario = f.read()
    except:
        print("Failed to load scenario. Exiting.")
        exit()

    preface = "Please use the following scenario to answer any questions."

    rules = []
    try:
        with open("rules.txt", "r") as f:
            rules = f.readlines()
    except:
        print("No rules.txt found, continuing without rules.")

    context = create_context(scenario, rules, preface)

    if rules:
        print_repeat("-", 80)
        print("The current rules for the AI are in effect:")
        for rule in rules:
            print(f"- {rule}")
        print_repeat("-", 80, suffix="\n")

    while True:
        print("Enter your scenario question or type 'quit' to exit.")
        prompt = input("> ")

        if prompt in quit_commands:
            break
        if prompt in restart_commands:
            os.execl(sys.executable, sys.executable, *sys.argv)
            break

        if len(prompt) < 1:
            print("Please enter a prompt.")
            continue
        if "python -u" in prompt:
            exit()

        print()
        print("Thinking...", end="\r")  # \r allows the line to be overwritten later

        try:
            response = generate_chat(context + prompt)
        except:
            print("Could not generate a response. There was likely an error connecting to OpenAI.")
            print("Exiting.")
            exit()

        print_repeat(" ", 80, end="\r")

        print("Response:")
        print(wrap(response, indent=4))

        print_repeat("-", 80, suffix="\n")
