""" 
Formula = 
Add to the decimal number x the value v of the roman numeral that you found:
x = x + v

Repeat stages 1 and 2 until you get all the roman numerals of r.
"""

romanValue = {
"I" : 	1,
"IV" :	4,
"V" :	5,
"IX" :	9,
"X" :	10,
"XL" :	40,
"L" :	50,
"XC" :	90,
"C" :	100,
"CD" :	400,
"D" :	500,
"CM" :	900,
"M" :	1000
}


def roman_deciman(roman):
    for i in range(len(roman)-1):
        left = roman[0] # "M"
        right = roman[-1] # "D"

roman_deciman("MD")


