from dataclasses import dataclass, field
from enums.gender import Gender

@dataclass
class Soul:

    personality: list[str] = field(default_factory=list)

    goals: list[str] = field(default_factory=list)

    fears: list[str] = field(default_factory=list)

    beliefs: list[str] = field(default_factory=list)

    gender: Gender = Gender.MALE