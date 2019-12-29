from random import randint


def if_alive(my_func):
    def wrapper(dragon, *args, **kwargs):
        if dragon.is_alive():
            my_func(dragon, *args, **kwargs)
        else:
            pass
    return wrapper


class Dragon(object):
    TEXTURE = r'img/dragon/alive.png'
    HEALTH_MIN, HEALTH_MAX = 50, 120
    GOLD_MIN, GOLD_MAX = 1, 100

    def __init__(self, name='smok', pos_x=0, pos_y=0):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.texture = self.TEXTURE
        self.life_status = 'LIVE'
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)

    def is_alive(self) -> bool:
        if self.life_status == 'LIVE':
            return True
        else:
            return False

    def is_dead(self) -> bool:
        return not self.is_alive()

    def update_status(self):
        if self.health > 0:
            self.life_status = 'LIVE'
        else:
            self.life_status = 'DEAD'
        print('status_update ', self.life_status)

    @if_alive
    def set_position(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y

    # set_position = is_alive(set_position)

    @if_alive
    def move(self, left=0, right=0, down=0, up=0) -> None:
        self.pos_x += right - left
        self.pos_y += down - up

    @if_alive
    def take_damage(self, damage: int):
        self.health -= damage
        self.update_status()
        print(f'damage {damage} {self.name} {self.health}')

    @if_alive
    def make_damage(self, damage: int):
        pass


if __name__ == '__main__':
    dr = Dragon(name= 'Wawelski',pos_x=20, pos_y=50)
    print(dr.name, dr.life_status, dr.health, dr.pos_x, dr.pos_y)
    dr.set_position(pos_x=30, pos_y= 120)
    dr.move(left=20, right=0, down=30, up=0)
    dr.take_damage(damage=15)
    dr.take_damage(damage=15)
    dr.take_damage(damage=15)
    dr.take_damage(damage=150)
    dr.take_damage(damage=15)
    dr.take_damage(damage=15)
    print(dr.name, dr.life_status,  dr.health, dr.pos_x, dr.pos_y)