import csv
import os

## def clearConsole

def clear_console():
   os.system('cls')

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

global print1
global print2

global pro3
global race
pro3 = True
race = True

auxiliarDeck = []
chineseDeck = []
chineseParkDeck = []
chineseRaceDeck = []
chineseWinDeck = []

## def non starting importExport functions

def importCSVinDeck(csvFile, deck):
   resetDeck(auxiliarDeck)
   copyCSVinAuxiliarDeck(csvFile)
   copyAuxiliarDeckinDeck(deck)
   resetDeck(auxiliarDeck)
	
def exportDeckinCSV(deck, csvFile):
   resetDeck(auxiliarDeck)
   copyDeckinAuxiliarDeck(deck)
   copyAuxiliarDeckinCSV(csvFile)
   resetDeck(auxiliarDeck)

## def functions inside non starting importExport functions

def resetDeck(deck):
   for capsule in range(len(deck)):
      del deck[0]
# capsule is a section of a deck composed of status line and statmentAnswer line

def copyCSVinAuxiliarDeck(csvFile):
   with open("{}.csv".format(csvFile)) as file:
      reader = csv.reader(file, delimiter=",")
      for row in reader:
            auxiliarDeck.append(row)

def copyAuxiliarDeckinDeck(deck):
   CSVline = 0
   linesPerCapsule = 2
   totalLines = len(auxiliarDeck)
   totalCapsules = int(totalLines / linesPerCapsule)
   for capsule in range(totalCapsules):
      deck.append([])
      for linea in range(linesPerCapsule):
         deck[capsule].append(auxiliarDeck[CSVline])         
         CSVline += 1

def copyDeckinAuxiliarDeck(deck):
   linesPerCapsule = 2
   for capsule in range(len(deck)):
      for line in range(linesPerCapsule):
         auxiliarDeck.append(deck[capsule][line])

def copyAuxiliarDeckinCSV(csvFile):
   with open("{}.csv".format(csvFile), "w", newline="") as file:
      writer = csv.writer(file, delimiter=",")
      writer.writerows(auxiliarDeck)

## def starting importExport functions

def importLanguageCSVinLanguageDeck(languageCSV, languageDeck):
   resetDeck(auxiliarDeck)
   copyLanguageCSVinAuxiliarDeck(languageCSV)
   copyAuxiliarDeckinLanguageDeck(languageDeck)
   resetDeck(auxiliarDeck)
	
def exportLanguageDeckinCSV(languageDeck, csvFile):
   resetDeck(auxiliarDeck)
   copyLanguageDeckinAuxiliarDeck(languageDeck)
   copyAuxiliarDeckinCSV(csvFile)
   resetDeck(auxiliarDeck)

## def functions inside starting importExport functions

def copyLanguageCSVinAuxiliarDeck(languageCSV):
   with open("{}.csv".format(languageCSV)) as file:
      reader = csv.reader(file, delimiter=",")
      for row in reader:
            auxiliarDeck.append(row)

def copyAuxiliarDeckinLanguageDeck(languageDeck):
   element = 0
   for element in range(len(auxiliarDeck)):
      languageDeck.append(auxiliarDeck[element])
      element += 1

def copyLanguageDeckinAuxiliarDeck(languageDeck):
   totalLines = len(languageDeck)
   for line in range(totalLines):
      auxiliarDeck.append([0, 0, 0])
      auxiliarDeck.append(languageDeck[line])


## def askCapsule

def askCapsule():
   previousFaultState = "noPriorFailure"
   showStatement(previousFaultState)
   askAnswer(previousFaultState)

## def showStatement

def showStatement(previousFaultState):
   global print1
   print1 = item["statement"]
   print(item["statement"])
   

## def askAnswer

def askAnswer(previousFaultState):
   global print2
   clear_console()
   print(print1)
   answerRequest = input(": ")
   clear_console()
   print2 = answerRequest
   print(print1 + ": " + print2)

   examAnswer = examRequestWithItem(answerRequest)
   examinationAction(examAnswer, previousFaultState)

## def examRequestWithItem

def examRequestWithItem(request):
   global print1
   clear_console()
   if request == "-showall":
      return "-showall"
   if request == "-showremain":
      return "-showremain"
   if request == "-showstudy":
      return "-showstudy"
   if request == "-showlearn":
      return "-showlearn"
   if request == "-reset":
      return "-reset"
   if request == "-exit":
      return "-exit"
   if request == "-help":
      return "-help"
   elif request == item["answer"]: 
      print1 += "\n:" + "\033[92m {}\033[00m" .format(print2)
      return "Correct"
   else:
      print(print1 + "\n:" + "\033[91m {}\033[00m" .format(print2))
      print(">", item["answer"])
      step = input()
      return "Incorrect"

## def examinationAction

def examinationAction(examAnswer, previousFaultState):
   if examAnswer == "-showall":
      showDeck(chineseDeck)
   if examAnswer == "-showremain":
      showDeck(chineseParkDeck)
   if examAnswer == "-showstudy":
      showDeck(chineseRaceDeck)
   if examAnswer == "-showlearn":
      showDeck(chineseWinDeck)
   elif examAnswer == "-reset":
      resetPro3()
   elif examAnswer == "-exit":
      exit()
   elif examAnswer == "-help":
      print("Use the following commands while studying:")
      print("'-showall', get all sentences/answers")
      print("'-showremain', get all remaining sentences/answers")
      print("'-showstudy', get all inProgress sentences/answers")
      print("'-showlearn', get all learned sentences/answers")
      print("'-reset', all time changes")
      print("'-exit', leave Pro3")
      print("'-help', get all commands")
   elif examAnswer == "Incorrect":
      failedAnswerAction(previousFaultState)
   elif examAnswer == "Correct":
      successfulAnswerAction(previousFaultState)

## def failedAnswerAction

def failedAnswerAction(previousFaultState):
   if previousFaultState == "noPriorFailure":
      chineseRaceDeck[0][0][1] = decreaseTank()

      askAnswer("priorFailure")

   elif previousFaultState == "priorFailure":
      askAnswer("priorFailure")

## def successfulAnswerAction

def successfulAnswerAction(previousFaultState):

   if previousFaultState == "noPriorFailure": 
      chineseRaceDeck[0][0][1] = increaseTank() 

   print(print1)
   
   examCapsuleMovement()

   adjustFuel()

   sortDeck(chineseRaceDeck)
   
   examCapsuleMovement()

## def decreaseTank

def decreaseTank():
   tankSelection = int(chineseRaceDeck[0][0][1])
   if tankSelection < 2:
      tankOperation = 0
   else:
      tankOperation = tankSelection - 2
   return str(tankOperation)

## def increaseTank 

def increaseTank():
   tankOperation = int(chineseRaceDeck[0][0][1]) + 2
   return str(tankOperation)

## def adjustFuel

def adjustFuel():     
   chineseRaceDeck[0][0][0] = refuel()

   spendFuel()

## def functions inside adjustFuel function

def refuel():
   return str(chineseRaceDeck[0][0][1]) 

def spendFuel():
   for row in chineseRaceDeck:
      fuelSelection = int(row[0][0])
      if fuelSelection > 0:
         fuelSelection -= 1
         row[0][0] = str(fuelSelection)

## def sortDeck and selectionParameterOrder

def sortDeck(deck):
   deck.sort(key=selectionParameterOrder)
def selectionParameterOrder(parameterOrder):
  return parameterOrder[0][0][0]

## def examCapsuleMovement

def examCapsuleMovement():
   fuel = int(chineseRaceDeck[0][0][0])
   tank = int(chineseRaceDeck[0][0][1])

   if tank >= 12:

      extractFromDeckInsertToDeck(chineseRaceDeck, chineseWinDeck)

      resetWinCapsule()

      exportDeckinCSV(chineseWinDeck, "chineseWin")
      exportDeckinCSV(chineseRaceDeck, "chineseRace")
      prYellow("WWWWWIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNNNN")
      step = input()

   if fuel >= 1:
   ## if elegirElemento("combustible")
      extractFromDeckInsertToDeck(chineseParkDeck, chineseRaceDeck)

      exportDeckinCSV(chineseParkDeck, "chinesePark")
      exportDeckinCSV(chineseRaceDeck, "chineseRace")
      prYellow("ONE MOOOOOREEEEEEE")
      step = input()

## def extractFromDeckInsertToDeck

def extractFromDeckInsertToDeck(extractionDeck, insertionDeck):
   insertionDeck.insert(0, extractCapsulefromDeck(extractionDeck, 0)) 
def extractCapsulefromDeck(deck, position):
   capsuleSave = deck[position]
   del deck[position]
   return capsuleSave

## def resetWinCapsule

def resetWinCapsule(): 
   chineseWinDeck[0][0][0] = 0
   chineseWinDeck[0][0][1] = 10
   chineseWinDeck[0][0][2] = 3

## def preparation

def preparation():
   extractFromDeckInsertToDeck(chineseParkDeck, chineseRaceDeck)
# to extract first capsule from park and insert in race to initiate correctly

## def showDeck

def showDeck(deck):
   try:
      if len(deck[0][1][0]) > 1:
         for capsule in range(len(deck)):
            print(str(capsule+1) + ". " + deck[capsule][1][0] + " - " + deck[capsule][1][1])
      elif len(deck) != 0:
         for line in range(len(deck)):
            print(str(line+1) + ". " + deck[line][0] + " - " + deck[line][1])
   except:
      print("No learned Sentences")

def resetPro3():
   global race
   resetDeck(chineseParkDeck)
   exportDeckinCSV(chineseParkDeck, "chinesePark")
   resetDeck(chineseRaceDeck)
   exportDeckinCSV(chineseRaceDeck, "chineseRace")
   resetDeck(chineseWinDeck)
   exportDeckinCSV(chineseWinDeck, "chineseWin")
   race = False

   print("Reset Complete")

def exit():
   global race
   global pro3
   pro3 = False
   race = False

## pro3 LOOP

while pro3:

   ## intructions

   if race == True:
      clear_console()
      prCyan("Welcome and let's learn!")
      print("")
      print("All changes are saved automatically")
      print("Use the following commands while studying:")
      print("'-showall', get all sentences/answers")
      print("'-showremain', get all remaining sentences/answers")
      print("'-showstudy', get all inProgress sentences/answers")
      print("'-showlearn', get all learned sentences/answers")
      print("'-reset', all time changes")
      print("'-exit', leave Program")
      print("'-help', get all commands")
      print("")
      print("Let's go to study!: pulse" + "\033[92m {}\033[00m" .format("ENTER"))
      step=input()

   ## importExport CSV and decks

   importLanguageCSVinLanguageDeck("chinese", chineseDeck)
   importCSVinDeck("chineseRace", chineseRaceDeck)

   if len(chineseRaceDeck) < 1:
      exportLanguageDeckinCSV(chineseDeck, "chinesePark")

   importCSVinDeck("chinesePark", chineseParkDeck)
   importCSVinDeck("chineseWin", chineseWinDeck)

   if len(chineseRaceDeck) < 1:
      preparation()

   exportDeckinCSV(chineseParkDeck, "chinesePark")
   exportDeckinCSV(chineseRaceDeck, "chineseRace")

   race = True

   ## MAIN LOOP

   while race:

      item = {
         "fuel": int(chineseRaceDeck[0][0][0]),
         "tank": int(chineseRaceDeck[0][0][1]),
         "statement": chineseRaceDeck[0][1][0],
         "answer": chineseRaceDeck[0][1][1],
      }

      print1 = ""
      print2 = ""

      askCapsule()

      exportDeckinCSV(chineseParkDeck, "chinesePark")
      exportDeckinCSV(chineseRaceDeck, "chineseRace")
      exportDeckinCSV(chineseWinDeck, "chineseWin")
      
      prYellow("CONTIIIINUE>>>>>>>>")
      step = input()


print("Exit Complete")
step=input()