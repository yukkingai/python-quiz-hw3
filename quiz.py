from components.quizQuestions import questions
from components import vars, quizTally
from emoji import emojize

print("■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□")
print("==============WELCOME TO THE MARVEL QUIZ===============")
print("■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□")
print("                                Are you ready ?? ^____^")

q1-4.4quest()



print("Total Scores You have: " + str(vars.quizTotal) + "\n")

#after answer all the questions, figure out who your character is
quizTally.total(vars.quizTotal)
