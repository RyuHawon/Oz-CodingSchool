from abc import ABC, abstractmethod

class WeaponBehavior(ABC):
    @abstractmethod
    def useWeapon(self):
        pass

class Character(ABC):
    def __init__(self):
        self.weapon = None
    
    def setWeapon(self, weapon: WeaponBehavior):
        self.weapon = weapon
    
    def fight(self):
        if self.weapon is None:
            print("무기가 없습니다.")
        else:
            self.weapon.useWeapon()

class SwordBehavior(WeaponBehavior):
    def useWeapon(self):
        print("검을 휘두른다.")

class KnifeBehavior(WeaponBehavior):
    def useWeapon(self):
        print("나이프를 휘두른다.")

class AxeBehavior(WeaponBehavior):
    def useWeapon(self):
        print("도끼를 휘두른다.")

class BowAndArrowBehavior(WeaponBehavior):
    def useWeapon(self):
        print("화살을 쏜다.")

class Queen(Character):
    def fight(self):
        print("여왕의 공격: ", end="")
        super().fight()

class King(Character):
    def fight(self):
        print("왕의 공격: ", end="")
        super().fight()

class Knight(Character):
    def fight(self):
        print("기사의 공격: ", end="")
        super().fight()

class Troll(Character):
    def fight(self):
        print("트롤의 공격: ", end="")
        super().fight()