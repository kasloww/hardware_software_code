def convo():
    print("What is your name?")
    name = input().lower().strip()
    if name == "exit":
        print("Too bad you did not want to chat! Maybe next time")
    else:
        print("What is your favorite show? " + name)
    show = input().lower().strip()
    if show == "exit":
        print("You answered one question. Goodbye")
    else:
        print("Thats a good show " + name)
def main():
    print("Welcome to my conversation program")
    print("I will keep asking questions until you type 'exit'")
    convo()
    print("Thanks for chatting with me.")
if __name__ == "__main__":
    main()
