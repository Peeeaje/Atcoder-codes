import sys


class Desks:
    def __init__(self, lines):
        self._field = lines
        self.height = len(lines)
        self.width = len(self._field[0])

    def get(self, row, col):
        return self._field[row][col]

    def is_novice(self, row, col):
        return self.get(row, col) == "N"

    def is_educator(self, row, col):
        return self.get(row, col) == "V"

    def search_educators(self, row, col):
        result = []
        for div_row, div_col in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            tar_row = row + div_row
            tar_col = col + div_col

            if (not 0 <= tar_col < self.width) or (not 0 <= tar_row < self.height):
                continue
            if self.get(tar_row, tar_col) == "V":
                result.append((tar_row, tar_col))
        return result

    def search_novices(self, row, col):
        result = ()
        for div_row, div_col in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            tar_row = row + div_row
            tar_col = col + div_col

            if (not 0 <= tar_col < self.width) or (not 0 <= tar_row < self.height):
                continue
            if self.get(tar_row, tar_col) == "N":
                result.append((tar_row, tar_col))
        return result


def main(lines):
    n, m = map(int, lines[0].split())
    desks = []
    for v in lines[1:]:
        desks.append(v)
    desks = Desks(desks)

    # 一人の初心者につく熟練者のリスト
    list_v = []
    for row in range(n):
        for col in range(m):
            if desks.is_novice(row, col):
                list_v.append(desks.search_educators(row, col))

    # 熟練者が担当できる初心者の人数
    novice_count = [[0] * n for _ in range(m)]
    for row in range(n):
        for col in range(m):
            if desks.is_educator(row, col):
                novice_count[row][col] = len(desks.search_novices(row, col))

    # list_vから働いた人を削除し、教えてくれる人が少ない順に並び替える
    def remove_worked_educator(list_v, worked_educator):
        for novice in list_v:
            if worked_educator in set(novice):
                novice.remove(worked_educator)
        list_v.sort(key=len)
        return list_v

    ans = 0
    worked_educators = set()
    list_v.sort(key=len)
    while len(list_v):
        assigned_educators = list_v.pop(0)
        assigned_educators.sort(key=lambda x: novice_count[x[0]][x[1]])
        the_novice_is_educated = False
        for educator in assigned_educators:
            if the_novice_is_educated:
                continue

            if educator not in worked_educators:
                worked_educators.add(educator)
                remove_worked_educator(list_v, educator)
                ans += 1
                the_novice_is_educated = True
    print(ans)


if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
