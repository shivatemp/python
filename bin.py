#This is the alternative for the tip.py course assignment using l and r - strip.

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    strip_d = d.lstrip("$")
    dollars = float(strip_d)
    return dollars


def percent_to_float(p):
    strip_p = p.rstrip("%")
    percent = float(strip_p)/100
    return percent


main()