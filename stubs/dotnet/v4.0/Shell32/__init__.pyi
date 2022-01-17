from typing import Tuple, Set, Iterable, List


class Folder:
    @property
    def Title(self) -> str: ...


class Folder2:
    @property
    def Title(self) -> str: ...
    def Items(self) -> FolderItems: ...


class FolderItem:
    @property
    def Name(self) -> str: ...
    @Name.setter
    def Name(self, pbs: str) -> None: ...


class FolderItem2:
    def ExtendedProperty(self, bstrPropName: str) -> Object: ...
    @property
    def Name(self) -> str: ...
    @property
    def Path(self) -> str: ...
    def InvokeVerb(self, vVerb: Object) -> None: ...
    @Name.setter
    def Name(self, pbs: str) -> None: ...
    def Verbs(self) -> FolderItemVerbs: ...


class FolderItems:
    pass


class FolderItems2:
    pass


class FolderItems3:
    @property
    def Verbs(self) -> FolderItemVerbs: ...
    def GetEnumerator(self) -> IEnumerator: ...


class FolderItemVerb:
    @property
    def Name(self) -> str: ...


class FolderItemVerbs:
    def GetEnumerator(self) -> IEnumerator: ...
    def Item(self, index: Object) -> FolderItemVerb: ...


class IShellDispatch:
    pass


class IShellDispatch2:
    pass


class IShellDispatch3:
    pass


class IShellDispatch4:
    def NameSpace(self, vDir: Object) -> Folder: ...


class IShellDispatch5:
    pass


class IShellDispatch6:
    pass


class Shell:
    pass


class ShellFolderItem:
    pass
