from typing import Optional
from pydantic import BaseModel, Field


class PersonalInfo(BaseModel):
    name: str = Field(
        ...,
        description="The individual's full name.",
        example="Tarun Reddy"
    )
    location: str = Field(
        ...,
        description="The current location of the individual.",
        example="Boston, MA"
    )
    phone: str = Field(
        ...,
        description="The individual's phone number.",
        example="(857)-693-4743"
    )
    email: str = Field(
        ...,
        description="The individual's email address.",
        example="thandu.t@northeastern.edu"
    )
    linkedin: Optional[str] = Field(
        None,
        description="The individual's LinkedIn profile URL (optional).",
        example="www.linkedin.com/in/tarun-reddy"
    )
