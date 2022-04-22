from dataclasses import fields, dataclass, Field
from typing import get_type_hints

from args.optionParser import BooleanOptionParser, SingleValueOptionParser


class Args:
    @classmethod
    def parse(cls, optionsClass: dataclass, *args: str):
        values = list(
            map(lambda x: cls.parseOption(args, x), fields(optionsClass))
        )
        return optionsClass(*values)

    PARSERS = {
        bool: BooleanOptionParser(),
        int: SingleValueOptionParser(int),
        str: SingleValueOptionParser(str)
    }

    @classmethod
    def parseOption(cls, args, option: Field):
        # flag = option.type.flag
        return cls.PARSERS.get(
            get_type_hints(option.type)['value']).parse(args, option)


def optionFactory(t: type, f: str):
    class Option:
        value: t
        flag = f
    return Option
