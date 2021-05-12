from typing import List, Set, Any

class Setting(object):
    def __init__(self, default: Any):
        self.default = default
    def parse(self,
            current: Any,
            value:   str) -> Any:
        return self.simple(value)
    def simple(self, value: str) -> Any:
        return value

    def serialize(self, value: Any) -> Any:
        return value
    def deserialize(self, value: Any) -> Any:
        return value

class SettingString(Setting):
    pass

class SettingBool(Setting):
    def simple(self, value: str) -> bool:
        if   value in {"on", "yes", "1", "true"}:
            return True
        elif value in {"off", "no", "0", "false"}:
            return False
        else:
            raise ValueError("value not 'on' or 'off'")

class SettingInt(Setting):
    def simple(self, value: str) -> int:
        return int(value)

class SettingFloat(Setting):
    def simple(self, value: str) -> float:
        return float(value)

class SettingSet(Setting):
    def parse(self,
            current: Set[str],
            value:   str
            ) -> List[str]:

        current = current.copy()
        op      = value[:1]
        items   = set(value[1:].split(","))

        if   op == "+":
            current |= items
        elif op == "-":
            current -= items
        elif op == "=":
            current  = items
        else:
            raise ValueError(f"unknown set operator '{op}'")

        return current

    # json doesnt like sets :[
    def serialize(self, value: Set[str]) -> List[str]:
        return list(value)
    def deserialize(self, value: List[str]) -> Set[str]:
        return set(value)

class SettingEnum(SettingSet):
    def __init__(self,
            default: Any,
            options: Set[str]):
        self._options = options
        super().__init__(default)

    def parse(self,
            current: Set[str],
            value:   str
            ) -> Set[str]:

        base    = super().parse(current, value)
        unknown = list(sorted(base-self._options))

        if unknown:
            raise ValueError(f"unknown value '{unknown[0]}'")
        else:
            return base
