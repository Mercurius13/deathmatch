from lancelot import *
from master import *
from rogue import *


class Battle:
    def __init__(self):
        self.one_player = None
        self.two_player = None
        self.current_player = None
        self.next_player = None
        self.p1_round_count = 0
        self.p2_round_count = -0.5
        self.p1_rogue_max_damage = 0
        self.p1_lancelot_max_damage = 0
        self.p1_master_max_damage = 0
        self.p2_rogue_max_damage = 0
        self.p2_lancelot_max_damage = 0
        self.p2_master_max_damage = 0
        self.d = 0
        self.d1 = 0
        self.d2 = 0

    def character_select(self, player1, player2):
        from graphics import username_1, username_2
        if player1 == "rogue":
            self.one_player = Rogue(username_1)
        elif player1 == "lancelot":
            self.one_player = Lancelot(username_1)
        elif player1 == "master":
            self.one_player = Master(username_1)

        if player2 == "rogue":
            self.two_player = Rogue(username_2)
        elif player2 == "lancelot":
            self.two_player = Lancelot(username_2)
        elif player2 == "master":
            self.two_player = Master(username_2)
        print(f"{self.one_player.name} is a {self.one_player.character}")
        print(f"{self.two_player.name} is a {self.two_player.character}")

    def calculation(self, one_player, two_player):
        from graphics import display_text
        self.d = 0
        if self.one_player.preservation_trigger:
            if self.two_player.attack > 75:
                self.two_player.attack = 75
            self.two_player.burn = self.two_player.burn.clear()
            self.two_player.bleed = self.two_player.bleed.clear()
            self.two_player.poison = self.two_player.poison.clear()
            self.two_player.stun = False
            self.two_player.temporary_attack_decrease = 0
            self.two_player.temporary_defence_decrease = 0
            self.two_player.temporary_healing_decrease = 0
        if not self.two_player.stun and not self.one_player.dodge_trigger:
            display_text((f"{self.one_player.name}'s turn!", 2))
            self.one_player.choose_die()
        if one_player.blood_pact_suicide:
            print(f"Health of {two_player.name}: {two_player.health}/{two_player.max_health}")
            print(f"Health of {one_player.name}: {one_player.health}/{one_player.max_health}")
            pass
        one_player.regen_aux()
        if two_player.temporary_attack_decrease > 0:
            one_player.attack -= two_player.temporary_attack_decrease
            two_player.temporary_attack_decrease = 0
        if two_player.temporary_defence_decrease > 0:
            one_player.shielding -= two_player.temporary_defence_decrease
            two_player.temporary_defence_decrease = 0
        if two_player.temporary_healing_decrease > 0:
            one_player.healing -= two_player.temporary_healing_decrease
            two_player.temporary_healing_decrease = 0
        for i in two_player.burn:
            two_player.attack += i[0]
        for i in two_player.bleed:
            two_player.attack += i[0]
        for i in two_player.poison:
            two_player.attack += i[0]
        self.d += one_player.attack + one_player.drain_attack
        one_player.enemy_attack = 0
        two_player.enemy_attack = one_player.attack
        two_player.enemy_drain_attack = one_player.drain_attack
        if one_player.shielding > two_player.attack:
            one_player.shielding -= two_player.attack
            two_player.attack = 0
        else:
            one_player.health += (one_player.shielding - two_player.attack)
            two_player.attack = 0
        if one_player.shielding > two_player.drain_attack:
            one_player.shielding -= two_player.drain_attack
            two_player.drain_attack = 0
        else:
            one_player.health += (one_player.shielding - two_player.drain_attack)
            two_player.health += two_player.drain_attack
            if two_player.health > two_player.max_health:
                two_player.health = two_player.max_health
            two_player.drain_attack = 0
        one_player.shielding = 0
        if one_player.health + one_player.healing > one_player.max_health:
            one_player.health = one_player.max_health
        else:
            one_player.health += one_player.healing
        one_player.healing = 0
        if not one_player.dodge_trigger and not one_player.stun:
            print(f"Health of {two_player.name}: {two_player.health}/{two_player.max_health}")
            print(f"Health of {one_player.name}: {one_player.health}/{one_player.max_health}")
        if one_player.dodge_trigger and one_player.dodge_cooldown == 1:
            one_player.dodge_trigger = False
        if two_player.stun_duration == 0:
            two_player.stun = False
        two_player.reset_cooldowns()

    def who_starts(self):
        from graphics import display_text
        from graphics import username_1, username_2
        display_text(("FLIPPING A COIN...", 2))
        time.sleep(1.5)
        if self.one_player.max_health > self.two_player.max_health:
            self.one_player, self.two_player = self.two_player, self.one_player
            display_text((f"TAILS! {username_2} starts first!", 1))
        elif self.one_player.max_health == self.two_player.max_health:
            coin_flip = random.choice([f"HEADS! {username_1} starts first!", f"TAILS! {username_2} starts first!"])
            print(coin_flip)
            if "TAILS!" in coin_flip:
                self.one_player, self.two_player = self.two_player, self.one_player
        else:
            print(f"HEADS! {username_1} starts first!")

    def turns(self):
        from graphics import display_text
        from sql_file import update_game_stats
        from graphics import holy_tuple_1, holy_tuple_2
        from graphics import return_to_main_menu
        from graphics import username_1, username_2
        self.who_starts()
        self.current_player = self.one_player
        self.next_player = self.two_player
        while self.one_player.health > 0 and self.two_player.health > 0:
            self.p1_round_count += 0.5
            self.p2_round_count += 0.5
            if self.one_player.name == username_1 or self.one_player.name == username_1 or self.one_player.name == username_1:
                if self.one_player.character == "rogue" and self.current_player == self.one_player:
                    self.d1 = self.d
                    if self.p1_rogue_max_damage < self.d1:
                        self.p1_rogue_max_damage = self.d
                        print(self.p1_rogue_max_damage)
                elif self.one_player.character == "lancelot" and self.current_player == self.one_player:
                    self.d1 = self.d
                    if self.p1_lancelot_max_damage < self.d1:
                        self.p1_lancelot_max_damage = self.d
                        print(self.p1_lancelot_max_damage)
                elif self.one_player.character == "master" and self.current_player == self.one_player:
                    self.d1 = self.d
                    if self.p1_master_max_damage < self.d1:
                        self.p1_master_max_damage = self.d
                        print(self.p1_master_max_damage)
            elif self.one_player.name == username_2 or self.one_player.name == username_2 or self.one_player.name == username_2:
                if self.one_player.character == "rogue" and self.current_player == self.one_player:
                    self.d2 = self.d
                    if self.p2_rogue_max_damage < self.d2:
                        self.p2_rogue_max_damage = self.d
                        print(self.p2_rogue_max_damage)
                elif self.one_player.character == "lancelot" and self.current_player == self.one_player:
                    self.d2 = self.d
                    if self.p2_lancelot_max_damage < self.d2:
                        self.p2_lancelot_max_damage = self.d
                        print(self.p2_lancelot_max_damage)
                elif self.one_player.character == "master" and self.current_player == self.one_player:
                    self.d2 = self.d
                    if self.p2_master_max_damage < self.d2:
                        self.p2_master_max_damage = self.d
                        print(self.p2_master_max_damage)
            else:
                print("Error")
            self.calculation(self.one_player, self.two_player)
            self.one_player, self.two_player = self.two_player, self.one_player
            self.current_player, self.next_player = self.next_player, self.current_player
        self.p1_round_count = self.p1_round_count // 1
        self.p2_round_count = self.p2_round_count // 1
        print(self.p1_round_count, self.p2_round_count)
        if self.one_player.health > self.two_player.health:
            display_text((f"{self.one_player.name.upper()} WINS!", 2))
            print(self.p2_rogue_max_damage, self.p2_lancelot_max_damage, self.p2_master_max_damage,
                  0, self.p2_round_count, holy_tuple_2)
            print(self.p1_rogue_max_damage, self.p1_lancelot_max_damage, self.p1_master_max_damage,
                  1, self.p1_round_count, holy_tuple_1)
            update_game_stats(self.p2_rogue_max_damage, self.p2_lancelot_max_damage, self.p2_master_max_damage,
                              0, self.p2_round_count, holy_tuple_2)
            update_game_stats(self.p1_rogue_max_damage, self.p1_lancelot_max_damage, self.p1_master_max_damage,
                              1, self.p1_round_count, holy_tuple_1)
            return_to_main_menu()
            del self.two_player
            del self.one_player
        else:
            display_text((f"{self.two_player.name.upper()} WINS!", 2))
            print(self.p2_rogue_max_damage, self.p2_lancelot_max_damage, self.p2_master_max_damage,
                  0, self.p2_round_count, holy_tuple_2)
            print(self.p1_rogue_max_damage, self.p1_lancelot_max_damage, self.p1_master_max_damage,
                  1, self.p1_round_count, holy_tuple_1)
            update_game_stats(self.p2_rogue_max_damage, self.p2_lancelot_max_damage, self.p2_master_max_damage,
                              1, self.p2_round_count, holy_tuple_2)
            update_game_stats(self.p1_rogue_max_damage, self.p1_lancelot_max_damage, self.p1_master_max_damage,
                              0, self.p1_round_count, holy_tuple_1)
            return_to_main_menu()
            del self.two_player
            del self.one_player
