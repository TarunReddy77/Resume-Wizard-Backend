from pydantic_models.projects_model import Projects
from pydantic_models.experiences_model import Experiences
from pydantic_models.skills_model import Skills
from pydantic_models.educations_model import Educations
from pydantic_models.personal_info_model import PersonalInfo
from pydantic_models.resume_model import Resume

from prompts.experiences_prompt import experiences_prompt
from prompts.skills_prompt import skills_prompt
from prompts.projects_prompt import projects_prompt

from my_content.personal_info import personal_info
from my_content.education import educations

from pydantic_models.schemas import EnhanceBulletPointRequest, EnhanceExperienceRequest, EnhanceProjectRequest

# from gpt import generate_resume_content
from langchain_operations import generate_resume_content, enhance_bullet_point as enhance_bullet_point_logic, enhance_experience as enhance_experience_logic, enhance_project as enhance_project_logic

from word_doc_creation import create_document

import os
import logging

logger = logging.getLogger("my_app_logger")

educations = Educations(educations=educations).educations
personal_info = PersonalInfo(name=personal_info['name'],
                             location=personal_info['location'],
                             phone=personal_info['phone'],
                             email=personal_info['email'],
                             linkedin=personal_info['linkedin'])


def get_resume_contents(job_desc):
    projects = generate_resume_content(projects_prompt, job_desc, Projects).projects
    logger.info('got projects model: %s', projects)
    experiences = generate_resume_content(experiences_prompt, job_desc, Experiences).experiences
    logger.info('got experiences model: %s', experiences)
    skills = generate_resume_content(skills_prompt, job_desc, Skills).skills
    logger.info('got skills model: %s', skills)

    resume_contents = Resume(personal_info=personal_info, educations=educations, skills=skills, experiences=experiences,
                             projects=projects)
    return resume_contents


def generate_word_doc(resume_contents):
    word_doc = create_document(resume_contents)
    logger.info('word doc created')

    current_dir = os.path.dirname(os.path.abspath(__file__))
    resume_path = os.path.join(current_dir, 'resumes', 'resume.docx')
    if os.path.exists(resume_path):
        os.remove(resume_path)
    word_doc.save(resume_path)
    logger.info('word doc saved')
    return resume_path


def enhance_bullet_point(enhancement_request: EnhanceBulletPointRequest):
    return enhance_bullet_point_logic(enhancement_request)


def enhance_experience(enhancement_request: EnhanceExperienceRequest):
    return enhance_experience_logic(enhancement_request)


def enhance_project(enhancement_request: EnhanceProjectRequest):
    return enhance_project_logic(enhancement_request)
