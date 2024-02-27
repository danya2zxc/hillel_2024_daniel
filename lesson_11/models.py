from dataclasses import dataclass


@dataclass
class SocialChannel:
    channel_type: str
    followers: int

    # def __iter__(self):
    #     yield self.channel_type
    #     yield self.followers


@dataclass
class Post:
    message: str
    timestamp: float

    def __iter__(self):
        yield self.message
        yield self.timestamp


@dataclass
class User:
    social: SocialChannel
    post: Post
