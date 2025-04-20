class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5         # Start at mid-level
        self.energy = 5         # Start at mid-level
        self.happiness = 5      # Start at mid-level
        self.tricks = []        # List to store learned tricks

    def eat(self):
        """Feeds the pet: reduces hunger and increases happiness."""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has eaten and feels happier!")

    def sleep(self):
        """Lets the pet sleep: increases energy."""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good nap and feels rested.")

    def play(self):
        """Plays with the pet: adjusts energy, happiness, and hunger."""
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played and had a blast!")
        else:
            print(f"{self.name} is too tired to play. Let them rest!")

    def train(self, trick):
        """Teaches the pet a new trick."""
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows how to {trick}!")

    def show_tricks(self):
        """Displays all tricks the pet has learned."""
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        """Displays the current state of the pet."""
        print(f"\n📋 {self.name}'s Status:")
        print(f"   Hunger   : {self.hunger}/10")
        print(f"   Energy   : {self.energy}/10")
        print(f"   Happiness: {self.happiness}/10\n")


# Test our Pet class with rex_pappi!
rex_pappi = Pet("Rex_Pappi")

# Display initial status
rex_pappi.get_status()

# Perform some actions
rex_pappi.eat()
rex_pappi.sleep()
rex_pappi.play()
rex_pappi.train("roll over")
rex_pappi.train("sit")
rex_pappi.train("roll over")  

# Show all learned tricks
rex_pappi.show_tricks()

# Display final status
rex_pappi.get_status()
