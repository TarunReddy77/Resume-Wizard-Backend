from pydantic import BaseModel, Field, field_validator
from typing import List, Optional


class ExperienceTitleContent(BaseModel):
    text: str = Field(
        ...,
        description="The text content of the title of the experience, representing the company name followed by the "
                    "job title.",
        example="Infosys, AI Engineer"
    )
    styles: List[str] = Field(
        ...,
        description="List of styles applied to the text. Styles should belong to the list - ['bold', 'italic']",
        example=["bold"]
    )


class ExperienceBulletPoint(BaseModel):
    content: List[ExperienceTitleContent] = Field(
        ...,
        description="List of content objects representing each bullet point. Each bullet point can contain multiple "
                    "styled text segments.",
        example=[
            {
                "text": "Led a team of 10+ engineers in developing AI solutions for healthcare applications, resulting in a 20% improvement in patient diagnosis accuracy.",
                "styles": []
            },
            {
                "text": "Spearheaded the integration of AI-driven chatbots for customer support, reducing response time by 50% and improving customer satisfaction by 30%.",
                "styles": []
            }
        ]
    )


class Experience(BaseModel):
    title_contents: List[ExperienceTitleContent] = Field(
        ...,
        description="A list of title content objects. This usually contains the main job title and any additional "
                    "styled text, such as company name.",
        example=[
            {"text": "Tech Innovations Inc., Lead AI Engineer", "styles": ["bold"]}
        ]
    )
    subtitle_contents: Optional[List[ExperienceTitleContent]] = Field(
        ...,
        description="A list of subtitle content objects. This field is optional and can contain styled text such as "
                    "location or department.",
        example=[
            {"text": "San Francisco, CA", "styles": []}
        ]
    )
    timeline: List[str] = Field(
        ...,
        description="A list containing the start and end dates or duration of the experience. The month names should "
                    "be restricted to 3 letters. For eaxmaple, 'January' should be 'Jan'",
        example=["Jan 2022 - May 2023"]
    )
    bullet_points: List[ExperienceBulletPoint] = Field(
        ...,
        description="A list of bullet points, where each bullet point contains styled text segments that describe key "
                    "achievements and responsibilities. There should be exactly 3 or 4 bullet points.",
        example=[
            {
                "content": [
                    {
                        "text": "Led a team of 10+ engineers in developing AI solutions for healthcare applications, resulting in a 20% improvement in patient diagnosis accuracy.",
                        "styles": []},
                    {
                        "text": "Spearheaded the integration of AI-driven chatbots for customer support, reducing response time by 50% and improving customer satisfaction by 30%.",
                        "styles": []}
                ]
            }
        ]
    )

    # @field_validator('bullet_points')
    # def check_bullet_points_length(cls, v):
    #     if not 3 <= len(v) <= 4:
    #         raise ValueError('bullet_points must contain between 3 and 4 items')
    #     return v


class Experiences(BaseModel):
    experiences: List[Experience] = Field(
        ...,
        description="A list of Experience objects representing all the work experiences to be included in the resume."
                    "There should be exactly 2 such experiences.",
        example=[
            {
                "title_contents": [
                    {"text": "Tech Innovations Inc., Lead AI Engineer, ", "styles": ["bold"]}
                ],
                "subtitle_contents": [
                    {"text": "San Francisco, CA", "styles": []}
                ],
                "timeline": ["Jan 2022 - Aug 2023"],
                "bullet_points": [
                    {
                        "content": [
                            {"text": "Led a team of 10+ engineers in developing AI solutions...", "styles": []},
                            {"text": "Spearheaded the integration of AI-driven chatbots...", "styles": []}
                        ]
                    }
                ]
            }
        ]
    )

    # @field_validator('experiences')
    # def check_experiences_length(cls, v):
    #     if len(v) != 3:
    #         raise ValueError('Exactly 3 experiences are required')
    #     return v
