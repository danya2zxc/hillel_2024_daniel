import random
from datetime import datetime


class YoutubeAPI:
    @staticmethod
    def post_a_message(
        message: str,
        channel: str,
        followers: int,
        time: datetime,
        user_name: str,
    ):
        print(
            f"Post '{message}'. From {user_name} post on "
            f"{channel} with {followers} followers on {time}"
        )
        return

    @staticmethod
    def is_available() -> bool:
        value = random.randint(1, 10)
        if value < 5:
            return True
        else:
            return False


class FacebookAPI:
    authorization_state: dict[str, bool] = {}

    @staticmethod
    def post_a_message(
        message: str,
        channel: str,
        followers: int,
        time: datetime,
        user_name: str,
    ):
        print(
            f"Post '{message}'. From {user_name} post on "
            f"{channel} with {followers} followers on {time}"
        )
        return

    @staticmethod
    def is_available() -> bool:
        value = random.randint(1, 10)
        if value < 5:
            return True
        else:
            return False


class TwitterAPI:
    @staticmethod
    def post_a_message(
        message: str,
        channel: str,
        followers: int,
        time: datetime,
        user_name: str,
    ) -> None:
        print(
            f"Post '{message}'. From {user_name} post on "
            f"{channel} with {followers} followers on {time}"
        )
        return

    @staticmethod
    def is_available() -> bool:
        value = random.randint(1, 10)
        if value < 5:
            return True
        else:
            return False
