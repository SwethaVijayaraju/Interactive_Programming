import math
def eqn(a):
    return (-5*a**5) + (69*a**2) - 47
print eqn(0)
print eqn(1)
print eqn(2)
print eqn(3)

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    return present_value*(1+rate_per_period)**periods

print "$1000 at 2% compounded daily for 3 years yields $", future_value(500, .04, 10, 10)

def polygon_area(sides, length):
    area = (sides*length**2)/(4*math.tan(math.pi/sides))
    return area
print (polygon_area(7, 3))