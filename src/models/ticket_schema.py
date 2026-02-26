from pydantic import BaseModel, Field
from typing import Literal

class CategorizedTicket(BaseModel):
    intent: Literal["Technical issue", "Billing inquiry", "Cancellation request", "Product inquiry", "Refund request"] = Field(
        description="The category of the ticket."
    )
    priority: Literal["Low", "Medium", "High", "Critical"] = Field(
        description="Priority level."
    )
    sentiment: Literal["Positive", "Neutral", "Frustrated", "Angry"] = Field(
        description="The emotional tone."
    )
    summary: str = Field(description="1-sentence summary.")