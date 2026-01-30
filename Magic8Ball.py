#Magic8Ball.py
#Name: Jenna Kramer
#Date: 01/28/26
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  input("Ask me a yes or no question.")
  answers = ("Yes", "No", "Perhaps", "Not yet", "In the near future", "Never", "No one knows", "Patience, little one", 
             "Ask again later", "You must donate to my gofundme for clarity", "Reflect upon yourself", "The future is murky", 
             "Your question needs refining", "Most definitely", "Yikes", "Proceed carefully", "You will see in due time", 
             "To the highest degree", "Absolutely not", "What a silly question") 
  
  #Answer question randomly with one of the options from your earlier list.
  r = random.random() * len(answers)
  r = int(r) #cut off any decimal values
  # print(r)
  response = answers[r]
  print(response)
if __name__ == '__main__':
  main()
