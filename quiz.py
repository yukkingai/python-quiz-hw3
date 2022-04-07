from components.quizQuestions import questions
from components import vars, quizTally, qfour
from art import *
from rich import print


print("\n")
tprint("HELLO !", font="random")
print("[bold red]■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□[/bold red]")
print("[bold magenta]■                                                     □[/bold magenta]")
print("[bold magenta]□ =========== WELCOME TO THE MARVEL QUIZ ============ ■[/bold magenta]")
print("[bold magenta]□                                                     ■[/bold magenta]")
print("[bold red]■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□■□■□■■□■□■□■□■□[/bold red]" "\n")
print("\n")
tprint("Let's Do It !", font="random-small")



qfour.quest()



print("Total Scores You have: " + str(vars.quizTotal) + "\n")

#after answer all the questions, figure out who your character is
quizTally.total(vars.quizTotal)
