# -*- coding: utf-8 -*-
from unit import unit
import pygame, random
from pygame import *

WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "white"#"#004400"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

class battle:
    def __init__(self):
        self.units = []

    def add_unit(self, x, y):
        self.units.append(unit(x, y))
        return 0

    def action(self):
        for u in self.units:
            u.act(self.units)
        for u in self.units:
            if u.health <= 0:
                self.units.remove(u)

    def draw(self, screen):
        for u in self.units:
            pygame.draw.circle(screen, [0, 0, 0], (u.x, u.y), 7, 0)

    def main(self):
        pygame.init() # Инициация PyGame, обязательная строчка
        screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
        pygame.display.set_caption("My PyGame") # Пишем в шапку
        bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
                                         # будем использовать как фон
        bg.fill(Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом
        clock = pygame.time.Clock()
        while 1: # Основной цикл программы
            clock.tick(10)
            for e in pygame.event.get(): # Обрабатываем события
                if e.type == QUIT:
                    raise SystemExit, "QUIT"
            screen.blit(bg, (0,0))      # Каждую итерацию необходимо всё перерисовывать
            self.action()
            self.draw(screen)
            pygame.display.update()     # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    tb = battle()
    for i in range(100):
        tb.add_unit(random.randint(100, 700), random.randint(100, 600))
    tb.add_unit(20, 20)
    tb.add_unit(200, 200)
    tb.main()