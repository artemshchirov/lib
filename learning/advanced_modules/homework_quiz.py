import time
from random import shuffle

question1 = ("Are potatoes a vegetable?", 't')
question2 = ("Is watermelon a fruit?", 'f')
question3 = ("Is lemon a fruit?", 't')
question4 = ("Does coffee grow on trees?", 't')

questions = [question1, question2, question3, question4]

shuffle(questions)

score = 0

start_time = time.perf_counter()

for question in questions:
    print(f'True or False: {question[0]}')
    answer = input('Please enter T if it is True or F if it is False:\n').lower()
    if answer == question[1]:
        score += 1
        print("You win!")
    else:
        print("You loose!")

end_time = time.perf_counter()

print(f'Congratulations! Your total score is: {score}/{len(questions)}, total time is: {end_time - start_time} seconds')
