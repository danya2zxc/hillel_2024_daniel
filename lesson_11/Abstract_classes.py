from abc import ABC, abstractmethod
from datetime import datetime

from .models import Post, SocialChannel  # type: ignore


class ChannelProvider(ABC):
    @abstractmethod
    def post_a_message(self, followers: int, message: str):
        pass


class Youtube(ChannelProvider):
    def post_a_message(self, followers: int, message: str) -> None:
        print(
            f"Post '{message}' on {type(self).__name__} "
            f"with {followers} followers"
        )


class Facebook(ChannelProvider):
    def post_a_message(self, followers: int, message: str) -> None:
        print(
            f"Post '{message}' on {type(self).__name__} "
            f"with {followers} followers"
        )


class Twitter(ChannelProvider):
    def post_a_message(self, followers: int, message: str) -> None:
        print(
            f"Post '{message}' on {type(self).__name__} "
            f"with {followers} followers"
        )


def provider_message(channel: str) -> ChannelProvider:
    if channel == "youtube":
        return Youtube()
    elif channel == "facebook":
        return Facebook()
    elif channel == "twitter":
        return Twitter()
    else:
        raise Exception(f"Provider {channel} is not supported")


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        message, timestamp = post

        for channel in channels:
            if float(timestamp) <= datetime.now().timestamp():
                provider = provider_message(channel=channel.channel_type)
                provider.post_a_message(
                    followers=channel.followers,
                    message=str(message),
                )


def main():
    channels: list[SocialChannel] = [
        SocialChannel(channel_type="youtube", followers=50000),
        SocialChannel(channel_type="facebook", followers=250),
        SocialChannel(channel_type="twitter", followers=1899),
    ]
    posts: list[Post] = [
        Post(message="video tomorrow", timestamp=datetime.now().timestamp()),
        Post(message="work every day", timestamp=datetime.now().timestamp()),
        Post(
            message="i guess i'm afraid", timestamp=datetime.now().timestamp()
        ),
    ]

    process_schedule(posts=posts, channels=channels)


if __name__ == "__main__":
    main()
