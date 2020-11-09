def leapyear(year):
    return (year % 4 == 0 and
            year % 100 != 0 or
            year % 400 == 0)

if (leapyear(1900)):
    print("Ja, das ist ein Schaltjahr.")
else:
    print("Nein, das ist kein Schaltjahr.")
print(leapyear(2000))
print(leapyear(2004))
print(leapyear(2006))
print(leapyear(1776))