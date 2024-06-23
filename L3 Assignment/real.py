def mask_credit_card(number):
    number_str = str(number)
    last_four = number_str[-4:]
    masked = '*' * (len(number_str) - 4) + last_four
    return masked

print(mask_credit_card(4444444444444444))  
print(mask_credit_card("1234567890123456"))  
