base = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
hundreds = ['One-Hundred', 'Two-Hundred', 'Three-Hundred', 'Four-Hundred', 'Five-Hundred', 'Six-Hundred', 'Seven-Hundred', 'Eight-Hundred', 'Nine-Hundred']
thousands = ['One-Thousand', 'Two-Thousand', 'Three-Thousand', 'Four-Thousand', 'Five-Thousand', 'Six-Thousand', 'Seven-Thousand', 'Eight-Thousand', 'Nine-Thousand']
millions = ['One-Million', 'Two-Million', 'Three-Million', 'Four-Million', 'Five-Million', 'Six-Million', 'Seven-Million', 'Eight-Million', 'Nine-Million']

def int_to_word(number):
   if number < 20: return base[number] #gets number from first array 
   if number < 100: return tens[-2 + number/10] + ('-' + base[number % 10] if (number % 10 != 0) else '') #you lost me
   if number < 1000: return hundreds[-1 + number/100] + ('-' + int_to_word(number % 100) if (number % 100 != 0) else '') 
   if number < 10000: return thousands[-1 + number/1000] + ('-' + int_to_word(number % 1000) if (number % 1000 != 0) else '')
   if number < 100000: return tens[-2 + number/10000] + ('-' + int_to_word(number % 10000) if (number % 10000 != 0) else '') #my attempt at going above 10000
   if number < 1000000: return hundreds[-1 + number/100000] + ('-' + int_to_word(number % 100000) if (number % 100000 != 0) else '') #completely broken, trying to follow pattern
   if number < 10000000: return millions[-1 + number/1000000] + ('-' + int_to_word(number % 1000000) if (number % 1000000 != 0) else '') #completely broken, trying to follow pattern

   return (str(number) + ' not recognized.')
