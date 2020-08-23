class CoffeeMachine:

    def __init__(self, money, water, milk, mejorante, beans, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.mejorante = mejorante
        self.beans = beans
        self.cups = cups
        self.user_input = None
        self.coffee_type = None
        self.question = None

    def ask_input(self):
        self.user_input = input("{}".format(self.question))
        return self.user_input

    def purchase(self):
        self.question = 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - cafe Paola, ' \
                        'back - to main menu:'
        self.coffee_type = CoffeeMachine.ask_input(self)
        if self.coffee_type == "1":  # 1 = expresso (250 ml of water and 16 g of coffee beans. It costs $4)
            self.money += 4
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            if self.water < 0:
                self.money -= 4
                self.water += 250
                self.beans += 16
                self.cups += 1
                print("Sorry, not enough water!")
                return self.money, self.water, self.beans, self.cups
            elif self.beans < 0:
                self.money -= 4
                self.water += 250
                self.beans += 16
                self.cups += 1
                print("Sorry, not enough coffee beans!")
                return self.money, self.water, self.beans, self.cups
            elif self.cups < 0:
                self.money -= 4
                self.water += 250
                self.beans += 16
                self.cups += 1
                print("Sorry, not enough disposable cups!")
                return self.money, self.water, self.beans, self.cups
            else:
                print("I have enough resources, making you a coffee!")
                return self.money, self.water, self.beans, self.cups

        elif self.coffee_type == "3":  # 3 = cappuccino (200 ml of water, 100 ml of milk, and 12 g of coffee.
            # It costs $6)
            self.money += 6
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            if self.water < 0:
                self.money -= 6
                self.water += 200
                self.milk += 100
                self.beans += 12
                self.cups += 1
                print("Sorry, not enough water!")
                return self.money, self.water, self.beans, self.cups, self.milk
            elif self.milk < 0:
                self.money -= 6
                self.water += 200
                self.milk += 100
                self.beans += 12
                self.cups += 1
                print("Sorry, not enough milk!")
                return self.money, self.water, self.beans, self.cups, self.milk
            elif self.beans < 0:
                self.money -= 6
                self.water += 200
                self.milk += 100
                self.beans += 12
                self.cups += 1
                print("Sorry, not enough coffee beans!")
                return self.money, self.water, self.beans, self.cups, self.milk
            elif self.cups < 0:
                self.money -= 6
                self.water += 200
                self.milk += 100
                self.beans += 12
                self.cups += 1
                print("Sorry, not enough disposable cups!")
                return self.money, self.water, self.beans, self.cups, self.milk
            else:
                print("I have enough resources, making you a coffee!")
                return self.money, self.water, self.beans, self.cups, self.milk

        elif self.coffee_type == "2":  # 2 = latte (350 ml of water, 75 ml of milk, and 20 g of coffee beans.
            # It costs $7)
            self.money += 7
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            if self.water < 0:
                self.money -= 7
                self.water += 350
                self.milk += 75
                self.beans += 20
                self.cups += 1
                print("Sorry, not enough water!")
                return self.money, self.water, self.beans, self.cups, self.milk
            elif self.milk < 0:
                self.money -= 7
                self.water += 350
                self.milk += 75
                self.beans += 20
                self.cups += 1
                print("Sorry, not enough milk!")
                return self.money, self.water, self.beans, self.cups, self.milk
            elif self.beans < 0:
                self.money -= 7
                self.water += 350
                self.milk += 75
                self.beans += 20
                self.cups += 1
                print("Sorry, not enough coffee beans!")
                return self.money, self.water, self.beans, self.cups, self.milk
            elif self.cups < 0:
                self.money -= 7
                self.water += 350
                self.milk += 75
                self.beans += 20
                self.cups += 1
                print("Sorry, not enough disposable cups!")
                return self.money, self.water, self.beans, self.cups, self.milk
            else:
                print("I have enough resources, making you a coffee!")
                return self.money, self.water, self.beans, self.cups, self.milk
        elif self.coffee_type == "4":  # 4 = cafe Paola (350 ml of water, 75 ml of milk, 10 ml de mejorante
            # and 20 g of coffee beans.It costs $10)
            self.money += 10
            self.water -= 350
            self.milk -= 75
            self.mejorante -= 10
            self.beans -= 20
            self.cups -= 1
            if self.water < 0:
                self.money -= 10
                self.water += 350
                self.milk += 75
                self.mejorante += 10
                self.beans += 20
                self.cups += 1
                print("Sorry, not enough water!")
                return self.money, self.water, self.beans, self.cups, self.milk, self.mejorante
            elif self.milk < 0:
                self.money -= 7
                self.water += 350
                self.milk += 75
                self.mejorante += 10
                self.beans += 20
                self.cups += 1
                print("Sorry, not enough milk!")
                return self.money, self.water, self.beans, self.cups, self.milk, self.mejorante
            elif self.mejorante < 0:
                self.money -= 7
                self.water += 350
                self.milk += 75
                self.mejorante += 10
                self.beans += 20
                self.cups += 1
                print("Oh no!!, no queda mejorante en la maquina! Que cosa mas cososa! :( ")
                print("NOTA : La maquina viene sin mejorante de fabrica porque es azucaroso y "
                      "atrae demasiadas hormigas, hay que rellenar. ( -> menu principal -> fill.) ")
                return self.money, self.water, self.beans, self.cups, self.milk, self.mejorante
            elif self.beans < 0:
                self.money -= 7
                self.water += 350
                self.milk += 75
                self.mejorante += 10
                self.beans += 20
                self.cups += 1
                print("Sorry, not enough coffee beans!")
                return self.money, self.water, self.beans, self.cups, self.milk, self.mejorante
            elif self.cups < 0:
                self.money -= 7
                self.water += 350
                self.milk += 75
                self.mejorante += 10
                self.beans += 20
                self.cups += 1
                print("Sorry, not enough disposable cups!")
                return self.money, self.water, self.beans, self.cups, self.milk, self.mejorante
            else:
                print("I have enough resources, making you un delicioso CAFE PAOLA!")
                return self.money, self.water, self.beans, self.cups, self.milk, self.mejorante
        elif self.coffee_type == "back":
            print("Returning to main menu")
            return self.money, self.water, self.beans, self.cups, self.milk
        else:
            print("not a valid choice")
            return self.money, self.water, self.beans, self.cups, self.milk

    def filling(self):
        self.question = "Write how many ml of water do you want to add:"
        fill_water = int(CoffeeMachine.ask_input(self))
        self.water += fill_water
        self.question = "Write how many ml of milk do you want to add:"
        fill_milk = int(CoffeeMachine.ask_input(self))
        self.milk += fill_milk
        self.question = "Write how many ml of delicioso mejorante do you want to add:"
        fill_mejorante = int(CoffeeMachine.ask_input(self))
        self.mejorante += fill_mejorante
        self.question = "Write how many grams of coffee beans do you want to add:"
        fill_beans = int(CoffeeMachine.ask_input(self))
        self.beans += fill_beans
        self.question = "Write how many disposable cups of coffee do you want to add:"
        fill_cups = int(CoffeeMachine.ask_input(self))
        self.cups += fill_cups
        return self.water, self.milk, self.beans, self.cups

    def taking(self):
        print("I gave you $", self.money)
        self.money = 0
        return self.money

    def supplies(self):
        print("The coffee machine has:")
        print(self.water, "ml of water")
        print(self.milk, "ml of milk")
        print(self.mejorante, "ml of mejorante")
        print(self.beans, "grams of coffee beans")
        print(self.cups, " disposable cups")
        print(self.money, " $")

    def main_menu(self):
        self.question = "Write action (buy, fill, take, remaining, exit):"
        action = CoffeeMachine.ask_input(self)
        while action != "exit":
            if action == "buy":
                CoffeeMachine.purchase(self)
                self.question = "Write action (buy, fill, take, remaining, exit):"
                action = CoffeeMachine.ask_input(self)
            elif action == "fill":
                CoffeeMachine.filling(self)
                self.question = "Write action (buy, fill, take, remaining, exit):"
                action = CoffeeMachine.ask_input(self)
            elif action == "take":
                CoffeeMachine.taking(self)
                self.question = "Write action (buy, fill, take, remaining, exit):"
                action = CoffeeMachine.ask_input(self)
            elif action == "remaining":
                CoffeeMachine.supplies(self)
                self.question = "Write action (buy, fill, take, remaining, exit):"
                action = CoffeeMachine.ask_input(self)
            else:
                print("Not a valid order")
                self.question = "Write action (buy, fill, take, remaining, exit):"
                action = CoffeeMachine.ask_input(self)


coffee = CoffeeMachine(550, 400, 540, 0, 120, 9)
coffee.__init__(550, 400, 540, 0, 120, 9)
coffee.main_menu()

#  NOTA : Mejorante = Leche condensada, para que a Paola le guste el cafe ^^

#  NOTA : La maquina viene de fabrica con estos subministros ya cargados:
#
#  money = 550
#  water = 400
#  milk = 540
#  mejorante = 0 (la maquina no lleva cargado de fabrica porque se pudre facil,
#                 hay que llenar antes de hacer un cafe para Paola -> orden "fill")
#  beans = 120
#  cups = 9
