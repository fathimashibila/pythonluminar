dob_date=int(input("enter the dob date="))
dob_month=int(input("enter the dob month="))
dob_year=int(input("enter the dob year="))
current_date=int(input("enter the current date="))
current_month=int(input("enter the current month="))
current_year=int(input("enter the current year="))

year=current_year-dob_year
month=current_month-dob_month
if(year==0):
    print("Age=", month, "months")
elif(year==1 & dob_month!=current_month ):
    print("Age=", month, "months")
else:
    print("Age=",year)