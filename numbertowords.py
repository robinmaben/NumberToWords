def words(num):
    places = ['', '', 'Hundred', 'Thousand', 'Thousand', 'Lac']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    numbers = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', ]

    digits = []
    index = 0

    while num > 0:
        digit = num % 10
        digits.insert(0, (digit, index))

        num -= digit
        num /= 10
        index += 1

    for digit in digits:
        if digit[1] == 1 or digit[1] == 4:
            getter = tens
        else:
            getter = numbers
        print(getter[int(digit[0])] + ' ' + places[int(digit[1])])
