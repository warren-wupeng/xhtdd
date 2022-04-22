from dataclasses import Field
from typing import Callable


class InterfaceOptionParser:

    def parse(self, args: list[str], option: Field):
        raise NotImplementedError


class BooleanOptionParser(InterfaceOptionParser):
    def parse(self, args: list[str], option: Field):
        return "-" + option.type.flag in args


class SingleValueOptionParser(InterfaceOptionParser):

    def __init__(self, valueParser: Callable):
        self.valueParser = valueParser

    def parse(self, args: list[str], option: Field):
        index = args.index("-" + option.type.flag)
        value = args[index + 1]
        return self.valueParser(value)
