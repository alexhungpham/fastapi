from msilib import schema
from pydantic import BaseModel, fields
rom schema.base_entity import Gender
from datetime import datetime
from uuid import UUID

class CompanyModel(BaseModel):
	id: UUID
	name: str
	description: str
	mode: str
	rating: int

class UserModel(BaseModel):
	id: UUID
	email: str
	username: str
	firstName: str
	lastName: str
	hashedPasswd: str
	isActive: bool
	isAdmin: bool
    
class TaskModel(BaseModel):
	id: UUID
	sumary: str
	description: str
	status: bool
	priority: str
