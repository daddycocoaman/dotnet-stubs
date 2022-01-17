from typing import Tuple, Set, Iterable, List


class XamlAccessLevel(Object):
    @overload
    def AssemblyAccessTo(assembly: Assembly) -> XamlAccessLevel: ...
    @overload
    def AssemblyAccessTo(assemblyName: AssemblyName) -> XamlAccessLevel: ...
    @property
    def AssemblyAccessToAssemblyName(self) -> AssemblyName: ...
    @property
    def PrivateAccessToTypeName(self) -> str: ...
    @overload
    def PrivateAccessTo(type: Type) -> XamlAccessLevel: ...
    @overload
    def PrivateAccessTo(assemblyQualifiedTypeName: str) -> XamlAccessLevel: ...


class XamlLoadPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, allowedAccess: XamlAccessLevel): ...
    @overload
    def __init__(self, allowedAccess: Iterable[XamlAccessLevel]): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, elem: SecurityElement) -> None: ...
    @property
    def AllowedAccess(self) -> List[XamlAccessLevel]: ...
    def Includes(self, requestedAccess: XamlAccessLevel) -> bool: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, other: IPermission) -> IPermission: ...
