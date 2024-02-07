# CRUD (Create Read Update Delete) operations

# Database representation
team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 31, "number": 12},
]


# Application source code
def repr_players(players: list[dict]):
    for player in players:
        print(
            f"\t[Player {player['number']}]: {player['name']},{player['age']}"
        )


def player_add(name: str, age: int, number: int) -> dict:
    for player_ in team:
        if player_["number"] == number:
            print(f"Player with this number {number} exists\n")
            return {}
    player: dict = {
        "name": name,
        "age": age,
        "number": number,
    }
    team.append(player)
    print(f"New player {name} has been added\n")

    return player


def player_delete(number: int) -> None:
    for player in team:
        if player["number"] == number:
            team.remove(player)
            print(f"Player with number {number} deleted\n")
            break


def player_update(number: int, new_name: str, new_age: int) -> None:
    for player in team:
        if player["number"] == number:
            player["name"] = new_name
            player["age"] = new_age
        print(f"Player with number {number} information has been updated\n")
        break


def main():
    operations = ("add", "del", "repr", "update", "exit")

    while True:
        operation = input("Please enter the operation: ")
        if operation not in operations:
            print(f"Operation: '{operation}' is not available\n")
            continue

        if operation == "exit":
            print("Bye")
            break
        elif operation == "repr":
            repr_players(team)
        elif operation == "add":
            user_data = input(
                "Enter new player information[name,age,number]: "
            )
            # Input: 'Clark,19,22'
            user_items: list[str] = user_data.split(",")
            # Result: ['Clark', '19', '22']
            name, age, number = user_items
            try:
                player_add(name=name, age=int(age), number=int(number))
            except ValueError:
                print("Age and number of player must be integers\n\n")
                continue
        elif operation == "update":
            player_number = input("Enter player number to update: ")
            new_name = input("Enter new player name: ")
            new_age = input("Enter new player age: ")
            player_update(
                number=int(player_number),
                new_name=new_name,
                new_age=int(new_age),
            )
        elif operation == "del":
            del_player = input("Enter the player number to delete: ")
            player_delete(number=int(del_player))
        else:
            raise NotImplementedError


if __name__ == "__main__":
    main()
