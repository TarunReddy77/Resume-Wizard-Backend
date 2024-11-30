from pydantic import BaseModel, Field
from typing import List


class SkillCategory(BaseModel):
    category: str = Field(
        ...,
        description="The name of the skill category, representing a broader area of expertise.",
        example="Machine Learning"
    )
    tools: List[str] = Field(
        ...,
        description="A list of tools, libraries, or technologies associated with the skill category. Each item in "
                    "this list represents a specific skill or technology.",
        example=["TensorFlow", "PyTorch", "scikit-learn", "Keras", "XGBoost"]
    )


class Skills(BaseModel):
    skills: List[SkillCategory] = Field(
        ...,
        description="A list of skill categories, each containing a list of relevant tools, libraries, "
                    "or technologies. This structure allows for an organized representation of technical and soft "
                    "skills on a resume.",
        example=[
            {
                "category": "Machine Learning",
                "tools": ["TensorFlow", "PyTorch", "scikit-learn", "Keras", "XGBoost"]
            },
            {
                "category": "Programming Languages",
                "tools": ["Python", "Java", "C++", "SQL", "Bash"]
            }
        ]
    )
