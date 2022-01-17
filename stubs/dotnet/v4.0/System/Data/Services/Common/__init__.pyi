from typing import Tuple, Set, Iterable, List


class DataServiceEntityAttribute(Attribute):
    def __init__(self): ...


class DataServiceKeyAttribute(Attribute):
    @overload
    def __init__(self, keyName: str): ...
    @overload
    def __init__(self, keyNames: Set(str)): ...
    @property
    def KeyNames(self) -> ReadOnlyCollection: ...


class DataServiceProtocolVersion:
    V1 = 0
    V2 = 1


class EntityPropertyMappingAttribute(Attribute):
    @overload
    def __init__(self, sourcePath: str, targetSyndicationItem: SyndicationItemProperty, targetTextContentKind: SyndicationTextContentKind, keepInContent: bool): ...
    @overload
    def __init__(self, sourcePath: str, targetPath: str, targetNamespacePrefix: str, targetNamespaceUri: str, keepInContent: bool): ...
    @property
    def KeepInContent(self) -> bool: ...
    @property
    def SourcePath(self) -> str: ...
    @property
    def TargetNamespacePrefix(self) -> str: ...
    @property
    def TargetNamespaceUri(self) -> str: ...
    @property
    def TargetPath(self) -> str: ...
    @property
    def TargetSyndicationItem(self) -> SyndicationItemProperty: ...
    @property
    def TargetTextContentKind(self) -> SyndicationTextContentKind: ...


class EntitySetAttribute(Attribute):
    def __init__(self, entitySet: str): ...
    @property
    def EntitySet(self) -> str: ...


class HasStreamAttribute(Attribute):
    def __init__(self): ...


class SyndicationItemProperty:
    CustomProperty = 0
    AuthorEmail = 1
    AuthorName = 2
    AuthorUri = 3
    ContributorEmail = 4
    ContributorName = 5
    ContributorUri = 6
    Updated = 7
    Published = 8
    Rights = 9
    Summary = 10
    Title = 11


class SyndicationTextContentKind:
    Plaintext = 0
    Html = 1
    Xhtml = 2
