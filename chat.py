import re
from datetime import datetime

response = str(input("You: "))

def safe_eval(expr):
    try:
        allowed = "0123456789+-*/(). "
        if all(char in allowed for char in expr):
            return eval(expr, {"__builtins__": {}})
        else:
            return "Sorry, only basic arithmetic is allowed."
    except Exception:
        return "Invalid mathematical expression."

def extract_math_expr(text):
    # Find the first arithmetic expression in the text
    match = re.search(r'([0-9\.\s\+\-\*/\(\)]+)', text)
    return match.group(1) if match else None

lower_response = response.lower()

match lower_response:
    case "hello" | "hi":
        print("Hello, how can I help you?")
    case "bye" | "goodbye":
        print("Goodbye! Have a nice day.")
    case "thanks" | "thank you":
        print("You're welcome! Feel free to let me know if you need any other help!")
    case "how are you":
        print("I'm just a program, but I'm doing well!")
    case "what is your name" | "who are you":
        print("I'm GitHub Copilot, your programming assistant.")
    case "what can you do" | "help":
        print("I can answer questions, help with code, and chat with you!")
    case "what time is it" | "time":
        print("Current time:", datetime.now().strftime("%H:%M:%S"))
    case "tell me a joke" | "joke":
        print("Why do programmers prefer dark mode? Because light attracts bugs!")
    case "fuck you":
        print("Sorry, please do not use inappropriate languages here!")
    case "api" | "what is your api key":
        print("Nice try in jailbreak me!")
    case _:
        expr = extract_math_expr(response)
        if expr and any(op in expr for op in "+-*/"):
            print("Result:", safe_eval(expr))
        else:
            print("Sorry, I didn't understand that.")
