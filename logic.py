import csv
import sys

def main():

    functions = ['namechange', 'flightchange']
    if sys.argv[2] not in functions:
        sys.exit("Error 1: Function not specified")

    # Assume csv file given is in the format of a list of dictionaries
    # flights is a list of flights, each being a dictionary containing flight info
    flights = []
    filename = sys.argv[1]
    with open(filename) as file:
        csv_reader = csv.DictReader(file)
        for item in csv_reader:
            flights.append(item)
           
    # Initialise namefee and flightfee to be 0
    namefee = 0
    flightfee = 0
    
    if sys.argv[2] == 'namechange':
        namefee = namechange()
    elif sys.argv[2] == 'flightchange':
        for flight in flights:
            if flight['EndLoc'] == sys.argv[3]:
                costfrom = flight['Cost']
            elif flight['EndLoc'] == sys.argv[4]:
                costto = flight['Cost']

        flightfee = flightchange(costfrom, costto)

    adminfee = namefee + flightfee
    return adminfee

def namechange(cost):
    #TODO


def flightchange(costfrom, costto):
    costto = int(costto)
    costfrom = int(costfrom)
    difference = costto - costfrom

    # If the second flight is cheaper, credit is not awarded
    if difference < 0:
        difference = 0

    return difference


if __name__ == "__main__":
    main()
