from hero import Hero


class Dungeon:
    def __init__(self, map_path):
        self.map_path = map_path
        self.actual_map = []
        self.create_field()
        self.hero_player = None
        self.orc_player = None
        self.hero_entity = None
        self.orc_entity = None

    def create_field(self):
        file = open(self.map_path, "r")
        for line in file:
            temp_list = []
            for char in line:
                if char != "\n":
                    temp_list.append(char)
            self.actual_map.append(temp_list)
        file.close()

    def print_map(self):
        for line in self.actual_map:
            print("".join(line))
        return True

    def spawn(self, player_name, entity):
        spoint_name = None
        if isinstance(entity, Hero):
            spoint_name = "H"
            self.hero_player = player_name
            self.hero_entity = entity
        else:
            spoint_name = "O"
            self.orc_player = player_name
            self.orc_entity = entity
        for i in range(len(self.actual_map)):
            for j in range(len(self.actual_map[0])):
                if self.actual_map[i][j] == 'S':
                    self.actual_map[i][j] = spoint_name
                    return True
        return False

    def move(self, player_name, direction):
        
