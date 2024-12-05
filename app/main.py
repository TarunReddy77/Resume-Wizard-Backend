from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import subprocess

import json
import traceback
import logging
import os

from resume_creation import get_resume_contents, generate_word_doc, enhance_bullet_point, enhance_experience, \
    enhance_project
from pydantic_models.schemas import JobDescription, GenerateDocumentRequest, EnhanceBulletPointRequest, \
    EnhanceExperienceRequest, EnhanceProjectRequest

logger = logging.getLogger("my_app_logger")
app = FastAPI()

# Allow frontend (Vue.js) to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=["http://localhost:5173"],  # Vite.js development server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.post("/craft-resume/")
# async def craft_resume(job_desc: JobDescription):
#     try:
#         resume = get_resume_contents(job_desc.job_description)
#         return resume
#     except Exception as e:
#         tb_str = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
#         logger.error(tb_str)
#         raise HTTPException(status_code=500, detail=str(e))


@app.post("/craft-resume/")
async def craft_resume(job_desc: JobDescription):
    with open("example_response.json", "r") as file:
        data = json.load(file)
    return data


@app.post("/generate-document/")
async def generate_document(request: GenerateDocumentRequest):
    try:
        logger.info(request.resume_contents['experiences'])
        word_path = generate_word_doc(request.resume_contents)
        if request.doc_type == "docx":
            return FileResponse(word_path,
                                media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                                filename="resume.docx")
        if request.doc_type == 'pdf':
            pdf_dir = os.path.dirname(word_path)  # Get the directory of the Word file
            pdf_path = word_path.replace('.docx', '.pdf')
            libreoffice_path = r"C:\Program Files (x86)\LibreOffice\program\soffice.exe"

            subprocess.run([
                libreoffice_path, '--headless', '--convert-to', 'pdf',
                word_path, '--outdir', pdf_dir
            ], check=True)  # run with libreoffice

            # subprocess.run(["docx2pdf", word_path, pdf_path], check=True)  # run with pywin32

            return FileResponse(pdf_path,
                                media_type='application/pdf',
                                filename="resume.pdf")

    except Exception as e:
        tb_str = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
        logger.error(tb_str)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/enhance-bullet-point/")
async def handle_enhance_bullet_point(request: EnhanceBulletPointRequest):
    try:
        return enhance_bullet_point(request)
    except Exception as e:
        tb_str = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
        logger.error(tb_str)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/enhance-experience/")
async def handle_enhance_experience(request: EnhanceExperienceRequest):
    try:
        return enhance_experience(request)
    except Exception as e:
        tb_str = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
        logger.error(tb_str)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/enhance-project/")
async def handle_enhance_project(request: EnhanceProjectRequest):
    try:
        return enhance_project(request)
    except Exception as e:
        tb_str = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
        logger.error(tb_str)
        raise HTTPException(status_code=500, detail=str(e))
