import pygame as pg

# КОНСТАНТЫ
SIZE = (900, 900)
FPS = 60
CELLS = (
    pg.Rect(0, 0, 300, 300), pg.Rect(300, 0, 300, 300), pg.Rect(600, 0, 300, 300),
    pg.Rect(0, 300, 300, 300), pg.Rect(300, 300, 300, 300), pg.Rect(600, 300, 300, 300),
    pg.Rect(0, 600, 300, 300), pg.Rect(300, 600, 300, 300), pg.Rect(600, 600, 300, 300)
)

LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (6, 4, 2), (0, 4, 8)
)


# Главная функция
def main() -> None:
    # загружаем звук
    pg.mixer.init()
    dog_sound = pg.mixer.Sound('лай собаки.mp3')
    dog_sound.set_volume(0.45)

    pg.display.set_caption('X_O')
    # загрузить картинку
    dog = pg.image.load('собака БАРАБАКА.jpg')

    # изменить размер
    dog = pg.transform.scale(dog, SIZE)
    clock = pg.time.Clock()
    screen = pg.display.set_mode(SIZE)
    draw(screen, dog)

    # содержимое клеточек
    cell_contents = ['', '', '',
                     '', '', '',
                     '', '', '']
    main_loop(cell_contents, screen, clock, dog_sound)


def main_loop(cell_contents, screen, clock, dog_sound):
    running = True
    active_player = 'X'
    while running:
        # обработать события
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                cell_number = get_rect_number(mouse_pos)
                if cell_contents[cell_number] == '':
                    if active_player == 'X':
                        # рисуем крестик
                        draw_x(cell_number, screen, cell_contents)
                        # переход хода
                        active_player = 'O'
                    else:
                        draw_o(cell_number, screen, cell_contents)
                        active_player = 'X'
                    dog_sound.play()
                    # проверяем победу
                    for line in LINES:
                        if (cell_contents[line[0]] == cell_contents[line[1]] == cell_contents[line[2]] and
                                cell_contents[line[2]] != ''):
                            running = False
                            break
        clock.tick(FPS)


def draw_x(cell_number, screen, cell_contents):
    cell = CELLS[cell_number]
    start = cell.topleft
    end = cell.bottomright
    pg.draw.line(screen, 'red', start, end, 15)
    two_start = cell.topright
    two_end = cell.bottomleft
    pg.draw.line(screen, 'red', two_start, two_end, 15)
    draw_cells(screen)
    pg.display.flip()
    cell_contents[cell_number] = 'X'


def draw_o(cell_number, screen, cell_contents):
    cell = CELLS[cell_number]
    pg.draw.circle(screen, 'blue', cell.center, 125, 15)
    pg.display.flip()
    cell_contents[cell_number] = 'O'


# функция рисование

def draw(screen, dog):
    screen.fill('red')
    screen.blit(dog, (0, 0))
    draw_cells(screen)
    pg.display.flip()


def draw_cells(screen):
    for cell in CELLS:
        pg.draw.rect(screen, 'black', cell, 25)


def get_rect_number(mouse_pos):
    # ДОЛЖНА ВОЗВРАЩАТЬ ИНДЕКС КЛЕТОЧКИ ИЗ СПИСКА CELLS ПО ПОЗИЦИИ МЫШКи
    x = mouse_pos[0]
    y = mouse_pos[1]
    # как определить столбик
    if 300 > x > 0:
        # 1 столбик
        if 300 > y > 0:
            return 0
        elif 600 > y > 300:
            return 3
        elif 900 > y > 600:
            return 6
    elif 600 > x > 300:
        #  2 столбик
        if 300 > y > 0:
            return 1
        elif 600 > y > 300:
            return 4
        elif 900 > y > 600:
            return 7
    elif 900 > x > 600:
        # 3 столбик
        if 300 > y > 0:
            return 2
        elif 600 > y > 300:
            return 5
        elif 900 > y > 600:
            return 8


#     active_player = ('X, O')
#     if active_player == f'X':  # если  активный игрок = х
#     active_player = f'O'  # меняем переменную на о
#     else :
#     # а если нет то
#     active_player = f'X'  # меняем переменную на х
# cell = [ [300,300], [300,600], [300,900],
#          [600,300], [600,600], [600,900],
#          [900,300], [900,600], [900,900]]
# active_player =
# Вход в программу
main()
