ninja = {
    "first_name": "Jesse",
    "last_name": "Awesome",
    "treats": "placeTreats",
    "pet_food": "placeFood",
}

pet = [
    {"name": "Chewy","type": "dog","tricks": "backflip"},
    {"name": "Leo","type": "dragon","tricks": "Breath_Fire"}
]

class Ninja:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.treats = data["treats"]
        self.pet_food = data["pet_food"]
        self.pet = Dragon(pet[1])                   # <- Change index of pet here. [0] is a dog that can backflip [1] is a dragon that can breath fire. they can not do one another's tricks
        # implement the following methods:
        # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self
    def show_time(self):
        self.pet.breath_fire()          # <- change your pets special trick here
        return self

class Pet:
    def __init__(self, data, health=100, energy=25):
        self.name = data["name"]
        self.type = data["type"]
        self.tricks = data["tricks"]
        self.health = health
        self.energy = energy

    # implement the following methods:
    def sleep(self):
        print(f"{self.name} is sleeping")
        self.energy += 25
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        print(f"Feeding {self.name}")
        self.energy += 5
        self.health += 10
        return self
    # play() - increases the pet's health by 5
    def play(self):
        print(f"Walking {self.name}")
        self.health +=5
        return self
    # noise() - prints out the pet's sound
    def noise(self):
        print(f"Bathing {self.name}, splish splash!")
        return self

class Dragon(Pet):
    def breath_fire(self):
        if self.type != "dragon":
            print(f"{self.name} can not preform this")
        else:
            print(f"{self.name} just spit flames")
            return self

class Dog(Pet):
    def backflip(self):
        if self.type != "dog":
            print(f"{self.name} can not preform this")
        else:
            print(f"{self.name} just did a backflip")
            return self

user_jes = Ninja(ninja).walk().feed().bathe().show_time()




