from pydantic import BaseModel
from pydantic_models.projects_model import Projects
from pydantic_models.experiences_model import Experiences
from pydantic_models.skills_model import Skills


class Resume(BaseModel):
    personal_info: = Field(
        ...,
        description="The type of the entry, always set to 'project'.",
        example="project"
    )
    education: education
    experiences: Experiences
    skills: Skills
    projects: Projects



class TitleContents(BaseModel):
    type: Literal['project'] = Field(
        ...,
        description="The type of the entry, always set to 'project'.",
        example="project"
    )
    domain: str = Field(
        ...,
        description="The domain or field of the project.",
        example="Machine Learning"
    )
    name: str = Field(
        ...,
        description="The name or title of the project.",
        example="Customer Segmentation using Clustering Algorithms"
    )
    additional_info: Optional[str] = Field(
        ...,
        description="Any additional information related to the project (optional).",
        example=""
    )