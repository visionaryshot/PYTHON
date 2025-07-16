Principal = int(input('Enter any amount:'))
Duration = int(input('For how many years:')) 
Rate = float(input('Enter your desire annual rate:'))
Monthly_Duration = 12 * Duration
Monthly_rate =  Rate / 100 / 12

Client = Monthly_rate * ((1 + Monthly_rate) **Monthly_Duration)
Customer = ((1 + Monthly_rate) **Monthly_Duration) - 1

Monthly_value = Principal * (Client / Customer)
print('Your monthly payment is:,' , Monthly_value)