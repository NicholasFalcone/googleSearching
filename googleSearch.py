from googlesearch import search, get_tbs
import datetime
import csv

class Settings:
    csvFilePath = 'out.csv'
    maxResults = 20
    tbs = datetime.datetime.now()
    tld = ".com"
    needToSave = False

settings = Settings()

#List of results
results = list()

title = """
_____________________________________________________________

                    Google search tool.
_____________________________________________________________

"""

def main():
    print(title)
    startProcess()

def startProcess():
    needToSave = False
    #Takeing information from the user to prepare the seaching
    query = input('Enter a query...\n')
    maxElements = inputNumber("Max results? ")
    setBaseInfo()
    setLevelOfDomain()
    createTBS()
    #Start method to generate results
    startSearching(query, maxElements)


#Function to class the Google API and extrapolate resutls
def startSearching(query, maxResults):
    print("Start searching...")
    for url in search(query, stop=maxResults, tbs=settings.tbs):
        print(url)
        results.append(url+" ")
    print(settings.csvFilePath)
    print("\n\n________Seaching end....________")
    if settings.needToSave:
        saveResult(results)
    else:
        main()
#Function to save all on csv file
def saveResult(results):
    print("\n\nSaving this record on " + settings.csvFilePath +"...\n\n")
    file = open (settings.csvFilePath, 'w')
    wtr = csv.writer(file, delimiter=' ', lineterminator='\n')
    for x in results : wtr.writerow ([x])
    file.close()
    main()
#loop back to take a number
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 
#loop back to take a boolean response 
def checkBooleanCondiction(message):
  while True:
    userInput = input(message)     
    if userInput != 'y' and userInput != 'n':
       print("Not an valid value! Try again.")
       continue
    else:
        if userInput == 'y':
            return True
        else:
            return False 

def createTBS():
    startDate = datetime.datetime.now()
    endPeriod = inputDate("Insert end period(enter of current day):\n")
    tbs = get_tbs(startDate, endPeriod)
    settings.tbs = tbs

def setBaseInfo():
    needToSave = checkBooleanCondiction("save on default csv file? (y/n)")
    settings.needToSave = needToSave
    if needToSave:
        print('Insert output file name...(current name: out.csv)')
        outFileName = input()
        if outFileName != "":
            settings.csvFilePath = outFileName

def setLevelOfDomain():
    topLayerOfDomain = input("(optional) Insert the top level of domain: ")
    if topLayerOfDomain == '':
        topLayerOfDomain = '.com'
    settings.tld = topLayerOfDomain

def inputDate(message):
    while True:
        try:
            date_entry = input('Enter a date in YYYY-MM-DD format')
            year, month, day = map(int, date_entry.split('-'))
            date = datetime.date( year, month, day)       
        except ValueError:
            print("Not a valid date! Try again.")
            continue
        else:
            return date 
            break 

main()