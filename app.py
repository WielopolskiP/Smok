from random import randint
from dataclasses import dataclass


def if_alive(my_func):
    def wrapper(dragon, *args, **kwargs):
        if dragon.is_alive():
            my_func(dragon, *args, **kwargs)
        else:
            pass
    return wrapper


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def __post_init__(self) ->None:
        if self.x < 0:
            raise ValueError('x cannot be negative')
        if self.y < 0:
            raise ValueError('y cannot be negative')


class Movable:
    @if_alive
    def set_position(self, position: Point = Point()) -> None:
        self.position: Point = position

    def get_position(self) -> Point:
        return self.position

    @if_alive
    def move(self, left: int = 0, right: int = 0, down: int = 0, up: int = 0) -> None:
        current_position = self.get_position()
        x: int = current_position.x + right - left
        y: int = current_position.y + down - up
        self.set_position(Point(x, y))


class Dragon(Movable):
    TEXTURE = r'img/dragon/alive.png'
    HEALTH_MIN, HEALTH_MAX = 50, 120
    GOLD_MIN, GOLD_MAX = 1, 100

    def __init__(self, name='smok', position: Point = Point()):
        self.name = name
        self.health = randint(self.HEALTH_MIN, self.HEALTH_MAX)
        self.texture = self.TEXTURE
        self.life_status = 'LIVE'
        self.gold = randint(self.GOLD_MIN, self.GOLD_MAX)
        self.set_position(position)

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
    def take_damage(self, damage: int):
        self.health -= damage
        self.update_status()
        print(f'damage {damage} {self.name} {self.health}')

    @if_alive
    def make_damage(self, damage: int):
        pass


if __name__ == '__main__':
    dr = Dragon(name= 'Wawelski', position=Point(20, 50))
    print(dr.name, dr.life_status, dr.health, dr.position)
    dr.set_position(position=Point(30, 120))
    dr.move(left=20, right=0, down=30, up=0)
    dr.take_damage(damage=15)
    dr.take_damage(damage=15)
    dr.take_damage(damage=15)
    dr.take_damage(damage=150)
    dr.take_damage(damage=15)
    dr.take_damage(damage=15)
    print(dr.name, dr.life_status,  dr.health, dr.position)