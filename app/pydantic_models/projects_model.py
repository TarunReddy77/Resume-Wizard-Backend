from my_content.projects import projects

from typing import Optional, List
from pydantic import BaseModel, Field
from typing_extensions import Literal


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

    class Config:
        extra = 'forbid'


class Project(BaseModel):
    title_contents: TitleContents = Field(
        ...,
        description="Title details including type, domain, name, and additional info.",
        example={
            "type": "project",
            "domain": "Generative AI",
            "name": "IntelliChat – An Advanced LLM-Powered Conversational Legal Assistant",
            "additional_info": ""
        }
    )
    subtitle_contents: Optional[str] = Field(
        ...,
        description="Subtitle or any additional information (optional). Prefer None.",
        example=""
    )
    timeline: str = Field(
        ...,
        description="The timeline of the project, including start and end dates. Use only 3 letter abbreviations for month names. For example, Septemember should be written as Sep.",
        example="May 2024 - Present"
    )
    bullet_points: List[str] = Field(
        ...,
        description="List of bullet points describing the project activities and achievements.",
        example=[
            "Developed a modular conversational agent for a law firm to answer queries regarding legal documents and rules utilizing RAG techniques, integrating vector and graph databases for efficient document retrieval, and employing LangChain with Google Vertex AI.",
            "Built a React frontend for seamless user interactions, supporting text, voice, and image generation, while FastAPI backend ensures low-latency communication with various proprietary and open-source LLMs.",
            "Deployed the solution on Hugging Face Spaces with Docker, implementing robust RAG evaluation metrics (precision, recall, F1 score) to optimize performance, achieving significant improvements in retrieval accuracy and response quality."
        ]
    )


class Projects(BaseModel):
    projects: List[Project] = Field(
        ...,
        description="List of projects.",
        example=projects
    )
