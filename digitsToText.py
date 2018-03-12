onesArray = ['','one','two', 'three','four','five',
                'six','seven','eight','nine','ten',
                'eleven','twelve','thirteen','fourteen',
                'fifteen','sixteen','seventeen','eighteen',
                'nineteen']
tensArray = ['','','twenty','thirty','forty','fifty','sixty',
                'seventy','eighty','ninety']


def ConvertDigitsToWords(digits):
    thousands = digits / 1000
    thousandsRemainder = digits % 1000

    hundreds = thousandsRemainder / 100
    hundredsRemainder = thousandsRemainder % 100

    #tens = hundredsRemainder / 10
    #tensRemainder = hundredsRemainder % 10

    thousandPart = onesArray[thousands] + " thousand " if thousands > 0 else ""
    hundredsPart = onesArray[hundreds] + " hundred " if hundreds > 0 else ""
    output = thousandPart + hundredsPart + TranslateTens(hundredsRemainder)

    return output

def TranslateTens(hundredsRemainder):
    if hundredsRemainder < 20:
        return str(onesArray[hundredsRemainder])
    else:
        tens = hundredsRemainder / 10
        tensRemainder = hundredsRemainder % 10
        return str(tensArray[tens]) + " " + str(onesArray[tensRemainder])



def main():
    test = input() #Type at least two digits in terminal separated by a comma, eg., 11, 13
    #test = [1, 11, 121, 1000, 200, 99, 1001] #test values
    for item in test:
        print (ConvertDigitsToWords(item))


if __name__ == '__main__':
    main()