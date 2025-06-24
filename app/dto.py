from pydantic import BaseModel, AnyUrl

class AddGift(BaseModel):
    thumb: AnyUrl
    name: str
    url: AnyUrl
    price: float

class UpdateGift(AddGift):
    id: int