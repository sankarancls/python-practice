## Day 1 Python Learning

def greet(name):
    """Function to greet a person with their name."""
    return f"Hello, {name}! Welcome to Day 1 of Python Learning."

if __name__ == "__main__":
    user_name = input("Please enter your name: ")
    greeting_message = greet(user_name)
    print(greeting_message)