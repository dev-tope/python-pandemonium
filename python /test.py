print("Welcone to Rock-Paper-Scissors")
print()
print("Are You Ready To Play")
print()
p1Name = input("Player1, whats your name? ")
print()
p2Name = input("Player2, whats your name? ") 

from getpass import getpass as input
print("""
  ROCK, PAPER OR SCISSORS?

  R - ROCK
  P - PAPER
  S - SCISSORS
""")



p1_score = 0
p2_score = 0
cont = ""

while True: 
  p1Selection = input(p1Name + " whats your play > ")
  p2Selection = input(p2Name + " whats your play > ")
  if p1Selection == "R":
    if p2Selection == "R":
      print("DRAW")
    elif p2Selection == "P":
      print(p2Name + " WINS")
      p2_score += 1
    elif p2Selection =="S":
      print(p1Name + " WINS")
      p1_score += 1 
  elif p1Selection == "P":
    if p2Selection == "R":
      print(p1Name + " WINS")
      p1_score += 1 
    elif p2Selection == "P":
      print("DRAW")
    elif p2Selection == "S":
      print (p2Name + " WINS")
      p2_score += 1
  elif p1Selection == "S":
    if p2Selection == "R":
      print (p2Name + " WINS")
      p2_score += 1
    elif p2Selection == "P":
      print (p1Name + " WINS")
      p1_score += 1 
    elif p2Selection == "S":
      print("DRAW")
  else:
    print("Invalid Entry")
    continue
  if p1_score == 3 or p2_score == 3:
    print("SCORE:", p1Name, " = ", p1_score, " | ", p2Name, " = ", p2_score)
    print()
    print("Thanks for playing")
    exit()
  else:
    continue



