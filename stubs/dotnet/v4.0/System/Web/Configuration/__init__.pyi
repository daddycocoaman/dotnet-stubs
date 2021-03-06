from typing import Tuple, Set, Iterable, List


class Converter(ConfigurationElement):
    def __init__(self): ...
    @property
    def Name(self) -> str: ...
    @property
    def Type(self) -> str: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Type.setter
    def Type(self, value: str) -> None: ...


class ConvertersCollection(ConfigurationElementCollection):
    def __init__(self): ...
    def Add(self, converter: Converter) -> None: ...
    def Clear(self) -> None: ...
    @property
    def Item(self, index: int) -> Converter: ...
    def Remove(self, converter: Converter) -> None: ...
    @Item.setter
    def Item(self, index: int, value: Converter) -> None: ...


class ScriptingAuthenticationServiceSection(ConfigurationSection):
    def __init__(self): ...
    @property
    def Enabled(self) -> bool: ...
    @property
    def RequireSSL(self) -> bool: ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @RequireSSL.setter
    def RequireSSL(self, value: bool) -> None: ...


class ScriptingJsonSerializationSection(ConfigurationSection):
    def __init__(self): ...
    @property
    def Converters(self) -> ConvertersCollection: ...
    @property
    def MaxJsonLength(self) -> int: ...
    @property
    def RecursionLimit(self) -> int: ...
    @MaxJsonLength.setter
    def MaxJsonLength(self, value: int) -> None: ...
    @RecursionLimit.setter
    def RecursionLimit(self, value: int) -> None: ...


class ScriptingProfileServiceSection(ConfigurationSection):
    def __init__(self): ...
    @property
    def Enabled(self) -> bool: ...
    @property
    def ReadAccessProperties(self) -> Set(str): ...
    @property
    def WriteAccessProperties(self) -> Set(str): ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @ReadAccessProperties.setter
    def ReadAccessProperties(self, value: Set(str)) -> None: ...
    @WriteAccessProperties.setter
    def WriteAccessProperties(self, value: Set(str)) -> None: ...


class ScriptingRoleServiceSection(ConfigurationSection):
    def __init__(self): ...
    @property
    def Enabled(self) -> bool: ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...


class ScriptingScriptResourceHandlerSection(ConfigurationSection):
    def __init__(self): ...
    @property
    def EnableCaching(self) -> bool: ...
    @property
    def EnableCompression(self) -> bool: ...
    @EnableCaching.setter
    def EnableCaching(self, value: bool) -> None: ...
    @EnableCompression.setter
    def EnableCompression(self, value: bool) -> None: ...


class ScriptingSectionGroup(ConfigurationSectionGroup):
    def __init__(self): ...
    @property
    def ScriptResourceHandler(self) -> ScriptingScriptResourceHandlerSection: ...
    @property
    def WebServices(self) -> ScriptingWebServicesSectionGroup: ...


class ScriptingWebServicesSectionGroup(ConfigurationSectionGroup):
    def __init__(self): ...
    @property
    def AuthenticationService(self) -> ScriptingAuthenticationServiceSection: ...
    @property
    def JsonSerialization(self) -> ScriptingJsonSerializationSection: ...
    @property
    def ProfileService(self) -> ScriptingProfileServiceSection: ...
    @property
    def RoleService(self) -> ScriptingRoleServiceSection: ...


class SystemWebExtensionsSectionGroup(ConfigurationSectionGroup):
    def __init__(self): ...
    @property
    def Scripting(self) -> ScriptingSectionGroup: ...
