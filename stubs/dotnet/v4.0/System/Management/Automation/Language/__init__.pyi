from typing import Tuple, Set, Iterable, List


class StaticBindingError(Object):
    @property
    def BindingException(self) -> ParameterBindingException: ...
    @property
    def CommandElement(self) -> CommandElementAst: ...
