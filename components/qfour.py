from components import quizQuestions, vars
from components.quizQuestions import questions
from emoji import emojize

def quest():

    answer1 = questions["q1"][input(questions["q1"]["question"])]
    print(answer1)

    vars.quizTotal += answer1
    moj = emojize(":fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire::fire:\n")
    print(moj)


    answer2 = questions["q2"][input(questions["q2"]["question"])]
    print(answer2)

    vars.quizTotal += answer2
    print(moj)


    answer3 = questions["q3"][input(questions["q3"]["question"])]
    print(answer3)

    vars.quizTotal += answer3
    print(moj)


    answer4 = questions["q4"][input(questions["q4"]["question"])]
    print(answer4)

    vars.quizTotal += answer4
    print(moj)
