"""Make a program that asks a person 5 questions about a crime. The questions are: 
    “Did you call the victim?” 
    “Were you at the crime scene?” 
    “Do you live near the victim?” 
    “Did you owe the victim?” 
    “Have you worked with the victim?” 
The program should ultimately issue a classification about the person’s participation in the crime. 
If the person answers positively to 2 questions, they should be classified as “Suspect”, between 3 and 4 as “Accomplice”, and 5 as “Murderer”. Otherwise, they will be classified as “Innocent”."""

print("Only answer with yes or no:")

questions = [
    "Did you call the victim?",
    "Were you at the crime scene?",
    "Do you live near the victim?",
    "Did you owe the victim?",
    "Have you worked with the victim?"
]

positive_responses = 0

for question in questions:
    response = input(question + " (yes/no): ")
    if response.lower() == "yes":
        positive_responses += 1

classification = "Innocent"
if positive_responses == 2:
    classification = "Suspect"
elif 3 <= positive_responses <= 4:
    classification = "Accomplice"
elif positive_responses == 5:
    classification = "Murderer"

print("The person is classified as: ", classification)