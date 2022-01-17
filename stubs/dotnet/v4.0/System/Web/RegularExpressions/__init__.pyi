from typing import Tuple, Set, Iterable, List


class AspCodeRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class AspEncodedExprRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class AspExprRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class CommentRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class DatabindExprRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class DataBindRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class DirectiveRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class EndTagRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class GTRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class IncludeRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class LTRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class RunatServerRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class ServerTagsRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class SimpleDirectiveRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class TagRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class TagRegex35(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...


class TextRegex(Regex):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, A_1: TimeSpan): ...
