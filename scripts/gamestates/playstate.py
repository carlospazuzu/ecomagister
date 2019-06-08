import pygame
from scripts.utils import assetsmanager
from scripts.gameobjects.hand import Hand
from scripts.gameobjects.garbagecan import GarbageCan
from scripts.gameobjects.trashthrower import TrashThrower
from scripts.gameobjects.spell import Spell
from scripts.gameobjects.groundcollisor import GroundCollisor
from scripts.gameobjects.dirt import Dirt

class PlayState:

    def __init__(self, sm):
        self.state_manager = sm        
        self.dirt_sound = pygame.mixer.Sound('audio/sfx/dirt.wav')
        self.bg = pygame.image.load('img/bg.jpg')
        self.score_font = assetsmanager.get('EXPLANATION')
        self.score = 0
        self.score_increaser = 0
        self.clock = 58
        self.clock_counter = 0
        self.player_hand = Hand()
        self.spell_group = pygame.sprite.Group()    
        self.dirt_group = pygame.sprite.Group()            
        self.garbage_cans = {}
        self.garbage_cans['plastic'] = GarbageCan(200, 450, 'plastic', self.player_hand, self)
        self.garbage_cans['paper'] = GarbageCan(300, 450, 'paper', self.player_hand, self)
        self.garbage_cans['glass'] = GarbageCan(400, 450, 'glass', self.player_hand, self)
        self.garbage_cans['organic'] = GarbageCan(500, 450, 'organic', self.player_hand, self)
        self.garbage_cans['metal'] = GarbageCan(600, 450, 'metal', self.player_hand, self)  
        self.ground_collisor = GroundCollisor()        

        self.garbage_can_group = pygame.sprite.Group()                
        self.trash_thrower = TrashThrower(self.player_hand)

    def increase_score(self):
        if self.score_increaser > 0:
            if self.score_increaser >= 11:
                self.score += 11
                self.score_increaser -= 11    
            else:
                self.score += 1
                self.score_increaser -= 1

    def handle_input(self, event):
        self.player_hand.handle_input(event)

    def update(self, dt):
        if not pygame.mixer.music.get_busy() and self.clock > 10:
            pygame.mixer.music.load('audio/music/digimon.ogg')
            pygame.mixer.music.play(0) # zero to set it not to loop
        self.clock_counter += dt * 1000
        if self.clock_counter >= 1000:
            self.clock_counter = 0
            self.clock -= 1
            if self.clock % 10 == 0:
                self.trash_thrower.throw_delay -= 450
            if self.clock <= 0:
                for t in self.trash_thrower.get_trash_list().sprites():
                    self.dirt_sound.play()
                    self.dirt_group.add(Dirt(t.rect.x, t.rect.y))
                self.trash_thrower.get_trash_list().empty()
                self.trash_thrower.keep_throwing = False
                self.clock = 0
                self.state_manager.states[3].set_final_score(self.score)
                pygame.mixer.music.fadeout(1000)                                   
                self.state_manager.change_state(3) # change to ending scene         
        self.player_hand.update(dt)
        self.trash_thrower.update(dt)

        for col in pygame.sprite.spritecollide(self.ground_collisor, self.trash_thrower.get_trash_list(), True):
            self.dirt_group.add(Dirt(col.rect.x, col.rect.y))
            self.dirt_sound.play()

        for k, v in self.garbage_cans.items():
            v.update(dt, self.trash_thrower.get_trash_list())

        self.spell_group.update(dt)
        self.dirt_group.update(dt)

        self.increase_score()

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        self.ground_collisor.draw(screen)
        for k, v in self.garbage_cans.items():
            v.draw(screen)
        self.trash_thrower.get_trash_list().draw(screen)
        self.player_hand.draw(screen)

        self.spell_group.draw(screen)
        self.dirt_group.draw(screen)
        if self.score > 0:
            screen.blit(self.score_font.render(str(self.score), 0, (34, 34, 34)), (10, 10))
        
        screen.blit(self.score_font.render(str(self.clock), 0, (87, 202, 71)), (720, 10))