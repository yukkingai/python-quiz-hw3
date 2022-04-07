from components.quizQuestions import questions
from components import vars, quizTally, qfour
from progress.bar import Bar

print("■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□")
print("■                                                     □")
print("□ =========== WELCOME TO THE MARVEL QUIZ ============ ■")
print("□                                                     ■")
print("■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□" "\n")
print("                                Are you ready ?? ^____^" "\n")

bar = Bar('Processing', max=20)
for i in range(20):
    bar.next()
bar.finish()

qfour.quest()



print("Total Scores You have: " + str(vars.quizTotal) + "\n")

#after answer all the questions, figure out who your character is
quizTally.total(vars.quizTotal)
