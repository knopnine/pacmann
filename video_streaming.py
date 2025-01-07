#import library
from tabulate import tabulate
import random
import string

# some data
userdata = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

data_list = [["Shandy", "Basic Plan", 12, "shandy-2134"],
            ["Cahya", "Standard Plan", 24, "cahya-abcd"],
            ["Ana", "Premium Plan", 5, "ana-2f9g"],
            ["Bagus", "Basic Plan", 11, "bagus-9f92"]]

headers= ["Feature", "Basic", "Standard", "Premium"]

plan = [["Stream", True, True, True],
        ["Download", True, True, False],
        ["SD Quality", True, True, False],
        ["HD Quality", False, True, True],
        ["UHD Quality", False, False, True],
        ["4K", False, False, True],
        ["8K", False, False, False],
        ["Device Limit", 1, 2, 4],
        ["Content","3rd party movie only","Basic Plan + sports", "Standard Plan + Original movies"],
        ["Price", 120_000, 160_000, 200_000]]


plan_index = {
            "Basic Plan": 1,
            "Standard Plan": 2,
            "Premium Plan": 3
        }

# print plan as table
print("Pacflix Plan List")
print(tabulate(plan, headers=headers, tablefmt="github"))

# class user
class User:
    #init username
    def __init__(self, username):
        self.username = username
        if self.username in userdata:
            self.current_plan = userdata[self.username][0]
            self.duration_plan = userdata[self.username][1]
            self.referral_id = userdata[self.username][2]
        else :
            NewUser(self.username)
    
    def check_benefit(self):        
        print("PacFlix Benefit Plans")
        print("")       
        print(tabulate(plan, headers=headers, tablefmt="pretty"))
        print("")

    def benefit_detail(self, plan, plan_name):      
        # Define the headers
        headers = ["Feature", plan_name]

        # chek if the plan name is valid
        if plan_name not in plan_index:
            print(f"Invalid plan name: {plan_name}")
            return
        
        # get the column index for the plan
        index = plan_index[plan_name]

        #select only the "Feature" and the plan column
        plan_detail = [[row[0], row[index]] for row in plan]

        # print the result
        print(tabulate(plan_detail, headers=headers, tablefmt="pretty"))

    def check_plan(self, username):
        #iterate through userdata
        for key, value in userdata.items():
            #if username is found
            if key == username:
                #print the user's plan
                print(f"Username: {key}")
                print(f"Plan: {value[0]}")
                print(f"Duration: {value[1]} bulan")
                print("") 
                print(f"{value[0]} Pacflic benefit list :")
                benefit_detail = self.benefit_detail(plan, value[0])
            #if username is not found
            else:
                continue

    def upgrade_plan(self, username, new_plan):
        DISCOUNT = 0.05
        for key, value in userdata.items():
            if username == key:
                current_plan = value[0]
                duration = value[1]
                index_currentplant = plan_index[current_plan]
                index_newplan = plan_index[new_plan]
                if index_newplan > index_currentplant:
                    if current_plan != new_plan:
                        if duration > 12:
                            if new_plan == "Basic Plan":
                                price = 120_000 - (120_000 * DISCOUNT)
                                userdata[username] = [new_plan, duration, value[2]]
                                return f"Upgrade to {new_plan} plan success, you get 5% discount, the price is Rp {price}"
                            elif new_plan == "Standard Plan":
                                price = 160_000 - (160_000 * DISCOUNT)
                                userdata[username] = [new_plan, duration, value[2]]
                                return f"Upgrade to {new_plan} plan success, you get 5% discount, the price is Rp {price}"
                            elif new_plan == "Premium Plan":
                                price = 200_000 - (200_000 * DISCOUNT)
                                userdata[username] = [new_plan, duration, value[2]]
                                return f"Upgrade to {new_plan} plan success, you get 5% discount, the price is Rp {price}"
                            else:
                                raise Exception("Invalid plan name")
                        else:
                            if new_plan == "Basic Plan":
                                userdata[username] = [new_plan, duration, value[2]]
                                return f"Upgrade to {new_plan} plan success, the price is Rp 120.000"
                            elif new_plan == "Standard Plan":
                                userdata[username] = [new_plan, duration, value[2]]
                                return f"Upgrade to {new_plan} plan success, the price is Rp 160.000"
                            elif new_plan == "Premium Plan":
                                userdata[username] = [new_plan, duration, value[2]]
                                return f"Upgrade to {new_plan} plan success, the price is Rp 200.000"
                            else:
                                raise Exception("Invalid plan name")
                    elif current_plan == None:
                        return "You don't have any plan yet"
                    else:
                        return "You already have this plan"
                else:
                    return "You can't downgrade your plan"   

# class new user
class NewUser(User):
    def __init__(self, username):
        self.username = username
        if self.username in userdata:
            print("Username already exist")
        else : 
            self.current_plan = None
            self.duration_plan = None
            self.referral_id = ""

    def get_referral_id(self, userdata):
        #get list of referral id from userdata
        referral_id = []
        for key, value in userdata.items():
            referral_id.append(value[2])
        return referral_id 

    def pick_plan(self, referral_id=str, plan=str):
        DISCOUNT = 0.04
        if referral_id in self.get_referral_id(userdata):
            if plan == "Basic Plan":
                price = 120_000 - (120_000 * DISCOUNT)
                self.duration_plan = 0
                self.referral_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
                userdata[self.username] = [plan, self.duration_plan, self.referral_id]
                return f"Pick {plan} plan success, you get 4% discount, the price is Rp {price}"
            elif plan == "Standard Plan":
                price = 160_000 - (160_000 * DISCOUNT)
                self.duration_plan = 0
                self.referral_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
                userdata[self.username] = [plan, self.duration_plan, self.referral_id]
                return f"Pick {plan} plan success, you get 4% discount, the price is Rp {price}"
            elif plan == "Premium Plan":
                price = 200_000 - (200_000 * DISCOUNT)
                self.duration_plan = 0
                self.referral_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
                userdata[self.username] = [plan, self.duration_plan, self.referral_id]
                return f"Pick {plan} plan success, you get 4% discount, the price is Rp {price}"
            else:
                raise Exception("Invalid plan name")
        else:
            if plan == "Basic Plan":
                self.duration_plan = 0
                self.referral_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
                userdata[self.username] = [plan, self.duration_plan, self.referral_id]
                return f"Pick {plan} plan success, the price is Rp 120.000"
            elif plan == "Standard Plan":
                self.duration_plan = 0
                self.referral_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
                userdata[self.username] = [plan, self.duration_plan, self.referral_id]
                return f"Pick {plan} plan success, the price is Rp 160.000"
            elif plan == "Premium Plan":
                self.duration_plan = 0
                self.referral_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
                userdata[self.username] = [plan, self.duration_plan, self.referral_id]
                return f"Pick {plan} success, the price is Rp 200.000"
            else:
                raise Exception("Invalid plan name")
    
    def check_plan(self, username):
        print("You don't have any plan yet")

# test case                        
user_1 = User(username = "Ana")
user_1.check_benefit()
user_1.check_plan("Ana")

user_2 = User(username = "Shandy")
user_2.check_benefit()
user_2.check_plan("Shandy")

user_1.upgrade_plan("Ana", "Standard Plan")
user_2.upgrade_plan("Shandy", "Premium Plan")
user_2.check_plan("Shandy")

user_3 = NewUser(username = "Budi")
user_3.pick_plan("shandy-2134", "Premium Plan")

print(userdata)

user_4 = User(username = "Budi")
user_4.check_benefit()
user_4.check_plan("Budi")
