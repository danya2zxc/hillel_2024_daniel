from dataclasses import dataclass
from datetime import datetime


@dataclass
class SocialChannel:
    channel_type: str
    followers: int


@dataclass
class Post:
    message: str
    timestamp: datetime


@dataclass
class User:
    user_name: str
    social: SocialChannel
    post: Post
