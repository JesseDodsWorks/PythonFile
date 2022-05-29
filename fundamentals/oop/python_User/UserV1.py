class User:
    def __init__(self, fname, lname, email, age, points=0, status=False):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.age = age

        self.is_rewards_member = status
        self.gold_card_points = points

    def display_info(self):     # Have this method print all of the users' details on separate lines.
        print("Name:", self.first_name, self.last_name, "\tAge:", self.age,"\tEmail:", self.email, " \tRewards Memeber:", self.is_rewards_member, "\tTotal Gold Points",self.gold_card_points)

    def enroll(self):   # Have this method change the user's member status to True and set their gold card points to 200.
        if self.is_rewards_member == True:
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points += 200
            print(f"You are now a Rewards Member! As a thank you, here is {self.gold_card_points} gold points just for signing up!")

    def spend_points(self,amount):     # have this method decrease the user's points by the amount specified.
            if self.gold_card_points < amount:
                print(f"Lack of gold points. You need {amount - self.gold_card_points} points")
            else:
                self.gold_card_points = self.gold_card_points - amount
                print(f"You used {amount}. \tYou have {self.gold_card_points} left." )

user_jes = User("Jesse", "Dods", "thisEmail@live.com", 24, 100, True)

user_greg = User("Greg", "Smith", "thatEmail@live.com", 36)

user_austin = User("Austin", "Webber", "theirEmail@live.com", 48, 40, True)

user_jes.spend_points(50)

user_greg.enroll()
user_greg.spend_points(80)

user_jes.display_info()
user_greg.display_info()
user_austin.display_info()

user_jes.enroll()

user_austin.spend_points(50)