from unicodedata import name



name = input("What's your request? ")

match name:
    case "Hello" | "Hello, Newman":
        print("$0")
    case "How you doing?":
        print("$20")
    case "What's happening?":
        print("$100")