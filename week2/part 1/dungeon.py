from functools import reduce
from copy import deepcopy
from hero import Hero
from orc import Orc
from fight import Fight
from weapon import Weapon
from random import randint


class Dungeon:

    def __init__(self, filename):
        self.weapons = []
        self.dungeon = self.load_map(filename)
        self.players = {}  # 'id': (entity, coord_x, coord_y)

    # the map is like a matrix, e.g. a list of lists!!!
    def load_map(self, filename):
        file = open(filename, "r")
        content = file.read().split('\n')
        file.close()

        dungeon = list(filter(lambda x: self.is_map_row(x) and len(x) != 0,
                              content))
        dungeon = list(map(lambda x: list(x), dungeon))

        weapons = list(filter(lambda x: x != '', content[len(dungeon):]))
        self.set_weapons(weapons)

        return dungeon

    def is_map_row(self, file_line):
        map_signs = ['S', '.', '#']
        return len(list(filter(lambda x: x in map_signs,
                   deepcopy(list(file_line))))) == len(file_line)

    def set_weapons(self, file_weapons):
        if len(file_weapons) != 0:
            for weapon in file_weapons:
                weapon = weapon.split(' ')
                self.weapons.append(Weapon(weapon[0],
                                    float(weapon[1]),
                                    float(weapon[2])))

    def print_map(self):
        for row in self.dungeon:
            print(''.join(row))
        return True

    def spawn(self, enitity_id, entity):
        if self.free_spawning_points() and enitity_id not in self.players:
            letter = self.entity_kind(entity)
            for coord_y, row in enumerate(self.dungeon):
                if 'S' in row:
                    coord_x = ''.join(row).find('S')
                    self.players[enitity_id] = (entity, coord_x, coord_y)
                    row[coord_x] = letter
                    break
            return True
        elif not self.free_spawning_points():
            print("There are no free spawning points.")
            return False
        else:
            message = 'There is already a player with that name.'
            raise ValueError(message)

    def free_spawning_points(self):
        return 'S' in reduce(lambda x, y: x + y, deepcopy(self.dungeon))

    def entity_kind(self, entity):
        if isinstance(entity, Hero):
            return 'H'
        elif isinstance(entity, Orc):
            return 'O'
        else:
            message = 'There is no such animal!'
            raise ValueError(message)

    def move(self, player_name, direction):
        if player_name in self.players:
            player = self.players[player_name]
            # go_to -> (coord_x1, coord_y1)
            go_to = self.go_to_field(player[1], player[2], direction)
            if go_to:
                if self.dungeon[go_to[1]][go_to[0]] == '#':
                    print('Obstacle in that direction.')
                    return False
                elif self.dungeon[go_to[1]][go_to[0]] == '.':
                    self.dungeon[go_to[1]][go_to[0]] = self.dungeon[
                        player[2]][player[1]]
                    self.dungeon[player[2]][player[1]] = '.'
                    self.players[player_name] = (player[0], go_to[0], go_to[1])
                elif self.dungeon[go_to[1]][go_to[0]] == 'W':
                    weapon = self.get_weapon(go_to[0], go_to[1])
                    player[0].equip_weapon(weapon)
                    self.dungeon[go_to[1]][go_to[0]] = self.dungeon[
                        player[2]][player[1]]
                    self.dungeon[player[2]][player[1]] = '.'
                    self.players[player_name] = (player[0], go_to[0], go_to[1])
                    print('{} weapon equipped!'.format(weapon.type))
                else:  # in that case we meet enemy
                    # recognise hero and orc
                    if isinstance(player[0], Hero):
                        hero = (player_name, player[0])
                        orc = self.entity_at_field(go_to[0], go_to[1])
                    else:
                        hero = self.entity_at_field(go_to[0], go_to[1])
                        orc = (player_name, player[0])

                    # get the winner
                    fight = Fight(hero[1], orc[1])
                    fight.simulate_fight()
                    if fight.hero.health != 0:
                        print('{} wins!!!'.format(hero[0]))
                        self.dungeon[go_to[1]][go_to[0]] = 'H'
                        self.players.pop(orc[0])
                        self.players[hero[0]] = (hero[1], go_to[0], go_to[1])
                    else:
                        print('{} wins!!!'.format(orc[0]))
                        self.dungeon[go_to[1]][go_to[0]] = 'O'
                        self.players.pop(hero[0])
                        self.players[orc[0]] = (orc[1], go_to[0], go_to[1])
                    self.dungeon[player[2]][player[1]] = '.'
            else:
                print('Movement out of bounds.')
                return False
        else:
            message = 'There is no such player in the game.'
            raise ValueError(message)

    def go_to_field(self, coord_x, coord_y, direction):
        if direction in ['up', 'left', 'right', 'down']:
            if direction == 'up':
                coord_x1 = coord_x
                coord_y1 = coord_y - 1
            elif direction == 'down':
                coord_x1 = coord_x
                coord_y1 = coord_y + 1
            elif direction == 'left':
                coord_x1 = coord_x - 1
                coord_y1 = coord_y
            else:
                coord_x1 = coord_x + 1
                coord_y1 = coord_y

            if (0 > coord_x1 or coord_x1 >= len(self.dungeon[0]) or
                    0 > coord_y1 or coord_y1 >= len(self.dungeon)):
                return False
            else:
                return (coord_x1, coord_y1)
        else:
            message = 'No such direction is invented yet.'
            raise ValueError(message)

    # (id, entity)
    def entity_at_field(self, coord_x, coord_y):
        for key in self.players:
            if (self.players[key][1] == coord_x and
                    self.players[key][2] == coord_y):
                return (key, self.players[key][0])

    def spawn_weapons(self):
        for index, weapon in enumerate(self.weapons):
            coordinates = self.generate_coordinates()
            self.dungeon[coordinates[1]][coordinates[0]] = 'W'
            self.weapons[index] = (weapon, coordinates[0], coordinates[1])

    def generate_coordinates(self):
        x = randint(0, len(self.dungeon[0]) - 1)
        y = randint(0, len(self.dungeon) - 1)
        while self.dungeon[y][x] != '.':
            x = randint(0, len(self.dungeon[0]) - 1)
            y = randint(0, len(self.dungeon) - 1)
        return (x, y)

    def get_weapon(self, coord_x, coord_y):
        for weapon in self.weapons:
            if weapon[1] == coord_x and weapon[2] == coord_y:
                w = weapon
        self.weapons.remove(w)
        return w[0]

    # for now functionallity of start_fight() is in move()
