move_dict = {".": [0, 0], "U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}


class Field:
    def __init__(self) -> None:
        self.condition = [[None] * 30 for _ in range(30)]

    def locate_object(self, coordinate, object):
        x, y = coordinate
        self.condition[x][y] = object

    @staticmethod
    def to_move(self, coordinate: list) -> list:
        x, y = coordinate
        candidates = [[x + 0, y + 1], [x + 0, y - 1], [x + 1, y + 0], [x - 1, y + 0]]

        for candidate in candidates:
            if (0 <= candidate[0] < 30 and 0 <= candidate[1] < 30) and (
                self.condition[candidate[0]][candidate[1]] is None
            ):
                return candidate


class Animal:
    def __init__(self, coordinate: list) -> None:
        self.coordinate = coordinate

    # def default_move(self, field: Field):
    #     nexts = field.to_move(self.coordinate)

    def move(self, field: Field, direction: str) -> None:
        x, y = self.coordinate
        print(direction)
        dev_x, dev_y = move_dict[direction]
        next_x, next_y = x + dev_x, y + dev_y

        field.condition[next_x][next_y], field.condition[x][y] = self, None


class Human:
    def __init__(self, coordinate: list):
        self.coordinate = coordinate


field = Field()
N = int(input())
animal_list = []
for i in range(N):
    px, py, pt = map(int, input().split())

    animal_list.append(Animal([px - 1, py - 1]))
    field.locate_object([px - 1, py - 1], animal_list[i])

M = int(input())
human_list = []
for i in range(M):
    px, py = map(int, input().split())

    human_list.append(Human([px - 1, py - 1]))
    field.locate_object([px - 1, py - 1], animal_list[i])

seed = int(input())

for i in range(300):
    print(input())
    # move_inputs = list(map(int, input().split()))
    for i in range(N):
        animal_list[i].move(field, move_inputs[i])
