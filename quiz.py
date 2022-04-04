from components.quizQuestions import questions
from components import vars, quizTally, qfour


print("■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□")
print("==============WELCOME TO THE MARVEL QUIZ===============")
print("■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□")
print("                                Are you ready ?? ^____^")

qfour.quest()



print("Total Scores You have: " + str(vars.quizTotal) + "\n")

#after answer all the questions, figure out who your character is
quizTally.total(vars.quizTotal)
