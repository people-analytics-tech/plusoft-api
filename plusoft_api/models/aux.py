from dataclasses import asdict, dataclass, is_dataclass


@dataclass
class NestedDataClass:
    def __post_init__(self):
        self.__nested_objs()

    def __nested_objs(self):
        parameters = self.__class__.__annotations__
        for key, value in parameters.items():
            args = getattr(value, "__args__", None)
            args = args[0] if args else None

            if is_dataclass(value) or is_dataclass(args):
                param_value = self.__dict__[key]
                if isinstance(param_value, dict):
                    self.__dict__[key] = value(**param_value)

                elif isinstance(param_value, list):
                    self.__dict__[key] = [args(**item) for item in param_value]


@dataclass
class PayloadDataClass(NestedDataClass):
    @property
    def as_dict(self) -> dict:
        return asdict(self)
