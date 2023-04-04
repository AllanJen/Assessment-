#The questions and answers stored.
questions = [" What main classes are in A block?", " What main classes are in B block?", " What main classes are in C block?", " What main classes are in E block?", " What main classes are in F block?", " What main classes are in G block?", " What main classes are in H block?", " What main classes are in M block?", ] #questions variable
answers = ["Art", "Tech", "Math", "Woodwork and Metalwork", "Science", "English", "Food", "Music"] #answers variable 


def Function():
#Code for the questions
  score = 0   

  print("Welcome to my test on what subjects are in each block at Rangiora High School!")

  for i in range(len(questions)):
      print("Question", i+1, "-", questions[i])
      user_answer = input("Answer = ") 
      if user_answer.lower() == answers[i].lower(): 
          print("Correct!") #shows the user they got it correct and adds 1 score
          score += 1   
      else:
          print("Incorrect. The correct answer is", answers[i])    #Dosen't add 1 to the score, also reveals the correct answer to the user.

  print("Your score is:", score, "out of", len(questions))    #determines how many questions you answered correctly and how many you got wrong.

Function()

print("Hope you had fun!")