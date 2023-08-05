import random
import time


class Master:
    def __init__(self, name):
        self.health = 100
        self.max_health = 100
        self.attack = 0
        self.shielding = 0
        self.healing = 0
        self.drain_attack = 0
        self.enemy_attack = 0
        self.shockwave_unlock = False
        # checks for shockwave unlock
        self.typhoon_unlock = False
        # checks for typhoon unlock
        self.caeli_infusion_cumulative = 0
        # total permanent defence increase from caeli infusion
        self.dodge_cooldown = 0
        # Dodge cooldown
        self.dodge_trigger = False
        # checks for dodge usage
        self.laserbeam_unlock = False
        # checks for laserbeam unlock
        self.needle_cumulative = 0
        # cumulative variable for needle
        self.thorns_trigger = False
        # checks for thorns usage
        self.assimilate_unlock = False
        # checks for assimilate unlock
        self.ruminate_unlock = False
        # checks for ruminate unlock
        self.anima_infusion_dice_value = 0
        # dice value storage
        self.preservation_trigger = False
        # checks for preservation usage
        self.shockwave_cooldown = 0
        # shockwave cooldown
        self.assimilate_cooldown = 0
        # assimilate cooldown
        self.typhoon_cooldown = 0
        # typhoon cooldown
        self.last_action = ''
        self.laserbeam_cooldown = 0
        # laserbeam cooldown
        self.ruminate_cooldown = 0
        # ruminate cooldown
        self.ruminate_trigger = False
        # checks for ruminate usage
        self.vitalize_cooldown = 0
        # vitalize cooldown
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
        self.action = ''
        self.blood_pact_suicide = False
        self.name = name
        self.thorns_attack_percentage = 1
        self.thorns_defence_and_healing_percentage = 1

    def regen_aux(self):
        pass

    def reset_cooldowns(self):
        if self.ruminate_trigger:
            self.dodge_cooldown = 0
            self.shockwave_cooldown = 0
            self.assimilate_cooldown = 0
            self.typhoon_cooldown = 0
            self.laserbeam_cooldown = 0
            self.ruminate_cooldown = self.ruminate_cooldown - 1 if self.ruminate_cooldown > 0 else 0
            self.vitalize_cooldown = 0
            self.ruminate_trigger = False
        else:
            self.dodge_cooldown = self.dodge_cooldown - 1 if self.dodge_cooldown > 0 else 0
            self.shockwave_cooldown = self.shockwave_cooldown - 1 if self.shockwave_cooldown > 0 else 0
            self.assimilate_cooldown = self.assimilate_cooldown - 1 if self.assimilate_cooldown > 0 else 0
            self.typhoon_cooldown = self.typhoon_cooldown - 1 if self.typhoon_cooldown > 0 else 0
            self.laserbeam_cooldown = self.laserbeam_cooldown - 1 if self.laserbeam_cooldown > 0 else 0
            self.ruminate_cooldown = self.ruminate_cooldown - 1 if self.ruminate_cooldown > 0 else 0
            self.vitalize_cooldown = self.vitalize_cooldown - 1 if self.vitalize_cooldown > 0 else 0
        if len(self.burn) > 0:
            for i in range(len(self.burn)):
                self.burn[i] = (self.burn[i][0], self.burn[i][1] - 1)
            for i in self.burn:
                if i[1] <= 0:
                    self.burn.remove(i)
        if len(self.bleed) > 0:
            for i in range(len(self.bleed)):
                self.bleed[i] = (self.bleed[i][0], self.bleed[i][1] - 1)
            for i in self.bleed:
                if i[1] <= 0:
                    self.bleed.remove(i)
        if len(self.poison) > 0:
            for i in range(len(self.poison)):
                self.poison[i] = (self.poison[i][0], self.poison[i][1] - 1)
            for i in self.poison:
                if i[1] <= 0:
                    self.poison.remove(i)
        self.stun_duration = self.stun_duration - 1 if self.stun_duration > 0 else 0

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
            print('(10) Terra Infusion')
            print('(10) Caeli Infusion')
            print('(0) Dodge (Cooldown = 2 rounds)')

        def present_red():
            print('You have chosen the red dice.')
            print('You can use: ')
            print('(10) Ignis Infusion')
            print('(20) Needle')
            print('(0) Thorns')

        def present_green():
            print('You have chosen the green dice.')
            print('You can use: ')
            print('(10) Aqua Infusion')
            print('(10) Anima Infusion')
            print('(0) Preservation')

        def present_black():
            print('You have chosen the black dice.')
            print('You can use:')
            print('(20) Shockwave (Terra)(Cooldown = 1 round)')
            print('(20) Typhoon (Caeli)(Cooldown = 1 round)')
            print('(20) Laserbeam (Ignis)(Cooldown = 1 round)')
            print('(20) Assimilate (Aqua)(Cooldown = 1 round)')
            print('(20) Ruminate (Anima)(Cooldown = 3 rounds)')
            print('(20) Vitalize (Cooldown = 1 round)')

        if color is None:
            if 'blue' in self.rgb:
                present_blue()
            elif 'red' in self.rgb:
                present_red()
            elif 'green' in self.rgb:
                present_green()
            elif 'black' in self.rgb:
                present_black()
        elif color == 'blue':
            present_blue()
        elif color == 'red':
            present_red()
        elif color == 'green':
            present_green()
        elif color == 'black':
            present_black()

    def choose_die(self):
        if self.preservation_trigger:
            racism = input("Choose two die: ").split(" ")
            if len(racism) != 2:
                condition = True
            else:
                condition = racism[0] not in ["blue", "red", "green", "black"] or racism[1] not in ["blue", "red", "green", "black"]
        else:
            racism = input("Choose three die: ").split(" ")
            if len(racism) != 3:
                condition = True
            else:
                condition = racism[0] not in ["blue", "red", "green", "black"] or racism[1] not in ["blue", "red", "green", "black"] or racism[2] not in ["blue", "red", "green", "black"]
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
            if "green" in racism:
                for i in range(racism.count("green")):
                    self.choose_rgb("green")
                    self.present_options()
                    self.choose_action(input("Choose your action!: "), 'green')
            if "black" in racism:
                for i in range(racism.count("black")):
                    self.choose_rgb("black")
                    self.present_options()
                    self.choose_action(input("Choose your action!: "), 'black')

    def terra_infusion(self):
        # Block x2, if 3-, shockwave can be played
        self.last_action = "Terra Infusion"
        number = self.roll_d10()
        time.sleep(1)
        print(f"You got {number}!")
        if number < 4:
            if not self.shockwave_unlock:
                time.sleep(0.5)
                print(f"You rolled 3 or less! You are now terra infused.")
                self.shockwave_unlock = True
        self.shielding += int(int(number * self.thorns_defence_and_healing_percentage) // 1) * 2 + self.permanent_defence_increase + self.temporary_defence_increase - self.temporary_defence_decrease
        if self.temporary_defence_decrease > 0:
            self.temporary_defence_decrease = 0
        if self.temporary_defence_increase > 0:
            self.temporary_defence_increase = 0
        time.sleep(0.5)
        print(f"Your shield is now {self.shielding}.")
        self.rgb.pop(self.rgb.index('blue'))

    def caeli_infusion(self):
        # Permanent defence increase, if 3-, Typhoon can be played
        self.last_action = "Caeli Infusion"
        number = self.roll_d10()
        time.sleep(1)
        print(f"You got {number}!")
        if number < 4:
            if not self.typhoon_unlock:
                time.sleep(0.5)
                print(f"You rolled 3 or less! You are now caeli infused.")
                self.typhoon_unlock = True
        self.caeli_infusion_cumulative += number
        if self.caeli_infusion_cumulative > 25:
            self.caeli_infusion_cumulative = 25
            time.sleep(0.5)
            print(f"You have reached the maximum defence increase of 25.")
        else:
            self.permanent_defence_increase += number
            time.sleep(0.5)
            print(f"Your defence is now permanently increased by {self.permanent_defence_increase}/25.")
        self.rgb.pop(self.rgb.index('blue'))

    def dodge(self):
        # Take no damage this turn, skip next turn
        self.last_action = "Dodge"
        self.dodge_cooldown = 1
        self.dodge_trigger = True
        time.sleep(1)
        print("You are dodging the enemy attack! You will not play next turn.")
        self.rgb.pop(self.rgb.index('blue'))

    def ignis_infusion(self):
        # Attack x2, if 3-, Laserbeam can be played
        self.last_action = "Ignis Infusion"
        number = self.roll_d10()
        time.sleep(1)
        print(f"You got {number}!")
        if number < 4:
            if not self.laserbeam_unlock:
                time.sleep(0.5)
                print(f"You rolled 3 or less! You are now ignis infused.")
                self.laserbeam_unlock = True
        self.attack += int(int(number * self.thorns_attack_percentage) // 1) * 2 + self.permanent_attack_increase + self.temporary_attack_increase - self.temporary_attack_decrease
        if self.temporary_attack_decrease > 0:
            self.temporary_attack_decrease = 0
        if self.temporary_attack_increase > 0:
            self.temporary_attack_increase = 0
        time.sleep(0.5)
        print(f"Your attack is now {self.attack}.")
        self.rgb.pop(self.rgb.index('red'))

    def needle(self):
        # If 11+, Attack = 20, else Attack = 0. Increase dmg by 5 for every use
        self.last_action = "Needle"
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        if number > 10:
            number = 20 + self.needle_cumulative
        else:
            number = self.needle_cumulative
        if number > 50:
            number = 50
        self.attack += int(int(number * self.thorns_attack_percentage) // 1) + self.permanent_attack_increase + self.temporary_attack_increase - self.temporary_attack_decrease
        if self.temporary_attack_decrease > 0:
            self.temporary_attack_decrease = 0
        if self.temporary_attack_increase > 0:
            self.temporary_attack_increase = 0
        self.needle_cumulative += 5
        time.sleep(0.5)
        print(f"Your attack is now {self.attack}.")
        self.rgb.pop(self.rgb.index('red'))

    def thorns(self):
        # All attacks have crit while all shields and heals are halved for the rest of the game
        self.last_action = "Thorns"
        self.thorns_trigger = True
        self.thorns_attack_percentage = 1.5
        self.thorns_defence_and_healing_percentage = 0.5
        time.sleep(0.5)
        print(f"Your attacks now have crit and your defence and heals are halved.")
        self.rgb.pop(self.rgb.index('red'))

    def aqua_infusion(self):
        # Heal x2, if 3-, Assimilate can be played
        self.last_action = "Aqua Infusion"
        number = self.roll_d10()
        time.sleep(1)
        print(f"You got {number}!")
        if number < 4:
            if not self.assimilate_unlock:
                time.sleep(0.5)
                print(f"You rolled 3 or less! You are now aqua infused.")
                self.assimilate_unlock = True
        self.healing += int(int(number * self.thorns_defence_and_healing_percentage) // 1) * 2 + self.permanent_healing_increase + self.temporary_healing_increase - self.temporary_healing_decrease
        if self.temporary_healing_decrease > 0:
            self.temporary_healing_decrease = 0
        if self.temporary_healing_increase > 0:
            self.temporary_healing_increase = 0
        time.sleep(0.5)
        print(f"Your healing is now {self.healing}.")
        self.rgb.pop(self.rgb.index('green'))

    def anima_infusion_aux(self):
        # Inflicts a buff on the player and two debuffs on the enemy
        b = random.randint(1, 6)
        if b == 1:
            self.permanent_attack_increase += self.anima_infusion_dice_value
            time.sleep(0.5)
            print(f"Your attack is now permanently increased by {self.permanent_attack_increase}.")
        elif b == 2:
            self.permanent_defence_increase += self.anima_infusion_dice_value
            time.sleep(0.5)
            print(f"Your defence is now permanently increased by {self.permanent_defence_increase}.")
        elif b == 3:
            self.permanent_healing_increase += self.anima_infusion_dice_value
            time.sleep(0.5)
            print(f"Your healing is now permanently increased by {self.permanent_healing_increase}.")
        elif b == 4:
            self.temporary_attack_increase += self.anima_infusion_dice_value
            time.sleep(0.5)
            print(f"Your next attack increased by {self.temporary_attack_increase}.")
        elif b == 5:
            self.temporary_defence_increase += self.anima_infusion_dice_value
            time.sleep(0.5)
            print(f"Your next shield is increased by {self.temporary_defence_increase}.")
        elif b == 6:
            self.temporary_healing_increase += self.anima_infusion_dice_value
            time.sleep(0.5)
            print(f"Your next heal is increased by {self.temporary_healing_increase}.")
        for i in range(2):
            d = random.randint(1, 7)
            if d == 1:
                self.temporary_attack_decrease += self.anima_infusion_dice_value
                time.sleep(0.5)
                print(f"The enemy's next attack is decreased by {self.temporary_attack_decrease}.")
            elif d == 2:
                self.temporary_defence_decrease += self.anima_infusion_dice_value
                time.sleep(0.5)
                print(f"The enemy's next shield is decreased by {self.temporary_defence_decrease}.")
            elif d == 3:
                self.temporary_healing_decrease += self.anima_infusion_dice_value
                time.sleep(0.5)
                print(f"The enemy's next heal is decreased by {self.temporary_healing_decrease}.")
            elif d == 4:
                self.burn.append((self.anima_infusion_dice_value, 1))
                time.sleep(0.5)
                print(f"You have inflicted {self.burn[-1][0]} burn on the enemy for 1 round.")
            elif d == 5:
                self.bleed.append((self.anima_infusion_dice_value, 1))
                time.sleep(0.5)
                print(f"You have inflicted {self.bleed[-1][0]} bleed on the enemy for 1 round.")
            elif d == 6:
                self.poison.append((self.anima_infusion_dice_value, 1))
                time.sleep(0.5)
                print(f"You have inflicted {self.poison[-1][0]} poison on the enemy for 1 round.")
            elif d == 7:
                self.stun = True
                self.stun_duration = 1
                time.sleep(0.5)
                print(f"You have inflicted stun on the enemy for 1 round.")

    def anima_infusion(self):
        # Heal, gain a buff, inflict two debuffs onto an enemy = value, if 3-, Ruminate can be played
        self.last_action = "Anima Infusion"
        number = self.roll_d10()
        self.anima_infusion_dice_value = number
        time.sleep(1)
        print(f"You got {number}!")
        if number < 4:
            if not self.ruminate_unlock:
                time.sleep(0.5)
                print(f"You rolled 3 or less! You are now anima infused.")
                self.ruminate_unlock = True
        self.healing += int(int(number * self.thorns_defence_and_healing_percentage) // 1) + self.permanent_healing_increase + self.temporary_healing_increase - self.temporary_healing_decrease
        if self.temporary_healing_decrease > 0:
            self.temporary_healing_decrease = 0
        if self.temporary_healing_increase > 0:
            self.temporary_healing_increase = 0
        time.sleep(0.5)
        print(f"Your healing is now {self.healing}.")
        self.anima_infusion_aux()
        self.rgb.pop(self.rgb.index('green'))

    def preservation(self):
        # Don't take 75+ damage and ignore debuffs but throw only 2 die for the rest of the game
        self.last_action = "Preservation"
        self.preservation_trigger = True
        time.sleep(0.5)
        print(f"You only take up to 75 damage now, and roll one dice less.")
        self.rgb.pop(self.rgb.index('green'))

    def shockwave(self):
        # Block x2, Attack = Block
        self.last_action = "Shockwave"
        self.shockwave_cooldown = 1
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        number = int(int(number * self.thorns_defence_and_healing_percentage) // 1) * 2 + self.permanent_defence_increase + self.temporary_defence_increase - self.temporary_defence_decrease
        self.shielding += number
        if self.temporary_defence_decrease > 0:
            self.temporary_defence_decrease = 0
        if self.temporary_defence_increase > 0:
            self.temporary_defence_increase = 0
        time.sleep(0.5)
        print(f"Your shield is now {self.shielding}.")
        self.attack += int(int(number * self.thorns_attack_percentage) // 1) + self.permanent_attack_increase + self.temporary_attack_increase - self.temporary_attack_decrease
        if self.temporary_attack_decrease > 0:
            self.temporary_attack_decrease = 0
        if self.temporary_attack_increase > 0:
            self.temporary_attack_increase = 0
        time.sleep(0.5)
        print(f"Your attack is now {self.attack}.")
        self.rgb.pop(self.rgb.index('black'))

    def assimilate(self):
        # Attack x2, Heal for dmg dealt
        self.last_action = "Assimilate"
        self.assimilate_cooldown = 1
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        self.drain_attack += int(int(number * self.thorns_attack_percentage) // 1) * 2 + self.permanent_attack_increase + self.temporary_attack_increase - self.temporary_attack_decrease
        if self.temporary_attack_decrease > 0:
            self.temporary_attack_decrease = 0
        if self.temporary_attack_increase > 0:
            self.temporary_attack_increase = 0
        time.sleep(0.5)
        print(f"Your drain is now {self.drain_attack}.")
        self.rgb.pop(self.rgb.index('black'))

    def laserbeam(self):
        # Attack x 2, Burn x 2
        self.last_action = "Laserbeam"
        self.laserbeam_cooldown = 1
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        self.attack += int(int(number * self.thorns_attack_percentage) // 1) * 2 + self.permanent_attack_increase + self.temporary_attack_increase - self.temporary_attack_decrease
        if self.temporary_attack_decrease > 0:
            self.temporary_attack_decrease = 0
        if self.temporary_attack_increase > 0:
            self.temporary_attack_increase = 0
        time.sleep(0.5)
        print(f"Your attack is now {self.attack}.")
        self.burn.append((int(int(number * self.thorns_attack_percentage) // 1) + self.permanent_attack_increase, 2))
        time.sleep(0.5)
        print(f"You have inflicted {self.burn[-1][0]} burn on the enemy for 2 rounds.")
        self.rgb.pop(self.rgb.index('black'))

    def typhoon(self):
        # Attack+10, If played after Laserbeam, Burn, if played after Assimilate, Temporary defence decrease, if played after Shockwave, 25% Stun
        self.typhoon_cooldown = 1
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        self.attack += int(int(number * self.thorns_attack_percentage) // 1) + 10 + self.permanent_attack_increase + self.temporary_attack_increase - self.temporary_attack_decrease
        if self.temporary_attack_decrease > 0:
            self.temporary_attack_decrease = 0
        if self.temporary_attack_increase > 0:
            self.temporary_attack_increase = 0
        time.sleep(0.5)
        print(f"Your attack is now {self.attack}.")
        if self.last_action == 'Shockwave':
            x = random.randint(1, 4)
            if x == 1:
                self.stun = True
                self.stun_duration = 1
                time.sleep(0.5)
                print(f"Enemy is now stunned.")
        elif self.last_action == 'Laserbeam':
            self.burn.append((int(int(number * self.thorns_attack_percentage) // 1) + self.permanent_attack_increase, 1))
            time.sleep(0.5)
            print(f"You have inflicted {self.burn[-1][0]} burn on the enemy for 1 round.")
        elif self.last_action == 'Assimilate':
            self.temporary_defence_decrease += number
            time.sleep(0.5)
            print(f"You have inflicted a total of {self.temporary_defence_decrease} Temporary Defence Decrease on the enemy.")
        self.last_action = "Typhoon"
        self.rgb.pop(self.rgb.index('black'))

    def ruminate(self):
        # Temporary damage increase, Temporary defence increase, remove cooldowns on all other actions
        self.last_action = "Ruminate"
        self.ruminate_cooldown = 3
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        self.temporary_attack_increase += number
        time.sleep(0.5)
        print(f"You now have a total of {self.temporary_attack_increase} Temporary Attack Increase.")
        self.temporary_defence_increase += number
        time.sleep(0.5)
        print(f"You now have a total of {self.temporary_defence_increase} Temporary Defence Increase.")
        self.ruminate_trigger = True
        self.rgb.pop(self.rgb.index('black'))

    def vitalize(self):
        # Heal x3, increase max HP by value
        self.last_action = "Vitalize"
        self.vitalize_cooldown = 1
        number = self.roll_d20()
        time.sleep(1)
        print(f"You got {number}!")
        self.healing += int(int(number * self.thorns_defence_and_healing_percentage) // 1) * 3 + self.permanent_healing_increase + self.temporary_healing_increase - self.temporary_healing_decrease
        if self.temporary_healing_decrease > 0:
            self.temporary_healing_decrease = 0
        if self.temporary_healing_increase > 0:
            self.temporary_healing_increase = 0
        time.sleep(0.5)
        print(f"Your healing is now {self.healing}.")
        self.max_health += number
        time.sleep(0.5)
        print(f"Your max health is now {self.max_health}.")
        self.rgb.pop(self.rgb.index('black'))

    def choose_action(self, action, colour):
        self.action = action.lower()
        if 'blue' not in colour and action in ['terra infusion', 'caeli infusion', 'dodge']:
            print("You can't do that.")
            print("You can only choose the actions that your dice colour allow.")
            self.present_options()
            action = input("Choose one of the above actions:\n")
            self.choose_action(action, colour)
        elif 'red' not in colour and action in ['ignis infusion', 'needle', 'thorns']:
            print("You can't do that.")
            print("You can only choose the actions that your dice colour allow.")
            self.present_options()
            action = input("Choose one of the above actions:\n")
            self.choose_action(action, colour)
        elif 'green' not in colour and action in ['aqua infusion', 'anima infusion', 'preservation']:
            print("You can't do that.")
            print("You can only choose the actions that your dice colour allow.")
            self.present_options()
            action = input("Choose one of the above actions:\n")
            self.choose_action(action, colour)
        elif 'black' not in colour and action in ['shockwave', 'assimilate', 'typhoon', 'laserbeam', 'ruminate', 'vitalize']:
            print("You can't do that.")
            print("You can only choose the actions that your dice colour allow.")
            self.present_options()
            action = input("Choose one of the above actions:\n")
            self.choose_action(action, colour)
        elif action == 'terra infusion':
            self.terra_infusion()
        elif action == 'caeli infusion':
            self.caeli_infusion()
        elif action == 'dodge':
            if self.dodge_cooldown == 0:
                self.dodge()
            else:
                print('Action is on cooldown! Choose another action.')
                self.choose_action(input("Choose another action: "), colour)
        elif action == 'ignis infusion':
            self.ignis_infusion()
        elif action == 'needle':
            self.needle()
        elif action == 'thorns':
            if self.thorns_trigger:
                print('This action can only be played once this combat! Choose another action.')
                self.choose_action(input("Choose another action: "), colour)
            else:
                self.thorns()
        elif action == 'aqua infusion':
            self.aqua_infusion()
        elif action == 'anima infusion':
            self.anima_infusion()
        elif action == 'preservation':
            if self.preservation_trigger:
                print('This action can only be played once this combat! Choose another action.')
                self.choose_action(input("Choose another action: "), colour)
            else:
                self.preservation()
        elif action == 'shockwave':
            if self.shockwave_unlock and self.shockwave_cooldown == 0:
                self.shockwave()
            elif not self.shockwave_unlock:
                print("You must first gain terra infusion!")
                self.choose_action(input("Choose another action: "), colour)
            else:
                print('Action is on cooldown!')
                self.choose_action(input("Choose another action: "), colour)
        elif action == 'assimilate':
            if self.assimilate_unlock and self.assimilate_cooldown == 0:
                self.assimilate()
            elif not self.typhoon_unlock:
                print("You must first gain aqua infusion!")
                self.choose_action(input("Choose another action: "), colour)
            else:
                print('Action is on cooldown!')
                self.choose_action(input("Choose another action: "), colour)
        elif action == 'typhoon':
            if self.typhoon_unlock and self.typhoon_cooldown == 0:
                self.typhoon()
            elif not self.laserbeam_unlock:
                print("You must first gain caeli infusion!")
                self.choose_action(input("Choose another action: "), colour)
            else:
                print('Action is on cooldown!')
                self.choose_action(input("Choose another action: "), colour)
        elif action == 'laserbeam':
            if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                self.laserbeam()
            elif not self.assimilate_unlock:
                print("You must first gain ignis infusion!")
                self.choose_action(input("Choose another action: "), colour)
            else:
                print('Action is on cooldown!')
                self.choose_action(input("Choose another action: "), colour)
        elif action == 'ruminate':
            if self.ruminate_unlock and self.ruminate_cooldown == 0:
                self.ruminate()
            elif not self.assimilate_unlock:
                print("You must first gain anima infusion!")
                self.choose_action(input("Choose another action: "), colour)
            else:
                print('Action is on cooldown!')
                self.choose_action(input("Choose another action: "), colour)
        elif action == 'vitalize':
            if self.vitalize_cooldown == 0:
                self.vitalize()
            else:
                print('Action is on cooldown!')
                self.choose_action(input("Choose another action: "), colour)
        else:
            print("You can't do that.")
            self.present_options()
            self.action = input("Choose one of the above actions: ")
            self.choose_action(self.action, colour)
