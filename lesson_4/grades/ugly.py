ERROR_MSG = "Score must be between 0.0 and 1.0"

score = input("Enter Score: ")
score = float(score)


def die():
  print(ERROR_MSG)
  quit()


if (score < 0.0):
  die()
elif (score > 1.0):
  die()
elif (score < 0.6):
  print("F")
  quit()
elif (score < 0.7):
  print("D")
  quit()
elif (score < 0.8):
  print("C")
  quit()
elif (score < 0.9):
  print("B")
  quit()
else:
  print("A")
  quit()
