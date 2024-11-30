from pydantic import BaseModel
from typing import Dict
from pydantic_models.experiences_model import Experience
from pydantic_models.projects_model import Project



class JobDescription(BaseModel):
    job_description: str


class EnhanceBulletPointRequest(BaseModel):
    section: str
    item_index: int
    bullet_point_index: int
    bullet_point_text: str
    enhancement_instructions: str


class EnhanceExperienceRequest(BaseModel):
    index: int
    experience: Experience
    enhancement_instructions: str


class EnhanceProjectRequest(BaseModel):
    index: int
    project: Project
    enhancement_instructions: str


class GenerateDocumentRequest(BaseModel):
    resume_contents: Dict
    doc_type: str
