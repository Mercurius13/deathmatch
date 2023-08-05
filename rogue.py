import random
import time


class Rogue:
    def __init__(self, name):
        self.health = 50
        self.max_health = 50
        self.attack = 0
        self.shielding = 0
        self.healing = 0
        self.drain_attack = 0
        # separate attack for drain function
        self.enemy_attack = 0
        # enemy attack
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
        self.rgb = ''
        self.action = ''
        self.blood_pact_looplock = False
        self.blood_pact_suicide = False
        self.tourniquet_looplock = False

        self.name = name
        self.percentage = 1
        # attack multiplier for blood pact and tourniquet

    def reset_cooldowns(self):
        self.blood_pact_looplock = False

    def regen_aux(self):
        pass

    @staticmethod
    def roll_d20():
        return random.randint(1, 20)

    @staticmethod
    def roll_d10():
        return random.randint(1, 10)

    def choose_rgb(self, rgb):
        self.rgb = rgb

    def present_options(self, color=None):
        def present_blue():
            print('You have chosen the blue dice.')
            print('You can use:')
            print('(20) Shield')
            print('(10) Parry')

        def present_red():
            print('You have chosen the red dice.')
            print('You can use: ')
            print('(20) Cleave')
            print('(10) Riposte')
            print('(10) Blood Pact')

        def present_green():
            print('You have chosen the green dice.')
            print('You can use:')
            print('(20) Tourniquet')
            print('(10) Drain')

        if color is None:
            if 'blue' in self.rgb:
                present_blue()
            elif 'red' in self.rgb:
                present_red()
            elif 'green' in self.rgb:
                present_green()
        elif color == 'blue':
            present_blue()
        elif color == 'red':
            present_red()
        elif color == 'green':
            present_green()

    def choose_die(self):
        racism = input("Choose two die: ").split(" ")
        if len(racism) != 2:
            condition = True
        else:
            condition = racism[0] not in ["blue", "red", "green"] or racism[1] not in ["blue", "red", "green"]
        if condition:
            print("Incorrect spelling or number of die.")
            self.choose_die()
        else:
            if "blue" in racism and not self.blood_pact_suicide:
                self.choose_rgb("blue")
                self.present_options()
                self.choose_action(input("Choose your action!: "), self.rgb)
            if "red" in racism and not self.blood_pact_suicide:
                self.choose_rgb("red")
                self.present_options()
                self.choose_action(input("Choose your action!: "), self.rgb)
            if "green" in racism and not self.blood_pact_suicide:
                self.choose_rgb("green")
                self.present_options()
                self.choose_action(input("Choose your action!: "), self.rgb)

    def shield(self):
        # Me when the enemy rolls a 20
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        if number >= 15:
            self.shielding += int((number * 1.5) // 1)
        else:
            self.shielding += number
        time.sleep(0.5)
        print(f"Your shield is now {self.shielding}.")

    def parry(self):
        # Block, if enemy is attacking, throw R
        number = self.roll_d10()
        time.sleep(1)
        print(f"You got {number}!")
        self.shielding += number
        time.sleep(0.5)
        print(f"Your shield is now {self.shielding}.")
        if number < 6:
            time.sleep(0.5)
            print("You rolled 5 or less! Rolling a red dice...")
            self.choose_rgb("red")
            self.present_options()
            self.choose_action(input("Choose your action!: "), self.rgb)

    def cleave(self):
        # Death and destruction
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        if number >= 15:
            self.attack += int((int((number * 1.5) // 1) * self.percentage) // 1)
        else:
            self.attack += int((number * self.percentage) // 1)
        if self.percentage != 1:
            self.percentage = 1
        time.sleep(0.5)
        print(f"Your attack is now {self.attack}.")

    def riposte(self):
        # Block, if all dmg blocked, Attack, else throw G
        number = self.roll_d10()
        time.sleep(1)
        print(f"You got {number}!")
        self.shielding += number
        time.sleep(0.5)
        print(f"Your shield is now {self.shielding}.")
        if self.enemy_attack == 0:
            pass
        elif self.shielding >= self.enemy_attack:
            time.sleep(0.5)
            print("Enemy attack has been negated! Attacking...")
            self.attack += number
            print(f"Your attack is now {self.attack}.")
        elif self.shielding < self.enemy_attack:
            time.sleep(0.5)
            print("Enemy attack has not been negated! Rolling a green dice...")
            self.choose_rgb("green")
            self.present_options()
            self.choose_action(input("Choose your action!: "), self.rgb)

    def blood_pact(self):
        # Self-Attack, Double next Attack, throw R
        if not self.blood_pact_looplock:
            self.blood_pact_looplock = True
            number = self.roll_d10()
            time.sleep(1)
            print(f"You got {number}!")
            self.health -= number
            if self.health <= 0:
                self.blood_pact_suicide = True
                pass
            time.sleep(0.5)
            print(f"Your health is now {self.health}.")
            time.sleep(0.5)
            print("Next attack is doubled!")
            self.percentage *= 2
            time.sleep(0.5)
            print("Rolling a red dice...")
            self.choose_rgb("red")
            self.present_options()
            self.choose_action(input("Choose your action!: "), self.rgb)
        else:
            time.sleep(0.5)
            print("You can only use this action once per turn!")
            self.choose_rgb("red")
            self.present_options()
            self.choose_action(input("Choose your action!: "), self.rgb)

    def tourniquet(self):
        # Heal, Half next Attack
        if not self.tourniquet_looplock:
            self.tourniquet_looplock = True
            number = self.roll_d20()
            time.sleep(1)
            print(f"You got {number}!")
            self.healing += number
            time.sleep(0.5)
            print(f"Your healing is now {self.healing}.")
            self.percentage *= 0.5
            time.sleep(0.5)
            print("Next attack is halved!")
        else:
            time.sleep(0.5)
            print("You can only use this action once per turn!")
            self.choose_rgb("green")
            self.present_options()
            self.choose_action(input("Choose your action!: "), self.rgb)

    def drain(self):
        # Attack, Heal = dmg dealt
        number = self.roll_d10()
        time.sleep(1)
        print(f"You got {number}!")
        self.drain_attack += int((number * self.percentage) // 1)
        time.sleep(0.5)
        print(f"Your drain is now {self.drain_attack}.")
        if self.percentage != 1:
            self.percentage = 1

    def choose_action(self, action, colour):
        self.action = action.lower()
        if 'blue' not in colour and self.action in ['shield', 'parry']:
            print("You can't do that.")
            print("You can only choose the actions that your dice colour allow.")
            self.present_options()
            self.action = input("Choose one of the above actions:\n")
            self.choose_action(self.action, colour)
        elif 'red' not in colour and self.action in ['cleave', 'riposte', 'blood pact']:
            print("You can't do that.")
            print("You can only choose the actions that your dice colour allow.")
            self.present_options()
            self.action = input("Choose one of the above actions:\n")
            self.choose_action(self.action, colour)
        elif 'green' not in colour and self.action in ['tourniquet', 'drain']:
            print("You can't do that.")
            print("You can only choose the actions that your dice colour allow.")
            self.present_options()
            self.action = input("Choose one of the above actions:\n")
            self.choose_action(self.action, colour)
        elif action == 'shield':
            self.shield()
        elif action == 'parry':
            self.parry()
        elif action == 'cleave':
            self.cleave()
        elif action == 'riposte':
            self.riposte()
        elif action == 'blood pact':
            self.blood_pact()
        elif action == 'tourniquet':
            self.tourniquet()
        elif action == 'drain':
            self.drain()
        else:
            print("You can't do that.")
            self.present_options()
            self.action = input("Choose one of the above actions: ")
            self.choose_action(self.action, colour)
