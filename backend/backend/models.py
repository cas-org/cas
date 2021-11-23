from enum import Enum
from typing import List, Optional, Union

from bson.objectid import ObjectId
from bson.timestamp import Timestamp
from pydantic import BaseModel


class ParticipationStatus(Enum, str):
    SIGNED_UP = "signed_up"
    ABSENT = "absent"
    PARTICIPATED = "participated"
    AWARDED = "awarded"
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"


class Participation(BaseModel):
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


class OccurringType(Enum, str):
    CONTEST = "contest"


class ContentType(Enum, str):
    OBJECTIVE = "objective"
    SUBJECTIVE = "subjective"
    TRUE_OR_FALSE = "true_or_false"
    MULTIPLE_OPTIONS = "multiple_options"


class ObjectiveAnswer(BaseModel):
    pass  # TODO


class SubjectiveAnswer(BaseModel):
    pass  # TODO


class TrueOrFalseAnswer(BaseModel):
    pass  # TODO


class MultipleOptionsAnswer(BaseModel):
    pass  # TODO


class OccurringContent(BaseModel):
    type: ContentType
    question: str
    description: str
    answer: Union[ObjectiveAnswer, SubjectiveAnswer,
                  TrueOrFalseAnswer, MultipleOptionsAnswer]


class Occurring(BaseModel):
    display: str
    type: OccurringType
    contents: List[OccurringContent]
    created_on: Timestamp
    edited_on: Timestamp


class OccurringInDb(Occurring):
    pass
