base = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen','Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
tens = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
hundreds = ['One-Hundred', 'Two-Hundred', 'Three-Hundred', 'Four-Hundred', 'Five-Hundred', 'Six-Hundred', 'Seven-Hundred','Eight-Hundred', 'Nine-Hundred']
thousands = ['One-Thousand', 'Two-Thousand', 'Three-Thousand', 'Four-Thousand', 'Five-Thousand', 'Six-Thousand', 'Seven-Thousand', 'Eight-Thousand', 'Nine-Thousand']

def int_to_word(number):
	if number < 20: return base[number]
	if number < 100: return tens[-1 + number/10] + ('-' + base[number % 10] if (number % 10 != 0) else '')
	if number < 1000: return hundreds[-1 + number/100] + ('-' + int_to_word(number % 100) if (number % 100 != 0) else '')
	if number < 10000: return thousands[-1 + number/1000] + ('-' + int_to_word(number % 1000) if (number % 1000 != 0) else '')
	if number < 100000: return base[number/1000] + '-Thousand' + ('-' + int_to_word(number % 1000) if (number % 1000 != 0) else '')
	if number < 1000000: return int_to_word(number/1000) + '-Thousand' + ('-' + int_to_word(number % 10000) if (number % 10000 != 0) else '')
	if number < 10000000: return int_to_word(number / 1000000) + '-Million' + ('-' + int_to_word(number % 1000000) if (number % 1000000 != 0) else '')

	return (str(number) + ' not recognized.')
