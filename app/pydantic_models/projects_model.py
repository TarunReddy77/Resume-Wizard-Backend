from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from my_content.projects import projects


class ProjectTitleContent(BaseModel):
    text: str = Field(
        ...,
        description="The text content of the title of the project. This is a string representing the title. It should "
                    "be of the form (Domain, Title)",
        example=projects[0]['title_contents'][0][0]
    )
    styles: List[str] = Field(
        ...,
        description="List of styles applied to the text. Styles should belong to the list - ['bold', 'italic']",
        example=projects[0]['title_contents'][0][1]
    )


class ProjectBulletPointContent(BaseModel):
    text: str = Field(
        ...,
        description="The text content of the bullet point of the project. This is a string representing the bullet "
                    "point. It should be a succinct bullet point describing a certain aspect of the project.",
        example=projects[0]['bullet_points'][0][0][0]
    )
    styles: List[str] = Field(
        ...,
        description="List of styles applied to the text. Styles should belong to the list - ['bold', 'italic']",
        example=projects[0]['bullet_points'][0][0][1]
    )


class ProjectBulletPoint(BaseModel):
    content: List[ProjectBulletPointContent] = Field(
        ...,
        description="List of content objects representing each bullet point. Each bullet point can contain multiple "
                    "styled text segments.",
        example=[
            {
                "text": "Developed a modular conversational agent for a law firm, leveraging Natural Language Processing (NLP) techniques to analyze legal queries, resulting in a 40% reduction in response time for client inquiries.",
                "styles": []
            },
            {
                "text": "Built a React frontend for seamless user interactions with the model, integrating real-time data processing that improved user engagement by 25%.",
                "styles": []
            },
            {
                "text": "Engineered a predictive maintenance system using machine learning algorithms to analyze sensor data, reducing equipment downtime by 30% and saving the company over $100,000 annually.",
                "styles": []
            },
            {
                "text": "Implemented a reinforcement learning model to optimize inventory management, achieving a 15% reduction in holding costs and enhancing the overall supply chain efficiency.",
                "styles": []
            },
            {
                "text": "Collaborated with cross-functional teams to design and deploy a customer segmentation model using clustering techniques, enabling targeted marketing strategies that increased conversion rates by 20%.",
                "styles": []
            }
        ]
    )

    # @field_validator('content')
    # def check_length(cls, v):
    #     if len(v) > 260:
    #         raise ValueError("Bullet points should be no longer than 260 characters.")
    #     return v


class Project(BaseModel):
    title_contents: List[ProjectTitleContent] = Field(
        ...,
        description="A list of title content objects. This usually contains the main title and any additional styled "
                    "text.",
        example=[
            {"text": "Generative AI, IntelliChat – An Advanced LLM-Powered Conversational Legal Assistant",
             "styles": ["bold"]}
        ]
    )
    subtitle_contents: Optional[List[ProjectTitleContent]] = Field(
        ...,
        description="A list of subtitle content objects. This field is optional and can contain styled text similar "
                    "to the title.",
        example=[
            {"text": "Implemented at ABC Tech Innovations", "styles": []}
        ]
    )
    timeline: List[str] = Field(
        ...,
        description="A list containing the start and end dates or duration of the project. THE MONTH NAMES SHOULD BE "
                    "RESTRICTED TO 3 LETTERS. FOR EXAMPLE, 'JANUARY' SHOULD BE 'JAN'",
        example=["May 2024 - Jun 2024"]
    )
    bullet_points: List[ProjectBulletPoint] = Field(
        ...,
        description="A list of bullet points, where each bullet point contains styled text segments. THERE SHOULD BE "
                    "EXACTLY 3 OR 4 BULLET POINTS.",
        example=[
            {
                "content": [
                    {"text": "Developed a modular conversational agent...", "styles": []},
                    {"text": "Built a React frontend...", "styles": []}
                ]
            }
        ]
    )

    # @field_validator('bullet_points')
    # def check_bullet_points_length(cls, v):
    #     if not 3 <= len(v) <= 4:
    #         raise ValueError('bullet_points must contain EXACTLY 3 OR 4 ITEMS.')
    #     return v

    # @field_validator('bullet_points')
    # def optimize_bullet_points(cls, v):
    #     optimized_points = []
    #     for point in v:
    #         # Join the text segments together for analysis
    #         combined_text = " ".join([segment.text for segment in point.content])
    #         sentences = combined_text.split('. ')
    #         optimized = []
    #         temp = ""
    #
    #         for sentence in sentences:
    #             if len(temp) + len(sentence) + 1 <= 130:
    #                 temp += sentence + ". "
    #             else:
    #                 optimized.append(temp.strip())
    #                 temp = sentence + ". "
    #         optimized.append(temp.strip())
    #
    #         # Reassign the text back to the bullet point's content segments
    #         optimized_segments = []
    #         remaining_text = " ".join(optimized)
    #         for segment in point.content:
    #             if remaining_text.startswith(segment.text):
    #                 optimized_segments.append(segment)
    #                 remaining_text = remaining_text[len(segment.text):].strip()
    #
    #         optimized_points.append({'content': optimized_segments})
    #     return optimized_points


class Projects(BaseModel):
    projects: List[Project] = Field(
        ...,
        description="A list of EXACTLY 3 PROJECT OBJECTS representing all the projects to be included in the resume.",
        example=projects
    )

    # @field_validator('projects')
    # def check_projects_length(cls, v):
    #     if len(v) != 3:
    #         raise ValueError('Exactly 3 projects are required.'.upper())
    #     return v
