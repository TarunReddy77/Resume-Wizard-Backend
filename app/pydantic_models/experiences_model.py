from my_content.experience import experiences

from typing import Optional, List
from pydantic import BaseModel, Field
from typing_extensions import Literal


class TitleContents(BaseModel):
    type: Literal['experience'] = Field(
        ...,
        description="The type of the entry, always set to 'experience'.",
        example="experience"
    )
    company: str = Field(
        ...,
        description="The name of the company or organization.",
        example="Infosys"
    )
    role: str = Field(
        ...,
        description="The job role or position held.",
        example="Specialist Programmer – Full Stack Developer"
    )
    location: str = Field(
        ...,
        description="The location of the company or where the job was based.",
        example="Bangalore, India"
    )
    additional_info: Optional[str] = Field(
        ...,  # Changed from "" to None
        description="Any additional information related to the experience (optional).",
        example="Worked on a high-impact project for a global client"
    )

    class Config:
        extra = 'forbid'


class Experience(BaseModel):
    title_contents: TitleContents = Field(
        ...,
        description="Details about the company's name, role, location, and additional information.",
        example={
            "type": "experience",
            "company": "Infosys",
            "role": "Specialist Programmer – Full Stack Developer",
            "location": "Bangalore, India",
            "additional_info": "Worked on a high-impact project for a global client"
        }
    )
    subtitle_contents: Optional[str] = Field(
        ...,
        description="Subtitle or additional context for the experience (optional). Prefer None.",
        example=""
    )
    timeline: str = Field(
        ...,
        description="The time period during which the experience took place. Use only 3 letter abbreviations for month names. For example, Septemember should be written as Sep.",
        example="Sep 2021 - Jan 2023"
    )
    bullet_points: List[str] = Field(
        ...,
        description="A list of bullet points summarizing key achievements and tasks in the role.",
        example=[
            "Engineered full-stack development for Apple's DevSecOps Portal, integrating new features and resolving existing feature bugs, ensuring user-friendly DevOps automation via Jenkins.",
            "Designed and programmed responsive web interfaces leveraging HTML, CSS, and Angular on the frontend, and executed database calls and REST API integration leveraging Spring Boot framework on the backend."
        ]
    )


class Experiences(BaseModel):
    experiences: List[Experience] = Field(
        ...,
        description="A list of Experience objects representing all the work experiences to be included in the resume."
                    "There should be exactly 2 such experiences.",
        example=experiences
    )
