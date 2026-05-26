from pydantic import BaseModel
from typing import List


class CVParsedResponse(BaseModel):
    result: dict