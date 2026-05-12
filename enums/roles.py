from enum import Enum


class Role(Enum):

    # Nobility

    KING = "king"

    LORD = "lord"

    EARL = "earl"

    KNIGHT = "knight"


    # Military

    MEN_AT_ARMS = "men_at_arms"

    ARCHER = "archer"

    GUARD = "guard"

    MERCENARY = "mercenary"

    SCOUT = "scout"


    # Village Professions

    FARMER = "farmer"

    FARMHAND = "farmhand"

    HUNTER = "hunter"

    FISHERMAN = "fisherman"

    BLACKSMITH = "blacksmith"

    WOODCUTTER = "woodcutter"

    MINER = "miner"

    TRADER = "trader"

    TAVERN_KEEPER = "tavern_keeper"

    HEALER = "healer"

    PRIEST = "priest"

    BAKER = "baker"

    BUTCHER = "butcher"


    # Lower Class

    PEASANT = "peasant"

    BEGGAR = "beggar"

    THIEF = "thief"


    # Special

    MESSENGER = "messenger"

    SCHOLAR = "scholar"

    SPY = "spy"

    WITCHER = "witcher"