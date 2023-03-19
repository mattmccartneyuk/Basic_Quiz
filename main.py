import random

def main():  
    
    quiz_items = [
        ["England", "London"],
        ["Wales", "Cardiff"],
        ["Scotland", "Edinburgh"],
        ["Ireland", "Dublin"],
        ["France", "Paris"],
        ["Germany", "Berlin"],
        ["United States of America", "Washington D.C"],
        ["Russia", "Moscow"],
        ["Spain", "Madrid"],
        ["Italy", "Rome"]        
    ]

    quiz_index = random.randint(0, len(quiz_items) - 1)
    chosen_city = quiz_items[quiz_index][1]
    chosen_country = quiz_items[quiz_index][0]
    quiz_items.pop(quiz_index)
    
    print(f"What is the capital of {chosen_country}?")

    question_prompts = []

    random_answer_placement = random.randint(0, 3)
    for i in range(4):
        if random_answer_placement == i:
            question_prompts.append(chosen_city)
        else:
            quiz_index = random.randint(0, len(quiz_items) - 1)
            question_prompts.append(quiz_items[quiz_index][1])
            quiz_items.pop(quiz_index)

    letter = ""
    for i in range(4):
        match i: 
            case 0:
                letter = "a"
            case 1:
                letter = "b"
            case 2:
                letter = "c"
            case 3:
                letter = "d"
        print(f"({letter}) - {question_prompts[i]}")
    
    user_input = input("Answer: ")

    letter_to_number = False
    match user_input:
        case "a":
            letter_to_number = 0
        case "b":
            letter_to_number = 1
        case "c":
            letter_to_number = 2
        case "d":
            letter_to_number = 3
    
    if letter_to_number == random_answer_placement:
        print("Correct!")
    else:
        print("Incorrect")

        

main()