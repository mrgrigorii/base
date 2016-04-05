# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 14:38:34 2016

@author: Григорий
"""

# Импортируем библиотеку pygame
import pygame
from pygame import *

#Объявляем переменные
WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "white"#"#004400"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

def main():
    pygame.init() # Инициация PyGame, обязательная строчка 
    screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
    pygame.display.set_caption("My PyGame") # Пишем в шапку
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
                                         # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))     # Заливаем поверхность сплошным цветом
    level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------        -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]
    i = 20
    clock = pygame.time.Clock()
    while 1: # Основной цикл программы
        if i == 600:
            i = 20
        clock.tick(40)
        for e in pygame.event.get(): # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit, "QUIT"
        screen.blit(bg, (0,0))      # Каждую итерацию необходимо всё перерисовывать 
        
        pygame.draw.ellipse(screen, [0, 0, 0], [i,20, 30, 30], 2)
        pygame.draw.circle(screen, [0, 0, 0], (i + 10,i + 10), 50, 0)
        i = i + 2
        pygame.display.update()     # обновление и вывод всех изменений на экран
        

if __name__ == "__main__":
    main()
