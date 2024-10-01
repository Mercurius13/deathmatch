import random
import time


class Lancelot:
    def __init__(self, name):
        self.character = "lancelot"
        self.health = 75
        self.enemy_health = 0
        self.max_health = 75
        self.attack = 0
        self.shielding = 0
        self.healing = 0
        self.drain_attack = 0
        self.enemy_attack = 0
        # enemy attack
        self.enemy_drain_attack = 0
        # enemy drain attack
        self.enemy_burn = []
        self.enemy_bleed = []
        self.enemy_poison = []
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
        self.x = 0

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

    def choose_die_aux(self, racism):
        from graphics import create_and_manage_buttons
        if racism == "blue":
            self.choose_rgb("blue")
            self.choose_action(create_and_manage_buttons(["armour", "reflect", 1])[0])
        elif racism == "red":
            self.choose_rgb("red")
            self.choose_action(create_and_manage_buttons(["crush", "charge", 'focus', 'swing', 1])[0])
        elif racism == "black":
            self.choose_rgb("black")
            self.choose_action(
                create_and_manage_buttons(["regenerate", "piercer", 'balanced strike', 'conserve energy', 1])[0])

    def choose_die(self):
        from graphics import create_and_manage_buttons
        from graphics import display_text
        if not self.name == 'AI':
            if self.extra_dice:
                racism = create_and_manage_buttons(["blue", "red", "black", 1])
                condition = racism[0] not in ["blue", "red", "black"] or len(racism) != 1
                if condition:
                    display_text(("Incorrect spelling or number of die.", 2))
                    self.choose_die()
                else:
                    if "blue" in racism:
                        for i in range(racism.count("blue")):
                            self.choose_rgb("blue")
                            self.choose_action(create_and_manage_buttons(["armour", "reflect", 1])[0])
                    if "red" in racism:
                        for i in range(racism.count("red")):
                            self.choose_rgb("red")
                            self.choose_action(create_and_manage_buttons(["crush", "charge", 'focus', 'swing', 1])[0])
                    if "black" in racism:
                        for i in range(racism.count("black")):
                            self.choose_rgb("black")
                            self.choose_action(create_and_manage_buttons(
                                ["regenerate", "piercer", 'balanced strike', 'conserve energy', 1])[0])
                    self.extra_dice = False
            elif self.conserve_energy_check:
                racism = create_and_manage_buttons(["blue", "red", "black", 2])
                if len(racism) != 2:
                    condition = True
                else:
                    condition = racism[0] not in ["blue", "red", "black"] or racism[1] not in ["blue", "red", "black"]
                if condition:
                    display_text(("Incorrect spelling or number of die.", 2))
                    self.choose_die()
                else:
                    if "blue" in racism:
                        for i in range(racism.count("blue")):
                            self.choose_rgb("blue")
                            self.choose_action(create_and_manage_buttons(["armour", "reflect", 1])[0])
                    if "red" in racism:
                        for i in range(racism.count("red")):
                            self.choose_rgb("red")
                            self.choose_action(create_and_manage_buttons(["crush", "charge", 'focus', 'swing', 1])[0])
                    if "black" in racism:
                        for i in range(racism.count("black")):
                            self.choose_rgb("black")
                            self.choose_action(create_and_manage_buttons(
                                ["regenerate", "piercer", 'balanced strike', 'conserve energy', 1])[0])
                    if self.conserve_energy_trigger == 0:
                        self.conserve_energy_check = False
            else:
                racism = create_and_manage_buttons(["blue", "red", "black", 1])
                condition = racism[0] not in ["blue", "red", "black"] or len(racism) != 1
                if condition:
                    display_text(("Incorrect spelling or number of die.", 2))
                    self.choose_die()
                else:
                    if "blue" in racism:
                        for i in range(racism.count("blue")):
                            self.choose_rgb("blue")
                            self.choose_action(create_and_manage_buttons(["armour", "reflect", 1])[0])
                    if "red" in racism:
                        for i in range(racism.count("red")):
                            self.choose_rgb("red")
                            self.choose_action(create_and_manage_buttons(["crush", "charge", 'focus', 'swing', 1])[0])
                    if "black" in racism:
                        for i in range(racism.count("black")):
                            self.choose_rgb("black")
                            self.choose_action(create_and_manage_buttons(
                                ["regenerate", "piercer", 'balanced strike', 'conserve energy', 1])[0])
        else:
            if self.extra_dice:
                if self.x - self.shielding > 15:
                    if self.regenerate_cooldown == 0 and self.health < 60 and self.x < 10:
                        print("regenerate")
                        self.rgb.append('black')
                        self.regenerate()
                    else:
                        if self.reflect_cooldown == 0:
                            print("reflect")
                            self.rgb.append('blue')
                            self.reflect()
                        else:
                            if self.conserve_energy_cooldown == 0:
                                print("conserve energy")
                                self.rgb.append('black')
                                self.conserve_energy()
                            else:
                                print("armour")
                                self.rgb.append('blue')
                                self.armour()
                elif self.x > 0:
                    if self.reflect_cooldown == 0 and self.x > 0:
                        print("reflect")
                        self.rgb.append('blue')
                        self.reflect()
                    else:
                        if self.regenerate_cooldown == 0 and self.health < 60 and self.x < 10:
                            print("regenerate")
                            self.rgb.append('black')
                            self.regenerate()
                        else:
                            if self.conserve_energy_cooldown == 0:
                                print("conserve energy")
                                self.rgb.append('black')
                                self.conserve_energy()
                            else:
                                if self.focus_cooldown == 0 and self.focus_cumulative < 25:
                                    print("focus")
                                    self.rgb.append('red')
                                    self.focus()
                                else:
                                    if self.swing_cooldown == 0:
                                        print("swing")
                                        self.rgb.append('red')
                                        self.swing()
                                    else:
                                        print("crush")
                                        self.rgb.append('red')
                                        self.crush()
                else:
                    if self.shielding > 10:
                        print("charge")
                        self.rgb.append('blue')
                        self.charge()
                    else:
                        if self.regenerate_cooldown == 0 and self.health < 60 and self.x < 10:
                            print("regenerate")
                            self.rgb.append('black')
                            self.regenerate()
                        else:
                            if self.focus_cooldown == 0 and self.focus_cumulative < 25:
                                print("focus")
                                self.rgb.append('red')
                                self.focus()
                            else:
                                if self.swing_cooldown == 0:
                                    print("swing")
                                    self.rgb.append('red')
                                    self.swing()
                                else:
                                    print("crush")
                                    self.rgb.append('red')
                                    self.crush()
                self.extra_dice = False
            elif self.conserve_energy_check:
                self.x = self.enemy_attack + self.enemy_drain_attack
                for i in self.enemy_burn:
                    self.x += i[0]
                for i in self.enemy_bleed:
                    self.x += i[0]
                for i in self.enemy_poison:
                    self.x += i[0]
                if self.x >= 20:
                    if self.reflect_cooldown == 0:
                        print("reflect")
                        self.rgb.append('blue')
                        self.reflect()
                    else:
                        if self.regenerate_cooldown == 0 and self.health < 60 and self.x < 10:
                            print("regenerate")
                            self.rgb.append('black')
                            self.regenerate()
                        else:
                            if self.conserve_energy_cooldown == 0:
                                print("conserve energy")
                                self.rgb.append('black')
                                self.conserve_energy()
                            else:
                                print("armour")
                                self.rgb.append('blue')
                                self.armour()
                    if self.x - self.shielding > 15:
                        if self.regenerate_cooldown == 0 and self.health < 60 and self.x < 10:
                            print("regenerate")
                            self.rgb.append('black')
                            self.regenerate()
                        else:
                            if self.conserve_energy_cooldown == 0:
                                print("conserve energy")
                                self.rgb.append('black')
                                self.conserve_energy()
                            else:
                                if self.reflect_cooldown == 0:
                                    print("reflect")
                                    self.rgb.append('blue')
                                    self.reflect()
                                else:
                                    print("armour")
                                    self.rgb.append('blue')
                                    self.armour()
                    else:
                        if self.conserve_energy_cooldown == 0:
                            print("conserve energy")
                            self.rgb.append('black')
                            self.conserve_energy()
                        else:
                            if self.regenerate_cooldown == 0 and self.health < 60 and self.x < 10:
                                print("regenerate")
                                self.rgb.append('black')
                                self.regenerate()
                            else:
                                if self.focus_cooldown == 0 and self.focus_cumulative < 25:
                                    print("focus")
                                    self.rgb.append('red')
                                    self.focus()
                                else:
                                    if self.swing_cooldown == 0:
                                        print("swing")
                                        self.rgb.append('red')
                                        self.swing()
                                    else:
                                        print("crush")
                                        self.rgb.append('red')
                                        self.crush()
                elif self.x > 0:
                    if self.reflect_cooldown == 0:
                        print("reflect")
                        self.rgb.append('blue')
                        self.reflect()
                    else:
                        if self.regenerate_cooldown == 0 and self.health < 60 and self.x < 10:
                            print("regenerate")
                            self.rgb.append('black')
                            self.regenerate()
                        else:
                            if self.conserve_energy_cooldown == 0:
                                print("conserve energy")
                                self.rgb.append('black')
                                self.conserve_energy()
                            else:
                                print("armour")
                                self.rgb.append('blue')
                                self.armour()
                elif self.x == 0:
                    if self.conserve_energy_cooldown == 0:
                        print("conserve energy")
                        self.rgb.append('black')
                        self.conserve_energy()
                    elif self.health > 30:
                        if self.piercer_cooldown == 0:
                            print("piercer")
                            self.rgb.append('black')
                            self.piercer()
                        else:
                            if self.balanced_strike_cooldown == 0:
                                print("balanced strike")
                                self.rgb.append('black')
                                self.balanced_strike()
                            else:
                                if self.regenerate_cooldown == 0 and self.health < 60 and self.x < 10:
                                    print("regenerate")
                                    self.rgb.append('black')
                                    self.regenerate()
                                else:
                                    if self.focus_cooldown == 0 and self.focus_cumulative < 25:
                                        print("focus")
                                        self.rgb.append('red')
                                        self.focus()
                                    else:
                                        if self.swing_cooldown == 0:
                                            print("swing")
                                            self.rgb.append('red')
                                            self.swing()
                                        else:
                                            print("crush")
                                            self.rgb.append('red')
                                            self.crush()
                    else:
                        if self.regenerate_cooldown == 0 and self.health < 60 and self.x < 10:
                            print("regenerate")
                            self.rgb.append('black')
                            self.regenerate()
                        else:
                            if self.balanced_strike_cooldown == 0:
                                print("balanced strike")
                                self.rgb.append('black')
                                self.balanced_strike()
                            else:
                                if self.focus_cooldown == 0 and self.focus_cumulative < 25:
                                    print("focus")
                                    self.rgb.append('red')
                                    self.focus()
                                else:
                                    if self.swing_cooldown == 0:
                                        print("swing")
                                        self.rgb.append('red')
                                        self.swing()
                                    else:
                                        print("crush")
                                        self.rgb.append('red')
                                        self.crush()
                    if self.x - self.shielding < 10:
                        if self.conserve_energy_cooldown == 0:
                            print("conserve energy")
                            self.rgb.append('black')
                            self.conserve_energy()
                        else:
                            if self.piercer_cooldown == 0:
                                print("piercer")
                                self.rgb.append('black')
                                self.piercer()
                            else:
                                if self.balanced_strike_cooldown == 0:
                                    print("balanced strike")
                                    self.rgb.append('black')
                                    self.balanced_strike()
                                else:
                                    if self.regenerate_cooldown == 0 and self.health < 60 and self.x < 10:
                                        print("regenerate")
                                        self.rgb.append('black')
                                        self.regenerate()
                                    else:
                                        if self.focus_cooldown == 0 and self.focus_cumulative < 25:
                                            print("focus")
                                            self.rgb.append('red')
                                            self.focus()
                                        else:
                                            if self.swing_cooldown == 0:
                                                print("swing")
                                                self.rgb.append('red')
                                                self.swing()
                                            else:
                                                print("crush")
                                                self.rgb.append('red')
                                                self.crush()
                    else:
                        if self.reflect_cooldown == 0:
                            print("reflect")
                            self.rgb.append('blue')
                            self.reflect()
                        else:
                            if self.regenerate_cooldown == 0 and self.health < 60 and self.x < 10:
                                print("regenerate")
                                self.rgb.append('black')
                                self.regenerate()
                            else:
                                if self.conserve_energy_cooldown == 0:
                                    print("conserve energy")
                                    self.rgb.append('black')
                                    self.conserve_energy()
                                else:
                                    print("armour")
                                    self.rgb.append('blue')
                                    self.armour()
                if self.conserve_energy_trigger == 0:
                    self.conserve_energy_check = False
            else:
                self.x = self.enemy_attack + self.enemy_drain_attack
                for i in self.enemy_burn:
                    self.x += i[0]
                for i in self.enemy_bleed:
                    self.x += i[0]
                for i in self.enemy_poison:
                    self.x += i[0]
                if self.x > 0:
                    if self.reflect_cooldown == 0:
                        print("reflect")
                        self.rgb.append('blue')
                        self.reflect()
                    else:
                        if self.regenerate_cooldown == 0 and self.health < 60 and self.x < 10:
                            print("regenerate")
                            self.rgb.append('black')
                            self.regenerate()
                        else:
                            if self.conserve_energy_cooldown == 0:
                                print("conserve energy")
                                self.rgb.append('black')
                                self.conserve_energy()
                            else:
                                print("armour")
                                self.rgb.append('blue')
                                self.armour()
                else:
                    if self.conserve_energy_cooldown == 0:
                        print("conserve energy")
                        self.rgb.append('black')
                        self.conserve_energy()
                    else:
                        if self.regenerate_cooldown == 0 and self.health < 60 and self.x < 10:
                            print("regenerate")
                            self.rgb.append('black')
                            self.regenerate()
                        else:
                            if self.focus_cooldown == 0 and self.focus_cumulative < 25:
                                print("focus")
                                self.rgb.append('red')
                                self.focus()
                            else:
                                if self.swing_cooldown == 0:
                                    print("swing")
                                    self.rgb.append('red')
                                    self.swing()
                                else:
                                    print("crush")
                                    self.rgb.append('red')
                                    self.crush()

    def armour(self):
        # Block+15
        from graphics import display_text
        from graphics import display_player_dice
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        self.shielding += number + 15
        time.sleep(0.5)
        display_text((f"Your shield is now {self.shielding}.", 2))
        self.rgb.pop(self.rgb.index('blue'))

    def reflect(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Block, if all dmg blocked, Attack = dmg received, else throw a die
        self.reflect_cooldown = 1
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        self.shielding += number
        time.sleep(0.5)
        display_text((f"Your shield is now {self.shielding}.", 2))
        self.rgb.pop(self.rgb.index('blue'))
        if self.enemy_attack <= self.shielding:
            time.sleep(0.5)
            display_text(("All damage is negated! Attacking...", 2))
            self.attack += self.enemy_attack + self.permanent_attack_increase
            time.sleep(0.5)
            display_text((f"Your attack is now {self.attack}.", 2))
        else:
            time.sleep(0.5)
            display_text(("All damage has not been negated! Rolling another dice...", 2))
            self.extra_dice = True
            self.choose_die()

    def crush(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Attack, if 5-, throw a die
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        self.rgb.pop(self.rgb.index('red'))
        if number >= 15:
            self.attack += int((int((number * 1.5) // 1) * self.percentage) // 1) + self.permanent_attack_increase
            time.sleep(0.5)
            display_text((f"Your attack is now {self.attack}.", 2))
        elif number <= 5:
            self.attack += int((number * self.percentage) // 1) + self.permanent_attack_increase
            time.sleep(0.5)
            display_text((f"Your attack is now {self.attack}.", 2))
            time.sleep(0.5)
            display_text(("You rolled 5 or less! Rolling another dice...", 2))
            self.extra_dice = True
            self.choose_die()
        else:
            self.attack += int((number * self.percentage) // 1) + self.permanent_attack_increase
            time.sleep(0.5)
            display_text((f"Your attack is now {self.attack}.", 2))
        if self.percentage != 1:
            self.percentage = 1

    def charge(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Attack = Block x value, remove block
        self.charge_cooldown = 3
        number = self.roll_d10()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        if self.shielding * number + self.permanent_attack_increase > 50:
            self.attack += 50
            time.sleep(0.5)
            display_text((f"Your attack is now {self.attack}.", 2))
        else:
            self.attack += self.shielding * number + self.permanent_attack_increase
            time.sleep(0.5)
            display_text((f"Your attack is now {self.attack}.", 2))
        self.shielding = 0
        time.sleep(0.5)
        display_text((f"Your shield is now {self.shielding}.", 2))
        time.sleep(0.5)
        display_text((f"Your attack is now {self.attack}.", 2))
        self.rgb.pop(self.rgb.index('red'))

    def focus(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Permanent damage increase
        self.focus_cooldown = 2
        number = self.roll_d20()
        display_player_dice(self.rgb[0], number)
        self.focus_cumulative += number
        if self.focus_cumulative > 25:
            self.focus_cumulative = 25
            time.sleep(1)
            display_text((f"You got {number}!", 2))
            time.sleep(0.5)
            display_text((f"You have reached the maximum damage increase of 25.", 2))
        else:
            time.sleep(1)
            display_text((f"You got {number}!", 2))
            self.permanent_attack_increase += number
            time.sleep(0.5)
            display_text((f"Your damage is now permanently increased by {self.permanent_attack_increase}/25.", 2))
        self.rgb.pop(self.rgb.index('red'))

    def swing(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Attack, if shielded, Attack again and roll a die
        self.swing_cooldown = 1
        number = self.roll_d10()
        display_player_dice(self.rgb[0], number)
        self.rgb.pop(self.rgb.index('red'))
        time.sleep(1)
        display_text((f"You got {number}!", 2))
        self.attack += number + self.permanent_attack_increase
        time.sleep(0.5)
        display_text((f"Your attack is now {self.attack}.", 2))
        if self.shielding > 0:
            time.sleep(0.5)
            display_text(("You are shielded! Attacking again...", 2))
            self.attack += number + self.permanent_attack_increase
            time.sleep(0.5)
            display_text((f"Your attack is now {self.attack}.", 2))
            time.sleep(0.5)
            display_text(("Rolling another dice...", 2))
            self.extra_dice = True
            self.choose_die()

    def regen_aux(self):
        from graphics import display_text
        # Called by regenerate function to increase health once every round for three rounds
        for i in self.regen:
            self.regeneration += i[0]
        if len(self.regen) > 0:
            time.sleep(0.5)
            display_text((f"Your regeneration is now {self.regeneration}.", 2))
            self.healing += self.regeneration
            self.regeneration = 0

    def regenerate(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Heal + 10 for 3 turns
        self.regenerate_cooldown = 2
        number = self.roll_d10()
        self.regen.append((number + 10, 3))
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        self.rgb.pop(self.rgb.index('black'))

    def piercer(self):
        from graphics import display_text
        from graphics import display_player_dice
        # If valve = 20, crit Attack x2, 15- = roll again
        self.piercer_cooldown = 2
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        if number <= 15:
            self.piercer()
        elif number == 20:
            time.sleep(0.5)
            display_text((f"Direct hit!", 2))
            self.attack += 60 + self.permanent_attack_increase
            time.sleep(0.5)
            display_text((f"Your attack is now {self.attack}.", 2))
            self.rgb.pop(self.rgb.index('black'))
        else:
            display_text(("You missed!", 2))
            time.sleep(0.5)
            display_text((f"Your attack is now {self.attack}.", 2))
            self.rgb.pop(self.rgb.index('black'))

    def balanced_strike(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Roll x3, Attack = average value+10
        self.balanced_strike_cooldown = 2
        avg = 0
        for i in range(1, 4):
            display_text((f"Roll number {i}...", 2))
            number = self.roll_d20()
            avg += number
            time.sleep(1)
            display_player_dice(self.rgb[0], number)
            display_text((f"You got {number}!", 2))
        avg //= 3
        time.sleep(0.5)
        display_text((f"Average roll value: {avg}", 2))
        self.attack += avg + 10 + self.permanent_attack_increase
        time.sleep(0.5)
        display_text((f"Your attack is now {self.attack}.", 2))
        self.rgb.pop(self.rgb.index('black'))

    def conserve_energy(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Heal, roll an extra dice next turn
        self.conserve_energy_cooldown = 1
        self.conserve_energy_trigger = 1
        self.conserve_energy_check = True
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        self.healing += number
        time.sleep(0.5)
        display_text((f"Your healing is now {self.healing}.", 2))
        self.rgb.pop(self.rgb.index('black'))

    def choose_action(self, action):
        from graphics import display_text
        from graphics import create_and_manage_buttons
        self.action = action.lower()
        if self.action == 'armour':
            self.armour()
        elif action == 'reflect':
            if self.reflect_cooldown == 0:
                self.reflect()
            else:
                display_text(('Action is on cooldown!', 2))
                self.choose_action(create_and_manage_buttons(["armour", "reflect", 1])[0])
        elif self.action == 'crush':
            if self.crush_cooldown == 0:
                self.crush()
            else:
                display_text(('This action cannot be played again this turn!', 2))
                self.choose_action(create_and_manage_buttons(["crush", "charge", 'focus', 'swing', 1])[0])
        elif self.action == 'charge':
            if self.charge_cooldown == 0:
                self.charge()
            else:
                display_text(('Action is on cooldown!', 2))
                self.choose_action(create_and_manage_buttons(["crush", "charge", 'focus', 'swing', 1])[0])
        elif self.action == 'focus':
            if self.focus_cooldown == 0:
                self.focus()
            else:
                display_text(('Action is on cooldown!', 2))
                self.choose_action(create_and_manage_buttons(["crush", "charge", 'focus', 'swing', 1])[0])
        elif self.action == 'swing':
            if self.swing_cooldown == 0:
                self.swing()
            else:
                display_text(('This action cannot be played again this turn!', 2))
                self.choose_action(create_and_manage_buttons(["crush", "charge", 'focus', 'swing', 1])[0])
        elif self.action == 'regenerate':
            if self.regenerate_cooldown == 0:
                self.regenerate()
            else:
                display_text(('Action is on cooldown!', 2))
                self.choose_action(
                    create_and_manage_buttons(["regenerate", "piercer", 'balanced strike', 'conserve energy', 1])[0])
        elif self.action == 'piercer':
            if self.piercer_cooldown == 0:
                self.piercer()
            else:
                display_text(('Action is on cooldown!', 2))
                self.choose_action(
                    create_and_manage_buttons(["regenerate", "piercer", 'balanced strike', 'conserve energy', 1])[0])
        elif self.action == 'balanced strike':
            if self.balanced_strike_cooldown == 0:
                self.balanced_strike()
            else:
                display_text(('Action is on cooldown!', 2))
                self.choose_action(
                    create_and_manage_buttons(["regenerate", "piercer", 'balanced strike', 'conserve energy', 1])[0])
        elif self.action == 'conserve energy':
            if self.conserve_energy_cooldown == 0:
                self.conserve_energy()
            else:
                display_text(('This action cannot be played again this turn!', 2))
                self.choose_action(
                    create_and_manage_buttons(["regenerate", "piercer", 'balanced strike', 'conserve energy', 1])[0])
        else:
            display_text(("You can't do that.", 2))
            self.choose_die()
