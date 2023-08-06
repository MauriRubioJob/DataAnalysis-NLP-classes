import random
import requests


def download_category(category):
    url = "https://raw.githubusercontent.com/uberspot/OpenTriviaQA/master/categories/"
    response = requests.get(url + category)
    if response.status_code == 200:
        return response.text
    else:
        print("Category download failed.")
        return None


def ask_for_category():
    available_categories = ["animals", "geography", "history", "general", "movies", "world"]
    print("Choose a category of questions from: " + str(available_categories))
    category = input()
    if category in available_categories:
        return category
    else:
        return ask_for_category()


# Open the questions file and read the contents
def open_questions(contents):
    questions = contents.split("\n\n")
    
    processed = []
    # Go through each question one at a time
    for q in questions:
        # Split the question into its component parts
        components = q.split("\n")

        # If we find a broken question, skip to the next
        if len(components) < 4:
            continue

        if components[-3].startswith("^"):
            # 2 answers
            question = {}
            # Take each line in reverse order, and add
            # them to the dictionary
            question["B"] = components.pop()
            question["A"] = components.pop()
            question["correct"] = components.pop()
            # Take all the lines left and join them together
            question["text"] = "\n".join(components)
        else:
            # 4 answers
            question = {}
            # Take each line in reverse order, and add
            # them to the dictionary
            question["D"] = components.pop()
            question["C"] = components.pop()
            question["B"] = components.pop()
            question["A"] = components.pop()
            question["correct"] = components.pop()
            # Take all the lines left and join them together
            question["text"] = "\n".join(components)

        # Add the formatted question to the new list
        processed.append(question)
    
    return processed


# Choose a random question
def choose_question(questions):
    return random.choice(questions)

# Display a question and the answers
def display_question(question):
    print(question["text"])
    print(question["A"])
    print(question["B"])
    print(question["C"])
    print(question["D"])
    print("Enter your guess, A, B, C, or D:")
    response = input()
    return response


def check_answer(question, answer):
    # Extract the text of the answer
    given_answer = question[answer][2:]
    correct_answer = question["correct"][2:]
    if given_answer == correct_answer:
        print("Well done! Correct!")
    else:
        print("Sorry. Correct answer was: " + correct_answer)
    

# Choose the category of questions
category = ask_for_category()
downloaded = download_category(category)

# Use the downloaded questions and run the quiz
questions = open_questions(downloaded)
q = choose_question(questions)
answer = display_question(q)
check_answer(q, answer)