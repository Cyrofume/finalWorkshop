# Initialize an empty list to store the user's top five choices
top_five_list = []

# Function to get the user's top five choices
def get_top_five_choices(subject):
    print(f"Please enter your top five {subject} choices:")
    for i in range(1, 6):
        choice = input(f"Choice {i}: ")
        top_five_list.append(choice)

# Function to display the user's top five choices
def display_top_five_choices(subject):
    print(f"Your top five {subject} choices are:")
    for i, choice in enumerate(top_five_list, 1):
        print(f"{i}. {choice}")

# Main program
if __name__ == "__main__":
    subject = input("Enter the subject (e.g., food, song, artist, etc.): ")
    get_top_five_choices(subject)
    display_top_five_choices(subject)
