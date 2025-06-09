# Polymorphism

Polymorphism allows methods with the same name to have different behavior in different classes.

### Example:

class Bird:
def fly(self):
print("Flying in the sky")

class Penguin(Bird):
def fly(self):
print("Penguins can't fly.")

def let_it_fly(bird):
bird.fly()

let_it_fly(Bird()) # Flying in the sky
let_it_fly(Penguin()) # Penguins can't fly.

This allows flexible and extensible code.
