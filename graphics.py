import pygame
import time
from sql_file import *
from turns import Battle


try:
    print(stage)
except NameError:
    pygame.init()
    username_color_active_1 = pygame.Color('lightskyblue3')
    username_color_passive_1 = pygame.Color('chartreuse4')
    password_color_active_1 = pygame.Color('lightskyblue3')
    password_color_passive_1 = pygame.Color('chartreuse4')
    username_color_1 = username_color_passive_1
    password_color_1 = password_color_passive_1
    username_color_active_2 = pygame.Color('lightskyblue3')
    username_color_passive_2 = pygame.Color('chartreuse4')
    password_color_active_2 = pygame.Color('lightskyblue3')
    password_color_passive_2 = pygame.Color('chartreuse4')
    username_color_2 = username_color_passive_2
    password_color_2 = password_color_passive_2
    screen = pygame.display.set_mode((1024, 640), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Deathmatch")
    running = True
    stage = "login_or_signup_1"
    screen.fill((0, 0, 0))
    image = pygame.image.load("images/loading_screen.jpg").convert()
    image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
    screen.blit(image, (0, 0))
    pygame.display.flip()
    pygame.time.wait(3000)
    screen.fill((0, 0, 0))
    pygame.display.flip()
    player_list = []
    holy_tuple_1 = ()
    holy_tuple_2 = ()
    dice_list = ["black", 20]
    username_active_1 = False
    password_active_1 = False
    username_active_2 = False
    password_active_2 = False
    battle = Battle()
    print(stage)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize font
font = pygame.font.Font(None, 40)


def return_to_main_menu():
    global battle
    del battle
    global stage
    stage = "main_menu"
    battle = Battle()


def display_battle_stats():
    # display text at the top of the screen for player 1's health attack and shield
    font = pygame.font.Font(None, 32)
    text = font.render(f"{battle.one_player.name}", 1, WHITE)
    text_rect = text.get_rect(center=(screen.get_width() * 0.5, screen.get_height() * 0.775))
    screen.blit(text, text_rect)
    text = font.render(f"Health: {battle.one_player.health}", 1, WHITE)
    text_rect = text.get_rect(center=(screen.get_width() * 0.5, screen.get_height() * 0.775 + 34))
    screen.blit(text, text_rect)
    text = font.render(f"Attack: {battle.one_player.attack + battle.one_player.drain_attack}", 1, WHITE)
    text_rect = text.get_rect(center=(screen.get_width() * 0.5, screen.get_height() * 0.775 + 68))
    screen.blit(text, text_rect)
    text = font.render(f"Shield: {battle.one_player.shielding}", 1, WHITE)
    text_rect = text.get_rect(center=(screen.get_width() * 0.5, screen.get_height() * 0.775 + 102))
    screen.blit(text, text_rect)
    text = font.render(f"Healing: {battle.one_player.healing}", 1, WHITE)
    text_rect = text.get_rect(center=(screen.get_width() * 0.5, screen.get_height() * 0.775 + 136))
    screen.blit(text, text_rect)

    # display text at the top of the screen for player 2's health attack and shield
    text = font.render(f"{battle.two_player.name}", 1, WHITE)
    text_rect = text.get_rect(center=(screen.get_width() * 0.5, screen.get_height() * 0.025))
    screen.blit(text, text_rect)
    text = font.render(f"Health: {battle.two_player.health}", 1, WHITE)
    text_rect = text.get_rect(center=(screen.get_width() * 0.5, screen.get_height() * 0.025 + 34))
    screen.blit(text, text_rect)
    text = font.render(f"Attack: {battle.two_player.attack + battle.two_player.drain_attack}", 1, WHITE)
    text_rect = text.get_rect(center=(screen.get_width() * 0.5, screen.get_height() * 0.025 + 68))
    screen.blit(text, text_rect)
    text = font.render(f"Shield: {battle.two_player.shielding}", 1, WHITE)
    text_rect = text.get_rect(center=(screen.get_width() * 0.5, screen.get_height() * 0.025 + 102))
    screen.blit(text, text_rect)
    text = font.render(f"Healing: {battle.two_player.healing}", 1, WHITE)
    text_rect = text.get_rect(center=(screen.get_width() * 0.5, screen.get_height() * 0.025 + 136))
    screen.blit(text, text_rect)


def display_player_dice(color="", number=0):
    if battle.current_player == battle.one_player:
        if color == "" and number == 0:
            image = pygame.image.load(f"images/{dice_list[0]}_dice/dice_ ({dice_list[1]}).png").convert()
            image = pygame.transform.scale(image, (screen.get_width() * 0.25, screen.get_height() * 0.25))
            screen.blit(image, (screen.get_width() * 0.75, screen.get_height() * 0.75))
        else:
            image = pygame.image.load(f"images/{color}_dice/dice_ ({number}).png").convert()
            image = pygame.transform.scale(image, (screen.get_width() * 0.25, screen.get_height() * 0.25))
            screen.blit(image, (screen.get_width() * 0.75, screen.get_height() * 0.75))
            dice_list[0] = color
            dice_list[1] = number
    else:
        if color == "" and number == 0:
            image = pygame.image.load(f"images/{dice_list[0]}_dice/dice_ ({dice_list[1]}).png").convert()
            image = pygame.transform.scale(image, (screen.get_width() * 0.25, screen.get_height() * 0.25))
            screen.blit(image, (screen.get_width() * 0.75, screen.get_height() * 0.75))
        else:
            image = pygame.image.load(f"images/{color}_dice/dice_ ({number}).png").convert()
            image = pygame.transform.scale(image, (screen.get_width() * 0.25, screen.get_height() * 0.25))
            screen.blit(image, (screen.get_width() * 0.75, screen.get_height() * 0.75))
            dice_list[0] = color
            dice_list[1] = number


# Function to display text on the screen
def display_text(tup):
    image = pygame.image.load("images/fight_bg.jpg").convert()
    image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
    screen.blit(image, (0, 0))

    image_character_1 = pygame.image.load(f"images/{battle.one_player.character}.jpg").convert()
    image_character_1 = pygame.transform.scale(image_character_1,
                                               (screen.get_width() * 0.225, screen.get_height() * 0.4))
    screen.blit(image_character_1, (0, screen.get_height() * 0.6))

    image_character_2 = pygame.image.load(f"images/{battle.two_player.character}.jpg").convert()
    image_character_2 = pygame.transform.scale(image_character_2,
                                               (screen.get_width() * 0.225, screen.get_height() * 0.4))
    screen.blit(image_character_2, (screen.get_width() * 0.775, 0))

    display_battle_stats()
    display_player_dice()

    text, pause = tup

    text = font.render(text, True, WHITE)
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)

    pygame.display.flip()
    time.sleep(pause)


# Function to create and manage buttons
def create_and_manage_buttons(buttons):
    image = pygame.image.load("images/fight_bg.jpg").convert()
    image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
    screen.blit(image, (0, 0))

    image_character_1 = pygame.image.load(f"images/{battle.one_player.character}.jpg").convert()
    image_character_1 = pygame.transform.scale(image_character_1,
                                               (screen.get_width() * 0.225, screen.get_height() * 0.4))
    screen.blit(image_character_1, (0, screen.get_height() * 0.6))

    image_character_2 = pygame.image.load(f"images/{battle.two_player.character}.jpg").convert()
    image_character_2 = pygame.transform.scale(image_character_2,
                                               (screen.get_width() * 0.225, screen.get_height() * 0.4))
    screen.blit(image_character_2, (screen.get_width() * 0.775, 0))

    display_battle_stats()
    display_player_dice()

    button_rects = []
    button_texts = []

    for button in buttons[:-1]:
        button_rect = pygame.Rect(screen.get_width() / 2 - 100, len(button_rects) * 60 + 225, 200, 50)
        button_rects.append(button_rect)

        if button == "blue":
            pygame.draw.rect(screen, BLUE, button_rect)
        elif button == "red":
            pygame.draw.rect(screen, RED, button_rect)
        elif button == "green":
            pygame.draw.rect(screen, GREEN, button_rect)
        else:
            pygame.draw.rect(screen, BLACK, button_rect)

        text = font.render(button.capitalize(), True, WHITE)
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)
        button_texts.append(button)

    if battle.current_player.character == "rogue":
        clicked_buttons = set()
    else:
        clicked_buttons = list()

    while len(clicked_buttons) < buttons[-1]:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button_rect in button_rects:
                    if button_rect.collidepoint(event.pos):
                        try:
                            clicked_buttons.add(button_texts[button_rects.index(button_rect)])
                        except:
                            clicked_buttons.append(button_texts[button_rects.index(button_rect)])

        pygame.display.flip()

        if len(clicked_buttons) == 2:
            break

    return list(clicked_buttons)


user_text_1 = ''
password_text_1 = ''
user_text_2 = ''
password_text_2 = ''

# Main game loop
while running:
    def game_loop():
        pass

        # Event handling


    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        elif event.type == pygame.KEYDOWN:
            if stage == "login_1":
                if username_active_1:
                    if event.key == pygame.K_BACKSPACE:
                        user_text_1 = user_text_1[:-1]

                    else:
                        user_text_1 += event.unicode
                elif password_active_1:
                    if event.key == pygame.K_BACKSPACE:
                        password_text_1 = password_text_1[:-1]

                    else:
                        password_text_1 += event.unicode
            elif stage == "login_2":
                if username_active_2:
                    if event.key == pygame.K_BACKSPACE:
                        user_text_2 = user_text_2[:-1]

                    else:
                        user_text_2 += event.unicode
                elif password_active_2:
                    if event.key == pygame.K_BACKSPACE:
                        password_text_2 = password_text_2[:-1]

                    else:
                        password_text_2 += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if stage == "login_or_signup_1":
                if button_rect_login_1.collidepoint(event.pos):
                    stage = "login_1"
                    screen.fill((0, 0, 0))
                elif button_rect_signup_1.collidepoint(event.pos):
                    stage = "signup_1"
                    screen.fill((0, 0, 0))
            elif stage == "login_1":
                if username_rect_1.collidepoint(event.pos):
                    username_active_1 = True
                    password_active_1 = False
                else:
                    username_active_1 = False
                if password_rect_1.collidepoint(event.pos):
                    password_active_1 = True
                    username_active_1 = False
                else:
                    password_active_1 = False
                if button_rect_login_1_submit.collidepoint(event.pos):
                    username_1 = user_text_1
                    password_1 = password_text_1
                    holy_tuple_1 = login(username_1, password_1)
                    if holy_tuple_1:
                        stage = "login_or_signup_2"
                    else:
                        screen.fill((0, 0, 0))
                        text = font.render("Incorrect username or password", True, WHITE)
                        text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
                        screen.blit(text, text_rect)
                        time.sleep(2)
                        pygame.display.flip()
                        stage = "login_1"
                    screen.fill((0, 0, 0))
                elif button_rect_login_1_return.collidepoint(event.pos):
                    stage = "login_or_signup_1"
                    screen.fill((0, 0, 0))
            elif stage == "signup_1":
                if username_rect_1.collidepoint(event.pos):
                    username_active_1 = True
                    password_active_1 = False
                else:
                    username_active_1 = False
                if password_rect_1.collidepoint(event.pos):
                    password_active_1 = True
                    username_active_1 = False
                else:
                    password_active_1 = False
                if button_rect_signup_1_submit.collidepoint(event.pos):
                    username_1 = user_text_1
                    password_1 = password_text_1
                    sign_up(username_1, password_1)
                    stage = "login_1"
                    screen.fill((0, 0, 0))
                elif button_rect_signup_1_return.collidepoint(event.pos):
                    stage = "login_or_signup_1"
                    screen.fill((0, 0, 0))
            elif stage == "login_or_signup_2":
                if button_rect_login_2.collidepoint(event.pos):
                    stage = "login_2"
                    screen.fill((0, 0, 0))
                elif button_rect_signup_2.collidepoint(event.pos):
                    stage = "signup_2"
                    screen.fill((0, 0, 0))
            elif stage == "login_2":
                if username_rect_2.collidepoint(event.pos):
                    username_active_2 = True
                    password_active_2 = False
                else:
                    username_active_2 = False
                if password_rect_2.collidepoint(event.pos):
                    password_active_2 = True
                    username_active_2 = False
                else:
                    password_active_2 = False
                if button_rect_login_2_submit.collidepoint(event.pos):
                    username_2 = user_text_2
                    password_2 = password_text_2
                    holy_tuple_2 = login(username_2, password_2)
                    if holy_tuple_2:
                        print(holy_tuple_1, holy_tuple_2)
                        stage = "main_menu"
                    else:
                        screen.fill((0, 0, 0))
                        text = font.render("Incorrect username or password", True, WHITE)
                        text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
                        screen.blit(text, text_rect)
                        time.sleep(2)
                        pygame.display.flip()
                        stage = "login_2"
                    screen.fill((0, 0, 0))
                elif button_rect_login_2_return.collidepoint(event.pos):
                    stage = "login_or_signup_2"
                    screen.fill((0, 0, 0))
            elif stage == "signup_2":
                if username_rect_2.collidepoint(event.pos):
                    username_active_2 = True
                    password_active_2 = False
                else:
                    username_active_2 = False
                if password_rect_2.collidepoint(event.pos):
                    password_active_2 = True
                    username_active_2 = False
                else:
                    password_active_2 = False
                if button_rect_signup_2_submit.collidepoint(event.pos):
                    username_2 = user_text_2
                    password_2 = password_text_2
                    sign_up(username_2, password_2)
                    stage = "login_2"
                    screen.fill((0, 0, 0))
                elif button_rect_signup_1_return.collidepoint(event.pos):
                    stage = "login_or_signup_2"
                    screen.fill((0, 0, 0))
            elif stage == "main_menu":
                player_list = []
                if button_rect_start.collidepoint(event.pos):
                    stage = "game1"
                    screen.fill((0, 0, 0))
                elif button_rect_info.collidepoint(event.pos):
                    stage = "info"
                    print(stage)
                    screen.fill((0, 0, 0))
                elif button_rect_master.collidepoint(event.pos):
                    stage = "stats"
                    screen.fill((0, 0, 0))

            elif stage.startswith("game") and stage != "game_loop":
                print(player_list)
                if button_rect_rogue.collidepoint(event.pos):
                    player_list.append("rogue")
                    screen.fill((0, 0, 0))
                    stage = "game2"
                elif button_rect_lancelot.collidepoint(event.pos):
                    player_list.append("lancelot")
                    screen.fill((0, 0, 0))
                    stage = "game2"
                elif button_rect_master.collidepoint(event.pos):
                    player_list.append("master")
                    screen.fill((0, 0, 0))
                    stage = "game2"
                if len(player_list) == 2:
                    print(battle)
                    battle.character_select(player_list[0], player_list[1])
                    stage = "game_loop"
                    battle.turns()

        elif stage == "stats":
            user_1_stats, user_2_stats = get_stats(((username_1, password_1), (username_2, password_2)))
            font = pygame.font.Font(None, 32)
            text = font.render("Player ID: " + str(user_1_stats[0]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.5, screen.get_height() * 0.05))
            screen.blit(text, text_rect)

            text = font.render("Username: " + str(user_1_stats[1]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.25, screen.get_height() * 0.15))
            screen.blit(text, text_rect)

            text = font.render("Number of Games: " + str(user_1_stats[3]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.25, screen.get_height() * 0.25))
            screen.blit(text, text_rect)

            text = font.render("Number of Wins: " + str(user_1_stats[4]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.25, screen.get_height() * 0.35))
            screen.blit(text, text_rect)

            text = font.render("Average Turns Per Game: " + str(user_1_stats[5]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.25, screen.get_height() * 0.45))
            screen.blit(text, text_rect)

            text = font.render("Max. Damage As Rogue: " + str(user_1_stats[6]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.75, screen.get_height() * 0.15))
            screen.blit(text, text_rect)

            text = font.render("Max. Damage As Lancelot: " + str(user_1_stats[7]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.75, screen.get_height() * 0.25))
            screen.blit(text, text_rect)

            text = font.render("Max. Damage As Master: " + str(user_1_stats[8]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.75, screen.get_height() * 0.35))
            screen.blit(text, text_rect)

            text = font.render("Max. Win Streak: " + str(user_1_stats[9]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.75, screen.get_height() * 0.45))
            screen.blit(text, text_rect)

            text = font.render("Player ID: " + str(user_2_stats[0]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.5, screen.get_height() * 0.55))
            screen.blit(text, text_rect)

            text = font.render("Username: " + str(user_2_stats[1]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.25, screen.get_height() * 0.65))
            screen.blit(text, text_rect)

            text = font.render("Number of Games: " + str(user_2_stats[3]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.25, screen.get_height() * 0.75))
            screen.blit(text, text_rect)

            text = font.render("Number of Wins: " + str(user_2_stats[4]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.25, screen.get_height() * 0.85))
            screen.blit(text, text_rect)

            text = font.render("Average Turns Per Game: " + str(user_2_stats[5]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.25, screen.get_height() * 0.95))
            screen.blit(text, text_rect)

            text = font.render("Max. Damage As Rogue: " + str(user_2_stats[6]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.75, screen.get_height() * 0.65))
            screen.blit(text, text_rect)

            text = font.render("Max. Damage As Lancelot: " + str(user_2_stats[7]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.75, screen.get_height() * 0.75))
            screen.blit(text, text_rect)

            text = font.render("Max. Damage As Master: " + str(user_2_stats[8]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.75, screen.get_height() * 0.85))
            screen.blit(text, text_rect)

            text = font.render("Max. Win Streak: " + str(user_2_stats[9]), True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() * 0.75, screen.get_height() * 0.95))
            screen.blit(text, text_rect)

            pygame.display.flip()

        elif stage == "login_or_signup_1":
            font = pygame.font.Font(None, 40)
            text = font.render("Player One", True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 200))
            screen.blit(text, text_rect)

            # two buttons one for login and one for signup
            font = pygame.font.Font(None, 32)
            button_rect_login_1 = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 100, 200, 50)
            pygame.draw.rect(screen, WHITE, button_rect_login_1, 0, 9)
            text = font.render("Login", True, BLACK)
            text_rect = text.get_rect(center=button_rect_login_1.center)
            screen.blit(text, text_rect)

            button_rect_signup_1 = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 50, 200, 50)
            pygame.draw.rect(screen, WHITE, button_rect_signup_1, 0, 9)
            text = font.render("Signup", True, BLACK)
            text_rect = text.get_rect(center=button_rect_signup_1.center)
            screen.blit(text, text_rect)

            pygame.display.flip()

        elif stage == "login_1":
            username_rect_1 = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 150, 200, 50)
            password_rect_1 = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 50, 200, 50)
            pygame.draw.rect(screen, username_color_1, username_rect_1)
            text_surface = font.render(user_text_1, True, (255, 255, 255))

            # render at position stated in arguments
            screen.blit(text_surface, (username_rect_1.x + 5, username_rect_1.y + 5))
            username_rect_1.w = max(100, text_surface.get_width() + 10)
            if username_active_1:
                username_color_1 = username_color_active_1
                password_color_1 = password_color_passive_1
            else:
                username_color_1 = username_color_passive_1
            pygame.display.flip()

            pygame.draw.rect(screen, password_color_1, password_rect_1)
            text_surface = font.render(password_text_1, True, (255, 255, 255))

            # render at position stated in arguments
            screen.blit(text_surface, (password_rect_1.x + 5, password_rect_1.y + 5))
            password_rect_1.w = max(100, text_surface.get_width() + 10)
            if password_active_1:
                password_color_1 = password_color_active_1
                username_color_1 = username_color_passive_1
            else:
                password_color_1 = password_color_passive_1
            pygame.display.flip()

            # make a button to submit
            button_rect_login_1_submit = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 75, 200,
                                                     50)
            pygame.draw.rect(screen, WHITE, button_rect_login_1_submit, 0, 9)
            text = font.render("Submit", True, BLACK)
            text_rect = text.get_rect(center=button_rect_login_1_submit.center)
            screen.blit(text, text_rect)

            # make another button to return to login_or_signup_1
            button_rect_login_1_return = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 175, 200,
                                                     50)
            pygame.draw.rect(screen, WHITE, button_rect_login_1_return, 0, 9)
            text = font.render("Return", True, BLACK)
            text_rect = text.get_rect(center=button_rect_login_1_return.center)
            screen.blit(text, text_rect)
            pygame.display.flip()

        elif stage == "signup_1":
            username_rect_1 = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 150, 200, 50)
            password_rect_1 = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 50, 200, 50)
            pygame.draw.rect(screen, username_color_1, username_rect_1)
            text_surface = font.render(user_text_1, True, (255, 255, 255))

            # render at position stated in arguments
            screen.blit(text_surface, (username_rect_1.x + 5, username_rect_1.y + 5))
            username_rect_1.w = max(100, text_surface.get_width() + 10)
            if username_active_1:
                username_color_1 = username_color_active_1
                password_color_1 = password_color_passive_1
            else:
                username_color_1 = username_color_passive_1
            pygame.display.flip()

            pygame.draw.rect(screen, password_color_1, password_rect_1)
            text_surface = font.render(password_text_1, True, (255, 255, 255))

            # render at position stated in arguments
            screen.blit(text_surface, (password_rect_1.x + 5, password_rect_1.y + 5))
            password_rect_1.w = max(100, text_surface.get_width() + 10)
            if password_active_1:
                password_color_1 = password_color_active_1
                username_color_1 = username_color_passive_1
            else:
                password_color_1 = password_color_passive_1
            pygame.display.flip()

            # make a button to submit
            button_rect_signup_1_submit = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 75, 200,
                                                      50)
            pygame.draw.rect(screen, WHITE, button_rect_signup_1_submit, 0, 9)
            text = font.render("Submit", True, BLACK)
            text_rect = text.get_rect(center=button_rect_signup_1_submit.center)
            screen.blit(text, text_rect)

            # make another button to return to login_or_signup_1
            button_rect_signup_1_return = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 175, 200,
                                                      50)
            pygame.draw.rect(screen, WHITE, button_rect_signup_1_return, 0, 9)
            text = font.render("Return", True, BLACK)
            text_rect = text.get_rect(center=button_rect_signup_1_return.center)
            screen.blit(text, text_rect)
            pygame.display.flip()

        elif stage == "login_or_signup_2":
            font = pygame.font.Font(None, 40)
            text = font.render("Player Two", True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 200))
            screen.blit(text, text_rect)

            # two buttons one for login and one for signup
            font = pygame.font.Font(None, 32)
            button_rect_login_2 = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 100, 200, 50)
            pygame.draw.rect(screen, WHITE, button_rect_login_2, 0, 9)
            text = font.render("Login", True, BLACK)
            text_rect = text.get_rect(center=button_rect_login_2.center)
            screen.blit(text, text_rect)

            button_rect_signup_2 = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 50, 200, 50)
            pygame.draw.rect(screen, WHITE, button_rect_signup_2, 0, 9)
            text = font.render("Signup", True, BLACK)
            text_rect = text.get_rect(center=button_rect_signup_2.center)
            screen.blit(text, text_rect)

            pygame.display.flip()

        elif stage == "login_2":
            username_rect_2 = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 150, 200, 50)
            password_rect_2 = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 50, 200, 50)
            pygame.draw.rect(screen, username_color_2, username_rect_2)
            text_surface = font.render(user_text_2, True, (255, 255, 255))

            # render at position stated in arguments
            screen.blit(text_surface, (username_rect_2.x + 5, username_rect_2.y + 5))
            username_rect_2.w = max(100, text_surface.get_width() + 10)
            if username_active_2:
                username_color_2 = username_color_active_2
                password_color_2 = password_color_passive_2
            else:
                username_color_2 = username_color_passive_2
            pygame.display.flip()

            pygame.draw.rect(screen, password_color_2, password_rect_2)
            text_surface = font.render(password_text_2, True, (255, 255, 255))

            # render at position stated in arguments
            screen.blit(text_surface, (password_rect_2.x + 5, password_rect_2.y + 5))
            password_rect_2.w = max(100, text_surface.get_width() + 10)
            if password_active_2:
                password_color_2 = password_color_active_2
                username_color_2 = username_color_passive_2
            else:
                password_color_2 = password_color_passive_2
            pygame.display.flip()

            # make a button to submit
            button_rect_login_2_submit = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 75, 200,
                                                     50)
            pygame.draw.rect(screen, WHITE, button_rect_login_2_submit, 0, 9)
            text = font.render("Submit", True, BLACK)
            text_rect = text.get_rect(center=button_rect_login_2_submit.center)
            screen.blit(text, text_rect)

            # make another button to return to login_or_signup_2
            button_rect_login_2_return = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 175, 200,
                                                     50)
            pygame.draw.rect(screen, WHITE, button_rect_login_2_return, 0, 9)
            text = font.render("Return", True, BLACK)
            text_rect = text.get_rect(center=button_rect_login_2_return.center)
            screen.blit(text, text_rect)
            pygame.display.flip()

        elif stage == "signup_2":
            username_rect_2 = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 150, 200, 50)
            password_rect_2 = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 50, 200, 50)
            pygame.draw.rect(screen, username_color_2, username_rect_2)
            text_surface = font.render(user_text_2, True, (255, 255, 255))

            # render at position stated in arguments
            screen.blit(text_surface, (username_rect_2.x + 5, username_rect_2.y + 5))
            username_rect_2.w = max(100, text_surface.get_width() + 10)
            if username_active_2:
                username_color_2 = username_color_active_2
                password_color_2 = password_color_passive_2
            else:
                username_color_2 = username_color_passive_2
            pygame.display.flip()

            pygame.draw.rect(screen, password_color_2, password_rect_2)
            text_surface = font.render(password_text_2, True, (255, 255, 255))

            # render at position stated in arguments
            screen.blit(text_surface, (password_rect_2.x + 5, password_rect_2.y + 5))
            password_rect_2.w = max(100, text_surface.get_width() + 10)
            if password_active_2:
                password_color_2 = password_color_active_2
                username_color_2 = username_color_passive_2
            else:
                password_color_2 = password_color_passive_2
            pygame.display.flip()

            # make a button to submit
            button_rect_signup_2_submit = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 75, 200,
                                                      50)
            pygame.draw.rect(screen, WHITE, button_rect_signup_2_submit, 0, 9)
            text = font.render("Submit", True, BLACK)
            text_rect = text.get_rect(center=button_rect_signup_2_submit.center)
            screen.blit(text, text_rect)

            # make another button to return to login_or_signup_2
            button_rect_signup_2_return = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 175, 200,
                                                      50)
            pygame.draw.rect(screen, WHITE, button_rect_signup_2_return, 0, 9)
            text = font.render("Return", True, BLACK)
            text_rect = text.get_rect(center=button_rect_signup_2_return.center)
            screen.blit(text, text_rect)
            pygame.display.flip()

        elif stage == "main_menu":
            image = pygame.image.load("images/main_menu_background.jpg").convert()
            image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
            screen.blit(image, (0, 0))
            pygame.display.flip()
            font = pygame.font.Font(None, 40)

            button_rect_start = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 100, 200, 50)
            pygame.draw.rect(screen, RED, button_rect_start, 0, 9)
            text = font.render("Start Game", True, BLACK)
            text_rect = text.get_rect(center=button_rect_start.center)
            screen.blit(text, text_rect)

            button_rect_info = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 25, 200, 50)
            pygame.draw.rect(screen, GREEN, button_rect_info, 0, 9)
            text = font.render("How To Play", True, BLACK)
            text_rect = text.get_rect(center=button_rect_info.center)
            screen.blit(text, text_rect)

            button_rect_master = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 50, 200, 50)
            pygame.draw.rect(screen, BLUE, button_rect_master, 0, 9)
            text = font.render("Statistics", True, BLACK)
            text_rect = text.get_rect(center=button_rect_master.center)
            screen.blit(text, text_rect)

            pygame.display.update([button_rect_start, button_rect_info, button_rect_master])

        elif stage == "game1":
            image = pygame.image.load("images/main_menu_background.jpg").convert()
            image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
            screen.blit(image, (0, 0))
            pygame.display.flip()
            font = pygame.font.Font(None, 40)

            text = font.render(f"{username_1}: Choose your character", 1, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 150))
            screen.blit(text, text_rect)

            button_rect_rogue = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 75, 200, 50)
            pygame.draw.rect(screen, RED, button_rect_rogue, 0, 9)
            text = font.render("Rogue", True, BLACK)
            text_rect = text.get_rect(center=button_rect_rogue.center)
            screen.blit(text, text_rect)

            button_rect_lancelot = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 0, 200, 50)
            pygame.draw.rect(screen, BLUE, button_rect_lancelot, 0, 9)
            text = font.render("Lancelot", True, BLACK)
            text_rect = text.get_rect(center=button_rect_lancelot.center)
            screen.blit(text, text_rect)

            button_rect_master = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 75, 200, 50)
            pygame.draw.rect(screen, GREEN, button_rect_master, 0, 9)
            text = font.render("Master", True, BLACK)
            text_rect = text.get_rect(center=button_rect_master.center)
            screen.blit(text, text_rect)

            pygame.display.flip()

        elif stage == "game2":
            image = pygame.image.load("images/main_menu_background.jpg").convert()
            image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
            screen.blit(image, (0, 0))
            pygame.display.flip()
            font = pygame.font.Font(None, 40)

            text = font.render(f"{username_2}: Choose your character", 1, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 150))
            screen.blit(text, text_rect)

            button_rect_rogue = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 75, 200, 50)
            pygame.draw.rect(screen, RED, button_rect_rogue, 0, 9)
            text = font.render("Rogue", True, BLACK)
            text_rect = text.get_rect(center=button_rect_rogue.center)
            screen.blit(text, text_rect)

            button_rect_lancelot = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 - 0, 200, 50)
            pygame.draw.rect(screen, BLUE, button_rect_lancelot, 0, 9)
            text = font.render("Lancelot", True, BLACK)
            text_rect = text.get_rect(center=button_rect_lancelot.center)
            screen.blit(text, text_rect)

            button_rect_master = pygame.Rect(screen.get_width() / 2 - 100, screen.get_height() / 2 + 75, 200, 50)
            pygame.draw.rect(screen, GREEN, button_rect_master, 0, 9)
            text = font.render("Master", True, BLACK)
            text_rect = text.get_rect(center=button_rect_master.center)
            screen.blit(text, text_rect)

            pygame.display.flip()

        elif stage == "game_loop":
            image = pygame.image.load("images/fight_bg.jpg").convert()
            image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
            screen.blit(image, (0, 0))

            image_character_1 = pygame.image.load(f"images/{battle.one_player.character}.jpg").convert()
            image_character_1 = pygame.transform.scale(image_character_1,
                                                       (screen.get_width() * 0.225, screen.get_height() * 0.4))
            screen.blit(image_character_1, (0, screen.get_height() * 0.6))

            image_character_2 = pygame.image.load(f"images/{battle.two_player.character}.jpg").convert()
            image_character_2 = pygame.transform.scale(image_character_2,
                                                       (screen.get_width() * 0.225, screen.get_height() * 0.4))
            screen.blit(image_character_2, (screen.get_width() * 0.775, 0))

            display_battle_stats()

            pygame.display.flip()

        clock.tick(60)

# Quit Pygame
pygame.quit()
