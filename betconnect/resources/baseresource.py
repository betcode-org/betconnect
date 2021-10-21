from pydantic import BaseModel


class BaseResource(BaseModel):
    _raw: dict

    class Config:
        allow_population_by_field_name = True
        allow_mutation=True
        allow='allow'

    @property
    def info(self):
        return self.dict()

    @property
    def _raw(self, exclude_fields:dict={}):
        assert isinstance(exclude_fields,dict)
        return self.dict(by_alias=True, exclude=exclude_fields)

    # helper function for backwards compatibility ?
    @classmethod
    def create_from_dict(cls, d):
        return cls.parse_obj(d)
