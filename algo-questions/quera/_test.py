# def number_to_word(number):
#     ones = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
#     tens = ["", "ده", "بیست", "سی", "چهل",
#             "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]
#     hundreds = ["", "صد", "دویست", "سیصد", "چهارصد",
#                 "پانصد", "ششصد", "هفتصد", "هشتصد", "نهصد"]
#     # اضافه کردن میلیون و میلیارد
#     thousands = ["", " هزار ", " میلیون ", " میلیارد "]
#     lennumber = len(number)
#     if int(number) == 0:
#         return "صفر"
#     if lennumber == 1:
#         return ones[int(number)]
#     elif lennumber == 2:
#         if int(number) < 20:
#             return ones[int(number)]
#         else:
#             return tens[int(number[0])] + " و " + ones[int(number[1])]
#     elif lennumber == 3:
#         return hundreds[int(number[0])] + " و " + tens[int(number[1])] + " و " + ones[int(number[2])]
#     else:
#         words = ''
#         for i in range((lennumber - 1) // 3, 0, -1):
#             if number[:-i*3] != '0':
#                 words += number_to_word(number[:-i*3]) + thousands[i]
#                 number = number[-i*3:]
#         words += number_to_word(number)
#         return words


# number = input("لطفا عدد را وارد کنید: ")
print("000" == "0")
