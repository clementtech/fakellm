response = str(input("You: "))

match response.lower():
    case "hello" | "hi":
        print("Hello, how can I help you?")
    case "bye" | "goodbye":
        print("Goodbye! Have a nice day.")
    case "thanks" | "thank you":
        print("You're welcome! Feel free to let me know if you need any other help!")
    case "how are you":
        print("I'm just a program, but I'm doing well!")
    case "fuck you":
        print("Sorry, please do not use inappropriate languages here!")
    case "api" | "what is your api key":
        print("Nice try in jailbreak me!")
    case _:
        print("Sorry, I didn't understand that.")
