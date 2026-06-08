from fastapi import FastAPI
from routes import cv_parser, upload_files

app = FastAPI()
app.include_router(upload_files.api_route)
app.include_router(cv_parser.router)
