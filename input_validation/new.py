class Car:
    def __init__(self, make, model, speed):
        self.make = make
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_speed(self):
        return self.speed

def main():
    manuf = input('Enter the car make: ')
    mod = input('Enter the car model: ')
    some_Speed_val = int(input('Enter the car speed: '))

    my_speed = Car(manuf, mod, some_Speed_val)

    for num in range(5):
        my_speed.accelerate()
        print('Current speed: ', my_speed.get_speed())
    for num in range(5):
        my_speed.brake()
        print('Current speed: ', my_speed.get_speed())

main()