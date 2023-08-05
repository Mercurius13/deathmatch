import random
import time


class Lancelot:
    def __init__(self, name):
        self.health = 75
        self.max_health = 75
        self.attack = 0
        self.shielding = 0
        self.healing = 0
        self.drain_attack = 0
        self.enemy_attack = 0
        self.action = ""
        self.reflect_cooldown = 0
        self.crush_cooldown = 0
        self.charge_cooldown = 0
        self.focus_cooldown = 0
        self.focus_cumulative = 0
        # total permanent attack increase from focus
        self.swing_cooldown = 0
        self.regenerate_cooldown = 0
        self.piercer_cooldown = 0
        self.balanced_strike_cooldown = 0
        self.conserve_energy_cooldown = 0
        self.conserve_energy_trigger = 0
        self.regen = []
        self.regeneration = 0
        self.conserve_energy_check = False
        self.thorns_trigger = False
        self.preservation_trigger = False
        self.dodge_trigger = False
        self.permanent_attack_increase = 0
        # Permanent Attack Increase(buff)1
        self.permanent_defence_increase = 0
        # Permanent Defence Increase(buff)2
        self.permanent_healing_increase = 0
        # Permanent Healing Increase(buff)3
        self.temporary_attack_increase = 0
        # Temporary Attack Increase(buff)4
        self.temporary_defence_increase = 0
        # Temporary Defence Increase(buff)5
        self.temporary_healing_increase = 0
        # Temporary Healing Increase(buff)6
        self.temporary_attack_decrease = 0
        # Temporary Attack Decrease(debuff)1
        self.temporary_defence_decrease = 0
        # Temporary Defence Decrease(debuff)2
        self.temporary_healing_decrease = 0
        # Temporary Healing Decrease(debuff)3
        self.burn = []
        # Burn debuff 4
        self.bleed = []
        # Bleed debuff 5
        self.poison = []
        # Poison debuff 6
        self.stun = False
        # checks for Stun debuff 7
        self.stun_duration = 0
        # Stun debuff iterative
        self.rgb = []
        self.blood_pact_suicide = False
        self.extra_dice = False
        self.name = name
        self.percentage = 1

    def reset_cooldowns(self):
        self.reflect_cooldown = self.reflect_cooldown - 1 if self.reflect_cooldown > 0 else 0
        self.charge_cooldown = self.charge_cooldown - 1 if self.charge_cooldown > 0 else 0
        self.focus_cooldown = self.focus_cooldown - 1 if self.focus_cooldown > 0 else 0
        self.swing_cooldown = self.swing_cooldown - 1 if self.swing_cooldown > 0 else 0
        self.regenerate_cooldown = self.regenerate_cooldown - 1 if self.regenerate_cooldown > 0 else 0
        self.piercer_cooldown = self.piercer_cooldown - 1 if self.piercer_cooldown > 0 else 0
        self.balanced_strike_cooldown = self.balanced_strike_cooldown - 1 if self.balanced_strike_cooldown > 0 else 0
        self.conserve_energy_cooldown = self.conserve_energy_cooldown - 1 if self.conserve_energy_cooldown > 0 else 0
        if len(self.regen) > 0:
            for i in range(len(self.regen)):
                self.regen[i] = (self.regen[i][0], self.regen[i][1] - 1)
            for i in self.regen:
                if i[1] <= 0:
                    self.regen.remove(i)
        self.conserve_energy_trigger = self.conserve_energy_trigger - 1 if self.conserve_energy_trigger > 0 else 0

    @staticmethod
    def roll_d20():
        return random.randint(1, 20)

    @staticmethod
    def roll_d10():
        return random.randint(1, 10)

    def choose_rgb(self, rgb):
        self.rgb.append(rgb)

    def present_options(self, color=None):
        def present_blue():
            print('You have chosen the blue dice.')
            print('You can use:')
            print('(20) Armour')
            print('(20) Reflect (cooldown = 2 rounds)')

        def present_red():
            print('You have chosen the red dice.')
            print('You can use: ')
            print('(20) Crush')
            print('(10) Charge (cooldown = 2 round)')
            print('(20) Focus (cooldown = 2 round)')
            print('(10) Swing (cooldown = 1 round)')

        def present_black():
            print('You have chosen the black dice.')
            print('You can use:')
            print('(10) Regenerate (cooldown = 2 rounds)')
            print('(20) Piercer (cooldown = 2 round)')
            print('(20) Balanced Strike (cooldown = 2 round)')
            print('(0) Conserve Energy (cooldown = 1 round)')

        if color is None:
            if 'blue' in self.rgb:
                present_blue()
            elif 'red' in self.rgb:
                present_red()
            elif 'black' in self.rgb:
                present_black()
        elif color == 'blue':
            present_blue()
        elif color == 'red':
            present_red()
        elif color == 'black':
            present_black()

    def choose_die_aux(self, racism):
        if racism == "blue":
            self.choose_rgb("blue")
            self.present_options()
            self.choose_action(input("Choose your action!: "), 'blue')
        elif racism == "red":
            self.choose_rgb("red")
            self.present_options()
            self.choose_action(input("Choose your action!: "), 'red')
        elif racism == "black":
            self.choose_rgb("black")
            self.present_options()
            self.choose_action(input("Choose your action!: "), 'black')
        else:
            print("Incorrect spelling or number of die.")
            self.choose_die()

    def choose_die(self):
        if self.extra_dice:
            racism = input("Choose a dice: ").split(" ")
            condition = racism[0] not in ["blue", "red", "black"] or len(racism) != 1
            if condition:
                print("Incorrect spelling or number of die.")
                self.choose_die()
            else:
                if "blue" in racism:
                    for i in range(racism.count("blue")):
                        self.choose_rgb("blue")
                        self.present_options()
                        self.choose_action(input("Choose your action!: "), 'blue')
                if "red" in racism:
                    for i in range(racism.count("red")):
                        self.choose_rgb("red")
                        self.present_options()
                        self.choose_action(input("Choose your action!: "), 'red')
                if "black" in racism:
                    for i in range(racism.count("black")):
                        self.choose_rgb("black")
                        self.present_options()
                        self.choose_action(input("Choose your action!: "), 'black')
                self.extra_dice = False
        elif self.conserve_energy_check:
            racism = input("Choose two die: ").split(" ")
            if len(racism) != 2:
                condition = True
            else:
                condition = racism[0] not in ["blue", "red", "black"] or racism[1] not in ["blue", "red", "black"]
            if condition:
                print("Incorrect spelling or number of die.")
                self.choose_die()
            else:
                if "blue" in racism:
                    for i in range(racism.count("blue")):
                        self.choose_rgb("blue")
                        self.present_options()
                        self.choose_action(input("Choose your action!: "), 'blue')
                if "red" in racism:
                    for i in range(racism.count("red")):
                        self.choose_rgb("red")
                        self.present_options()
                        self.choose_action(input("Choose your action!: "), 'red')
                if "black" in racism:
                    for i in range(racism.count("black")):
                        self.choose_rgb("black")
                        self.present_options()
                        self.choose_action(input("Choose your action!: "), 'black')
                if self.conserve_energy_trigger == 0:
                    self.conserve_energy_check = False
        else:
            racism = input("Choose a dice: ").split(" ")
            condition = racism[0] not in ["blue", "red", "black"] or len(racism) != 1
            if condition:
                print("Incorrect spelling or number of die.")
                self.choose_die()
            else:
                if "blue" in racism:
                    for i in range(racism.count("blue")):
                        self.choose_rgb("blue")
                        self.present_options()
                        self.choose_action(input("Choose your action!: "), 'blue')
                if "red" in racism:
                    for i in range(racism.count("red")):
                        self.choose_rgb("red")
                        self.present_options()
                        self.choose_action(input("Choose your action!: "), 'red')
                if "black" in racism:
                    for i in range(racism.count("black")):
                        self.choose_rgb("black")
                        self.present_options()
                        self.choose_action(input("Choose your action!: "), 'black')

    def armour(self):
        # Block+10
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        self.shielding += number + 10
        time.sleep(0.5)
        print(f"Your shield is now {self.shielding}.")
        self.rgb.pop(self.rgb.index('blue'))

    def reflect(self):
        # Block, if all dmg blocked, Attack = dmg received, else throw a dice
        self.reflect_cooldown = 2
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        self.shielding += number
        time.sleep(0.5)
        print(f"Your shield is now {self.shielding}.")
        self.rgb.pop(self.rgb.index('blue'))
        if self.enemy_attack <= self.shielding:
            time.sleep(0.5)
            print("All damage is negated! Attacking...")
            self.attack += self.enemy_attack + self.permanent_attack_increase
            time.sleep(0.5)
            print(f"Your attack is now {self.attack}.")
        else:
            time.sleep(0.5)
            print("All damage is not negated! Rolling another dice...")
            self.extra_dice = True
            self.choose_die()

    def crush(self):
        # Attack, if 5-, throw a dice
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        self.rgb.pop(self.rgb.index('red'))
        if number >= 15:
            self.attack += int((int((number * 1.5) // 1) * self.percentage) // 1) + self.permanent_attack_increase
            time.sleep(0.5)
            print(f"Your attack is now {self.attack}.")
        elif number <= 5:
            self.attack += int((number * self.percentage) // 1) + self.permanent_attack_increase
            time.sleep(0.5)
            print(f"Your attack is now {self.attack}.")
            time.sleep(0.5)
            print("You rolled 5 or less! Rolling another dice...")
            self.extra_dice = True
            self.choose_die()
        else:
            self.attack += int((number * self.percentage) // 1) + self.permanent_attack_increase
            time.sleep(0.5)
            print(f"Your attack is now {self.attack}.")
        if self.percentage != 1:
            self.percentage = 1

    def charge(self):
        # Attack = Block x value, remove block
        self.charge_cooldown = 2
        number = self.roll_d10()
        time.sleep(1)
        print(f"You got {number}!")
        if self.shielding * number + self.permanent_attack_increase > 50:
            self.attack += 50
            time.sleep(0.5)
            print(f"Your attack is now {self.attack}.")
        else:
            self.attack += self.shielding * number + self.permanent_attack_increase
            time.sleep(0.5)
            print(f"Your attack is now {self.attack}.")
        self.shielding = 0
        time.sleep(0.5)
        print(f"Your shield is now {self.shielding}.")
        time.sleep(0.5)
        print(f"Your attack is now {self.attack}.")
        self.rgb.pop(self.rgb.index('red'))

    def focus(self):
        # Permanent damage increase
        self.focus_cooldown = 2
        number = self.roll_d20()
        self.focus_cumulative += number
        if self.focus_cumulative > 25:
            self.focus_cumulative = 25
            time.sleep(0.5)
            print(f"You have reached the maximum damage increase of 25.")
        else:
            time.sleep(1)
            print(f"You got {number}!")
            self.permanent_attack_increase += number
            time.sleep(0.5)
            print(f"Your damage is now permanently increased by {self.permanent_attack_increase}/25.")
        self.rgb.pop(self.rgb.index('red'))

    def swing(self):
        # Attack, if shielded, Attack again and roll a dice
        self.rgb.pop(self.rgb.index('red'))
        self.swing_cooldown = 1
        number = self.roll_d10()
        time.sleep(1)
        print(f"You got {number}!")
        self.attack += number + self.permanent_attack_increase
        time.sleep(0.5)
        print(f"Your attack is now {self.attack}.")
        if self.shielding > 0:
            time.sleep(0.5)
            print("You are shielded! Attacking again...")
            self.attack += number + self.permanent_attack_increase
            time.sleep(0.5)
            print(f"Your attack is now {self.attack}.")
            time.sleep(0.5)
            print("Rolling another dice...")
            self.extra_dice = True
            self.choose_die()

    def regen_aux(self):
        # Called by regenerate function to increase health once every round for three rounds
        for i in self.regen:
            self.regeneration += i[0]
        if len(self.regen) > 0:
            time.sleep(0.5)
            print(f"Your regeneration is now {self.regeneration}.")
            self.healing += self.regeneration
            self.regeneration = 0

    def regenerate(self):
        # Heal for 3 turns
        self.regenerate_cooldown = 2
        number = self.roll_d10()
        self.regen.append((number, 3))
        time.sleep(1)
        print(f"You got {number}!")
        self.rgb.pop(self.rgb.index('black'))

    def piercer(self):
        # If valve = 20, crit Attack x2, 15- = roll again
        self.piercer_cooldown = 2
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        if number <= 15:
            self.piercer()
        elif number == 20:
            time.sleep(0.5)
            print(f"Direct hit!")
            self.attack += 60 + self.permanent_attack_increase
            time.sleep(0.5)
            print(f"Your attack is now {self.attack}.")
            self.rgb.pop(self.rgb.index('black'))
        else:
            print("You missed!")
            time.sleep(0.5)
            print(f"Your attack is now {self.attack}.")
            self.rgb.pop(self.rgb.index('black'))

    def balanced_strike(self):
        # Roll x3, Attack = average value+10
        self.balanced_strike_cooldown = 2
        avg = 0
        for i in range(1, 4):
            print(f"Roll number {i}...")
            number = self.roll_d20()
            avg += number
            time.sleep(1)
            print(f"You got {number}!")
        avg //= 3
        time.sleep(0.5)
        print(f"Average roll value: {avg}")
        self.attack += avg + 10 + self.permanent_attack_increase
        time.sleep(0.5)
        print(f"Your attack is now {self.attack}.")
        self.rgb.pop(self.rgb.index('black'))

    def conserve_energy(self):
        # Heal, roll an extra dice next turn
        self.conserve_energy_cooldown = 1
        self.conserve_energy_trigger = 1
        self.conserve_energy_check = True
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        self.healing += number
        time.sleep(0.5)
        print(f"Your healing is now {self.healing}.")
        self.rgb.pop(self.rgb.index('black'))

    def choose_action(self, action, colour):
        self.action = action.lower()
        if 'blue' != colour and self.action in ['armour', 'reflect']:
            print("You can't do that.")
            print("You can only choose the actions that your dice colour allow.")
            self.present_options()
            self.action = input("Choose one of the above actions:\n")
            self.choose_action(self.action, colour)
        elif 'red' != colour and self.action in ['crush', 'charge', 'focus', 'swing']:
            print("You can't do that.")
            print("You can only choose the actions that your dice colour allow.")
            self.present_options()
            self.action = input("Choose one of the above actions:\n")
            self.choose_action(self.action, colour)
        elif 'black' != colour and self.action in ['regenerate', 'piercer', 'balanced strike', 'conserve energy']:
            print(self.rgb, self.action)
            print("You can't do that.")
            print("You can only choose the actions that your dice colour allow.")
            self.present_options()
            self.action = input("Choose one of the above actions:\n")
            self.choose_action(self.action, colour)
        elif self.action == 'armour':
            self.armour()
        elif action == 'reflect':
            if self.reflect_cooldown == 0:
                self.reflect()
            else:
                print('Action is on cooldown!')
                self.choose_action(input("Choose another action: "), colour)
        elif self.action == 'crush':
            if self.crush_cooldown == 0:
                self.crush()
            else:
                print('This action cannot be played again this turn!')
                self.choose_action(input("Choose another action: "), colour)
        elif self.action == 'charge':
            if self.charge_cooldown == 0:
                self.charge()
            else:
                print('Action is on cooldown!')
                self.choose_action(input("Choose another action: "), colour)
        elif self.action == 'focus':
            if self.focus_cooldown == 0:
                self.focus()
            else:
                print('Action is on cooldown!')
                self.choose_action(input("Choose another action: "), colour)
        elif self.action == 'swing':
            if self.swing_cooldown == 0:
                self.swing()
            else:
                print('This action cannot be played again this turn!')
                self.choose_action(input("Choose another action: "), colour)
        elif self.action == 'regenerate':
            if self.regenerate_cooldown == 0:
                self.regenerate()
            else:
                print('Action is on cooldown!')
                self.choose_action(input("Choose another action: "), colour)
        elif self.action == 'piercer':
            if self.piercer_cooldown == 0:
                self.piercer()
            else:
                print('Action is on cooldown!')
                self.choose_action(input("Choose another action: "), colour)
        elif self.action == 'balanced strike':
            if self.balanced_strike_cooldown == 0:
                self.balanced_strike()
            else:
                print('Action is on cooldown!')
                self.choose_action(input("Choose another action: "), colour)
        elif self.action == 'conserve energy':
            if self.conserve_energy_cooldown == 0:
                self.conserve_energy()
            else:
                print('This action cannot be played again this turn!')
                self.choose_action(input("Choose another action: "), colour)
        else:
            print("You can't do that.")
            self.present_options()
            self.action = input("Choose one of the above actions: ")
            self.choose_action(self.action, colour)
