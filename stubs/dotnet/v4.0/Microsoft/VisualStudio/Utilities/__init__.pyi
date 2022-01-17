__all__ = ['Implementation']
from typing import Tuple, Set, Iterable, List


class BaseDefinitionAttribute(MultipleBaseMetadataAttribute):
    def __init__(self, name: str): ...
    @property
    def BaseDefinition(self) -> str: ...


class ContentTypeAttribute(MultipleBaseMetadataAttribute):
    def __init__(self, name: str): ...
    @property
    def ContentTypes(self) -> str: ...


class ContentTypeDefinition:
    def __init__(self): ...


class DisplayNameAttribute(SingletonBaseMetadataAttribute):
    def __init__(self, displayName: str): ...
    @property
    def DisplayName(self) -> str: ...


class FileExtensionAttribute(SingletonBaseMetadataAttribute):
    def __init__(self, fileExtension: str): ...
    @property
    def FileExtension(self) -> str: ...


class FileExtensionToContentTypeDefinition:
    def __init__(self): ...


class IContentType:
    @property
    def BaseTypes(self) -> Iterable[IContentType]: ...
    @property
    def DisplayName(self) -> str: ...
    @property
    def TypeName(self) -> str: ...
    def IsOfType(self, type: str) -> bool: ...


class IContentTypeDefinition:
    @property
    def BaseDefinitions(self) -> Iterable[str]: ...
    @property
    def Name(self) -> str: ...


class IContentTypeDefinitionSource:
    @property
    def Definitions(self) -> Iterable[IContentTypeDefinition]: ...


class IContentTypeRegistryService:
    def AddContentType(self, typeName: str, baseTypeNames: Iterable[str]) -> IContentType: ...
    @property
    def ContentTypes(self) -> Iterable[IContentType]: ...
    @property
    def UnknownContentType(self) -> IContentType: ...
    def GetContentType(self, typeName: str) -> IContentType: ...
    def RemoveContentType(self, typeName: str) -> None: ...


class IFileExtensionRegistryService:
    def AddFileExtension(self, extension: str, contentType: IContentType) -> None: ...
    def GetContentTypeForExtension(self, extension: str) -> IContentType: ...
    def GetExtensionsForContentType(self, contentType: IContentType) -> Iterable[str]: ...
    def RemoveFileExtension(self, extension: str) -> None: ...


class IObjectTracker:
    def TrackObject(self, value: Object, bucketName: str) -> None: ...


class IOrderable:
    @property
    def After(self) -> Iterable[str]: ...
    @property
    def Before(self) -> Iterable[str]: ...
    @property
    def Name(self) -> str: ...


class IPropertyOwner:
    @property
    def Properties(self) -> PropertyCollection: ...


class MultipleBaseMetadataAttribute:
    pass


class NameAttribute(SingletonBaseMetadataAttribute):
    def __init__(self, name: str): ...
    @property
    def Name(self) -> str: ...


class OrderAttribute(MultipleBaseMetadataAttribute):
    def __init__(self): ...
    @property
    def After(self) -> str: ...
    @property
    def Before(self) -> str: ...
    @After.setter
    def After(self, value: str) -> None: ...
    @Before.setter
    def Before(self, value: str) -> None: ...


class Orderer:
    def Order(itemsToOrder: Iterable[Lazy]) -> IList: ...


class PropertyCollection:
    def __init__(self): ...
    def AddProperty(self, key: Object, property: Object) -> None: ...
    def ContainsProperty(self, key: Object) -> bool: ...
    @property
    def Item(self, key: Object) -> Object: ...
    @property
    def PropertyList(self) -> ReadOnlyCollection: ...
    @overload
    def GetOrCreateSingletonProperty(self, creator: Func) -> T: ...
    @overload
    def GetOrCreateSingletonProperty(self, key: Object, creator: Func) -> T: ...
    @overload
    def GetProperty(self, key: Object) -> TProperty: ...
    @overload
    def GetProperty(self, key: Object) -> Object: ...
    def RemoveProperty(self, key: Object) -> bool: ...
    @Item.setter
    def Item(self, key: Object, value: Object) -> None: ...
    def TryGetProperty(self, key: Object) -> Tuple[bool, TProperty]: ...


class SingletonBaseMetadataAttribute:
    pass
