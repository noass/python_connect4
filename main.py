import pygame

pygame.init()
font = pygame.font.Font("Roboto.ttf", 30)
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Python Connect 4")
clock = pygame.time.Clock()
running = True
won = False

rows, cols = (6, 7)
grid = [[0 for i in range(cols)] for j in range(rows)]

cursor_location = 0
player_turn = "red"
red_won = False
yellow_won = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if cursor_location >= 0 and cursor_location <= 6:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    for j in range(rows):
                        for i in range(cols):
                            grid[j][i] = 0
                    won = False
                    red_won = False
                    yellow_won = False
                    cursor_location = 0
                    player_turn = "red"
                    print("reset")
                if event.key == pygame.K_LEFT and not won:
                    cursor_location -= 1
                elif event.key == pygame.K_RIGHT and not won:
                    cursor_location += 1
                elif event.key == pygame.K_SPACE and not won:
                    for j in range(rows-1, -1, -1):
                        if grid[j][cursor_location] == 0:
                            if player_turn == "red":
                                grid[j][cursor_location] = 1
                                player_turn = "yellow"
                            else:
                                grid[j][cursor_location] = 2
                                player_turn = "red"
                            break
                    for j in range(rows):
                        for i in range(cols - 3):
                            # Horizontal check (already exists)
                            if grid[j][i] == 1 and grid[j][i+1] == 1 and grid[j][i+2] == 1 and grid[j][i+3] == 1:
                                print("Red wins!")
                                won = True
                                red_won = True
                            elif grid[j][i] == 2 and grid[j][i+1] == 2 and grid[j][i+2] == 2 and grid[j][i+3] == 2:
                                print("Yellow wins!")
                                won = True
                                yellow_won = True

                    for j in range(rows - 3):
                        for i in range(cols):
                            # Vertical check
                            if grid[j][i] == 1 and grid[j+1][i] == 1 and grid[j+2][i] == 1 and grid[j+3][i] == 1:
                                print("Red wins!")
                                won = True
                                red_won = True
                            elif grid[j][i] == 2 and grid[j+1][i] == 2 and grid[j+2][i] == 2 and grid[j+3][i] == 2:
                                print("Yellow wins!")
                                won = True
                                yellow_won = True

                    # Diagonal checks
                    for j in range(rows - 3):
                        for i in range(cols - 3):
                            # Diagonal check: positive slope (top-left to bottom-right)
                            if grid[j][i] == 1 and grid[j+1][i+1] == 1 and grid[j+2][i+2] == 1 and grid[j+3][i+3] == 1:
                                print("Red wins!")
                                won = True
                                red_won = True
                            elif grid[j][i] == 2 and grid[j+1][i+1] == 2 and grid[j+2][i+2] == 2 and grid[j+3][i+3] == 2:
                                print("Yellow wins!")
                                won = True
                                yellow_won = True

                    for j in range(3, rows):
                        for i in range(cols - 3):
                            # Diagonal check: negative slope (bottom-left to top-right)
                            if grid[j][i] == 1 and grid[j-1][i+1] == 1 and grid[j-2][i+2] == 1 and grid[j-3][i+3] == 1:
                                print("Red wins!")
                                won = True
                                red_won = True
                            elif grid[j][i] == 2 and grid[j-1][i+1] == 2 and grid[j-2][i+2] == 2 and grid[j-3][i+3] == 2:
                                print("Yellow wins!")
                                won = True
                                yellow_won = True

                    print()
                    for row in grid:
                        print(row)
                                    
    screen.fill("black")
    
    if red_won:
        text_surface = font.render("Red won!", True, (255, 0, 0))
        screen.blit(text_surface, (10, 10))
        text_surface = font.render("Press R to restart!", True, (255, 255, 255))
        screen.blit(text_surface, (10, 50))
    elif yellow_won:
        text_surface = font.render("Yellow won!", True, (255, 255, 0))
        screen.blit(text_surface, (10, 10))
        text_surface = font.render("Press R to restart!", True, (255, 255, 255))
        screen.blit(text_surface, (10, 50))
    
    if cursor_location < 0:
        cursor_location = 0
    elif cursor_location > 6:
        cursor_location = 6
    
    if cursor_location == 0:
        pygame.draw.polygon(screen, player_turn, [[35+pygame.Surface.get_width(screen)/3-35, (35+pygame.Surface.get_width(screen)/3-35)-250], [35+pygame.Surface.get_width(screen)/3-35 - 28, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250], [35+pygame.Surface.get_width(screen)/3-35 + 28, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250]])
    elif cursor_location == 1:
        pygame.draw.polygon(screen, player_turn, [[(35+pygame.Surface.get_width(screen)/3-35)+70, (35+pygame.Surface.get_width(screen)/3-35)-250], [(35+pygame.Surface.get_width(screen)/3-35 - 28)+70, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250], [(35+pygame.Surface.get_width(screen)/3-35 + 28)+70, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250]])
    elif cursor_location == 2:
        pygame.draw.polygon(screen, player_turn, [[(35+pygame.Surface.get_width(screen)/3-35)+105*1.35, (35+pygame.Surface.get_width(screen)/3-35)-250], [(35+pygame.Surface.get_width(screen)/3-35 - 28)+105*1.35, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250], [(35+pygame.Surface.get_width(screen)/3-35 + 28)+105*1.35, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250]])
    elif cursor_location == 3:
        pygame.draw.polygon(screen, player_turn, [[(35+pygame.Surface.get_width(screen)/3-35)+140*1.50, (35+pygame.Surface.get_width(screen)/3-35)-250], [(35+pygame.Surface.get_width(screen)/3-35 - 28)+140*1.50, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250], [(35+pygame.Surface.get_width(screen)/3-35 + 28)+140*1.50, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250]])
    elif cursor_location == 4:
        pygame.draw.polygon(screen, player_turn, [[(35+pygame.Surface.get_width(screen)/3-35)+175*1.60, (35+pygame.Surface.get_width(screen)/3-35)-250], [(35+pygame.Surface.get_width(screen)/3-35 - 28)+175*1.60, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250], [(35+pygame.Surface.get_width(screen)/3-35 + 28)+175*1.60, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250]])
    elif cursor_location == 5:
        pygame.draw.polygon(screen, player_turn, [[(35+pygame.Surface.get_width(screen)/3-35)+210*1.66, (35+pygame.Surface.get_width(screen)/3-35)-250], [(35+pygame.Surface.get_width(screen)/3-35 - 28)+210*1.66, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250], [(35+pygame.Surface.get_width(screen)/3-35 + 28)+210*1.66, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250]])
    elif cursor_location == 6:
        pygame.draw.polygon(screen, player_turn, [[(35+pygame.Surface.get_width(screen)/3-35)+245*1.71, (35+pygame.Surface.get_width(screen)/3-35)-250], [(35+pygame.Surface.get_width(screen)/3-35 - 28)+245*1.71, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250], [(35+pygame.Surface.get_width(screen)/3-35 + 28)+245*1.71, (35+pygame.Surface.get_width(screen)/3-35 - 35)-250]])
    
    for i in range(cols):
        for j in range(rows):
            if grid[j][i] == 1:
                pygame.draw.circle(screen, "red", (i*35*2+pygame.Surface.get_width(screen)/3, j*35*2+pygame.Surface.get_height(screen)/3), 35)
                pygame.draw.rect(screen, "blue", (i*35*2+pygame.Surface.get_width(screen)/3-35, j*35*2+pygame.Surface.get_height(screen)/3-35, 35*2, 35*2), width=4)
            elif grid[j][i] == 2:
                pygame.draw.circle(screen, "yellow", (i*35*2+pygame.Surface.get_width(screen)/3, j*35*2+pygame.Surface.get_height(screen)/3), 35)
                pygame.draw.rect(screen, "blue", (i*35*2+pygame.Surface.get_width(screen)/3-35, j*35*2+pygame.Surface.get_height(screen)/3-35, 35*2, 35*2), width=4)
            else:
                pygame.draw.rect(screen, "blue", (i*35*2+pygame.Surface.get_width(screen)/3-35, j*35*2+pygame.Surface.get_height(screen)/3-35, 35*2, 35*2), width=4)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()