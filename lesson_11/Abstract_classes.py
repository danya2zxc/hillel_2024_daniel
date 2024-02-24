from abc import ABC, abstractmethod
from datetime import datetime 
from typing import Any

from .api import FacebookAPI, TwitterAPI, YoutubeAPI # type: ignore
from .models import Post, SocialChannel, User # type: ignore


def catch_errors(func: Any) -> Any:
    def inner(*args: Any, **kwargs: Any):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(f"Error catched: {error}")
        return None

    return inner


class ChannelsProvider(ABC):
    def __init__(self, user: User) -> None:
        self.user = user

    @abstractmethod
    def post_a_message(self):
        pass

    @abstractmethod
    def healthcheck(self):
        pass


class post_to_youtube(ChannelsProvider):
    def post_a_message(self) -> None:
        YoutubeAPI.post_a_message(
            message=self.user.post.message,
            channel=self.user.social.channel_type,
            followers=self.user.social.followers,
            time=self.user.post.timestamp,
            user_name=self.user.user_name,
        )

    def healthcheck(self) -> None:
        if YoutubeAPI.is_available() is False:
            raise Exception("Youtube is NOT available")


class post_to_facebook(ChannelsProvider):
    def post_a_message(self) -> None:
        FacebookAPI.post_a_message(
            message=self.user.post.message,
            channel=self.user.social.channel_type,
            followers=self.user.social.followers,
            time=self.user.post.timestamp,
            user_name=self.user.user_name,
        )

    def healthcheck(self) -> None:
        if FacebookAPI.is_available() is False:
            raise Exception("Facebook is NOT available")


class post_to_twitter(ChannelsProvider):
    def post_a_message(self) -> None:
        TwitterAPI.post_a_message(
            message=self.user.post.message,
            channel=self.user.social.channel_type,
            followers=self.user.social.followers,
            time=self.user.post.timestamp,
            user_name=self.user.user_name,
        )

    def healthcheck(self) -> None:
        if TwitterAPI.is_available() is False:
            raise Exception("Twitter is NOT available")


@catch_errors
def provider_message(channel: str, user: User) -> ChannelsProvider:
    if channel == "youtube":
        return post_to_youtube(user=user)
    elif channel == "facebook":
        return post_to_facebook(user=user)
    elif channel == "twitter":
        return post_to_twitter(user=user)
    else:
        raise Exception(f"Provider {channel} is not supported")


def main():
    john = User(
        user_name="John322",
        social=SocialChannel(channel_type="youtube", followers=50000),
        post=Post(message="new video tomorrow", timestamp=datetime.now()),
    )

    merry = User(
        user_name="Merryweather",
        social=SocialChannel(channel_type="facebook", followers=250),
        post=Post(message="We work every day", timestamp=datetime.now()),
    )

    arthur = User(
        user_name="Morgan",
        social=SocialChannel(channel_type="twitter", followers=1899),
        post=Post(message="i guess i'm afraid", timestamp=datetime.now()),
    )
    # social_y = SocialChannel(channel_type="youtube",followers=50000)
    # social_f = SocialChannel(channel_type="facebook",followers=200)
    # social_t = SocialChannel(channel_type="twitter",followers=1600)

    channels_provider_1: ChannelsProvider = provider_message(
        channel="youtube", user=john
    )
    try:
        channels_provider_1.healthcheck()
        channels_provider_1.post_a_message()
    except Exception as e:
        print(f"Error catched: {e}")

    channels_provider_2: ChannelsProvider = provider_message(
        channel="facebook", user=merry
    )
    try:
        channels_provider_2.healthcheck()
        channels_provider_2.post_a_message()
    except Exception as e:
        print(f"Error catched: {e}")

    channels_provider_3: ChannelsProvider = provider_message(
        channel="twitter", user=arthur
    )
    try:
        channels_provider_3.healthcheck()
        channels_provider_3.post_a_message()
    except Exception as e:
        print(f"Error catched: {e}")

    provider_message(channel="instagram", user=john)


if __name__ == "__main__":
    main()
