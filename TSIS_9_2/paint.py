# Paint
import pygame, random


# (x1, y1), (x2, y2)
# A = y2 - y1
# B = x1 - x2
# C = x2 * y1 - x1 * y2
# Ax + By + C = 0
# (x - x1) / (x2 - x1) = (y - y1) / (y2 - y1)

def drawLine(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)


def drawEllipse(screen, x1, y1, x2, y2, color, radius):
    if x1 >= x2 and y1 >= y2:
        pygame.draw.ellipse(screen, color, (x2, y2, x1 - x2, y1 - y2), radius)
    if x2 >= x1 and y2 >= y1:
        pygame.draw.ellipse(screen, color, (x1, y1, x2 - x1, y2 - y1), radius)
    if x2 >= x1 and y1 >= y2:
        pygame.draw.ellipse(screen, color, (x1, y2, x2 - x1, y1 - y2), radius)
    if x1 >= x2 and y2 >= y1:
        pygame.draw.ellipse(screen, color, (x2, y1, x1 - x2, y2 - y1), radius)


def main():
    screen = pygame.display.set_mode((800, 600))
    mode = 'random'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 1

    #tools
    circle = False
    rectangle = False
    pen = True
    eraser = False
    selection = False


    #stating colors
    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0)
    }

    #initial coordinates of mouse
    x1 = 0
    y1 = 0

    #surface for gradient tool
    surf = pygame.Surface((256, 256))
    image = pygame.image.load("selection.jpg")
    surf.blit(image, (0, 0))
    screen.blit(surf, (0, 0))

    while True:
        surf.blit(image, (0, 0))
        screen.blit(surf, (0, 0))

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Hotkeys:
            #Exit by a Hotkey
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return

                #Selecting colors by a hotkey
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_g:
                    mode = 'green'

                #Radius of a pixel
                if event.key == pygame.K_UP:
                    radius += 1
                if event.key == pygame.K_DOWN:
                    radius -= 1

                #Hotkeys for tools
                if event.key == pygame.K_p:
                    pen = True
                    circle = False
                    rectangle = False
                    eraser = False
                    selection = False
                if event.key == pygame.K_c:
                    circle = True
                    pen = False
                    rectangle = False
                    eraser = False
                    selection = False
                if event.key == pygame.K_t:
                    rectangle = True
                    pen = False
                    circle = False
                    eraser = False
                    selection = False
                if event.key == pygame.K_e:
                    eraser = True
                    pen = False
                    circle = False
                    rectangle = False
                    selection = False
                if event.key == pygame.K_s:
                    selection = True
                    pen = False
                    circle = False
                    rectangle = False
                    eraser = False
                if event.key == pygame.K_SPACE:
                    pygame.image.save(screen, "save.png")

            #Random Color
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if mode == 'random':
                #     color = (random.randrange(256), random.randrange(256), random.randrange(256))
                # else:
                #     color = colors[mode]
                if selection:
                    print(screen.get_at(event.pos))
                    selected_color = (screen.get_at(event.pos))
                    color = (selected_color[0], selected_color[1], selected_color[2])

                if pen:
                    pygame.draw.circle(screen, color, event.pos, radius)
                    draw_on = True

                if eraser:
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)
                    draw_on = True

                if rectangle or circle:
                    x1 = event.pos[0]
                    y1 = event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                draw_on = False
                if rectangle:
                    pygame.draw.rect(screen, color, (x1, y1, event.pos[0] - x1, event.pos[1] - y1), radius)
                if circle:
                    drawEllipse(screen, x1, y1, event.pos[0], event.pos[1], color, radius)

            if event.type == pygame.MOUSEMOTION:
                if draw_on and pen:
                    drawLine(screen, last_pos, event.pos, radius, color)
                    # pygame.draw.circle(screen, color, event.pos, radius)
                if draw_on and eraser:
                    drawLine(screen, last_pos, event.pos, radius, (0, 0, 0))
                    # pygame.draw.circle(screen, color, event.pos, radius)
                last_pos = event.pos
        pygame.display.flip()

pygame.quit()

main()