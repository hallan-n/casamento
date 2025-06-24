from pydantic import AnyUrl, BaseModel


class AddGift(BaseModel):
    thumb: AnyUrl
    name: str
    url: AnyUrl
    price: float


class UpdateGift(AddGift):
    id: int
