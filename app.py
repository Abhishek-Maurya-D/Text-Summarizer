# # # # fastapi 
# # # from fastapi import FastAPI, Request
# # # from pydantic import BaseModel
# # # from transformers import T5ForConditionalGeneration, T5Tokenizer
# # # import torch
# # # import re
# # # from fastapi.templating import Jinja2Templates # UI
# # # from fastapi.responses import HTMLResponse 
# # # from fastapi.staticfiles import StaticFiles 

# # # # initialize the FastAPI app
# # # app = FastAPI(title="Text Summarizer App", description="Text Summarization using T5", version="1.0")

# # # # Load model and tokenizer
# # # model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
# # # tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")

# # # # device
# # # if torch.backends.mps.is_available():
# # #     device = torch.device("mps")
# # # elif torch.cuda.is_available():
# # #     device = torch.device("cuda")
# # # else:
# # #     device = torch.device("cpu")
    
# # # print("Device:", device)
# # # model.to(device)

# # # # templating
# # # templates = Jinja2Templates(directory=".")

# # # # Input schema for dialogue => string
# # # class DialogueInput(BaseModel):
# # #     dialogue: str
    
# # # def clean_data(text: str) -> str:
# # #     text = re.sub(r"\r\n", " ", text)   # replacing new lines characters with blank space
# # #     text = re.sub(r"\s+", " ", text)   # replacing new line spaces or any type of space with single blank space
# # #     text = re.sub(r"<.*?>", " ", text)   # replacing html tags with blank space
# # #     text = text.strip().lower() # converting the text to lower case and cleaning the extra training spaces from both sides 
# # #     return text

# # # def summarize_dialogue(dialogue: str) -> str:
# # #     # Clean the input dialogue
# # #     cleaned_dialogue = clean_data(dialogue)
    
# # #     # Tokenize the input dialogue
# # #     inputs = tokenizer(cleaned_dialogue, return_tensors="pt", padding="max_length", max_length=512, truncation=True)
    
# # #     # Move inputs to the appropriate device
# # #     inputs = {key: value.to(device) for key, value in inputs.items()}
    
# # #     # Generate summary using the model
# # #     summary_ids = model.generate(inputs["input_ids"], attention_mask=inputs["attention_mask"], max_length=128, num_beams=4, early_stopping=True)
    
# # #     # Decode the generated summary
# # #     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
# # #     return summary

# # # # API endpoint
# # # @app.post("/summarize/")
# # # async def summarize(dialogue_input: DialogueInput):
# # #     summary = summarize_dialogue(dialogue_input.dialogue)
# # #     return {"summary": summary}

# # # @app.get("/", response_class=HTMLResponse)
# # # async def home(request: Request):
# # #     return templates.TemplateResponse("index.html", {"request": request})


# # # fastapi
# # from fastapi import FastAPI, Request
# # from pydantic import BaseModel
# # from transformers import T5ForConditionalGeneration, T5Tokenizer
# # import torch
# # import re
# # from fastapi.templating import Jinja2Templates  # UI
# # from fastapi.responses import HTMLResponse
# # from fastapi.staticfiles import StaticFiles

# # # initialize the FastAPI app
# # app = FastAPI(title="Text Summarizer App", description="Text Summarization using T5", version="1.0")

# # # Load model and tokenizer
# # model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
# # tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")

# # # device
# # if torch.backends.mps.is_available():
# #     device = torch.device("mps")
# # elif torch.cuda.is_available():
# #     device = torch.device("cuda")
# # else:
# #     device = torch.device("cpu")

# # print("Device:", device)
# # model.to(device)

# # # templating -> points to the "templates" folder where index.html actually lives
# # templates = Jinja2Templates(directory="templates")


# # # Input schema for dialogue => string
# # class DialogueInput(BaseModel):
# #     dialogue: str


# # def clean_data(text: str) -> str:
# #     text = re.sub(r"\r\n", " ", text)   # replacing new lines characters with blank space
# #     text = re.sub(r"\s+", " ", text)    # replacing new line/space sequences with a single blank space
# #     text = re.sub(r"<.*?>", " ", text)  # replacing html tags with blank space
# #     text = text.strip().lower()         # lowercase + trim extra spaces
# #     return text


# # def summarize_dialogue(dialogue: str) -> str:
# #     # Clean the input dialogue
# #     cleaned_dialogue = clean_data(dialogue)

# #     # Tokenize the input dialogue
# #     inputs = tokenizer(cleaned_dialogue, return_tensors="pt", padding="max_length", max_length=512, truncation=True)

# #     # Move inputs to the appropriate device
# #     inputs = {key: value.to(device) for key, value in inputs.items()}

# #     # Generate summary using the model
# #     summary_ids = model.generate(
# #         inputs["input_ids"],
# #         attention_mask=inputs["attention_mask"],
# #         max_length=128,
# #         num_beams=4,
# #         early_stopping=True
# #     )

# #     # Decode the generated summary
# #     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# #     return summary


# # # API endpoint
# # @app.post("/summarize/")
# # async def summarize(dialogue_input: DialogueInput):
# #     summary = summarize_dialogue(dialogue_input.dialogue)
# #     return {"summary": summary}


# # @app.get("/", response_class=HTMLResponse)
# # async def home(request: Request):
# #     return templates.TemplateResponse("index.html", {"request": request})


# # fastapi
# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# from transformers import T5ForConditionalGeneration, T5Tokenizer
# import torch
# import re
# from fastapi.templating import Jinja2Templates  # UI
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles

# # initialize the FastAPI app
# app = FastAPI(title="Text Summarizer App", description="Text Summarization using T5", version="1.0")

# # Load model and tokenizer
# model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
# tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")

# # device
# if torch.backends.mps.is_available():
#     device = torch.device("mps")
# elif torch.cuda.is_available():
#     device = torch.device("cuda")
# else:
#     device = torch.device("cpu")

# print("Device:", device)
# model.to(device)

# # templating -> points to the "templates" folder where index.html actually lives
# templates = Jinja2Templates(directory="templates")


# # Input schema for dialogue => string
# class DialogueInput(BaseModel):
#     dialogue: str


# def clean_data(text: str) -> str:
#     text = re.sub(r"\r\n", " ", text)   # replacing new lines characters with blank space
#     text = re.sub(r"\s+", " ", text)    # replacing new line/space sequences with a single blank space
#     text = re.sub(r"<.*?>", " ", text)  # replacing html tags with blank space
#     text = text.strip().lower()         # lowercase + trim extra spaces
#     return text


# def summarize_dialogue(dialogue: str) -> str:
#     # Clean the input dialogue
#     cleaned_dialogue = clean_data(dialogue)

#     # Tokenize the input dialogue
#     inputs = tokenizer(cleaned_dialogue, return_tensors="pt", padding="max_length", max_length=512, truncation=True)

#     # Move inputs to the appropriate device
#     inputs = {key: value.to(device) for key, value in inputs.items()}

#     # Generate summary using the model
#     summary_ids = model.generate(
#         inputs["input_ids"],
#         attention_mask=inputs["attention_mask"],
#         max_length=128,
#         num_beams=4,
#         early_stopping=True
#     )

#     # Decode the generated summary
#     summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#     return summary


# # API endpoint
# @app.post("/summarize/")
# async def summarize(dialogue_input: DialogueInput):
#     summary = summarize_dialogue(dialogue_input.dialogue)
#     return {"summary": summary}


# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse(request=request, name="index.html")


# fastapi
from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re
from fastapi.templating import Jinja2Templates  # UI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# initialize the FastAPI app
app = FastAPI(title="Text Summarizer App", description="Text Summarization using T5", version="1.0")

# Load model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")

# device
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print("Device:", device)
model.to(device)

# templating -> points to the "templates" folder where index.html actually lives
templates = Jinja2Templates(directory=".")


# Input schema for dialogue => string
class DialogueInput(BaseModel):
    dialogue: str


def clean_data(text: str) -> str:
    text = re.sub(r"\r\n", " ", text)   # replacing new lines characters with blank space
    text = re.sub(r"\s+", " ", text)    # replacing new line/space sequences with a single blank space
    text = re.sub(r"<.*?>", " ", text)  # replacing html tags with blank space
    text = text.strip().lower()         # lowercase + trim extra spaces
    return text


def summarize_dialogue(dialogue: str) -> str:
    # Clean the input dialogue
    cleaned_dialogue = clean_data(dialogue)

    # Tokenize the input dialogue
    inputs = tokenizer(cleaned_dialogue, return_tensors="pt", padding="max_length", max_length=512, truncation=True)

    # Move inputs to the appropriate device
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # Generate summary using the model
    summary_ids = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=128,
        num_beams=4,
        early_stopping=True
    )

    # Decode the generated summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary


# API endpoint
@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    summary = summarize_dialogue(dialogue_input.dialogue)
    return {"summary": summary}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")