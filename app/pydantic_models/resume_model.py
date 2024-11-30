from pydantic import BaseModel
from typing import List
from pydantic_models.personal_info_model import PersonalInfo
from pydantic_models.educations_model import Education
from pydantic_models.projects_model import Project
from pydantic_models.experiences_model import Experience
from pydantic_models.skills_model import SkillCategory


class Resume(BaseModel):
    personal_info: PersonalInfo
    educations: List[Education]
    experiences: List[Experience]
    skills: List[SkillCategory]
    projects: List[Project]
