from account import Account
from car import Car
from uberX import UberX
from user import User
from driver import Driver


if __name__ == "__main__":
    print("Nuestros Autos")

    car = UberX("AD122JM", Account("Dickinson Duran",
                "19671029", "dickinson@gmail.com", "4564"), "Chevrolet", "Aveo")
    print(vars(car))
    print(vars(car.driver))

    user = User("Johana Hernadez", "22498939", "joha_02@gmail.com", "369")
    print(vars(user))
