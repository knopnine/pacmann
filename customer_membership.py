# Import Library
from tabulate import tabulate
import math

# Membership Table
headers= ["Benefit", "Silver", "Gold", "Platinum"]

membership = [["Discount", 0.08, 0.1, 0.15],
        ["Food Voucher", True, True, True],
        ["Online Transport Voucher", False, True, True],
        ["Holiday Voucher", False, False, True],
        ["Cashback", 0, 0, 0.3]]

print(tabulate(membership, headers, tablefmt="github"))

# Membership Requirement Table
headers2= ["Service", "Silver", "Gold", "Platinum"]

membership_req = [["Monthly Expense", 5_000_000, 6_000_000, 8_000_000],
                  ["Monthly Income", 7_000_000, 10_000_000, 15_000_000]]

print(tabulate(membership_req, headers, tablefmt="github"))

# Existing Member
member_list = { "Sumbul" : "Platinum", 
               "Ana" : "Gold",
                "Cahya " :  "Platinum" }

class Member:
    def __init__(self, username):
        self.username = username
        if self.username in member_list.keys():
            self.membership_type = member_list.values()
            self.grocery = []
        else:        
            self.membership_type = ""
            self.membership_discount = 0
            self.food_voucher = False
            self.online_transport_voucher = False
            self.holiday_voucher = False
            self.cashback = 0
            self.grocery = []

    def available_membership(self):
        print("PacCommerce Membership Plans")
        print("")       
        print(tabulate(membership, headers=headers, tablefmt="pretty"))
        print("")

    def membership_requirement(self):
        print("PacCommerce Membership Requirement")
        print("")       
        print(tabulate(membership_req, headers=headers2, tablefmt="pretty"))
        print("")

    def predict_membership(self, monthly_expense, monthly_income):
        silver = math.sqrt((5_000_000 - monthly_expense)**2 + (7_000_000 - monthly_income)**2)
        gold = math.sqrt((6_000_000 - monthly_expense)**2 + (10_000_000 - monthly_income)**2)
        platinum = math.sqrt((8_000_000 - monthly_expense)**2 + (15_000_000 - monthly_income)**2)

        if silver < gold and silver < platinum:
            print("Your monthly expense is", monthly_expense)
            print("Your monthly income is", monthly_income)
            print("You are eligible for Silver Membership")
            self.membership_type = "Silver"
            self.membership_discount = 0.08
            self.food_voucher = True
            member_list[self.username] = self.membership_type

        elif gold < silver and gold < platinum:
            print("Your monthly expense is", monthly_expense)
            print("Your monthly income is", monthly_income)
            print("You are eligible for Gold Membership")
            self.membership_type = "Gold"
            self.membership_discount = 0.1
            self.food_voucher = True
            self.online_transport_voucher = True
            member_list[self.username] = self.membership_type

        else:
            print("Your monthly expense is", monthly_expense)
            print("Your monthly income is", monthly_income)
            print("You are eligible for Platinum Membership")
            self.membership_type = "Platinum"
            self.membership_discount = 0.15
            self.food_voucher = True
            self.online_transport_voucher = True
            self.holiday_voucher = True
            self.cashback = 0.3
            member_list[self.username] = self.membership_type

    def get_membership(self):
        if self.membership_type == "Silver":
            print("You are a Silver Member")
            print("You have a discount of 8%")
            print("You have a Food Voucher")
        elif self.membership_type == "Gold":
            print("You are a Gold Member")
            print("You have a discount of 10%")
            print("You have a Food Voucher")
            print("You have an Online Transport Voucher")
        else:
            print("You are a Platinum Member")
            print("You have a discount of 15%")
            print("You have a Food Voucher")
            print("You have an Online Transport Voucher")
            print("You have a Holiday Voucher")
            print("You have a Cashback of 30%") 

    def calculate_expenses(self):
        grocery = self.grocery
        while True:
            try:
                grocery.append(float(input("Enter the price of the grocery item: ")))
                more_items = input("Do you want to add more items? (y/n): ").strip().lower()
                if more_items == "n":
                    break
                elif more_items == "y":
                    continue
                else:
                    print("Please enter 'y' or 'n'.")
            except ValueError:
                print("Please enter a valid number.")
        
        if self.membership_type == "Silver":
            total = sum(grocery) - (sum(grocery) * 0.08)
        elif self.membership_type == "Gold":
            total = sum(grocery) - (sum(grocery) * 0.1)
        else:
            total = sum(grocery) - (sum(grocery) * 0.15)
        print("Your total expense is", total)

#test unit
user1 = Member("Albar")
user1.available_membership()
user1.membership_requirement()
user1.predict_membership(7_000_000, 12_000_000)
print(user1.get_membership())
print(member_list)
user1.calculate_expenses()

user2 = Member("Ana")
user2.get_membership()
user2.calculate_expenses()