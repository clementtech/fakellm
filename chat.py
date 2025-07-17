from datetime import datetime

response = str(input("You: "))

def safe_eval(expr):
    try:
        # Only allow numbers and math operators
        allowed = "0123456789+-*/(). "
        if all(char in allowed for char in expr):
            return eval(expr, {"__builtins__": {}})
        else:
            return "Sorry, only basic arithmetic is allowed."
    except Exception:
        return "Invalid mathematical expression."

match response.lower():
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
    case "what time is it":
        print("Current time:", datetime.now().strftime("%H:%M:%S"))
    case "tell me a joke" | "joke":
        print("Why do programmers prefer dark mode? Because light attracts bugs!")
    case "fuck you":
        print("Sorry, please do not use inappropriate languages here!")
    case "api" | "what is your api key":
        print("Nice try in jailbreak me!")
    case _ if response.replace(" ", "").isdigit() or any(op in response for op in "+-*/"):
        print("Result:", safe_eval(response))
    case _:
        print("Sorry, I didn't understand that.")
