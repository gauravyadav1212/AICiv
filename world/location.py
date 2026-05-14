class Location:

    def __init__(
        self,
        name: str,
        description: str,
        location_type: str,
        owner=None,
        social_class=None,
        danger_level=0.0
    ):

        self.name = name

        self.description = description

        self.lore = []

        self.location_type = location_type

        self.owner = owner

        self.social_class = social_class

        self.danger_level = danger_level

        self.connected_locations = []

        self.rumors = []

    def connect(self, location):

        if location not in self.connected_locations:

            self.connected_locations.append(location)

            location.connected_locations.append(self)

    def add_rumor(self, rumor: str):

        self.rumors.append(rumor)

    def add_lore(self, lore: str):

        self.lore.append(lore)