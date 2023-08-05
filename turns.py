from rogue import *
from lancelot import *
from master import *
import time

print("WELCOME TO DEATHMATCH!")
time.sleep(1)
player1 = input("Enter Player 1 name: ")
time.sleep(0.5)
player2 = input("Enter Player 2 name: ")
time.sleep(0.5)


def cs(player1, player2):
    print("CHARACTERS:", "ROGUE", "difficulty: 1", "LANCELOT", "difficulty: 2", "MASTER", "difficulty: 3", sep="\n")
    cs1 = input(f"{player1} character select: ").lower()
    if cs1 != "rogue" and cs1 != "lancelot" and cs1 != "master":
        print("You may only choose a character from the list given")
        cs(player1, player2)
    cs2 = input(f"{player2} character select: ").lower()
    if cs2 != "rogue" and cs2 != "lancelot" and cs2 != "master":
        print("You may only choose a character from the list given")
        cs(player1, player2)
    return cs1, cs2


cs1, cs2 = cs(player1, player2)

if cs1 == "rogue":
    one_player = Rogue(player1)
elif cs1 == "lancelot":
    one_player = Lancelot(player1)
elif cs1 == "master":
    one_player = Master(player1)

if cs2 == "rogue":
    two_player = Rogue(player2)
elif cs2 == "lancelot":
    two_player = Lancelot(player2)
elif cs2 == "master":
    two_player = Master(player2)

print("FLIPPING A COIN...")
time.sleep(1.5)
if one_player.max_health > two_player.max_health:
    one_player, two_player = two_player, one_player
    print(f"TAILS! {player2} starts first!")
elif one_player.max_health == two_player.max_health:
    coin_flip = random.choice([f"HEADS! {player1} starts first!", f"TAILS! {player2} starts first!"])
    print(coin_flip)
    if "TAILS!" in coin_flip:
        one_player, two_player = two_player, one_player
else:
    print(f"HEADS! {player1} starts first!")


def calculation(one_player, two_player):
    if one_player.preservation_trigger:
        if two_player.attack > 75:
            two_player.attack = 75
            two_player.burn = two_player.burn.clear()
            two_player.bleed = two_player.bleed.clear()
            two_player.poison = two_player.poison.clear()
            two_player.stun = False
            two_player.temporary_attack_decrease = 0
            two_player.temporary_defence_decrease = 0
            two_player.temporary_healing_decrease = 0
    if not two_player.stun and not one_player.dodge_trigger:
        print(f"{one_player.name}'s turn!")
        one_player.choose_die()
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
    one_player.health += one_player.healing
    for i in two_player.burn:
        two_player.attack += i[0]
    for i in two_player.bleed:
        two_player.attack += i[0]
    for i in two_player.poison:
        two_player.attack += i[0]
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
        two_player.drain_attack = 0
    one_player.enemy_attack = 0
    two_player.enemy_attack = one_player.attack
    one_player.is_enemy_attacking = False
    one_player.shielding = 0
    one_player.healing = 0
    if one_player.health > one_player.max_health:
        one_player.health = one_player.max_health
    if not one_player.dodge_trigger and not one_player.stun:
        print(f"Health of {two_player.name}: {two_player.health}/{two_player.max_health}")
        print(f"Health of {one_player.name}: {one_player.health}/{one_player.max_health}")
    if one_player.dodge_trigger:
        one_player.dodge_trigger = False
    if two_player.stun_duration == 0:
        two_player.stun = False
    if one_player.attack > 0:
        two_player.is_enemy_attacking = True
    two_player.reset_cooldowns()


def turns(one_player, two_player):
    player = two_player
    while one_player.health > 0 and two_player.health > 0:
        if player == two_player:
            player = one_player
        calculation(one_player, two_player)
        x = one_player
        one_player = two_player
        two_player = x
        calculation(one_player, two_player)
        x = two_player
        two_player = one_player
        one_player = x

    if one_player.health > two_player.health:
        print(f"{one_player.name.upper()} WINS!")
    else:
        print(f"{two_player.name.upper()} WINS!")


turns(one_player, two_player)
