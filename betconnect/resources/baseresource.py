from pydantic import BaseModel


class BaseResource(BaseModel):
    class Config:
        allow_population_by_field_name = True
        allow_mutation = True
        allow = "allow"  # TODO should this be extra = 'allow'

    @property
    def info(self):
        return self.dict()

    @property
    def _raw(self, exclude_fields: dict = None):
        exclude_fields = exclude_fields if exclude_fields else {}
        assert isinstance(exclude_fields, dict)
        return self.dict(by_alias=True, exclude=exclude_fields)

    # helper function for backwards compatibility ?
    @classmethod
    def create_from_dict(cls, d):
        if "line" in d:
            return cls.parse_obj(d["line"])
        else:
            return cls.parse_obj(d)
