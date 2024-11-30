from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
# from langchain_google_vertexai import ChatVertexAI
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import SystemMessage, trim_messages
from operator import itemgetter
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate

from pydantic_models.schemas import EnhanceBulletPointRequest, EnhanceExperienceRequest, EnhanceProjectRequest
from pydantic_models.enhanced_bullet_point import EnhancedBulletPoint
from pydantic_models.experiences_model import Experience
from pydantic_models.projects_model import Project


from dotenv import load_dotenv
import os
import yaml

import logging
import logging_config  # This ensures that the logging is configured as per logging_config.py

logger = logging.getLogger("my_app_logger")

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    raise ValueError("OPENAI_API_KEY is not set")

tavily_api_key = os.getenv("TAVILY_API_KEY")
if tavily_api_key is None:
    raise ValueError("TAVILY_API_KEY is not set")

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'config.yaml')

with open(config_path) as f:
    config = yaml.safe_load(f)

# Create the agent
# memory = MemorySaver()
# search = TavilySearchResults(max_results=2)
# tools = [search]


# Use the agent
# llm_config = {"configurable": {"thread_id": "abc123"}}

chat_history = InMemoryChatMessageHistory()
session_id = 'abc124'


def get_chat_history(chat_id: str) -> BaseChatMessageHistory:
    return chat_history


# def get_model():
#     model = ChatOpenAI(model_name=config['model'])
#     return model


# def get_messages_trimmer(model):
#     trimmer = trim_messages(
#         max_tokens=config["langchain"]["messages_trimmer"]["max_tokens"],
#         strategy="last",
#         token_counter=model,
#         include_system=True,
#         allow_partial=False,
#         start_on="human",
#     )
#     return trimmer


def get_prompt(system_message):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_message,
            ),
            MessagesPlaceholder(variable_name="messages")
        ]
    )
    return prompt


def get_chain(prompt, model):
    chain = (
            RunnablePassthrough.assign(messages=itemgetter("messages"))
            | prompt
            | model
    )
    return chain


def get_runnable_with_history(chain):
    runnable = RunnableWithMessageHistory(
        chain,
        get_chat_history,
        input_messages_key="messages",
    )
    return runnable


def get_langchain_runnable(model, prompt):
    chain = get_chain(prompt, model)
    runnable_with_history = get_runnable_with_history(chain)
    return runnable_with_history


# def get_response(text: str, message_history, config):
#     global chat_history
#     chat_history = message_history
#     for chunk in get_langchain_runnable().stream({"messages": [HumanMessage(content=text)]}, config=config):
#         yield chunk.content


def generate_resume_content(prompt, job_desc, response_format):
    model = ChatOpenAI(model_name=config['model'], response_format=response_format)
    prompt = get_prompt(prompt)
    # agent_executor = create_react_agent(model, tools, checkpointer=memory)
    # return agent_executor.stream({"messages": [SystemMessage(content=prompt), HumanMessage(content=job_desc)]}, llm_config)

    response = get_langchain_runnable(model, prompt).invoke({"messages": [HumanMessage(content=job_desc)]},
                                                            config={"configurable": {
                                                                "session_id": session_id}}).additional_kwargs['parsed']

    return response


def get_enhance_bullet_point_prompt(enhancement_request: EnhanceBulletPointRequest):
    prompt = f'''{enhancement_request.bullet_point_text}
    
    Given above is bullet point number {enhancement_request.bullet_point_index + 1} in the element number 
    {enhancement_request.item_index + 1} in the {enhancement_request.section} section of the resume. Please modify and 
    enhance the bullet point according to the instructions given below:
    
    {enhancement_request.enhancement_instructions}
    '''
    return prompt


def enhance_bullet_point(enhancement_request: EnhanceBulletPointRequest):
    model = ChatOpenAI(model_name=config['model'], response_format=EnhancedBulletPoint)
    prompt = get_prompt('')
    response = get_langchain_runnable(model, prompt).invoke(
        {"messages": [HumanMessage(content=get_enhance_bullet_point_prompt(enhancement_request))]},
        config={"configurable": {"session_id": session_id}}).additional_kwargs['parsed']

    return response


def get_enhance_experience_prompt(enhancement_request: EnhanceExperienceRequest):
    prompt = f'''{enhancement_request.experience}

    Given above is experience number {enhancement_request.index + 1} in the experiences section of the resume. Please 
    modify and enhance the experience according to the instructions given below:

    {enhancement_request.enhancement_instructions}
    '''
    return prompt


def enhance_experience(enhancement_request: EnhanceExperienceRequest):
    model = ChatOpenAI(model_name=config['model'], response_format=Experience)
    prompt = get_prompt('')
    response = get_langchain_runnable(model, prompt).invoke(
        {"messages": [HumanMessage(content=get_enhance_experience_prompt(enhancement_request))]},
        config={"configurable": {"session_id": session_id}}).additional_kwargs['parsed']

    return response


def get_enhance_project_prompt(enhancement_request: EnhanceProjectRequest):
    prompt = f'''{enhancement_request.project}

    Given above is project number {enhancement_request.index + 1} in the projects section of the resume. Please 
    modify and enhance the project according to the instructions given below:

    {enhancement_request.enhancement_instructions}
    '''
    return prompt


def enhance_project(enhancement_request: EnhanceProjectRequest):
    model = ChatOpenAI(model_name=config['model'], response_format=Project)
    prompt = get_prompt('')
    response = get_langchain_runnable(model, prompt).invoke(
        {"messages": [HumanMessage(content=get_enhance_project_prompt(enhancement_request))]},
        config={"configurable": {"session_id": session_id}}).additional_kwargs['parsed']

    return response
