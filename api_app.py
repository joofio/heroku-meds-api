from fastapi import FastAPI
import numpy as np
import pandas as pd
from pydantic import BaseModel, Field
import datetime
from enum import Enum
import re
from collections import Counter
from datetime import datetime
import math
from textdistance import damerau_levenshtein,jaro_winkler,jaccard,overlap,lcsseq,lcsstr,ratcliff_obershelp,levenshtein
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/extract-meds")
async def extract_meds():
    return {"message": "Hello World"}
