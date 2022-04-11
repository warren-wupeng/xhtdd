import dataclasses
from dataclasses import fields, dataclass


class Args:
    @classmethod
    def parse(cls, optionsClass: dataclass, *args: str):
        # flag = fields(optionsClass)[0].type.flag

        return optionsClass(True)


def option(t: type, f: str):
    class Option:
        value: t
        flag = f
    return Option