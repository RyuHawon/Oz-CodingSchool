import random

class Bird():
    def __init__(self, kind, sound, fly, distance=0):
        self.kind = kind
        self.sound = sound
        self.fly = fly
        self.distance = distance
    
    def __str__(self):
        self.distance = random.randint(1, 100)
        return (
            f'{self.kind} 출발!!!\n'
            f'{self.sound}\n'
            f'{self.fly} 날았습니다.\n'
            f'결과는 {self.distance}m 입니다.'
        )

class Rubberduck(Bird):
    def __init__(self, kind, sound, fly, distance=0):
        super().__init__(kind, sound, fly, distance)
    
    def __str__(self):
        self.distance = 0
        return (
            f'{self.kind} 출발!!!\n'
            f'{self.sound}\n'
            f'{self.fly}\n'
            f'결과는 {self.distance}m 입니다.'
        )

bird_kind = {
    "앵무새": Bird('앵무새', '까악', '날개를 힘차게'),
    "참새": Bird('참새', '짹짹', '날개를 빠르게'),
    "비둘기": Bird('비둘기', '구구', '날개를 부드럽게'),
    "닭": Bird('닭', '꼬끼오', '날개를 퍼덕이며'),
    "러버덕": Rubberduck('러버덕', '삑삑삑', '날지 못함')
}

def bird_rpg():
    user_input = input("새를 선택하세요: 앵무새, 참새, 비둘기, 닭, 러버덕 ")
    print(bird_kind[user_input])
    

if __name__ == "__main__":
    bird_rpg()