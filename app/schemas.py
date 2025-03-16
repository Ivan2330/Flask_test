from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserUpdate(BaseModel):
    name: str = None
    email: EmailStr = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

class UserListResponse(BaseModel):
    users: List[UserResponse]
