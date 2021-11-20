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


class QuestionType(Enum):
    Objective = auto()
    Subjective = auto()
    TrueOrFalse = auto()
    MultipleOption = auto()
    
class OptionStatus(Enum):
    Option = auto()
    Answer = auto()
    
class QuestionOption:
    status: OptionStatus
    option1: str
    option2: str
    option3: str
    option4: str

class QuestionStatement:
    Statementid: ObjectId  
    Statement: str  

class QuestionContent:
    ref: ObjectId
    status: QuestionType
    statement: QuestionStatement
    option: Optional[List[QuestionOption]]
    

class Occurring(BaseModel):
    display: str
    type: OccurringType
    content: List[QuestionContent]
    created_on: Timestamp
    edited_on: Timestamp


class OccurringInDb(Occurring):
    pass
