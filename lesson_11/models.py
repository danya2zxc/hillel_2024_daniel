from dataclasses import dataclass


@dataclass
class SocialChannel:
    channel_type: str
    followers: int


@dataclass
class Post:
    message: str
    timestamp: float

    def __iter__(self):
        yield self.message
        yield self.timestamp
