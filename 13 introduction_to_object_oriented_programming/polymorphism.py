# Polymorphism Example: Same method, different behavior

class Bird:
    def fly(self):
        print("Flying in the sky")

class Penguin(Bird):
    def fly(self):
        print("Penguins can't fly.")

def let_it_fly(bird):
    bird.fly()

bird = Bird()
penguin = Penguin()

let_it_fly(bird)     # Flying in the sky
let_it_fly(penguin)  # Penguins can't fly.
