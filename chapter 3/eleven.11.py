total_miles = 0
total_gallons = 0

miles = int(input("Enter miles driven (-1 to end): "))

while miles != -1:
    gallons = int(input("Enter gallons used: "))
    mpg = miles / gallons
    print("Miles per gallon for this tankful:", round(mpg))

    total_miles = total_miles + miles
    total_gallons = total_gallons + gallons

    miles = int(input("Enter miles driven (-1 to end): "))

if total_gallons != 0:
    combined_mpg = total_miles / total_gallons
    print("Combined miles per gallon:", round(combined_mpg))
else:
    print("Blank data.")

   