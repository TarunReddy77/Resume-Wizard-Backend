from typing import List, Literal, Optional
from pydantic import BaseModel, Field

from my_content.education import educations


class TitleContents(BaseModel):
    type: Literal['education'] = Field(
        "education",
        description="The type of the entry, always set to 'education'.",
        example="education"
    )
    university: str = Field(
        ...,
        description="The name of the university or educational institution.",
        example="Khoury College of Computer Sciences, Northeastern University"
    )
    location: str = Field(
        ...,
        description="The location of the university.",
        example="Boston, MA"
    )


class Education(BaseModel):
    title_contents: TitleContents = Field(
        ...,
        description="Details about the education, including the type, university, and location.",
        example={
            "type": "education",
            "university": "Khoury College of Computer Sciences, Northeastern University",
            "location": "Boston, MA"
        }
    )
    subtitle_contents: Optional[str] = Field(
        "",
        description="Subtitle or additional information about the education (optional).",
        example="Master of Science in Artificial Intelligence (GPA 3.95/4)"
    )
    timeline: str = Field(
        ...,
        description="The time period during which the education took place. Use only 3 letter abbreviations for month names. For example, Septemember should be written as Sep.",
        example="Expected Dec 2024"
    )
    bullet_points: List[str] = Field(
        ...,
        description="A list of bullet points summarizing key courses, roles, and achievements.",
        example=[
            "Courses: Large Language Models, AI for Human Computer Interaction, Deep Learning, Machine Learning, Natural Language Processing",
            "Roles: Head Teaching Assistant for Graduate Level Natural Language Processing"
        ]
    )


class Educations(BaseModel):
    educations: List[Education] = Field(
        ...,
        description="A list of Education objects representing all the educational experiences to be included in the resume.",
        example=educations
    )
