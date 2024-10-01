import random
import time


class Rogue:
    def __init__(self, name):
        self.character = "rogue"
        self.health = 50
        self.enemy_health = 0
        self.max_health = 50
        self.attack = 0
        self.shielding = 0
        self.healing = 0
        self.drain_attack = 0
        # separate attack for drain function
        self.enemy_attack = 0
        # enemy attack
        self.enemy_drain_attack = 0
        # enemy drain attack
        self.enemy_burn = []
        self.enemy_bleed = []
        self.enemy_poison = []
        self.thorns_trigger = False
        self.preservation_trigger = False
        self.dodge_trigger = False
        self.permanent_attack_increase = 0
        # Permanent Attack Increase(buff)1
        self.permanent_defence_increase = 0
        # Permanent defence Increase(buff)2
        self.permanent_healing_increase = 0
        # Permanent Healing Increase(buff)3
        self.temporary_attack_increase = 0
        # Temporary Attack Increase(buff)4
        self.temporary_defence_increase = 0
        # Temporary defence Increase(buff)5
        self.temporary_healing_increase = 0
        # Temporary Healing Increase(buff)6
        self.temporary_attack_decrease = 0
        # Temporary Attack Decrease(debuff)1
        self.temporary_defence_decrease = 0
        # Temporary defence Decrease(debuff)2
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
        self.x = 0

    def reset_cooldowns(self):
        self.blood_pact_looplock = False
        self.tourniquet_looplock = False

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

    def choose_die(self):
        from graphics import display_text
        if self.name != 'AI':
            from graphics import create_and_manage_buttons
            from graphics import display_text
            racism = create_and_manage_buttons(["blue", "red", "green", 2])
            if "blue" in racism and not self.blood_pact_suicide:
                self.choose_rgb("blue")
                self.choose_action(create_and_manage_buttons(["shield", "parry", 1])[0])
            if "red" in racism and not self.blood_pact_suicide:
                self.choose_rgb("red")
                self.choose_action(create_and_manage_buttons(["cleave", "riposte", "blood pact", 1])[0])
            if "green" in racism and not self.blood_pact_suicide:
                self.choose_rgb("green")
                self.choose_action(create_and_manage_buttons(["tourniquet", "drain", 1])[0])
        else:
            self.x = self.enemy_attack + self.enemy_drain_attack
            for i in self.enemy_burn:
                self.x += i[0]
            for i in self.enemy_bleed:
                self.x += i[0]
            for i in self.enemy_poison:
                self.x += i[0]
            if self.x >= 25 or self.health < 20:
                if not self.blood_pact_suicide:
                    display_text("shield")
                    self.shield()
                    if self.shielding > self.x:
                        display_text("cleave")
                        self.cleave()
                    else:
                        if self.x - self.shielding > 10:
                            if not self.tourniquet_looplock:
                                display_text("tourniquet")
                                self.tourniquet()
                            else:
                                display_text("drain")
                                self.drain()
                        else:
                            display_text("drain")
                            self.drain()
                else:
                    pass
            elif self.x >= 10 or (self.health < 40 and self.enemy_attack + self.enemy_drain_attack > 0):
                if not self.blood_pact_suicide:
                    display_text("parry")
                    self.parry_alt()
                    if self.shielding > self.x:
                        if self.health > 10:
                            display_text("blood pact")
                            self.blood_pact_alt()
                        else:
                            if self.health < 40:
                                display_text("drain")
                                self.drain()
                            else:
                                display_text("cleave")
                                self.cleave()
                    else:
                        display_text("riposte")
                        self.riposte_alt()
                else:
                    pass
            else:
                if not self.blood_pact_suicide:
                    if not self.blood_pact_looplock:
                        if self.health > 30:
                            display_text("blood pact")
                            self.blood_pact_alt()
                        else:
                            display_text("cleave")
                            self.cleave()
                        if self.health < 15:
                            if not self.tourniquet_looplock:
                                display_text("tourniquet")
                                self.tourniquet()
                            else:
                                display_text("drain")
                                self.drain()
                        else:
                            display_text("drain")
                            self.drain()
                    else:
                        display_text("cleave")
                        self.cleave()
                        if self.health < 15:
                            if not self.tourniquet_looplock:
                                display_text("tourniquet")
                                self.tourniquet()
                            else:
                                display_text("drain")
                                self.drain()
                else:
                    pass

    def parry_alt(self):
        from graphics import display_text
        from graphics import display_player_dice
        number = self.roll_d10()
        time.sleep(1)
        display_player_dice(self.rgb, number)
        display_text((f"You got {number}!", 1))
        self.shielding += number
        time.sleep(0.5)
        display_text((f"Your shield is now {self.shielding}.", 1))
        if number < 6:
            time.sleep(0.5)
            display_text(("You rolled 5 or less! Rolling a red dice...", 1))
            if self.x >= 10:
                self.riposte_alt()
            elif self.health > 20:
                if not self.blood_pact_looplock:
                    display_text("blood pact")
                    self.blood_pact_alt()
                else:
                    display_text("cleave")
                    self.cleave()
            else:
                display_text("cleave")
                self.cleave()

    def riposte_alt(self):
        from graphics import display_text
        from graphics import display_player_dice
        number = self.roll_d10()
        time.sleep(1)
        display_player_dice(self.rgb, number)
        display_text((f"You got {number}!", 1))
        self.shielding += number
        time.sleep(0.5)
        display_text((f"Your shield is now {self.shielding}.", 1))
        if self.enemy_attack + self.enemy_drain_attack == 0:
            pass
        elif self.shielding >= self.enemy_attack + self.enemy_drain_attack:
            time.sleep(0.5)
            display_text(("Enemy attack has been negated! Attacking...", 1))
            self.attack += number
            display_text((f"Your attack is now {self.attack}.", 1))
        elif self.shielding < self.enemy_attack + self.enemy_drain_attack:
            time.sleep(0.5)
            display_text(("Enemy attack has not been negated! Rolling a green dice...", 1))
            if self.x - self.shielding > 10:
                if not self.tourniquet_looplock:
                    display_text("tourniquet")
                    self.tourniquet()
                else:
                    display_text("drain")
                    self.drain()
            else:
                display_text("drain")
                self.drain()

    def blood_pact_alt(self):
        from graphics import display_text
        from graphics import display_player_dice
        if not self.blood_pact_looplock:
            self.blood_pact_looplock = True
            number = self.roll_d10()
            time.sleep(1)
            display_player_dice(self.rgb, number)
            display_text((f"You got {number}!", 1))
            self.health -= number
            if self.health <= 0:
                self.blood_pact_suicide = True
                pass
            time.sleep(0.5)
            display_text((f"Your health is now {self.health}.", 1))
            time.sleep(0.5)
            display_text(("Next attack is doubled!", 1))
            self.percentage *= 2
            time.sleep(0.5)
            display_text(("Rolling a red dice...", 1))
            if self.x - self.shielding > 10:
                display_text("riposte")
                self.riposte_alt()
            else:
                display_text("cleave")
                self.cleave()
        else:
            if self.x - self.shielding > 10:
                display_text("riposte")
                self.riposte_alt()
            else:
                display_text("cleave")
                self.cleave()

    def shield(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Me when the enemy rolls a 20
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb, number)
        display_text((f"You got {number}!", 2))
        if number >= 15:
            self.shielding += int((number * 1.5) // 1)
        else:
            self.shielding += number
        time.sleep(0.5)
        display_text((f"Your shield is now {self.shielding}.", 2))

    def parry(self):
        from graphics import create_and_manage_buttons
        from graphics import display_text
        from graphics import display_player_dice
        # Block, 5- = throw R
        number = self.roll_d10()
        time.sleep(1)
        display_player_dice(self.rgb, number)
        display_text((f"You got {number}!", 2))
        self.shielding += number
        time.sleep(0.5)
        display_text((f"Your shield is now {self.shielding}.", 2))
        if number < 6:
            time.sleep(0.5)
            display_text(("You rolled 5 or less! Rolling a red dice...", 2))
            self.choose_rgb("red")
            self.choose_action(create_and_manage_buttons(["cleave", "riposte", "blood pact", 1])[0])

    def cleave(self):
        from graphics import display_text
        from graphics import display_player_dice
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb, number)
        display_text((f"You got {number}!", 2))
        if number >= 15:
            self.attack += int((int((number * 1.5) // 1) * self.percentage) // 1)
        else:
            self.attack += int((number * self.percentage) // 1)
        if self.percentage != 1:
            self.percentage = 1
        time.sleep(0.5)
        display_text((f"Your attack is now {self.attack}.", 2))

    def riposte(self):
        from graphics import create_and_manage_buttons
        from graphics import display_text
        from graphics import display_player_dice
        # Block, if all dmg blocked, Attack, else throw G
        number = self.roll_d10()
        time.sleep(1)
        display_player_dice(self.rgb, number)
        display_text((f"You got {number}!", 2))
        self.shielding += number
        time.sleep(0.5)
        display_text((f"Your shield is now {self.shielding}.", 2))
        if self.enemy_attack + self.enemy_drain_attack == 0:
            pass
        elif self.shielding >= self.enemy_attack + self.enemy_drain_attack:
            time.sleep(0.5)
            display_text(("Enemy attack has been negated! Attacking...", 2))
            self.attack += number
            display_text((f"Your attack is now {self.attack}.", 2))
        elif self.shielding < self.enemy_attack + self.enemy_drain_attack:
            time.sleep(0.5)
            display_text(("Enemy attack has not been negated! Rolling a green dice...", 2))
            self.choose_rgb("green")
            self.choose_action(create_and_manage_buttons(["tourniquet", "drain", 1])[0])

    def blood_pact(self):
        from graphics import create_and_manage_buttons
        from graphics import display_text
        from graphics import display_player_dice
        # Self-Attack, Double next Attack, throw R
        if not self.blood_pact_looplock:
            self.blood_pact_looplock = True
            number = self.roll_d10()
            time.sleep(1)
            display_player_dice(self.rgb, number)
            display_text((f"You got {number}!", 2))
            self.health -= number
            if self.health <= 0:
                self.blood_pact_suicide = True
                pass
            time.sleep(0.5)
            display_text((f"Your health is now {self.health}.", 2))
            time.sleep(0.5)
            display_text(("Next attack is doubled!", 2))
            self.percentage *= 2
            time.sleep(0.5)
            display_text(("Rolling a red dice...", 2))
            self.choose_rgb("red")
            self.choose_action(create_and_manage_buttons(["cleave", "riposte", "blood pact", 1])[0])
        else:
            time.sleep(0.5)
            display_text(("You can only use this action once per turn!", 2))
            self.choose_rgb("red")
            self.choose_action(create_and_manage_buttons(["cleave", "riposte", "blood pact", 1])[0])

    def tourniquet(self):
        from graphics import create_and_manage_buttons
        from graphics import display_text
        from graphics import display_player_dice
        # Heal, Half next Attack
        if not self.tourniquet_looplock:
            self.tourniquet_looplock = True
            number = self.roll_d20()
            time.sleep(1)
            display_player_dice(self.rgb, number)
            display_text((f"You got {number}!", 2))
            self.healing += number
            time.sleep(0.5)
            display_text((f"Your healing is now {self.healing}.", 2))
            self.percentage *= 0.5
            time.sleep(0.5)
            display_text(("Next attack is halved!", 2))
        else:
            time.sleep(0.5)
            display_text(("You can only use this action once per turn!", 2))
            self.choose_rgb("green")
            self.choose_action(create_and_manage_buttons(["tourniquet", "drain", 1])[0])

    def drain(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Attack, Heal = dmg dealt
        number = self.roll_d10()
        time.sleep(1)
        display_player_dice(self.rgb, number)
        display_text((f"You got {number}!", 2))
        self.drain_attack += int((number * self.percentage) // 1)
        time.sleep(0.5)
        display_text((f"Your drain is now {self.drain_attack}.", 2))
        if self.percentage != 1:
            self.percentage = 1

    def choose_action(self, action):
        self.action = action.lower()
        if action == 'shield':
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
