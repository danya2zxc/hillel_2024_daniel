from abc import ABC, abstractmethod
from datetime import datetime

from .models import Post, SocialChannel, User  # type: ignore


class ChannelProvider(ABC):
    def __init__(self, channel_type: str, followers: int) -> None:
        self.channel_type = channel_type
        self.followers = followers

    @abstractmethod
    def post_a_message(self, message: str):
        pass


class post_to_youtube(ChannelProvider):
    def post_a_message(self, message: str) -> None:
        print(
            f"Post '{message}' on {self.channel_type} "
            f"with {self.followers} followers"
        )
        return


class post_to_facebook(ChannelProvider):
    def post_a_message(self, message: str) -> None:
        print(
            f"Post '{message}' on {self.channel_type} "
            f"with {self.followers} followers"
        )
        return


class post_to_twitter(ChannelProvider):
    def post_a_message(self, message: str) -> None:
        print(
            f"Post '{message}' on {self.channel_type}"
            f"with {self.followers} followers"
        )
        return


def provider_message(channel: SocialChannel) -> ChannelProvider:
    if channel.channel_type == "youtube":
        return post_to_youtube(
            channel_type=channel.channel_type, followers=channel.followers
        )
    elif channel.channel_type == "facebook":
        return post_to_facebook(
            channel_type=channel.channel_type, followers=channel.followers
        )
    elif channel.channel_type == "twitter":
        return post_to_twitter(
            channel_type=channel.channel_type, followers=channel.followers
        )
    else:
        raise Exception(f"Provider {channel.channel_type} is not supported")


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        message, timestamp = post
        timestamp = int(timestamp)

        for channel in channels:
            if timestamp < datetime.now().timestamp():
                provider = provider_message(
                    channel=channel,
                )
                provider.post_a_message(str(message))


def main():
    john = User(
        social=SocialChannel(channel_type="youtube", followers=50000),
        post=Post(
            message="new video tomorrow", timestamp=datetime.now().timestamp()
        ),
    )

    merry = User(
        social=SocialChannel(channel_type="facebook", followers=250),
        post=Post(
            message="We work every day", timestamp=datetime.now().timestamp()
        ),
    )

    arthur = User(
        social=SocialChannel(channel_type="twitter", followers=1899),
        post=Post(
            message="i guess i'm afraid", timestamp=datetime.now().timestamp()
        ),
    )

    process_schedule(
        posts=[john.post, merry.post, arthur.post],
        channels=[john.social, merry.social, arthur.social],
    )


if __name__ == "__main__":
    main()
