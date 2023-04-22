import pygame as pg
import sys
from bird import *
from pipes import *
from game_objects import *
from settings import *
from fire import *
# Класс "Игра"
class FlappyDoom:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.load_assets()
        self.sound = Sound()
        self.score = Score(self)
        self.fire = DoomFire(self)
        self.new_game()
# загрузка ресурсов игры
    def load_assets(self):
        # птица
        self.bird_images = [pg.image.load(f'assets/bird/{i}.png').convert_alpha() for i in range(5)]
        bird_image = self.bird_images[0]
        bird_size = bird_image.get_width() * BIRD_SCALE, bird_image.get_height() * BIRD_SCALE
        self.bird_images = [pg.transform.scale(sprite, bird_size) for sprite in self.bird_images]
        # фон
        self.background_image = pg.image.load('assets/images/bg.png').convert()
        self.background_image = pg.transform.scale(self.background_image, RES)
        # земля
        self.ground_image = pg.image.load('assets/images/ground.png').convert()
        self.ground_image = pg.transform.scale(self.ground_image, (WIDTH, GROUND_HEIGHT))
        # трубы
        self.top_pipe_image = pg.image.load('assets/images/top_pipe.png').convert_alpha()
        self.top_pipe_image = pg.transform.scale(self.top_pipe_image, (PIPE_WIDTH, PIPE_HEIGHT))
        self.bottom_pipe_image = pg.transform.flip(self.top_pipe_image, False, True)
        # птичья маска
        mask_image = pg.image.load('assets/bird/mask.png').convert_alpha()
        mask_size = mask_image.get_width() * BIRD_SCALE, mask_image.get_height() * BIRD_SCALE
        self.mask_image = pg.transform.scale(mask_image, mask_size)
# создание новой игры
    def new_game(self):
        self.all_sprites_group = pg.sprite.Group()
        self.pipe_group = pg.sprite.Group()
        self.bird = Bird(self)
        self.background = Background(self)
        self.ground = Ground(self)
        self.pipe_handler = PipeHandler(self)

# отрисовка компонентов игры
    def draw(self):
        self.background.draw()
        self.fire.draw()
        self.all_sprites_group.draw(self.screen)
        self.ground.draw()
        self.score.draw()
        pg.display.flip()
# обновление компонентов игры
    def update(self):
        self.background.update()
        self.fire.update()
        self.all_sprites_group.update()
        self.ground.update()
        self.pipe_handler.update()
        self.clock.tick(FPS)
# проверка события
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            self.bird.check_event(event)
# запуск
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
# Эта часть программного кода гласит "Запущенна в основном файле а не ипортированна"
if __name__ == '__main__':
    game = FlappyDoom()
    game.run()