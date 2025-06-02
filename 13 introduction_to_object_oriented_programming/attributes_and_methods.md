# Attributes and Methods

- **Attributes:** Variables attached to objects.
- **Methods:** Functions defined in a class, acting on objects.

### Example:

class Rectangle:
def init(self, width, height):
self.width = width
self.height = height
def area(self):
return self.width \* self.height
rect = Rectangle(10, 5)
print(rect.area()) # Output: 50

Methods typically use `self` to access attributes and other methods.

---
