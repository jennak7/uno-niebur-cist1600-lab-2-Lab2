#FutureTime.py
#Name: Jenna Kramer
#Date: 01/28/26
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour % 24
  currentMinute = now.minute

  #print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  moreHours = int(input("How many hours in the future would you like me to calculate?"))


  #Ask user for minutes
  moreMinutes = int(input("How many minutes in the future would you like me to calculate?")) 
 

  #Calculate the time after the user-supplied time has passed.
  futureMinutes = (currentMinute + moreMinutes) % 60
  extraHour = (currentMinute + moreMinutes) // 60
  futureHour = (currentHour + moreHours + extraHour) % 24

  #Do not use any if statements in calculating the time.
  #Output the future time in standard format "HH:MM"
  formattedFutureHour = str(futureHour) 
  if futureHour < 10: 
    formattedFutureHour = "0" + str(futureHour)
  formattedFutureMinutes = str(futureMinutes)
  if futureMinutes < 10: 
    formattedFutureMinutes = "0" + str(futureMinutes)
  

  print("The future time is", formattedFutureHour, ":", formattedFutureMinutes)


if __name__ == '__main__':
  main()
