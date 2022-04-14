from dataclasses import fields, dataclass
from typing import get_type_hints


class Args:
    @classmethod
    def parse(cls, optionsClass: dataclass, *args: str):
        values = list(
            map(lambda x: cls.parseOption(args, x), fields(optionsClass))
        )
        return optionsClass(*values)

    @classmethod
    def parseOption(cls, args, parameter):
        value = None
        flag = parameter.type.flag
        if get_type_hints(parameter.type)['value'] == bool:
            value = "-" + flag in args
        if get_type_hints(parameter.type)['value'] == int:
            index = args.index("-" + flag)
            value = int(args[index + 1])
        if get_type_hints(parameter.type)['value'] == str:
            index = args.index("-" + flag)
            value = args[index + 1]
        return value


def option(t: type, f: str):
    class Option:
        value: t
        flag = f
    return Option
