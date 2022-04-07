from components import quizQuestions, vars
from components.quizQuestions import questions
from emoji import emojize

woman = emojize(":woman: :woman: :woman: :woman: :woman: :woman: :woman: :woman: :woman: :woman: :woman: :woman: :woman: :woman: :woman: :woman: :woman: :woman: :woman: :woman:\n")
um = emojize(":umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella: :umbrella:\n")
moj = emojize(":fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: :fire: \n")
up = emojize(":thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up: :thumbs_up:")

def quest():
    answer1 = questions["q1"][input(questions["q1"]["question"])]
    print(answer1)
    vars.quizTotal += answer1
    print(up)

    answer2 = questions["q2"][input(questions["q2"]["question"])]
    print(answer2)

    vars.quizTotal += answer2

    print(woman)


    answer3 = questions["q3"][input(questions["q3"]["question"])]
    print(answer3)

    vars.quizTotal += answer3
    print(moj)


    answer4 = questions["q4"][input(questions["q4"]["question"])]
    print(answer4)

    vars.quizTotal += answer4
    print(moj)


    answer5 = questions["q5"][input(questions["q5"]["question"])]
    print(answer5)

    vars.quizTotal += answer5
    print(um)
