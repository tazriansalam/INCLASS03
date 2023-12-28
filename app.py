class Weapon:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.level = 1
    def upgrade(self):
        self.level = 1
    def display(self):
        print(f"Weapon Name: {self.name}")
        print(f"Weapon Type: {self.type}")
        print(f"Weapon Level: {self.level}")

    def run():
        # Create two instances of the Weapon class
        weapon1 = Weapon("Sword", "Melee")
        weapon2 = Weapon("Bow", "Ranged")

        # Display initial details of the weapons
        weapon1.display()
        weapon2.display()

        # Upgrade the first weapon and display its updated details
        weapon1.upgrade()
        weapon1.display()