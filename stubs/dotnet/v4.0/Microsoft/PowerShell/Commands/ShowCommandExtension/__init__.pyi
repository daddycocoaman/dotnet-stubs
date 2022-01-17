from typing import Tuple, Set, Iterable, List


class ShowCommandCommandInfo:
    @overload
    def __init__(self, other: CommandInfo): ...
    @overload
    def __init__(self, other: PSObject): ...
    @property
    def CommandType(self) -> CommandTypes: ...
    @property
    def Definition(self) -> str: ...
    @property
    def Module(self) -> ShowCommandModuleInfo: ...
    @property
    def ModuleName(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def ParameterSets(self) -> ICollection: ...


class ShowCommandModuleInfo:
    @overload
    def __init__(self, other: PSModuleInfo): ...
    @overload
    def __init__(self, other: PSObject): ...
    @property
    def Name(self) -> str: ...


class ShowCommandParameterInfo:
    @overload
    def __init__(self, other: CommandParameterInfo): ...
    @overload
    def __init__(self, other: PSObject): ...
    @property
    def HasParameterSet(self) -> bool: ...
    @property
    def IsMandatory(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def ParameterType(self) -> ShowCommandParameterType: ...
    @property
    def Position(self) -> int: ...
    @property
    def ValidParamSetValues(self) -> List[str]: ...
    @property
    def ValueFromPipeline(self) -> bool: ...


class ShowCommandParameterSetInfo:
    @overload
    def __init__(self, other: CommandParameterSetInfo): ...
    @overload
    def __init__(self, other: PSObject): ...
    @property
    def IsDefault(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Parameters(self) -> ICollection: ...


class ShowCommandParameterType:
    @overload
    def __init__(self, other: Type): ...
    @overload
    def __init__(self, other: PSObject): ...
    @property
    def ElementType(self) -> ShowCommandParameterType: ...
    @property
    def EnumValues(self) -> ArrayList: ...
    @property
    def FullName(self) -> str: ...
    @property
    def HasFlagAttribute(self) -> bool: ...
    @property
    def ImplementsDictionary(self) -> bool: ...
    @property
    def IsArray(self) -> bool: ...
    @property
    def IsBoolean(self) -> bool: ...
    @property
    def IsEnum(self) -> bool: ...
    @property
    def IsScriptBlock(self) -> bool: ...
    @property
    def IsString(self) -> bool: ...
    @property
    def IsSwitch(self) -> bool: ...
