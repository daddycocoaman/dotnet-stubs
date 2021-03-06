from typing import Tuple, Set, Iterable, List


class Atom10FeedFormatter(SyndicationFeedFormatter):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, feedTypeToCreate: Type): ...
    @overload
    def __init__(self, feedToWrite: SyndicationFeed): ...
    def CanRead(self, reader: XmlReader) -> bool: ...
    @property
    def PreserveAttributeExtensions(self) -> bool: ...
    @property
    def PreserveElementExtensions(self) -> bool: ...
    @property
    def Version(self) -> str: ...
    def ReadFrom(self, reader: XmlReader) -> None: ...
    @PreserveAttributeExtensions.setter
    def PreserveAttributeExtensions(self, value: bool) -> None: ...
    @PreserveElementExtensions.setter
    def PreserveElementExtensions(self, value: bool) -> None: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...




class Atom10ItemFormatter(SyndicationItemFormatter):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, itemTypeToCreate: Type): ...
    @overload
    def __init__(self, itemToWrite: SyndicationItem): ...
    def CanRead(self, reader: XmlReader) -> bool: ...
    @property
    def PreserveAttributeExtensions(self) -> bool: ...
    @property
    def PreserveElementExtensions(self) -> bool: ...
    @property
    def Version(self) -> str: ...
    def ReadFrom(self, reader: XmlReader) -> None: ...
    @PreserveAttributeExtensions.setter
    def PreserveAttributeExtensions(self, value: bool) -> None: ...
    @PreserveElementExtensions.setter
    def PreserveElementExtensions(self, value: bool) -> None: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...




class AtomPub10CategoriesDocumentFormatter(CategoriesDocumentFormatter):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, documentToWrite: CategoriesDocument): ...
    @overload
    def __init__(self, inlineDocumentType: Type, referencedDocumentType: Type): ...
    def CanRead(self, reader: XmlReader) -> bool: ...
    @property
    def Version(self) -> str: ...
    def ReadFrom(self, reader: XmlReader) -> None: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...


class AtomPub10ServiceDocumentFormatter(ServiceDocumentFormatter):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, documentTypeToCreate: Type): ...
    @overload
    def __init__(self, documentToWrite: ServiceDocument): ...
    def CanRead(self, reader: XmlReader) -> bool: ...
    @property
    def Version(self) -> str: ...
    def ReadFrom(self, reader: XmlReader) -> None: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...




class CategoriesDocument(Object):
    @overload
    def Create(categories: Collection) -> InlineCategoriesDocument: ...
    @overload
    def Create(linkToCategoriesDocument: Uri) -> ReferencedCategoriesDocument: ...
    @overload
    def Create(categories: Collection, isFixed: bool, scheme: str) -> InlineCategoriesDocument: ...
    @property
    def AttributeExtensions(self) -> Dictionary: ...
    @property
    def BaseUri(self) -> Uri: ...
    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection: ...
    @property
    def Language(self) -> str: ...
    def GetFormatter(self) -> CategoriesDocumentFormatter: ...
    def Load(reader: XmlReader) -> CategoriesDocument: ...
    def Save(self, writer: XmlWriter) -> None: ...
    @BaseUri.setter
    def BaseUri(self, value: Uri) -> None: ...
    @Language.setter
    def Language(self, value: str) -> None: ...


class CategoriesDocumentFormatter(Object):
    def CanRead(self, reader: XmlReader) -> bool: ...
    @property
    def Document(self) -> CategoriesDocument: ...
    @property
    def Version(self) -> str: ...
    def ReadFrom(self, reader: XmlReader) -> None: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...


class InlineCategoriesDocument(CategoriesDocument):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, categories: Iterable[SyndicationCategory]): ...
    @overload
    def __init__(self, categories: Iterable[SyndicationCategory], isFixed: bool, scheme: str): ...
    @property
    def Categories(self) -> Collection: ...
    @property
    def IsFixed(self) -> bool: ...
    @property
    def Scheme(self) -> str: ...
    @IsFixed.setter
    def IsFixed(self, value: bool) -> None: ...
    @Scheme.setter
    def Scheme(self, value: str) -> None: ...


class ReferencedCategoriesDocument(CategoriesDocument):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, link: Uri): ...
    @property
    def Link(self) -> Uri: ...
    @Link.setter
    def Link(self, value: Uri) -> None: ...


class ResourceCollectionInfo(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, title: str, link: Uri): ...
    @overload
    def __init__(self, title: TextSyndicationContent, link: Uri): ...
    @overload
    def __init__(self, title: TextSyndicationContent, link: Uri, categories: Iterable[CategoriesDocument], allowsNewEntries: bool): ...
    @overload
    def __init__(self, title: TextSyndicationContent, link: Uri, categories: Iterable[CategoriesDocument], accepts: Iterable[str]): ...
    @property
    def Accepts(self) -> Collection: ...
    @property
    def AttributeExtensions(self) -> Dictionary: ...
    @property
    def BaseUri(self) -> Uri: ...
    @property
    def Categories(self) -> Collection: ...
    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection: ...
    @property
    def Link(self) -> Uri: ...
    @property
    def Title(self) -> TextSyndicationContent: ...
    @BaseUri.setter
    def BaseUri(self, value: Uri) -> None: ...
    @Link.setter
    def Link(self, value: Uri) -> None: ...
    @Title.setter
    def Title(self, value: TextSyndicationContent) -> None: ...


class Rss20FeedFormatter(SyndicationFeedFormatter):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, feedTypeToCreate: Type): ...
    @overload
    def __init__(self, feedToWrite: SyndicationFeed): ...
    @overload
    def __init__(self, feedToWrite: SyndicationFeed, serializeExtensionsAsAtom: bool): ...
    def CanRead(self, reader: XmlReader) -> bool: ...
    @property
    def PreserveAttributeExtensions(self) -> bool: ...
    @property
    def PreserveElementExtensions(self) -> bool: ...
    @property
    def SerializeExtensionsAsAtom(self) -> bool: ...
    @property
    def Version(self) -> str: ...
    def ReadFrom(self, reader: XmlReader) -> None: ...
    @PreserveAttributeExtensions.setter
    def PreserveAttributeExtensions(self, value: bool) -> None: ...
    @PreserveElementExtensions.setter
    def PreserveElementExtensions(self, value: bool) -> None: ...
    @SerializeExtensionsAsAtom.setter
    def SerializeExtensionsAsAtom(self, value: bool) -> None: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...




class Rss20ItemFormatter(SyndicationItemFormatter):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, itemTypeToCreate: Type): ...
    @overload
    def __init__(self, itemToWrite: SyndicationItem): ...
    @overload
    def __init__(self, itemToWrite: SyndicationItem, serializeExtensionsAsAtom: bool): ...
    def CanRead(self, reader: XmlReader) -> bool: ...
    @property
    def PreserveAttributeExtensions(self) -> bool: ...
    @property
    def PreserveElementExtensions(self) -> bool: ...
    @property
    def SerializeExtensionsAsAtom(self) -> bool: ...
    @property
    def Version(self) -> str: ...
    def ReadFrom(self, reader: XmlReader) -> None: ...
    @PreserveAttributeExtensions.setter
    def PreserveAttributeExtensions(self, value: bool) -> None: ...
    @PreserveElementExtensions.setter
    def PreserveElementExtensions(self, value: bool) -> None: ...
    @SerializeExtensionsAsAtom.setter
    def SerializeExtensionsAsAtom(self, value: bool) -> None: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...




class ServiceDocument(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, workspaces: Iterable[Workspace]): ...
    @property
    def AttributeExtensions(self) -> Dictionary: ...
    @property
    def BaseUri(self) -> Uri: ...
    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection: ...
    @property
    def Language(self) -> str: ...
    @property
    def Workspaces(self) -> Collection: ...
    def GetFormatter(self) -> ServiceDocumentFormatter: ...
    @overload
    def Load(reader: XmlReader) -> ServiceDocument: ...
    @overload
    def Load(reader: XmlReader) -> TServiceDocument: ...
    def Save(self, writer: XmlWriter) -> None: ...
    @BaseUri.setter
    def BaseUri(self, value: Uri) -> None: ...
    @Language.setter
    def Language(self, value: str) -> None: ...


class ServiceDocumentFormatter(Object):
    def CanRead(self, reader: XmlReader) -> bool: ...
    @property
    def Document(self) -> ServiceDocument: ...
    @property
    def Version(self) -> str: ...
    def ReadFrom(self, reader: XmlReader) -> None: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...


class SyndicationCategory(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str): ...
    @overload
    def __init__(self, name: str, scheme: str, label: str): ...
    def Clone(self) -> SyndicationCategory: ...
    @property
    def AttributeExtensions(self) -> Dictionary: ...
    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection: ...
    @property
    def Label(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def Scheme(self) -> str: ...
    @Label.setter
    def Label(self, value: str) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Scheme.setter
    def Scheme(self, value: str) -> None: ...


class SyndicationContent(Object):
    def Clone(self) -> SyndicationContent: ...
    def CreateHtmlContent(content: str) -> TextSyndicationContent: ...
    def CreatePlaintextContent(content: str) -> TextSyndicationContent: ...
    def CreateUrlContent(url: Uri, mediaType: str) -> UrlSyndicationContent: ...
    def CreateXhtmlContent(content: str) -> TextSyndicationContent: ...
    @overload
    def CreateXmlContent(xmlReader: XmlReader) -> XmlSyndicationContent: ...
    @overload
    def CreateXmlContent(dataContractObject: Object) -> XmlSyndicationContent: ...
    @overload
    def CreateXmlContent(dataContractObject: Object, dataContractSerializer: XmlObjectSerializer) -> XmlSyndicationContent: ...
    @overload
    def CreateXmlContent(xmlSerializerObject: Object, serializer: XmlSerializer) -> XmlSyndicationContent: ...
    @property
    def AttributeExtensions(self) -> Dictionary: ...
    @property
    def Type(self) -> str: ...
    def WriteTo(self, writer: XmlWriter, outerElementName: str, outerElementNamespace: str) -> None: ...


class SyndicationElementExtension(Object):
    @overload
    def __init__(self, xmlReader: XmlReader): ...
    @overload
    def __init__(self, dataContractExtension: Object): ...
    @overload
    def __init__(self, dataContractExtension: Object, dataContractSerializer: XmlObjectSerializer): ...
    @overload
    def __init__(self, xmlSerializerExtension: Object, serializer: XmlSerializer): ...
    @overload
    def __init__(self, outerName: str, outerNamespace: str, dataContractExtension: Object): ...
    @overload
    def __init__(self, outerName: str, outerNamespace: str, dataContractExtension: Object, dataContractSerializer: XmlObjectSerializer): ...
    @property
    def OuterName(self) -> str: ...
    @property
    def OuterNamespace(self) -> str: ...
    @overload
    def GetObject(self) -> TExtension: ...
    @overload
    def GetObject(self, serializer: XmlObjectSerializer) -> TExtension: ...
    @overload
    def GetObject(self, serializer: XmlSerializer) -> TExtension: ...
    def GetReader(self) -> XmlReader: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...


class SyndicationElementExtensionCollection:
    @overload
    def Add(self, extension: Object) -> None: ...
    @overload
    def Add(self, xmlReader: XmlReader) -> None: ...
    @overload
    def Add(self, dataContractExtension: Object, serializer: DataContractSerializer) -> None: ...
    @overload
    def Add(self, xmlSerializerExtension: Object, serializer: XmlSerializer) -> None: ...
    @overload
    def Add(self, outerName: str, outerNamespace: str, dataContractExtension: Object) -> None: ...
    @overload
    def Add(self, outerName: str, outerNamespace: str, dataContractExtension: Object, dataContractSerializer: XmlObjectSerializer) -> None: ...
    def GetReaderAtElementExtensions(self) -> XmlReader: ...
    @overload
    def ReadElementExtensions(self, extensionName: str, extensionNamespace: str) -> Collection: ...
    @overload
    def ReadElementExtensions(self, extensionName: str, extensionNamespace: str, serializer: XmlSerializer) -> Collection: ...
    @overload
    def ReadElementExtensions(self, extensionName: str, extensionNamespace: str, serializer: XmlObjectSerializer) -> Collection: ...


class SyndicationFeed(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, items: Iterable[SyndicationItem]): ...
    @overload
    def __init__(self, title: str, description: str, feedAlternateLink: Uri): ...
    @overload
    def __init__(self, title: str, description: str, feedAlternateLink: Uri, items: Iterable[SyndicationItem]): ...
    @overload
    def __init__(self, title: str, description: str, feedAlternateLink: Uri, id: str, lastUpdatedTime: DateTimeOffset): ...
    @overload
    def __init__(self, title: str, description: str, feedAlternateLink: Uri, id: str, lastUpdatedTime: DateTimeOffset, items: Iterable[SyndicationItem]): ...
    def Clone(self, cloneItems: bool) -> SyndicationFeed: ...
    @property
    def AttributeExtensions(self) -> Dictionary: ...
    @property
    def Authors(self) -> Collection: ...
    @property
    def BaseUri(self) -> Uri: ...
    @property
    def Categories(self) -> Collection: ...
    @property
    def Contributors(self) -> Collection: ...
    @property
    def Copyright(self) -> TextSyndicationContent: ...
    @property
    def Description(self) -> TextSyndicationContent: ...
    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection: ...
    @property
    def Generator(self) -> str: ...
    @property
    def Id(self) -> str: ...
    @property
    def ImageUrl(self) -> Uri: ...
    @property
    def Items(self) -> Iterable[SyndicationItem]: ...
    @property
    def Language(self) -> str: ...
    @property
    def LastUpdatedTime(self) -> DateTimeOffset: ...
    @property
    def Links(self) -> Collection: ...
    @property
    def Title(self) -> TextSyndicationContent: ...
    def GetAtom10Formatter(self) -> Atom10FeedFormatter: ...
    @overload
    def GetRss20Formatter(self) -> Rss20FeedFormatter: ...
    @overload
    def GetRss20Formatter(self, serializeExtensionsAsAtom: bool) -> Rss20FeedFormatter: ...
    @overload
    def Load(reader: XmlReader) -> TSyndicationFeed: ...
    @overload
    def Load(reader: XmlReader) -> SyndicationFeed: ...
    def SaveAsAtom10(self, writer: XmlWriter) -> None: ...
    def SaveAsRss20(self, writer: XmlWriter) -> None: ...
    @BaseUri.setter
    def BaseUri(self, value: Uri) -> None: ...
    @Copyright.setter
    def Copyright(self, value: TextSyndicationContent) -> None: ...
    @Description.setter
    def Description(self, value: TextSyndicationContent) -> None: ...
    @Generator.setter
    def Generator(self, value: str) -> None: ...
    @Id.setter
    def Id(self, value: str) -> None: ...
    @ImageUrl.setter
    def ImageUrl(self, value: Uri) -> None: ...
    @Items.setter
    def Items(self, value: Iterable[SyndicationItem]) -> None: ...
    @Language.setter
    def Language(self, value: str) -> None: ...
    @LastUpdatedTime.setter
    def LastUpdatedTime(self, value: DateTimeOffset) -> None: ...
    @Title.setter
    def Title(self, value: TextSyndicationContent) -> None: ...


class SyndicationFeedFormatter(Object):
    def CanRead(self, reader: XmlReader) -> bool: ...
    @property
    def Feed(self) -> SyndicationFeed: ...
    @property
    def Version(self) -> str: ...
    def ReadFrom(self, reader: XmlReader) -> None: ...
    def ToString(self) -> str: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...


class SyndicationItem(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, title: str, content: str, itemAlternateLink: Uri): ...
    @overload
    def __init__(self, title: str, content: str, itemAlternateLink: Uri, id: str, lastUpdatedTime: DateTimeOffset): ...
    @overload
    def __init__(self, title: str, content: SyndicationContent, itemAlternateLink: Uri, id: str, lastUpdatedTime: DateTimeOffset): ...
    def AddPermalink(self, permalink: Uri) -> None: ...
    def Clone(self) -> SyndicationItem: ...
    @property
    def AttributeExtensions(self) -> Dictionary: ...
    @property
    def Authors(self) -> Collection: ...
    @property
    def BaseUri(self) -> Uri: ...
    @property
    def Categories(self) -> Collection: ...
    @property
    def Content(self) -> SyndicationContent: ...
    @property
    def Contributors(self) -> Collection: ...
    @property
    def Copyright(self) -> TextSyndicationContent: ...
    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection: ...
    @property
    def Id(self) -> str: ...
    @property
    def LastUpdatedTime(self) -> DateTimeOffset: ...
    @property
    def Links(self) -> Collection: ...
    @property
    def PublishDate(self) -> DateTimeOffset: ...
    @property
    def SourceFeed(self) -> SyndicationFeed: ...
    @property
    def Summary(self) -> TextSyndicationContent: ...
    @property
    def Title(self) -> TextSyndicationContent: ...
    def GetAtom10Formatter(self) -> Atom10ItemFormatter: ...
    @overload
    def GetRss20Formatter(self) -> Rss20ItemFormatter: ...
    @overload
    def GetRss20Formatter(self, serializeExtensionsAsAtom: bool) -> Rss20ItemFormatter: ...
    @overload
    def Load(reader: XmlReader) -> SyndicationItem: ...
    @overload
    def Load(reader: XmlReader) -> TSyndicationItem: ...
    def SaveAsAtom10(self, writer: XmlWriter) -> None: ...
    def SaveAsRss20(self, writer: XmlWriter) -> None: ...
    @BaseUri.setter
    def BaseUri(self, value: Uri) -> None: ...
    @Content.setter
    def Content(self, value: SyndicationContent) -> None: ...
    @Copyright.setter
    def Copyright(self, value: TextSyndicationContent) -> None: ...
    @Id.setter
    def Id(self, value: str) -> None: ...
    @LastUpdatedTime.setter
    def LastUpdatedTime(self, value: DateTimeOffset) -> None: ...
    @PublishDate.setter
    def PublishDate(self, value: DateTimeOffset) -> None: ...
    @SourceFeed.setter
    def SourceFeed(self, value: SyndicationFeed) -> None: ...
    @Summary.setter
    def Summary(self, value: TextSyndicationContent) -> None: ...
    @Title.setter
    def Title(self, value: TextSyndicationContent) -> None: ...


class SyndicationItemFormatter(Object):
    def CanRead(self, reader: XmlReader) -> bool: ...
    @property
    def Item(self) -> SyndicationItem: ...
    @property
    def Version(self) -> str: ...
    def ReadFrom(self, reader: XmlReader) -> None: ...
    def ToString(self) -> str: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...


class SyndicationLink(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, uri: Uri): ...
    @overload
    def __init__(self, uri: Uri, relationshipType: str, title: str, mediaType: str, length: Int64): ...
    def Clone(self) -> SyndicationLink: ...
    @overload
    def CreateAlternateLink(uri: Uri) -> SyndicationLink: ...
    @overload
    def CreateAlternateLink(uri: Uri, mediaType: str) -> SyndicationLink: ...
    def CreateMediaEnclosureLink(uri: Uri, mediaType: str, length: Int64) -> SyndicationLink: ...
    @overload
    def CreateSelfLink(uri: Uri) -> SyndicationLink: ...
    @overload
    def CreateSelfLink(uri: Uri, mediaType: str) -> SyndicationLink: ...
    @property
    def AttributeExtensions(self) -> Dictionary: ...
    @property
    def BaseUri(self) -> Uri: ...
    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection: ...
    @property
    def Length(self) -> Int64: ...
    @property
    def MediaType(self) -> str: ...
    @property
    def RelationshipType(self) -> str: ...
    @property
    def Title(self) -> str: ...
    @property
    def Uri(self) -> Uri: ...
    def GetAbsoluteUri(self) -> Uri: ...
    @BaseUri.setter
    def BaseUri(self, value: Uri) -> None: ...
    @Length.setter
    def Length(self, value: Int64) -> None: ...
    @MediaType.setter
    def MediaType(self, value: str) -> None: ...
    @RelationshipType.setter
    def RelationshipType(self, value: str) -> None: ...
    @Title.setter
    def Title(self, value: str) -> None: ...
    @Uri.setter
    def Uri(self, value: Uri) -> None: ...


class SyndicationPerson(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, email: str): ...
    @overload
    def __init__(self, email: str, name: str, uri: str): ...
    def Clone(self) -> SyndicationPerson: ...
    @property
    def AttributeExtensions(self) -> Dictionary: ...
    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection: ...
    @property
    def Email(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def Uri(self) -> str: ...
    @Email.setter
    def Email(self, value: str) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Uri.setter
    def Uri(self, value: str) -> None: ...


class SyndicationVersions(Object):
    pass


class TextSyndicationContent(SyndicationContent):
    @overload
    def __init__(self, text: str): ...
    @overload
    def __init__(self, text: str, textKind: TextSyndicationContentKind): ...
    def Clone(self) -> SyndicationContent: ...
    @property
    def Text(self) -> str: ...
    @property
    def Type(self) -> str: ...


class TextSyndicationContentKind:
    Plaintext = 0
    Html = 1
    XHtml = 2


class UrlSyndicationContent(SyndicationContent):
    def __init__(self, url: Uri, mediaType: str): ...
    def Clone(self) -> SyndicationContent: ...
    @property
    def Type(self) -> str: ...
    @property
    def Url(self) -> Uri: ...


class Workspace(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, title: str, collections: Iterable[ResourceCollectionInfo]): ...
    @overload
    def __init__(self, title: TextSyndicationContent, collections: Iterable[ResourceCollectionInfo]): ...
    @property
    def AttributeExtensions(self) -> Dictionary: ...
    @property
    def BaseUri(self) -> Uri: ...
    @property
    def Collections(self) -> Collection: ...
    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection: ...
    @property
    def Title(self) -> TextSyndicationContent: ...
    @BaseUri.setter
    def BaseUri(self, value: Uri) -> None: ...
    @Title.setter
    def Title(self, value: TextSyndicationContent) -> None: ...


class XmlSyndicationContent(SyndicationContent):
    @overload
    def __init__(self, reader: XmlReader): ...
    @overload
    def __init__(self, type: str, extension: SyndicationElementExtension): ...
    @overload
    def __init__(self, type: str, dataContractExtension: Object, dataContractSerializer: XmlObjectSerializer): ...
    @overload
    def __init__(self, type: str, xmlSerializerExtension: Object, serializer: XmlSerializer): ...
    def Clone(self) -> SyndicationContent: ...
    @property
    def Extension(self) -> SyndicationElementExtension: ...
    @property
    def Type(self) -> str: ...
    def GetReaderAtContent(self) -> XmlDictionaryReader: ...
    @overload
    def ReadContent(self) -> TContent: ...
    @overload
    def ReadContent(self, dataContractSerializer: XmlObjectSerializer) -> TContent: ...
    @overload
    def ReadContent(self, serializer: XmlSerializer) -> TContent: ...
