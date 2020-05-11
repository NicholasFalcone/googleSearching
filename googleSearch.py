from googlesearch import search
import csv

#List of results
results = list()
csvFilePath = 'out.csv'

title = """
_____________________________________________________________

            Google search tool.
_____________________________________________________________

"""

def main():
    print(title);
    startProcess()

def startProcess():
    needToSave = False
    #Takeing information from the user to prepare the seaching
    query = input('Enter a query...\n')
    maxElements = inputNumber("Max results? ")
    save = input("save on default csv file? (y/n)")
    topLayerOfDomain = input("(optional) Insert the top level of domain: ")

    if topLayerOfDomain == '':
        topLayerOfDomain = '.com'
    if save == 'y':
        needToSave = True
    else:
        needToSave = False
    #Start method to generate results
    startSearching(query, topLayerOfDomain, maxElements, needToSave)

#Function to class the Google API and extrapolate resutls
def startSearching(query, tld, maxResults, save):
    print("Start searching...")
    for url in search(query, stop=maxResults):
        print(url)
        results.append(url+" ")
    print("\n\n________Seaching end....________")
    if save:
        saveResult(results)
    else:
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
     
#Function to save all on csv file
def saveResult(results):
    print("\n\nSaving this record on " + csvFilePath + '...\n\n');
    file = open (csvFilePath, 'w')
    wtr = csv.writer(file, delimiter=' ', lineterminator='\n')
    for x in results : wtr.writerow ([x])
    file.close()
    main()

main()