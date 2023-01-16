from google.cloud import ndb
from pydantic import BaseModel
from typing import Optional
client = ndb.Client()

class MovieSchema(BaseModel):
    key: Optional[int]
    title: str
    year: int
    overview: str

class Movie(ndb.Model):
    title = ndb.StringProperty()
    year = ndb.IntegerProperty()
    overview = ndb.StringProperty()

    def ser(self):
        data = self.to_dict()
        data["key"] = self.key.id()
        return data