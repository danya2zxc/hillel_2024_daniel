from typing import Generator


class Player:
    def __init__(self, first_name: str, last_name: str):
        self.first_name: str = first_name
        self.last_name: str = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


team: list[Player] = [
    Player("John", "Smith"),
    Player("Marry", "Smith"),
    Player("Jack", "Hill"),
    Player("Nick", "Doe"),
    Player("John", "Doe"),
    Player("Marry", "Doe"),
]


def dedup(collection) -> Generator[Player, None, None]:
    unique_players_names = set()
    for player in collection:
        if player.first_name not in unique_players_names:
            unique_players_names.add(player.first_name)
            yield player.first_name


print("All names of players:")
for player in team:
    print(player)


print("\nUnique Players names:")
for player in dedup(team):
    print(player)

# Expected Output:
# John Smith
# Marry Smith
# Jack Hill
# Nick Doe


# Output:
# All names of players:
# John Smith
# Marry Smith
# Jack Hill
# Nick Doe
# John Doe
# Marry Doe

#  Unique Players names:
# Jack
# Nick
# Marry
# John
