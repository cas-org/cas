from enum import Enum, auto
from typing import List, Optional
from pydantic import BaseModel
from bson.timestamp import Timestamp
from bson.objectid import ObjectId


class ParticipationStatus(Enum):
    SIGNED_UP = auto()
    ABSENT = auto()
    PARTICIPATED = auto()
    AWARDED = auto()
    BRONZE = auto()
    SILVER = auto()
    GOLD = auto()


class Participation:
    ref: ObjectId
    status: ParticipationStatus
    marks: Optional[int]
    participated_on: Optional[Timestamp]


class User(BaseModel):
    name: str
    joined_on: Timestamp
    participation: List[Participation]


class UserInDb(User):
    pass


class OccurringType(Enum):
    CONTEST = auto()


class Occurring(BaseModel):
    display: str
    type: OccurringType
    # TODO Decide what occuring content should consist of
    # content: OccurringContent
    created_on: Timestamp
    edited_on: Timestamp


class OccurringInDb(Occurring):
    pass
