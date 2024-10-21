import random

# List of dictionaries containing Spanish words and their English translations
words = [
    {"spanish": "de", "english": "of"},
    {"spanish": "la", "english": "the (feminine)"},
    {"spanish": "que", "english": "that"},
    {"spanish": "el", "english": "the (masculine)"},
    {"spanish": "en", "english": "in"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to"},
    {"spanish": "los", "english": "the (plural, masculine)"},
    {"spanish": "del", "english": "of the"},
    {"spanish": "se", "english": "oneself, himself, herself"},
    {"spanish": "las", "english": "the (plural, feminine)"},
    {"spanish": "por", "english": "by, for"},
    {"spanish": "un", "english": "a, an"},
    {"spanish": "para", "english": "for, in order to"},
    {"spanish": "con", "english": "with"},
    {"spanish": "no", "english": "no"},
    {"spanish": "una", "english": "a, an (feminine)"},
    {"spanish": "su", "english": "his, her, their"},
    {"spanish": "al", "english": "to the"},
    {"spanish": "lo", "english": "it"},
    {"spanish": "como", "english": "like, as"},
    {"spanish": "más", "english": "more"},
    {"spanish": "pero", "english": "but"},
    {"spanish": "sus", "english": "his, her, their (plural)"},
    {"spanish": "le", "english": "to him, to her"},
    {"spanish": "ya", "english": "already"},
    {"spanish": "o", "english": "or"},
    {"spanish": "este", "english": "this"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "porque", "english": "because"},
    {"spanish": "muy", "english": "very"},
    {"spanish": "sin", "english": "without"},
    {"spanish": "sobre", "english": "on, about"},
    {"spanish": "me", "english": "me"},
    {"spanish": "hasta", "english": "until"},
    {"spanish": "hay", "english": "there is, there are"},
    {"spanish": "donde", "english": "where"},
    {"spanish": "quién", "english": "who"},
    {"spanish": "cuando", "english": "when"},
    {"spanish": "él", "english": "he"},
    {"spanish": "está", "english": "is (temporary)"},
    {"spanish": "tú", "english": "you (informal)"},
    {"spanish": "nos", "english": "us"},
    {"spanish": "nada", "english": "nothing"},
    {"spanish": "todo", "english": "all, everything"},
    {"spanish": "después", "english": "after"},
    {"spanish": "te", "english": "you (object)"},
    {"spanish": "bien", "english": "well"},
    {"spanish": "ni", "english": "neither"},
    {"spanish": "mucho", "english": "much, a lot"},
    {"spanish": "mi", "english": "my"},
    {"spanish": "cómo", "english": "how"},
    {"spanish": "ahora", "english": "now"},
    {"spanish": "quiero", "english": "I want"},
    {"spanish": "tengo", "english": "I have"},
    {"spanish": "esa", "english": "that"},
    {"spanish": "eso", "english": "that (neutral)"},
    {"spanish": "algo", "english": "something"},
    {"spanish": "nunca", "english": "never"},
    {"spanish": "poco", "english": "little"},
    {"spanish": "vamos", "english": "we go"},
    {"spanish": "sea", "english": "be (subjunctive)"},
    {"spanish": "tienen", "english": "they have"},
    {"spanish": "están", "english": "they are"},
    {"spanish": "tienes", "english": "you have"},
    {"spanish": "puede", "english": "he/she can"},
    {"spanish": "estoy", "english": "I am"},
    {"spanish": "solo", "english": "only, alone"},
    {"spanish": "cosas", "english": "things"},
    {"spanish": "mismo", "english": "same"},
    {"spanish": "dónde", "english": "where"},
    {"spanish": "has", "english": "you have"},
    {"spanish": "tiempo", "english": "time"},
    {"spanish": "entonces", "english": "then"},
    {"spanish": "ahí", "english": "there"},
    {"spanish": "ser", "english": "to be"},
    {"spanish": "vez", "english": "time (instance)"},
    {"spanish": "decir", "english": "to say"},
    {"spanish": "cada", "english": "each"},
    {"spanish": "otro", "english": "other"},
    {"spanish": "tan", "english": "so"},
    {"spanish": "dos", "english": "two"},
    {"spanish": "puedo", "english": "I can"},
    {"spanish": "ver", "english": "to see"},
    {"spanish": "aquí", "english": "here"},
    {"spanish": "quieres", "english": "you want"},
    {"spanish": "pues", "english": "well"},
    {"spanish": "hoy", "english": "today"},
    {"spanish": "he", "english": "I have (auxiliary)"},
    {"spanish": "ah", "english": "ah"},
    {"spanish": "veces", "english": "times"},
    {"spanish": "muchos", "english": "many"},
    {"spanish": "gracias", "english": "thanks"},
    {"spanish": "favor", "english": "favor"},
    {"spanish": "día", "english": "day"},
    {"spanish": "señor", "english": "Mr., sir"},
    {"spanish": "trabajo", "english": "work"},
    {"spanish": "vida", "english": "life"}
]


def quiz_user(words): # Function to quiz the user with a random word from the list
    random.shuffle(words) # Shuffle the list to ensure a random quiz order
    score = 0

    for word in words: # Loop through each word in the shuffled list
        print(f"What is the English translation of '{word['spanish']}'?") # Ask the user to translate the Spanish word to English
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower().replace('(', ',').replace(')', '').split(',')  # Convert correct answers to a list

        if user_answer in [ans.strip() for ans in correct_answer]: # Check if the user's answer is in the list of correct answers
            print("Correct!\n")
            score += 1 # Increment score if the answer is correct
        else:
            print(f"Wrong! The correct answer is '{word['english']}'.\n")

        print(f"Your score: {score}/{len(words)}")


def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == '__main__':
    main()