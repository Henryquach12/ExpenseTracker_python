def credit_card(digits):
    if (digits[:2] == "34" or digits[:2] == "37") and len(digits) == 15:
        print("This is an American Express credit card")
    elif (digits[:2] == "51" or digits[:2] == "52" or digits[:2] == "53"  or digits[:1] == "54"  or digits[:1] == "55") and len(digits) == 16:
        print("This is a Mastercard")
    elif digits[:2] == "4" and (len(digits) == 13 or len(digits) == 16):
        print("This is a Visa cards")
    odd_digits = 0
    even_digits = 0
    total = 0
    digits = digits.replace("-","")
    digits = digits.replace(" ","")
    digits = digits[::-1]
    for digit in digits[::2]:
        odd_digits += int(digit)
    for digit in digits[1::2]:
        double_digits = int(digit) * 2
        if double_digits >= 10:
            even_digits += double_digits % 10 + double_digits // 10
        else: 
            even_digits += double_digits
    total = odd_digits + even_digits 
    if total % 10 == 0:
        print("Your credit card is valid")
    else:
        print("Your credit card is invalid")
running = True
while running:     
    credit_card(input("Enter your credit card number: "))

