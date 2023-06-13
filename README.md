# Flexiscoot
SIA App Challenge

#### Description:
Backend logic that calculates the admin fee for a given flight from Singapore to another country. Admin fee is calculated either from the change in cost of flight or the cost to change name. Only 1 of flight or name can be changed at a time. If both name and flight are to be changed, a new ticket must be bought entirely, and the price paid for the old ticket is forfeited.

#### Assumptions
1. All flight data is to be taken from Scoot's database/API. logic.py may be converted into an adminfee() function that simply returns the admin fee as calculated. adminfee() will take in necessary arguments from user input that determines whether a name or flight change is being requested
2. In the sample datasets, it is assumed that there is only 1 flight per destination. In reality, this is will be circumvented by using an index for each flight instead.
