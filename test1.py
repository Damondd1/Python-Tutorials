"""
        1. ორი რიცხვის გამოთვლა
        მოცემულია a = 17 და b = 5. გამოიტანე ჯამი, სხვაობა, ნამრავლი, 
        ჩვეულებრივი გაყოფა, მთელი გაყოფა, ნაშთი და a რიცხვი b ხარისხში
"""
"""
a = 17
b = 5 
print(a + b)
print(a - b)
print(a * b)
print(a / b)
"""

"""
price = 25
quantity = 4 
delivery = 7

print(price * quantity + delivery)
"""
"""
price = 200
discount_percent = 30
print (price - discount_percent)
"""
"""
minutes = 135 
print (minutes / 60 )
"""
"""
balance = 100
print(100 - 50 + 30)
"""

# num = 6
# numbers = [10,20,30,40]
# whole = 1
# for number in numbers:
#         whole + number
#         print(whole)



""""
number = 65
sold = 38
print(number - sold)

if number > 30:
    print("შესაკვეთია") 

else: 
    print("საკმარისია")
    """

"""""
Students = 29
Bus1 = 12
print(Students / Bus1)
print(Students // Bus1)
print(Students - Bus1 * 2)

if Students / Bus1 < 4:
    print("3")
    """

""""
notebook_price = 3.50
sold = 4 
discount = 0.0
total_price = notebook_price * sold

if notebook_price * sold > 10:
    discount = (total_price / 100) * 10

payment_amount = total_price - discount


print("ჯამური თანხა:",total_price)
print("ფასდაკლება:",discount)
print("გადასახდელი თანხა: ",payment_amount)
"""

"""""
total_amount = 47.50
extra_amount = (47.50 / 100 * 10)
person_three = (3)
total_three = (total_amount + extra_amount) / person_three
print(total_amount + extra_amount)

print(round(total_three,2))
"""
'''
first_name = "  nino  ".strip()
first_letter = first_name[0].upper() 
first_name = first_name.replace('n',first_letter,1)
last_name = "  BERIDZE ".lower().strip()
print(first_name)
print(last_name)
'''
'''
thislist_shopping = ["პური", "რძე", "კვერცხი", "შაქარი"]

thislist_shopping.remove("შაქარი")
thislist_shopping.append("ყველი")
thislist_shopping[1] = "მაწონი"


print(thislist_shopping)    
print(len(thislist_shopping))
'''

''''
prices = [12.5, 8.0, 25.0, 4.5, 18.0]

value = 15
prices_upper_value = []
for rec in prices:
    if rec <= value:
        prices_upper_value.append(rec)
        


print(prices_upper_value)
'''

'''
grades = {"მათემატიკა": 8, "ინგლისური": 7, "ქართული": 9}
grades["ინგლისური"] = 9
grades.update ({"ისტორია": 10})
print("საშუალო ქულა: ",sum(grades.values())/len(grades))
'''
''''
football = {"ნინო", "გიორგი", "ლუკა", "ანა"}
chess = {"ანა", "გიორგი", "მარიამი"}
print(football.intersection(chess))
print(football.difference(chess))
print(football.union(chess))


print(football.symmetric_difference(chess))
'''
""""
dimensions = (40, 25, 20)
length = 40
width = 25
height = 20  
whole = length * width * height
if whole > 15000:

    print("დიდი ამანათი")
else:
    print("პატარა ამანათი")
"""

sessions = (12, 15, 18, 21)
current_hour = 16


rem_sessions = []
rem2_sessions = []
for session in sessions:
    if session > current_hour:
        rem_sessions.append(session)
        
    elif session < current_hour :
        rem2_sessions.append(session)
        
    

            

    
print("გვიან იწყება:",rem_sessions)
print("ადრე იწყება:",rem2_sessions)




















