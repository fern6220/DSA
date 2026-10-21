'''
Act in DSA
Programmed by: Obet Fernando
Course: ACT2
DATE: 07/02/26
'''
#Input
fam_name = input("Enter your Family name: ")
adult_tix = int(input("Enter number Adult ticket: "))
child_tix = int(input("Enter number Child ticket: "))
large_pop = int(input("Enter number of Large Popopcorn: "))
soda = int(input("Enter number of Soda: "))

#Price Input
adult_price = 100
child_price = 80
largePop_price = 50
soda_price = 30

#Process
ticket_sub = (adult_price + child_price) * (adult_tix + child_tix)
snacks_sub = (largePop_price + soda_price) * (large_pop + soda) 
grand_sub = snacks_sub + ticket_sub

discount = grand_sub * 0.90

#Output
print("===============================================")
print("   CINE NIGHT RECEIPT!")
print("===============================================")

print(f"Family           : {fam_name}")
print(F"Adult tickets    : {adult_tix} x 1000")
print(F"Child tickets    : {child_tix} x 80")
print(F"Large Popopcorn  : {large_pop} x 50 ")
print(f"Soda             : {soda} x 30")
print("-----------------------------------------------")
print(f"Subtotal         : {grand_sub}")
print(f"FInal Ttal (10% discount) :{discount}")
print("===============================================")
print("Enjoy the movie!")

