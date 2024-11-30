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

from gpt import get_content
from word import create_document

import os
import logging

logger = logging.getLogger("my_app_logger")

educations = Educations(educations=educations).educations
personal_info = PersonalInfo(name=personal_info['name'],
                             location=personal_info['location'],
                             phone=personal_info['phone'],
                             email=personal_info['email'],
                             linkedin=personal_info['linkedin'])


def create_word_doc(job_desc):
    projects = get_content(projects_prompt, job_desc, Projects).projects
    logger.info('got projects model: %s', projects)
    experiences = get_content(experiences_prompt, job_desc, Experiences).experiences
    logger.info('got experiences model: %s', experiences)
    skills = get_content(skills_prompt, job_desc, Skills).skills
    logger.info('got skills model: %s', skills)

    resume_contents = Resume(personal_info=personal_info, educations=educations, skills=skills, experiences=experiences,
                             projects=projects)
    return resume_contents


def generate_word_doc(resume_contents):
    word_doc = create_document(resume_contents)
    logger.info('doc created')

    current_dir = os.path.dirname(os.path.abspath(__file__))
    resume_path = os.path.join(current_dir, 'resumes', 'resume.docx')
    word_doc.save(resume_path)
    return resume_path
