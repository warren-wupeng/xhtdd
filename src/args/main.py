from dataclasses import fields, dataclass
from typing import get_type_hints


class Args:
    @classmethod
    def parse(cls, optionsClass: dataclass, *args: str):
        parameter = fields(optionsClass)[0]
        flag = parameter.type.flag

        value = None
        if get_type_hints(parameter.type)['value'] == bool:
            value = "-" + flag in args
        if get_type_hints(parameter.type)['value'] == int:
            index = args.index("-" + flag)
            value = int(args[index+1])
        if get_type_hints(parameter.type)['value'] == str:
            index = args.index("-" + flag)
            value = args[index+1]
        return optionsClass(value)


def option(t: type, f: str):
    class Option:
        value: t
        flag = f
    return Option
