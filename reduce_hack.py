from fractions import Fraction
from functools import reduce

def product(fracs):
	t = Fraction(reduce(lambda x,y: x*y, fracs))
	return t.numerator, t.denominator

if __name__ == '__main__':
	total_fractions_enter = int(input('Enter total number of fractions:'))
	fractions = []
	for fraction in range(0,total_fractions_enter):
		numerator = int(input('Enter numerator of '+str(fraction+1)+' fraction:'))
		denominator = int(input('Enter denominator of '+str(fraction+1)+' fraction:'))
		fractions.append(Fraction(numerator,denominator))

	numerator, denominator = product(fractions)
	print(numerator, denominator)
