import random
import time


class Master:
    def __init__(self, name):
        self.character = "master"
        self.health = 100
        self.enemy_health = 0
        self.max_health = 100
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
        self.pneuma_infusion_dice_value = 0
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
        self.x = 0

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

    def choose_die(self):
        from graphics import create_and_manage_buttons
        if not self.name == 'AI':
            if self.preservation_trigger:
                racism = create_and_manage_buttons(["blue", "red", "green", "black", 2])
                if len(racism) != 2:
                    condition = True
                else:
                    condition = racism[0] not in ["blue", "red", "green", "black"] or racism[1] not in ["blue", "red",
                                                                                                        "green",
                                                                                                        "black"]
            else:
                racism = create_and_manage_buttons(["blue", "red", "green", "black", 2])
                if len(racism) != 3:
                    condition = True
                else:
                    condition = racism[0] not in ["blue", "red", "green", "black"] or racism[1] not in ["blue", "red",
                                                                                                        "green",
                                                                                                        "black"] or \
                                racism[2] not in ["blue", "red", "green", "black"]

            racism = create_and_manage_buttons(["blue", "red", "green", "black", 3])
            if "blue" in racism:
                for i in range(racism.count("blue")):
                    self.choose_rgb("blue")
                    self.choose_action(create_and_manage_buttons(["Terra Infusion", "Caeli Infusion", "Dodge", 1]),
                                       self.rgb)
            if "red" in racism:
                for i in range(racism.count("red")):
                    self.choose_rgb("red")
                    self.choose_action(create_and_manage_buttons(["Ignis Infusion", "Needle", "Thorns", 1]), self.rgb)
            if "green" in racism:
                for i in range(racism.count("green")):
                    self.choose_rgb("green")
                    self.choose_action(
                        create_and_manage_buttons(["Aqua Infusion", "Pneuma Infusion", "Preservation", 2]),
                        self.rgb)
            if "black" in racism:
                for i in range(racism.count("black")):
                    self.choose_rgb("black")
                    self.choose_action(create_and_manage_buttons(["Shockwave (Terra)(Cooldown = 1 round)",
                                                                  "Typhoon (Caeli)(Cooldown = 1 round)",
                                                                  "Laserbeam (Ignis)(Cooldown = 1 round)",
                                                                  "Assimilate (Aqua)(Cooldown = 1 round)",
                                                                  "Ruminate (Pneuma)(Cooldown = 3 rounds)",
                                                                  "Vitalize", 1]), self.rgb)
        else:
            if self.preservation_trigger:  # 2 die
                self.x = self.enemy_attack + self.enemy_drain_attack
                for i in self.enemy_burn:
                    self.x += i[0]
                for i in self.enemy_bleed:
                    self.x += i[0]
                for i in self.enemy_poison:
                    self.x += i[0]
                if self.x > 0:
                    if self.max_health - self.health >= 20 and self.vitalize_cooldown == 0:
                        print("vitalize")
                        self.rgb.append('black')
                        self.vitalize()
                        if self.healing > self.x:
                            if self.max_health - self.health >= 20:
                                if self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                            else:
                                if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                        else:
                            if self.max_health - self.health >= 20:
                                if self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                else:
                                    if self.assimilate_unlock:
                                        if self.shockwave_unlock:
                                            if self.typhoon_unlock:
                                                if self.ruminate_unlock:
                                                    if self.laserbeam_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("ignis infusion")
                                                        self.rgb.append('red')
                                                        self.ignis_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                            else:
                                if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                    else:
                        if self.max_health - self.health - self.x >= 20:
                            if self.assimilate_unlock and self.assimilate_cooldown == 0:
                                print("assimilate")
                                self.rgb.append('black')
                                self.assimilate()
                            elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                print("shockwave")
                                self.rgb.append('black')
                                self.shockwave()
                            elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                print("laserbeam")
                                self.rgb.append('black')
                                self.laserbeam()
                            elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                print("typhoon")
                                self.rgb.append('black')
                                self.typhoon()
                            else:
                                if self.assimilate_unlock:
                                    if self.shockwave_unlock:
                                        if self.typhoon_unlock:
                                            if self.ruminate_unlock:
                                                if self.laserbeam_unlock:
                                                    if self.ruminate_cooldown == 0:
                                                        print("ruminate")
                                                        self.rgb.append('black')
                                                        self.ruminate()
                                                    else:
                                                        print("needle")
                                                        self.rgb.append('red')
                                                        self.needle()
                                                else:
                                                    print("ignis infusion")
                                                    self.rgb.append('red')
                                                    self.ignis_infusion()
                                            else:
                                                print("pneuma infusion")
                                                self.rgb.append('green')
                                                self.pneuma_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("terra infusion")
                                        self.rgb.append('blue')
                                        self.terra_infusion()
                                else:
                                    print("aqua infusion")
                                    self.rgb.append('green')
                                    self.aqua_infusion()
                            if self.healing + self.shielding > self.x:
                                if self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                else:
                                    if self.assimilate_unlock:
                                        if self.shockwave_unlock:
                                            if self.typhoon_unlock:
                                                if self.ruminate_unlock:
                                                    if self.laserbeam_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("ignis infusion")
                                                        self.rgb.append('red')
                                                        self.ignis_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                            else:
                                if self.max_health - self.health >= 20:
                                    if self.assimilate_unlock and self.assimilate_cooldown == 0:
                                        print("assimilate")
                                        self.rgb.append('black')
                                        self.assimilate()
                                    elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                        print("shockwave")
                                        self.rgb.append('black')
                                        self.shockwave()
                                    elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                        print("laserbeam")
                                        self.rgb.append('black')
                                        self.laserbeam()
                                    elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                        print("typhoon")
                                        self.rgb.append('black')
                                        self.typhoon()
                                    else:
                                        if self.assimilate_unlock:
                                            if self.shockwave_unlock:
                                                if self.typhoon_unlock:
                                                    if self.ruminate_unlock:
                                                        if self.laserbeam_unlock:
                                                            if self.ruminate_cooldown == 0:
                                                                print("ruminate")
                                                                self.rgb.append('black')
                                                                self.ruminate()
                                                            else:
                                                                print("needle")
                                                                self.rgb.append('red')
                                                                self.needle()
                                                        else:
                                                            print("ignis infusion")
                                                            self.rgb.append('red')
                                                            self.ignis_infusion()
                                                    else:
                                                        print("pneuma infusion")
                                                        self.rgb.append('green')
                                                        self.pneuma_infusion()
                                                else:
                                                    print("caeli infusion")
                                                    self.rgb.append('blue')
                                                    self.caeli_infusion()
                                            else:
                                                print("terra infusion")
                                                self.rgb.append('blue')
                                                self.terra_infusion()
                                        else:
                                            print("aqua infusion")
                                            self.rgb.append('green')
                                            self.aqua_infusion()
                                else:
                                    if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                        print("laserbeam")
                                        self.rgb.append('black')
                                        self.laserbeam()
                                    elif self.assimilate_unlock and self.assimilate_cooldown == 0:
                                        print("assimilate")
                                        self.rgb.append('black')
                                        self.assimilate()
                                    elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                        print("shockwave")
                                        self.rgb.append('black')
                                        self.shockwave()
                                    elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                        print("typhoon")
                                        self.rgb.append('black')
                                        self.typhoon()
                                    else:
                                        if self.laserbeam_unlock:
                                            if self.typhoon_unlock:
                                                if self.assimilate_unlock:
                                                    if self.ruminate_unlock:
                                                        if self.shockwave_unlock:
                                                            if self.ruminate_cooldown == 0:
                                                                print("ruminate")
                                                                self.rgb.append('black')
                                                                self.ruminate()
                                                            else:
                                                                print("needle")
                                                                self.rgb.append('red')
                                                                self.needle()
                                                        else:
                                                            print("terra infusion")
                                                            self.rgb.append('blue')
                                                            self.terra_infusion()
                                                    else:
                                                        print("pneuma infusion")
                                                        self.rgb.append('green')
                                                        self.pneuma_infusion()
                                                else:
                                                    print("aqua infusion")
                                                    self.rgb.append('green')
                                                    self.aqua_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("ignis infusion")
                                            self.rgb.append('red')
                                            self.ignis_infusion()
                        else:
                            if self.max_health - self.health >= 20:
                                if self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                                if self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                            else:
                                if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                                if self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                elif self.x > 0:
                    if self.health - self.enemy_health >= 40:
                        if not self.thorns_trigger:
                            print("thorns")
                            self.rgb.append('red')
                            self.thorns()
                        elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                            print("laserbeam")
                            self.rgb.append('black')
                            self.laserbeam()
                        elif self.assimilate_unlock and self.assimilate_cooldown == 0:
                            print("assimilate")
                            self.rgb.append('black')
                            self.assimilate()
                        elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                            print("shockwave")
                            self.rgb.append('black')
                            self.shockwave()
                        elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                            print("typhoon")
                            self.rgb.append('black')
                            self.typhoon()
                        else:
                            if self.laserbeam_unlock:
                                if self.typhoon_unlock:
                                    if self.assimilate_unlock:
                                        if self.ruminate_unlock:
                                            if self.shockwave_unlock:
                                                if self.ruminate_cooldown == 0:
                                                    print("ruminate")
                                                    self.rgb.append('black')
                                                    self.ruminate()
                                                else:
                                                    print("needle")
                                                    self.rgb.append('red')
                                                    self.needle()
                                            else:
                                                print("terra infusion")
                                                self.rgb.append('blue')
                                                self.terra_infusion()
                                        else:
                                            print("pneuma infusion")
                                            self.rgb.append('green')
                                            self.pneuma_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                                else:
                                    print("caeli infusion")
                                    self.rgb.append('blue')
                                    self.caeli_infusion()
                            else:
                                print("ignis infusion")
                                self.rgb.append('red')
                                self.ignis_infusion()
                        if self.typhoon_unlock and self.typhoon_cooldown == 0:
                            print("typhoon")
                            self.rgb.append('black')
                            self.typhoon()
                        elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                            print("laserbeam")
                            self.rgb.append('black')
                            self.laserbeam()
                        elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                            print("assimilate")
                            self.rgb.append('black')
                            self.assimilate()
                        elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                            print("shockwave")
                            self.rgb.append('black')
                            self.shockwave()
                        else:
                            if self.laserbeam_unlock:
                                if self.typhoon_unlock:
                                    if self.assimilate_unlock:
                                        if self.ruminate_unlock:
                                            if self.shockwave_unlock:
                                                if self.ruminate_cooldown == 0:
                                                    print("ruminate")
                                                    self.rgb.append('black')
                                                    self.ruminate()
                                                else:
                                                    print("needle")
                                                    self.rgb.append('red')
                                                    self.needle()
                                            else:
                                                print("terra infusion")
                                                self.rgb.append('blue')
                                                self.terra_infusion()
                                        else:
                                            print("pneuma infusion")
                                            self.rgb.append('green')
                                            self.pneuma_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                                else:
                                    print("caeli infusion")
                                    self.rgb.append('blue')
                                    self.caeli_infusion()
                            else:
                                print("ignis infusion")
                                self.rgb.append('red')
                                self.ignis_infusion()
                    else:
                        if self.max_health - self.health >= 20:
                            if self.assimilate_unlock and self.assimilate_cooldown == 0:
                                print("assimilate")
                                self.rgb.append('black')
                                self.assimilate()
                            elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                print("laserbeam")
                                self.rgb.append('black')
                                self.laserbeam()
                            elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                print("shockwave")
                                self.rgb.append('black')
                                self.shockwave()
                            elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                print("typhoon")
                                self.rgb.append('black')
                                self.typhoon()
                            else:
                                if self.laserbeam_unlock:
                                    if self.typhoon_unlock:
                                        if self.assimilate_unlock:
                                            if self.ruminate_unlock:
                                                if self.shockwave_unlock:
                                                    if self.ruminate_cooldown == 0:
                                                        print("ruminate")
                                                        self.rgb.append('black')
                                                        self.ruminate()
                                                    else:
                                                        print("needle")
                                                        self.rgb.append('red')
                                                        self.needle()
                                                else:
                                                    print("terra infusion")
                                                    self.rgb.append('blue')
                                                    self.terra_infusion()
                                            else:
                                                print("pneuma infusion")
                                                self.rgb.append('green')
                                                self.pneuma_infusion()
                                        else:
                                            print("aqua infusion")
                                            self.rgb.append('green')
                                            self.aqua_infusion()
                                    else:
                                        print("caeli infusion")
                                        self.rgb.append('blue')
                                        self.caeli_infusion()
                                else:
                                    print("ignis infusion")
                                    self.rgb.append('red')
                                    self.ignis_infusion()
                            if self.typhoon_unlock and self.typhoon_cooldown == 0:
                                print("typhoon")
                                self.rgb.append('black')
                                self.typhoon()
                            elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                print("assimilate")
                                self.rgb.append('black')
                                self.assimilate()
                            elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                print("laserbeam")
                                self.rgb.append('black')
                                self.laserbeam()
                            elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                print("shockwave")
                                self.rgb.append('black')
                                self.shockwave()
                            else:
                                if self.laserbeam_unlock:
                                    if self.typhoon_unlock:
                                        if self.assimilate_unlock:
                                            if self.ruminate_unlock:
                                                if self.shockwave_unlock:
                                                    if self.ruminate_cooldown == 0:
                                                        print("ruminate")
                                                        self.rgb.append('black')
                                                        self.ruminate()
                                                    else:
                                                        print("needle")
                                                        self.rgb.append('red')
                                                        self.needle()
                                                else:
                                                    print("terra infusion")
                                                    self.rgb.append('blue')
                                                    self.terra_infusion()
                                            else:
                                                print("pneuma infusion")
                                                self.rgb.append('green')
                                                self.pneuma_infusion()
                                        else:
                                            print("aqua infusion")
                                            self.rgb.append('green')
                                            self.aqua_infusion()
                                    else:
                                        print("caeli infusion")
                                        self.rgb.append('blue')
                                        self.caeli_infusion()
                                else:
                                    print("ignis infusion")
                                    self.rgb.append('red')
                                    self.ignis_infusion()
                        else:
                            if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                print("laserbeam")
                                self.rgb.append('black')
                                self.laserbeam()
                            elif self.assimilate_unlock and self.assimilate_cooldown == 0:
                                print("assimilate")
                                self.rgb.append('black')
                                self.assimilate()
                            elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                print("shockwave")
                                self.rgb.append('black')
                                self.shockwave()
                            elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                print("typhoon")
                                self.rgb.append('black')
                                self.typhoon()
                            else:
                                if self.laserbeam_unlock:
                                    if self.typhoon_unlock:
                                        if self.assimilate_unlock:
                                            if self.ruminate_unlock:
                                                if self.shockwave_unlock:
                                                    if self.ruminate_cooldown == 0:
                                                        print("ruminate")
                                                        self.rgb.append('black')
                                                        self.ruminate()
                                                    else:
                                                        print("needle")
                                                        self.rgb.append('red')
                                                        self.needle()
                                                else:
                                                    print("terra infusion")
                                                    self.rgb.append('blue')
                                                    self.terra_infusion()
                                            else:
                                                print("pneuma infusion")
                                                self.rgb.append('green')
                                                self.pneuma_infusion()
                                        else:
                                            print("aqua infusion")
                                            self.rgb.append('green')
                                            self.aqua_infusion()
                                    else:
                                        print("caeli infusion")
                                        self.rgb.append('blue')
                                        self.caeli_infusion()
                                else:
                                    print("ignis infusion")
                                    self.rgb.append('red')
                                    self.ignis_infusion()
                            if self.typhoon_unlock and self.typhoon_cooldown == 0:
                                print("typhoon")
                                self.rgb.append('black')
                                self.typhoon()
                            elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                print("laserbeam")
                                self.rgb.append('black')
                                self.laserbeam()
                            elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                print("assimilate")
                                self.rgb.append('black')
                                self.assimilate()
                            elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                print("shockwave")
                                self.rgb.append('black')
                                self.shockwave()
                            else:
                                if self.laserbeam_unlock:
                                    if self.typhoon_unlock:
                                        if self.assimilate_unlock:
                                            if self.ruminate_unlock:
                                                if self.shockwave_unlock:
                                                    if self.ruminate_cooldown == 0:
                                                        print("ruminate")
                                                        self.rgb.append('black')
                                                        self.ruminate()
                                                    else:
                                                        print("needle")
                                                        self.rgb.append('red')
                                                        self.needle()
                                                else:
                                                    print("terra infusion")
                                                    self.rgb.append('blue')
                                                    self.terra_infusion()
                                            else:
                                                print("pneuma infusion")
                                                self.rgb.append('green')
                                                self.pneuma_infusion()
                                        else:
                                            print("aqua infusion")
                                            self.rgb.append('green')
                                            self.aqua_infusion()
                                    else:
                                        print("caeli infusion")
                                        self.rgb.append('blue')
                                        self.caeli_infusion()
                                else:
                                    print("ignis infusion")
                                    self.rgb.append('red')
                                    self.ignis_infusion()
                else:
                    if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                        print("laserbeam")
                        self.rgb.append('black')
                        self.laserbeam()
                    elif self.assimilate_unlock and self.assimilate_cooldown == 0:
                        print("assimilate")
                        self.rgb.append('black')
                        self.assimilate()
                    elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                        print("shockwave")
                        self.rgb.append('black')
                        self.shockwave()
                    elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                        print("typhoon")
                        self.rgb.append('black')
                        self.typhoon()
                    else:
                        if self.laserbeam_unlock:
                            if self.typhoon_unlock:
                                if self.assimilate_unlock:
                                    if self.ruminate_unlock:
                                        if self.shockwave_unlock:
                                            if self.ruminate_cooldown == 0:
                                                print("ruminate")
                                                self.rgb.append('black')
                                                self.ruminate()
                                            else:
                                                print("needle")
                                                self.rgb.append('red')
                                                self.needle()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("pneuma infusion")
                                        self.rgb.append('green')
                                        self.pneuma_infusion()
                                else:
                                    print("aqua infusion")
                                    self.rgb.append('green')
                                    self.aqua_infusion()
                            else:
                                print("caeli infusion")
                                self.rgb.append('blue')
                                self.caeli_infusion()
                        else:
                            print("ignis infusion")
                            self.rgb.append('red')
                            self.ignis_infusion()
                    if self.typhoon_unlock and self.typhoon_cooldown == 0:
                        print("typhoon")
                        self.rgb.append('black')
                        self.typhoon()
                    elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                        print("laserbeam")
                        self.rgb.append('black')
                        self.laserbeam()
                    elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                        print("assimilate")
                        self.rgb.append('black')
                        self.assimilate()
                    elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                        print("shockwave")
                        self.rgb.append('black')
                        self.shockwave()
                    else:
                        if self.laserbeam_unlock:
                            if self.typhoon_unlock:
                                if self.assimilate_unlock:
                                    if self.ruminate_unlock:
                                        if self.shockwave_unlock:
                                            if self.ruminate_cooldown == 0:
                                                print("ruminate")
                                                self.rgb.append('black')
                                                self.ruminate()
                                            else:
                                                print("needle")
                                                self.rgb.append('red')
                                                self.needle()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("pneuma infusion")
                                        self.rgb.append('green')
                                        self.pneuma_infusion()
                                else:
                                    print("aqua infusion")
                                    self.rgb.append('green')
                                    self.aqua_infusion()
                            else:
                                print("caeli infusion")
                                self.rgb.append('blue')
                                self.caeli_infusion()
                        else:
                            print("ignis infusion")
                            self.rgb.append('red')
                            self.ignis_infusion()
            else:  # 3 die
                self.x = self.enemy_attack + self.enemy_drain_attack
                for i in self.enemy_burn:
                    self.x += i[0]
                for i in self.enemy_bleed:
                    self.x += i[0]
                for i in self.enemy_poison:
                    self.x += i[0]
                if self.x > 0:
                    if self.x - self.max_health > 0 and self.health < 50:
                        print("preservation")
                        self.rgb.append('green')
                        self.preservation()
                    elif self.x - self.max_health > 0 and self.dodge_cooldown == 0:
                        print("dodge")
                        self.rgb.append('blue')
                        self.dodge()
                    elif self.max_health - self.health >= 20 and self.vitalize_cooldown == 0:
                        print("vitalize")
                        self.rgb.append('black')
                        self.vitalize()
                        if self.healing > self.x:
                            if self.max_health - self.health >= 20:
                                if self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                else:
                                    if self.assimilate_unlock:
                                        if self.shockwave_unlock:
                                            if self.typhoon_unlock:
                                                if self.ruminate_unlock:
                                                    if self.laserbeam_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("ignis infusion")
                                                        self.rgb.append('red')
                                                        self.ignis_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                                if self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                else:
                                    if self.assimilate_unlock:
                                        if self.shockwave_unlock:
                                            if self.typhoon_unlock:
                                                if self.ruminate_unlock:
                                                    if self.laserbeam_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("ignis infusion")
                                                        self.rgb.append('red')
                                                        self.ignis_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                                if self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                else:
                                    if self.assimilate_unlock:
                                        if self.shockwave_unlock:
                                            if self.typhoon_unlock:
                                                if self.ruminate_unlock:
                                                    if self.laserbeam_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("ignis infusion")
                                                        self.rgb.append('red')
                                                        self.ignis_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                            else:
                                if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                else:
                                    if self.assimilate_unlock:
                                        if self.shockwave_unlock:
                                            if self.typhoon_unlock:
                                                if self.ruminate_unlock:
                                                    if self.laserbeam_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("ignis infusion")
                                                        self.rgb.append('red')
                                                        self.ignis_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                                if self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                else:
                                    if self.assimilate_unlock:
                                        if self.shockwave_unlock:
                                            if self.typhoon_unlock:
                                                if self.ruminate_unlock:
                                                    if self.laserbeam_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("ignis infusion")
                                                        self.rgb.append('red')
                                                        self.ignis_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                                if self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                else:
                                    if self.assimilate_unlock:
                                        if self.shockwave_unlock:
                                            if self.typhoon_unlock:
                                                if self.ruminate_unlock:
                                                    if self.laserbeam_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("ignis infusion")
                                                        self.rgb.append('red')
                                                        self.ignis_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                        else:
                            if self.max_health - self.health >= 20:
                                if self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                else:
                                    if self.assimilate_unlock:
                                        if self.shockwave_unlock:
                                            if self.typhoon_unlock:
                                                if self.ruminate_unlock:
                                                    if self.laserbeam_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("ignis infusion")
                                                        self.rgb.append('red')
                                                        self.ignis_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                                if self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                else:
                                    if self.assimilate_unlock:
                                        if self.shockwave_unlock:
                                            if self.typhoon_unlock:
                                                if self.ruminate_unlock:
                                                    if self.laserbeam_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("ignis infusion")
                                                        self.rgb.append('red')
                                                        self.ignis_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                                if self.healing + self.shielding > self.x:
                                    if self.typhoon_unlock and self.typhoon_cooldown == 0:
                                        print("typhoon")
                                        self.rgb.append('black')
                                        self.typhoon()
                                    elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                        print("assimilate")
                                        self.rgb.append('black')
                                        self.assimilate()
                                    elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                        print("shockwave")
                                        self.rgb.append('black')
                                        self.shockwave()
                                    elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                        print("laserbeam")
                                        self.rgb.append('black')
                                        self.laserbeam()
                                    else:
                                        if self.assimilate_unlock:
                                            if self.shockwave_unlock:
                                                if self.typhoon_unlock:
                                                    if self.ruminate_unlock:
                                                        if self.laserbeam_unlock:
                                                            if self.ruminate_cooldown == 0:
                                                                print("ruminate")
                                                                self.rgb.append('black')
                                                                self.ruminate()
                                                            else:
                                                                print("needle")
                                                                self.rgb.append('red')
                                                                self.needle()
                                                        else:
                                                            print("ignis infusion")
                                                            self.rgb.append('red')
                                                            self.ignis_infusion()
                                                    else:
                                                        print("pneuma infusion")
                                                        self.rgb.append('green')
                                                        self.pneuma_infusion()
                                                else:
                                                    print("caeli infusion")
                                                    self.rgb.append('blue')
                                                    self.caeli_infusion()
                                            else:
                                                print("terra infusion")
                                                self.rgb.append('blue')
                                                self.terra_infusion()
                                        else:
                                            print("aqua infusion")
                                            self.rgb.append('green')
                                            self.aqua_infusion()
                                else:
                                    if self.max_health - self.health >= 20:
                                        if self.assimilate_unlock and self.assimilate_cooldown == 0:
                                            print("assimilate")
                                            self.rgb.append('black')
                                            self.assimilate()
                                        elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                            print("shockwave")
                                            self.rgb.append('black')
                                            self.shockwave()
                                        elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                            print("laserbeam")
                                            self.rgb.append('black')
                                            self.laserbeam()
                                        elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                            print("typhoon")
                                            self.rgb.append('black')
                                            self.typhoon()
                                        else:
                                            if self.assimilate_unlock:
                                                if self.shockwave_unlock:
                                                    if self.typhoon_unlock:
                                                        if self.ruminate_unlock:
                                                            if self.laserbeam_unlock:
                                                                if self.ruminate_cooldown == 0:
                                                                    print("ruminate")
                                                                    self.rgb.append('black')
                                                                    self.ruminate()
                                                                else:
                                                                    print("needle")
                                                                    self.rgb.append('red')
                                                                    self.needle()
                                                            else:
                                                                print("ignis infusion")
                                                                self.rgb.append('red')
                                                                self.ignis_infusion()
                                                        else:
                                                            print("pneuma infusion")
                                                            self.rgb.append('green')
                                                            self.pneuma_infusion()
                                                    else:
                                                        print("caeli infusion")
                                                        self.rgb.append('blue')
                                                        self.caeli_infusion()
                                                else:
                                                    print("terra infusion")
                                                    self.rgb.append('blue')
                                                    self.terra_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                            else:
                                if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                                if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                                if self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                    else:
                        if self.max_health - self.health - self.x >= 20:
                            if self.assimilate_unlock and self.assimilate_cooldown == 0:
                                print("assimilate")
                                self.rgb.append('black')
                                self.assimilate()
                            elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                print("shockwave")
                                self.rgb.append('black')
                                self.shockwave()
                            elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                print("laserbeam")
                                self.rgb.append('black')
                                self.laserbeam()
                            elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                print("typhoon")
                                self.rgb.append('black')
                                self.typhoon()
                            else:
                                if self.assimilate_unlock:
                                    if self.shockwave_unlock:
                                        if self.typhoon_unlock:
                                            if self.ruminate_unlock:
                                                if self.laserbeam_unlock:
                                                    if self.ruminate_cooldown == 0:
                                                        print("ruminate")
                                                        self.rgb.append('black')
                                                        self.ruminate()
                                                    else:
                                                        print("needle")
                                                        self.rgb.append('red')
                                                        self.needle()
                                                else:
                                                    print("ignis infusion")
                                                    self.rgb.append('red')
                                                    self.ignis_infusion()
                                            else:
                                                print("pneuma infusion")
                                                self.rgb.append('green')
                                                self.pneuma_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("terra infusion")
                                        self.rgb.append('blue')
                                        self.terra_infusion()
                                else:
                                    print("aqua infusion")
                                    self.rgb.append('green')
                                    self.aqua_infusion()
                            if self.healing + self.shielding > self.x:
                                if self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                else:
                                    if self.assimilate_unlock:
                                        if self.shockwave_unlock:
                                            if self.typhoon_unlock:
                                                if self.ruminate_unlock:
                                                    if self.laserbeam_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("ignis infusion")
                                                        self.rgb.append('red')
                                                        self.ignis_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                            else:
                                if self.max_health - self.health >= 20:
                                    if self.assimilate_unlock and self.assimilate_cooldown == 0:
                                        print("assimilate")
                                        self.rgb.append('black')
                                        self.assimilate()
                                    elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                        print("shockwave")
                                        self.rgb.append('black')
                                        self.shockwave()
                                    elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                        print("laserbeam")
                                        self.rgb.append('black')
                                        self.laserbeam()
                                    elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                        print("typhoon")
                                        self.rgb.append('black')
                                        self.typhoon()
                                    else:
                                        if self.assimilate_unlock:
                                            if self.shockwave_unlock:
                                                if self.typhoon_unlock:
                                                    if self.ruminate_unlock:
                                                        if self.laserbeam_unlock:
                                                            if self.ruminate_cooldown == 0:
                                                                print("ruminate")
                                                                self.rgb.append('black')
                                                                self.ruminate()
                                                            else:
                                                                print("needle")
                                                                self.rgb.append('red')
                                                                self.needle()
                                                        else:
                                                            print("ignis infusion")
                                                            self.rgb.append('red')
                                                            self.ignis_infusion()
                                                    else:
                                                        print("pneuma infusion")
                                                        self.rgb.append('green')
                                                        self.pneuma_infusion()
                                                else:
                                                    print("caeli infusion")
                                                    self.rgb.append('blue')
                                                    self.caeli_infusion()
                                            else:
                                                print("terra infusion")
                                                self.rgb.append('blue')
                                                self.terra_infusion()
                                else:
                                    if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                        print("laserbeam")
                                        self.rgb.append('black')
                                        self.laserbeam()
                                    elif self.assimilate_unlock and self.assimilate_cooldown == 0:
                                        print("assimilate")
                                        self.rgb.append('black')
                                        self.assimilate()
                                    elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                        print("shockwave")
                                        self.rgb.append('black')
                                        self.shockwave()
                                    elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                        print("typhoon")
                                        self.rgb.append('black')
                                        self.typhoon()
                                    else:
                                        if self.laserbeam_unlock:
                                            if self.typhoon_unlock:
                                                if self.assimilate_unlock:
                                                    if self.ruminate_unlock:
                                                        if self.shockwave_unlock:
                                                            if self.ruminate_cooldown == 0:
                                                                print("ruminate")
                                                                self.rgb.append('black')
                                                                self.ruminate()
                                                            else:
                                                                print("needle")
                                                                self.rgb.append('red')
                                                                self.needle()
                                                        else:
                                                            print("terra infusion")
                                                            self.rgb.append('blue')
                                                            self.terra_infusion()
                                                    else:
                                                        print("pneuma infusion")
                                                        self.rgb.append('green')
                                                        self.pneuma_infusion()
                                                else:
                                                    print("aqua infusion")
                                                    self.rgb.append('green')
                                                    self.aqua_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("ignis infusion")
                                            self.rgb.append('red')
                                            self.ignis_infusion()
                            if self.healing + self.shielding > self.x:
                                if self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                else:
                                    if self.assimilate_unlock:
                                        if self.shockwave_unlock:
                                            if self.typhoon_unlock:
                                                if self.ruminate_unlock:
                                                    if self.laserbeam_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("ignis infusion")
                                                        self.rgb.append('red')
                                                        self.ignis_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("aqua infusion")
                                        self.rgb.append('green')
                                        self.aqua_infusion()
                            else:
                                if self.max_health - self.health >= 20:
                                    if self.assimilate_unlock and self.assimilate_cooldown == 0:
                                        print("assimilate")
                                        self.rgb.append('black')
                                        self.assimilate()
                                    elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                        print("shockwave")
                                        self.rgb.append('black')
                                        self.shockwave()
                                    elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                        print("laserbeam")
                                        self.rgb.append('black')
                                        self.laserbeam()
                                    elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                        print("typhoon")
                                        self.rgb.append('black')
                                        self.typhoon()
                                    else:
                                        if self.assimilate_unlock:
                                            if self.shockwave_unlock:
                                                if self.typhoon_unlock:
                                                    if self.ruminate_unlock:
                                                        if self.laserbeam_unlock:
                                                            if self.ruminate_cooldown == 0:
                                                                print("ruminate")
                                                                self.rgb.append('black')
                                                                self.ruminate()
                                                            else:
                                                                print("needle")
                                                                self.rgb.append('red')
                                                                self.needle()
                                                        else:
                                                            print("ignis infusion")
                                                            self.rgb.append('red')
                                                            self.ignis_infusion()
                                                    else:
                                                        print("pneuma infusion")
                                                        self.rgb.append('green')
                                                        self.pneuma_infusion()
                                                else:
                                                    print("caeli infusion")
                                                    self.rgb.append('blue')
                                                    self.caeli_infusion()
                                            else:
                                                print("terra infusion")
                                                self.rgb.append('blue')
                                                self.terra_infusion()
                                        else:
                                            print("aqua infusion")
                                            self.rgb.append('green')
                                            self.aqua_infusion()
                                else:
                                    if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                        print("laserbeam")
                                        self.rgb.append('black')
                                        self.laserbeam()
                                    elif self.assimilate_unlock and self.assimilate_cooldown == 0:
                                        print("assimilate")
                                        self.rgb.append('black')
                                        self.assimilate()
                                    elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                        print("shockwave")
                                        self.rgb.append('black')
                                        self.shockwave()
                                    elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                        print("typhoon")
                                        self.rgb.append('black')
                                        self.typhoon()
                                    else:
                                        if self.laserbeam_unlock:
                                            if self.typhoon_unlock:
                                                if self.assimilate_unlock:
                                                    if self.ruminate_unlock:
                                                        if self.shockwave_unlock:
                                                            if self.ruminate_cooldown == 0:
                                                                print("ruminate")
                                                                self.rgb.append('black')
                                                                self.ruminate()
                                                            else:
                                                                print("needle")
                                                                self.rgb.append('red')
                                                                self.needle()
                                                        else:
                                                            print("terra infusion")
                                                            self.rgb.append('blue')
                                                            self.terra_infusion()
                                                    else:
                                                        print("pneuma infusion")
                                                        self.rgb.append('green')
                                                        self.pneuma_infusion()
                                                else:
                                                    print("aqua infusion")
                                                    self.rgb.append('green')
                                                    self.aqua_infusion()
                                            else:
                                                print("caeli infusion")
                                                self.rgb.append('blue')
                                                self.caeli_infusion()
                                        else:
                                            print("ignis infusion")
                                            self.rgb.append('red')
                                            self.ignis_infusion()
                        else:
                            if self.max_health - self.health >= 20:
                                if self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                                if self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                                if self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                            else:
                                if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                                if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                                if self.typhoon_unlock and self.typhoon_cooldown == 0:
                                    print("typhoon")
                                    self.rgb.append('black')
                                    self.typhoon()
                                elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                                    print("laserbeam")
                                    self.rgb.append('black')
                                    self.laserbeam()
                                elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                                    print("assimilate")
                                    self.rgb.append('black')
                                    self.assimilate()
                                elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                                    print("shockwave")
                                    self.rgb.append('black')
                                    self.shockwave()
                                else:
                                    if self.laserbeam_unlock:
                                        if self.typhoon_unlock:
                                            if self.assimilate_unlock:
                                                if self.ruminate_unlock:
                                                    if self.shockwave_unlock:
                                                        if self.ruminate_cooldown == 0:
                                                            print("ruminate")
                                                            self.rgb.append('black')
                                                            self.ruminate()
                                                        else:
                                                            print("needle")
                                                            self.rgb.append('red')
                                                            self.needle()
                                                    else:
                                                        print("terra infusion")
                                                        self.rgb.append('blue')
                                                        self.terra_infusion()
                                                else:
                                                    print("pneuma infusion")
                                                    self.rgb.append('green')
                                                    self.pneuma_infusion()
                                            else:
                                                print("aqua infusion")
                                                self.rgb.append('green')
                                                self.aqua_infusion()
                                        else:
                                            print("caeli infusion")
                                            self.rgb.append('blue')
                                            self.caeli_infusion()
                                    else:
                                        print("ignis infusion")
                                        self.rgb.append('red')
                                        self.ignis_infusion()
                else:
                    if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                        print("laserbeam")
                        self.rgb.append('black')
                        self.laserbeam()
                    elif self.assimilate_unlock and self.assimilate_cooldown == 0:
                        print("assimilate")
                        self.rgb.append('black')
                        self.assimilate()
                    elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                        print("shockwave")
                        self.rgb.append('black')
                        self.shockwave()
                    elif self.typhoon_unlock and self.typhoon_cooldown == 0:
                        print("typhoon")
                        self.rgb.append('black')
                        self.typhoon()
                    else:
                        if self.laserbeam_unlock:
                            if self.typhoon_unlock:
                                if self.assimilate_unlock:
                                    if self.ruminate_unlock:
                                        if self.shockwave_unlock:
                                            if self.ruminate_cooldown == 0:
                                                print("ruminate")
                                                self.rgb.append('black')
                                                self.ruminate()
                                            else:
                                                print("needle")
                                                self.rgb.append('red')
                                                self.needle()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("pneuma infusion")
                                        self.rgb.append('green')
                                        self.pneuma_infusion()
                                else:
                                    print("aqua infusion")
                                    self.rgb.append('green')
                                    self.aqua_infusion()
                            else:
                                print("caeli infusion")
                                self.rgb.append('blue')
                                self.caeli_infusion()
                        else:
                            print("ignis infusion")
                            self.rgb.append('red')
                            self.ignis_infusion()
                    if self.typhoon_unlock and self.typhoon_cooldown == 0:
                        print("typhoon")
                        self.rgb.append('black')
                        self.typhoon()
                    elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                        print("laserbeam")
                        self.rgb.append('black')
                        self.laserbeam()
                    elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                        print("assimilate")
                        self.rgb.append('black')
                        self.assimilate()
                    elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                        print("shockwave")
                        self.rgb.append('black')
                        self.shockwave()
                    else:
                        if self.laserbeam_unlock:
                            if self.typhoon_unlock:
                                if self.assimilate_unlock:
                                    if self.ruminate_unlock:
                                        if self.shockwave_unlock:
                                            if self.ruminate_cooldown == 0:
                                                print("ruminate")
                                                self.rgb.append('black')
                                                self.ruminate()
                                            else:
                                                print("needle")
                                                self.rgb.append('red')
                                                self.needle()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("pneuma infusion")
                                        self.rgb.append('green')
                                        self.pneuma_infusion()
                                else:
                                    print("aqua infusion")
                                    self.rgb.append('green')
                                    self.aqua_infusion()
                            else:
                                print("caeli infusion")
                                self.rgb.append('blue')
                                self.caeli_infusion()
                        else:
                            print("ignis infusion")
                            self.rgb.append('red')
                            self.ignis_infusion()
                    if self.typhoon_unlock and self.typhoon_cooldown == 0:
                        print("typhoon")
                        self.rgb.append('black')
                        self.typhoon()
                    elif self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                        print("laserbeam")
                        self.rgb.append('black')
                        self.laserbeam()
                    elif self.max_health - self.health >= 20 and self.assimilate_unlock and self.assimilate_cooldown == 0:
                        print("assimilate")
                        self.rgb.append('black')
                        self.assimilate()
                    elif self.shockwave_unlock and self.shockwave_cooldown == 0:
                        print("shockwave")
                        self.rgb.append('black')
                        self.shockwave()
                    else:
                        if self.laserbeam_unlock:
                            if self.typhoon_unlock:
                                if self.assimilate_unlock:
                                    if self.ruminate_unlock:
                                        if self.shockwave_unlock:
                                            if self.ruminate_cooldown == 0:
                                                print("ruminate")
                                                self.rgb.append('black')
                                                self.ruminate()
                                            else:
                                                print("needle")
                                                self.rgb.append('red')
                                                self.needle()
                                        else:
                                            print("terra infusion")
                                            self.rgb.append('blue')
                                            self.terra_infusion()
                                    else:
                                        print("pneuma infusion")
                                        self.rgb.append('green')
                                        self.pneuma_infusion()
                                else:
                                    print("aqua infusion")
                                    self.rgb.append('green')
                                    self.aqua_infusion()
                            else:
                                print("caeli infusion")
                                self.rgb.append('blue')
                                self.caeli_infusion()
                        else:
                            print("ignis infusion")
                            self.rgb.append('red')
                            self.ignis_infusion()

    def terra_infusion(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Block x2, if 3-, shockwave can be played
        self.last_action = "Terra Infusion"
        number = self.roll_d10()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        if number < 4:
            if not self.shockwave_unlock:
                time.sleep(0.5)
                display_text((f"You rolled 3 or less! You are now terra infused.", 2))
                self.shockwave_unlock = True
        self.shielding += int(
            int(number * self.thorns_defence_and_healing_percentage) // 1) * 2 + self.permanent_defence_increase + self.temporary_defence_increase
        if self.temporary_defence_increase > 0:
            self.temporary_defence_increase = 0
        time.sleep(0.5)
        display_text((f"Your shield is now {self.shielding}.", 2))
        self.rgb.pop(self.rgb.index('blue'))

    def caeli_infusion(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Permanent defence increase, if 3-, Typhoon can be played
        self.last_action = "Caeli Infusion"
        number = self.roll_d10()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        if number < 4:
            if not self.typhoon_unlock:
                time.sleep(0.5)
                display_text((f"You rolled 3 or less! You are now caeli infused.", 2))
                self.typhoon_unlock = True
        self.caeli_infusion_cumulative += number
        if self.caeli_infusion_cumulative > 25:
            self.caeli_infusion_cumulative = 25
            time.sleep(0.5)
            display_text((f"You have reached the maximum defence increase of 25.", 2))
        else:
            self.permanent_defence_increase += number
            time.sleep(0.5)
            display_text((f"Your defence is now permanently increased by {self.permanent_defence_increase}/25.", 2))
        self.rgb.pop(self.rgb.index('blue'))

    def dodge(self):
        from graphics import display_text
        # Take no damage this turn, skip next turn
        self.last_action = "Dodge"
        self.dodge_cooldown = 2
        self.dodge_trigger = True
        time.sleep(1)
        display_text(("You are dodging the enemy attack! You will not play next turn.", 2))
        self.rgb.pop(self.rgb.index('blue'))

    def ignis_infusion(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Attack x2, if 3-, Laserbeam can be played
        self.last_action = "Ignis Infusion"
        number = self.roll_d10()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        if number < 4:
            if not self.laserbeam_unlock:
                time.sleep(0.5)
                display_text((f"You rolled 3 or less! You are now ignis infused.", 2))
                self.laserbeam_unlock = True
        self.attack += int(
            int(number * self.thorns_attack_percentage) // 1) * 2 + self.permanent_attack_increase + self.temporary_attack_increase
        if self.temporary_attack_increase > 0:
            self.temporary_attack_increase = 0
        time.sleep(0.5)
        display_text((f"Your attack is now {self.attack}.", 2))
        self.rgb.pop(self.rgb.index('red'))

    def needle(self):
        from graphics import display_text
        from graphics import display_player_dice
        # If 11+, Attack = 20, else Attack = 0. Increase dmg by 5 for every use
        self.last_action = "Needle"
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        if number > 10:
            number = 20 + self.needle_cumulative
        else:
            number = self.needle_cumulative
        if number > 50:
            number = 50
        self.attack += int(
            int(number * self.thorns_attack_percentage) // 1) + self.permanent_attack_increase + self.temporary_attack_increase
        if self.temporary_attack_increase > 0:
            self.temporary_attack_increase = 0
        self.needle_cumulative += 5
        time.sleep(0.5)
        display_text((f"Your attack is now {self.attack}.", 2))
        self.rgb.pop(self.rgb.index('red'))

    def thorns(self):
        from graphics import display_text
        # All attacks have crit while all shields and heals are halved for the rest of the game
        self.last_action = "Thorns"
        self.thorns_trigger = True
        self.thorns_attack_percentage = 1.5
        self.thorns_defence_and_healing_percentage = 0.5
        time.sleep(0.5)
        display_text((f"Your attacks now have crit and your defence and heals are halved.", 2))
        self.rgb.pop(self.rgb.index('red'))

    def aqua_infusion(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Heal x2, if 3-, Assimilate can be played
        self.last_action = "Aqua Infusion"
        number = self.roll_d10()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        if number < 4:
            if not self.assimilate_unlock:
                time.sleep(0.5)
                display_text((f"You rolled 3 or less! You are now aqua infused.", 2))
                self.assimilate_unlock = True
        self.healing += int(
            int(number * self.thorns_defence_and_healing_percentage) // 1) * 2 + self.permanent_healing_increase + self.temporary_healing_increase
        if self.temporary_healing_increase > 0:
            self.temporary_healing_increase = 0
        time.sleep(0.5)
        display_text((f"Your healing is now {self.healing}.", 2))
        self.rgb.pop(self.rgb.index('green'))

    def pneuma_infusion_aux(self):
        from graphics import display_text
        # Inflicts a buff on the player and two debuffs on the enemy
        b = random.randint(1, 6)
        if b == 1:
            self.permanent_attack_increase += self.pneuma_infusion_dice_value
            time.sleep(0.5)
            display_text((f"Your attack is now permanently increased by {self.permanent_attack_increase}.", 2))
        elif b == 2:
            self.permanent_defence_increase += self.pneuma_infusion_dice_value
            time.sleep(0.5)
            display_text((f"Your defence is now permanently increased by {self.permanent_defence_increase}.", 2))
        elif b == 3:
            self.permanent_healing_increase += self.pneuma_infusion_dice_value
            time.sleep(0.5)
            display_text((f"Your healing is now permanently increased by {self.permanent_healing_increase}.", 2))
        elif b == 4:
            self.temporary_attack_increase += self.pneuma_infusion_dice_value
            time.sleep(0.5)
            display_text((f"Your next attack increased by {self.temporary_attack_increase}.", 2))
        elif b == 5:
            self.temporary_defence_increase += self.pneuma_infusion_dice_value
            time.sleep(0.5)
            display_text((f"Your next shield is increased by {self.temporary_defence_increase}.", 2))
        elif b == 6:
            self.temporary_healing_increase += self.pneuma_infusion_dice_value
            time.sleep(0.5)
            display_text((f"Your next heal is increased by {self.temporary_healing_increase}.", 2))
        for i in range(2):
            d = random.randint(1, 6)
            if d == 1:
                self.temporary_attack_decrease += self.pneuma_infusion_dice_value
                time.sleep(0.5)
                display_text((f"The enemy's next attack is decreased by {self.temporary_attack_decrease}.", 2))
            elif d == 2:
                self.temporary_defence_decrease += self.pneuma_infusion_dice_value
                time.sleep(0.5)
                display_text((f"The enemy's next shield is decreased by {self.temporary_defence_decrease}.", 2))
            elif d == 3:
                self.temporary_healing_decrease += self.pneuma_infusion_dice_value
                time.sleep(0.5)
                display_text((f"The enemy's next heal is decreased by {self.temporary_healing_decrease}.", 2))
            elif d == 4:
                self.burn.append((self.pneuma_infusion_dice_value, 1))
                time.sleep(0.5)
                display_text((f"You have inflicted {self.burn[-1][0]} burn on the enemy for 1 round.", 2))
            elif d == 5:
                self.bleed.append((self.pneuma_infusion_dice_value, 1))
                time.sleep(0.5)
                display_text((f"You have inflicted {self.bleed[-1][0]} bleed on the enemy for 1 round.", 2))
            elif d == 6:
                self.poison.append((self.pneuma_infusion_dice_value, 1))
                time.sleep(0.5)
                display_text((f"You have inflicted {self.poison[-1][0]} poison on the enemy for 1 round.", 2))

    def pneuma_infusion(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Heal, gain a buff, inflict two debuffs onto an enemy = value, if 3-, Ruminate can be played
        self.last_action = "pneuma Infusion"
        number = self.roll_d10()
        self.pneuma_infusion_dice_value = number
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        if number < 4:
            if not self.ruminate_unlock:
                time.sleep(0.5)
                display_text((f"You rolled 3 or less! You are now pneuma infused.", 2))
                self.ruminate_unlock = True
        self.healing += int(
            int(number * self.thorns_defence_and_healing_percentage) // 1) + self.permanent_healing_increase + self.temporary_healing_increase
        if self.temporary_healing_increase > 0:
            self.temporary_healing_increase = 0
        time.sleep(0.5)
        display_text((f"Your healing is now {self.healing}.", 2))
        self.pneuma_infusion_aux()
        self.rgb.pop(self.rgb.index('green'))

    def preservation(self):
        from graphics import display_text
        # Don't take 75+ damage and ignore debuffs but throw only 2 die for the rest of the game
        self.last_action = "Preservation"
        self.preservation_trigger = True
        time.sleep(0.5)
        display_text((f"You only take up to 40 damage now, and roll one dice less.", 2))
        self.rgb.pop(self.rgb.index('green'))

    def shockwave(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Block x2, Attack = Block
        self.last_action = "Shockwave"
        self.shockwave_cooldown = 1
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        number = int(
            int(number * self.thorns_defence_and_healing_percentage) // 1) * 2 + self.permanent_defence_increase + self.temporary_defence_increase
        self.shielding += number
        if self.temporary_defence_increase > 0:
            self.temporary_defence_increase = 0
        time.sleep(0.5)
        display_text((f"Your shield is now {self.shielding}.", 2))
        self.attack += int(
            int(number * self.thorns_attack_percentage) // 1) + self.permanent_attack_increase + self.temporary_attack_increase
        if self.temporary_attack_increase > 0:
            self.temporary_attack_increase = 0
        time.sleep(0.5)
        display_text((f"Your attack is now {self.attack}.", 2))
        self.rgb.pop(self.rgb.index('black'))

    def assimilate(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Attack x2, Heal for dmg dealt
        self.last_action = "Assimilate"
        self.assimilate_cooldown = 1
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        self.drain_attack += int(
            int(number * self.thorns_attack_percentage) // 1) * 2 + self.permanent_attack_increase + self.temporary_attack_increase
        if self.temporary_attack_increase > 0:
            self.temporary_attack_increase = 0
        time.sleep(0.5)
        display_text((f"Your drain is now {self.drain_attack}.", 2))
        self.rgb.pop(self.rgb.index('black'))

    def laserbeam(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Attack x 2, Burn x 2
        self.last_action = "Laserbeam"
        self.laserbeam_cooldown = 1
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        self.attack += int(
            int(number * self.thorns_attack_percentage) // 1) * 2 + self.permanent_attack_increase + self.temporary_attack_increase
        if self.temporary_attack_increase > 0:
            self.temporary_attack_increase = 0
        time.sleep(0.5)
        display_text((f"Your attack is now {self.attack}.", 2))
        self.burn.append((int(int(number * self.thorns_attack_percentage) // 1) + self.permanent_attack_increase, 2))
        time.sleep(0.5)
        display_text((f"You have inflicted {self.burn[-1][0]} burn on the enemy for 2 rounds.", 2))
        self.rgb.pop(self.rgb.index('black'))

    def typhoon(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Attack+10, If played after Laserbeam, Burn, if played after Assimilate, Temporary defence decrease, if played after Shockwave, 25% Stun
        self.typhoon_cooldown = 1
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        self.attack += int(
            int(number * self.thorns_attack_percentage) // 1) + 10 + self.permanent_attack_increase + self.temporary_attack_increase
        if self.temporary_attack_increase > 0:
            self.temporary_attack_increase = 0
        time.sleep(0.5)
        display_text((f"Your attack is now {self.attack}.", 2))
        if self.last_action == 'Shockwave':
            x = random.randint(1, 4)
            if x == 1:
                self.stun = True
                self.stun_duration = 1
                time.sleep(0.5)
                display_text((f"Enemy is now stunned.", 2))
        elif self.last_action == 'Laserbeam':
            self.burn.append(
                (int(int(number * self.thorns_attack_percentage) // 1) + self.permanent_attack_increase, 1))
            time.sleep(0.5)
            display_text((f"You have inflicted {self.burn[-1][0]} burn on the enemy for 1 round.", 2))
        elif self.last_action == 'Assimilate':
            self.temporary_defence_decrease += number
            time.sleep(0.5)
            display_text((
                         f"You have inflicted a total of {self.temporary_defence_decrease} Temporary Defence Decrease on the enemy.",
                         2))
        self.last_action = "Typhoon"
        self.rgb.pop(self.rgb.index('black'))

    def ruminate(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Temporary damage increase, Temporary defence increase, remove cooldowns on all other actions
        self.last_action = "Ruminate"
        self.ruminate_cooldown = 3
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        self.temporary_attack_increase += number
        time.sleep(0.5)
        display_text((f"You now have a total of {self.temporary_attack_increase} Temporary Attack Increase.", 2))
        self.temporary_defence_increase += number
        time.sleep(0.5)
        display_text((f"You now have a total of {self.temporary_defence_increase} Temporary Defence Increase.", 2))
        self.ruminate_trigger = True
        self.rgb.pop(self.rgb.index('black'))

    def vitalize(self):
        from graphics import display_text
        from graphics import display_player_dice
        # Heal x3, increase max HP by value
        self.last_action = "Vitalize"
        self.vitalize_cooldown = 1
        number = self.roll_d20()
        time.sleep(1)
        display_player_dice(self.rgb[0], number)
        display_text((f"You got {number}!", 2))
        self.healing += int(
            int(number * self.thorns_defence_and_healing_percentage) // 1) + 15 + self.permanent_healing_increase + self.temporary_healing_increase
        if self.temporary_healing_increase > 0:
            self.temporary_healing_increase = 0
        time.sleep(0.5)
        display_text((f"Your healing is now {self.healing}.", 2))
        self.max_health += number
        time.sleep(0.5)
        display_text((f"Your max health is now {self.max_health}.", 2))
        self.rgb.pop(self.rgb.index('black'))

    def choose_action(self, action, colour):
        from graphics import display_text
        from graphics import create_and_manage_buttons
        self.action = action.lower()
        if action == 'terra infusion':
            self.terra_infusion()
        elif action == 'caeli infusion':
            self.caeli_infusion()
        elif action == 'dodge':
            if self.dodge_cooldown == 0:
                self.dodge()
            else:
                display_text(('Action is on cooldown! Choose another action.', 2))
                self.choose_action(create_and_manage_buttons(["Terra Infusion", "Caeli Infusion", "Dodge", 1]),
                                   self.rgb)
        elif action == 'ignis infusion':
            self.ignis_infusion()
        elif action == 'needle':
            self.needle()
        elif action == 'thorns':
            if self.thorns_trigger:
                display_text(('This action can only be played once this combat! Choose another action.', 2))
                self.choose_action(create_and_manage_buttons(["Ignis Infusion", "Needle", "Thorns", 1]), self.rgb)
            else:
                self.thorns()
        elif action == 'aqua infusion':
            self.aqua_infusion()
        elif action == 'pneuma infusion':
            self.pneuma_infusion()
        elif action == 'preservation':
            if self.preservation_trigger:
                display_text(('This action can only be played once this combat! Choose another action.', 2))
                self.choose_action(create_and_manage_buttons(["Aqua Infusion", "Pneuma Infusion", "Preservation", 2]),
                                   self.rgb)
            else:
                self.preservation()
        elif action == 'shockwave':
            if self.shockwave_unlock and self.shockwave_cooldown == 0:
                self.shockwave()
            elif not self.shockwave_unlock:
                display_text(("You must first gain terra infusion!", 2))
                self.choose_action(create_and_manage_buttons(["Shockwave (Terra)(Cooldown = 1 round)",
                                                              "Typhoon (Caeli)(Cooldown = 1 round)",
                                                              "Laserbeam (Ignis)(Cooldown = 1 round)",
                                                              "Ruminate (Pneuma)(Cooldown = 3 rounds)",
                                                              "Vitalize", 1]), self.rgb)
            else:
                display_text(('Action is on cooldown!', 2))
                self.choose_action(create_and_manage_buttons(["Shockwave (Terra)(Cooldown = 1 round)",
                                                              "Typhoon (Caeli)(Cooldown = 1 round)",
                                                              "Laserbeam (Ignis)(Cooldown = 1 round)",
                                                              "Ruminate (Pneuma)(Cooldown = 3 rounds)",
                                                              "Vitalize", 1]), self.rgb)
        elif action == 'assimilate':
            if self.assimilate_unlock and self.assimilate_cooldown == 0:
                self.assimilate()
            elif not self.typhoon_unlock:
                display_text(("You must first gain aqua infusion!", 2))
                self.choose_action(create_and_manage_buttons(["Shockwave (Terra)(Cooldown = 1 round)",
                                                              "Typhoon (Caeli)(Cooldown = 1 round)",
                                                              "Laserbeam (Ignis)(Cooldown = 1 round)",
                                                              "Ruminate (Pneuma)(Cooldown = 3 rounds)",
                                                              "Vitalize", 1]), self.rgb)
            else:
                display_text(('Action is on cooldown!', 2))
                self.choose_action(create_and_manage_buttons(["Shockwave (Terra)(Cooldown = 1 round)",
                                                              "Typhoon (Caeli)(Cooldown = 1 round)",
                                                              "Laserbeam (Ignis)(Cooldown = 1 round)",
                                                              "Ruminate (Pneuma)(Cooldown = 3 rounds)",
                                                              "Vitalize", 1]), self.rgb)
        elif action == 'typhoon':
            if self.typhoon_unlock and self.typhoon_cooldown == 0:
                self.typhoon()
            elif not self.laserbeam_unlock:
                display_text(("You must first gain caeli infusion!", 2))
                self.choose_action(create_and_manage_buttons(["Shockwave (Terra)(Cooldown = 1 round)",
                                                              "Typhoon (Caeli)(Cooldown = 1 round)",
                                                              "Laserbeam (Ignis)(Cooldown = 1 round)",
                                                              "Ruminate (Pneuma)(Cooldown = 3 rounds)",
                                                              "Vitalize", 1]), self.rgb)
            else:
                display_text(('Action is on cooldown!', 2))
                self.choose_action(create_and_manage_buttons(["Shockwave (Terra)(Cooldown = 1 round)",
                                                              "Typhoon (Caeli)(Cooldown = 1 round)",
                                                              "Laserbeam (Ignis)(Cooldown = 1 round)",
                                                              "Ruminate (Pneuma)(Cooldown = 3 rounds)",
                                                              "Vitalize", 1]), self.rgb)
        elif action == 'laserbeam':
            if self.laserbeam_unlock and self.laserbeam_cooldown == 0:
                self.laserbeam()
            elif not self.assimilate_unlock:
                display_text(("You must first gain ignis infusion!", 2))
                self.choose_action(create_and_manage_buttons(["Shockwave (Terra)(Cooldown = 1 round)",
                                                              "Typhoon (Caeli)(Cooldown = 1 round)",
                                                              "Laserbeam (Ignis)(Cooldown = 1 round)",
                                                              "Ruminate (Pneuma)(Cooldown = 3 rounds)",
                                                              "Vitalize", 1]), self.rgb)
            else:
                display_text(('Action is on cooldown!', 2))
                self.choose_action(create_and_manage_buttons(["Shockwave (Terra)(Cooldown = 1 round)",
                                                              "Typhoon (Caeli)(Cooldown = 1 round)",
                                                              "Laserbeam (Ignis)(Cooldown = 1 round)",
                                                              "Ruminate (Pneuma)(Cooldown = 3 rounds)",
                                                              "Vitalize", 1]), self.rgb)
        elif action == 'ruminate':
            if self.ruminate_unlock and self.ruminate_cooldown == 0:
                self.ruminate()
            elif not self.assimilate_unlock:
                display_text(("You must first gain pneuma infusion!", 2))
                self.choose_action(create_and_manage_buttons(["Shockwave (Terra)(Cooldown = 1 round)",
                                                              "Typhoon (Caeli)(Cooldown = 1 round)",
                                                              "Laserbeam (Ignis)(Cooldown = 1 round)",
                                                              "Ruminate (Pneuma)(Cooldown = 3 rounds)",
                                                              "Vitalize", 1]), self.rgb)
            else:
                display_text(('Action is on cooldown!', 2))
                self.choose_action(create_and_manage_buttons(["Shockwave (Terra)(Cooldown = 1 round)",
                                                              "Typhoon (Caeli)(Cooldown = 1 round)",
                                                              "Laserbeam (Ignis)(Cooldown = 1 round)",
                                                              "Ruminate (Pneuma)(Cooldown = 3 rounds)",
                                                              "Vitalize", 1]), self.rgb)
        elif action == 'vitalize':
            if self.vitalize_cooldown == 0:
                self.vitalize()
            else:
                display_text(('Action is on cooldown!', 2))
                self.choose_action(create_and_manage_buttons(["Shockwave (Terra)(Cooldown = 1 round)",
                                                              "Typhoon (Caeli)(Cooldown = 1 round)",
                                                              "Laserbeam (Ignis)(Cooldown = 1 round)",
                                                              "Ruminate (Pneuma)(Cooldown = 3 rounds)",
                                                              "Vitalize", 1]), self.rgb)
        else:
            display_text(("You can't do that.", 2))
            self.choose_die()
