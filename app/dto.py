from pydantic import UUID4, AnyUrl, BaseModel


class AddGift(BaseModel):
    thumb: AnyUrl
    name: str
    url: AnyUrl
    price: float


class UpdateGift(AddGift):
    id: int
    guest_id: UUID4 | None = None


class PostLogin(BaseModel):
    user: str
    password: str


class AddGuest(BaseModel):
    name: str
    phone: str
    is_confirmed: bool = False
    description: str
    max_companion: int
    companion_1: str = None
    companion_2: str = None
    companion_3: str = None
    companion_4: str = None
    companion_5: str = None


class UpdateGuest(AddGuest):
    id: UUID4
