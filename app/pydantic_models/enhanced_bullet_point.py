from pydantic import BaseModel, Field


class EnhancedBulletPoint(BaseModel):
    text: str = Field(
        ...,
        description="The enhanced bullet point according to the instructions provided. The text must not contain any "
                    "additional information that is addressed to the user such as 'Certainly! Here is the "
                    "enhanced bullet point'.",
    )
