from datetime import datetime

def start_date():
    syear = int(input("Please Enter the Year: "))
    smonth = int(input("Please Enter the Month: "))
    sday = int(input("Please Enter the Day: "))
    sdate = datetime(syear, smonth, sday)
    return sdate
    

def end_date():
    eyear = int(input("Please Enter the Year: "))
    emonth = int(input("Please Enter the Month: "))
    eday = int(input("Please Enter the Day: "))
    edate = datetime(eyear, emonth, eday)
    return edate

if __name__ == "__main__":

    start = start_date()
    end = end_date()

    days_between = end - start

    print(f"The days between given dates is {days_between}")
    


