onesArray = ['','one','two', 'three','four','five',
                'six','seven','eight','nine','ten',
                'eleven','twelve','thirteen','fourteen',
                'fifteen','sixteen','seventeen','eighteen',
                'nineteen']
tensArray = ['','','twenty','thirty','forty','fifty','sixty',
                'seventy','eighty','ninety']


def ConvertDigitsToWords(digits):
    millions = digits / 1000000
    millionsRemainder = digits % 1000000

    thousands = millionsRemainder / 1000
    thousandsRemainder = millionsRemainder % 1000

    hundreds = thousandsRemainder / 100
    hundredsRemainder = thousandsRemainder % 100

    millionsPart = TranslateNumber(millions) + " million " if millions > 0 else ""
    thousandsPart = TranslateNumber(thousands) + " thousand " if thousands > 0 else ""
    hundredsPart = onesArray[hundreds] + " hundred " if hundreds > 0 else ""

    output = millionsPart + thousandsPart + hundredsPart + TranslateTens(hundredsRemainder)

    return output


def TranslateNumber(number):
    output = ""
    if number/100 > 0:
        output += onesArray[number/100] + " hundred "
    if number%100 > 0:
        output += TranslateTens(number % 100)
    return output


def TranslateTens(number):
    if number < 20:
        return str(onesArray[number])
    else:
        tens = number / 10
        tensRemainder = number % 10
        return str(tensArray[tens]) + " " + str(onesArray[tensRemainder])


def main():
    print("Enter number to convert: ")
    number = input() 
    print (ConvertDigitsToWords(number))


if __name__ == '__main__':
    main()