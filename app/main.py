from datetime import date
from fastapi import FastAPI, Query, Depends
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Arg в конце для гет а S(schema) в начале для постов

