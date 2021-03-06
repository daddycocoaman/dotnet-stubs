from typing import Tuple, Set, Iterable, List


class DefaultManagementInstaller(Installer):
    def __init__(self): ...


class InstrumentationManager(Object):
    def Publish(value: Object) -> None: ...
    def RegisterAssembly(managementAssembly: Assembly) -> None: ...
    def RegisterType(managementType: Type) -> None: ...
    def Revoke(value: Object) -> None: ...
    def UnregisterAssembly(managementAssembly: Assembly) -> None: ...
    def UnregisterType(managementType: Type) -> None: ...


class ManagedCommonProvider(Object):
    def __init__(self): ...


class ManagementQualifierAttribute(Attribute):
    def __init__(self, name: str): ...
    @property
    def Flavor(self) -> ManagementQualifierFlavors: ...
    @property
    def Name(self) -> str: ...
    @property
    def Value(self) -> Object: ...
    @Flavor.setter
    def Flavor(self, value: ManagementQualifierFlavors) -> None: ...
    @Value.setter
    def Value(self, value: Object) -> None: ...


class ManagementQualifierFlavors:
    Amended = 1
    DisableOverride = 2
    ClassOnly = 4
    ThisClassOnly = 8


class WmiProviderInstallationException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
