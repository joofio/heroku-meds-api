from fastapi import FastAPI
import numpy as np
import pandas as pd
from pydantic import BaseModel, Field
from enum import Enum
import re
from collections import Counter
import datetime
import math
from textdistance import damerau_levenshtein,jaro_winkler,jaccard,overlap,lcsseq,lcsstr,ratcliff_obershelp,levenshtein
import json
from typing import List, Optional


app = FastAPI()

errors_dict=pd.read_csv("truth_error.csv")
class Summary(BaseModel):
    corpus: str

class Output(BaseModel):
    display: str
    ID: str
    atc: str

class Result(BaseModel):
    input: str
    output: Output

class Extraction(BaseModel):
    results: List[Result]
    timestamp: datetime.date


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/extract-meds",response_model=Extraction)
async def extract_meds(summary: Summary):
    final_list=[]
    for x in summary.corpus.split():
        if len(errors_dict[errors_dict["error"]==x.lower()])>0:
            key=errors_dict[errors_dict["error"]==x.lower()]["truth"].values[0]
            doc={"input":x,"output":{"display":key,"ID":"","atc":""}}
            final_list.append(doc)
        if len(errors_dict[errors_dict["truth"]==x.lower()])>0:
            key=errors_dict[errors_dict["truth"]==x.lower()]["truth"].values[0]
            doc={"input":x,"output":{"display":key,"ID":"","atc":""}}
            final_list.append(doc)
    return {"results":final_list,"timestamp":datetime.datetime.now()}