class Ferrari:
    def accelerate(self):
        print("Ferrari accelerates rapidly with a loud roar!")
    def brake(self):
        print("Ferrari brakes smoothly using carbon ceramic brakes.")
class BMW:
    def accelerate(self):
        print("BMW accelerates with a refined and powerful surge.")
    def brake(self):
        print("BMW applies hydraulic braking technology.")
def test_drive(car):
    car.accelerate()
    car.brake()
    print()
f = Ferrari()
b = BMW()
test_drive(f)
test_drive(b)