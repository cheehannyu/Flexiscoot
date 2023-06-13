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
         for flight in flights:
            if flight['EndLoc'] == sys.argv[3]:
                cost = flight['Cost']

         for flight in flights:
            if flight['EndLoc'] == sys.argv[3]:
                days_left = flight['Days']
                
        namefee = namechange(cost, days_left)
        
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
    namefee = 0
    if int(days_left) > 30:
         namefee = round(int(cost) * 0.5, 2)
    else:
        # this allows the namefee paid to increase as the days left before the flight decreases
        namefee = round(int(cost) * 0.5 * 30 / int(days_left) + (int(cost) * 0.5) )

    # since name change fee is capped at $100 for extra-long-haul flights, namefee will be capped at $100
    # https://cdn.flyscoot.com/prod/docs/default-source/fee-chart/scoot_fees_chart_en.pdf
    if namefee > 100:
         namefee = 100

    return namefee


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
