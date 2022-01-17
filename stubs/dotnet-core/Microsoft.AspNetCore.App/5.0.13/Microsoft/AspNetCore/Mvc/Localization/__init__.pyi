from typing import Tuple, Set, Iterable, List


class HtmlLocalizer:
    def __init__(self, localizer: IStringLocalizer): ...
    @property
    def Item(self, name: str) -> LocalizedHtmlString: ...
    @property
    def Item(self, name: str, arguments: Set(Object)) -> LocalizedHtmlString: ...
    def GetAllStrings(self, includeParentCultures: bool) -> Iterable[LocalizedString]: ...
    @overload
    def GetString(self, name: str) -> LocalizedString: ...
    @overload
    def GetString(self, name: str, arguments: Set(Object)) -> LocalizedString: ...




class HtmlLocalizerExtensions:
    def GetAllStrings(htmlLocalizer: IHtmlLocalizer) -> Iterable[LocalizedString]: ...
    @overload
    def GetHtml(htmlLocalizer: IHtmlLocalizer, name: str) -> LocalizedHtmlString: ...
    @overload
    def GetHtml(htmlLocalizer: IHtmlLocalizer, name: str, arguments: Set(Object)) -> LocalizedHtmlString: ...


class HtmlLocalizerFactory:
    def __init__(self, localizerFactory: IStringLocalizerFactory): ...
    @overload
    def Create(self, resourceSource: Type) -> IHtmlLocalizer: ...
    @overload
    def Create(self, baseName: str, location: str) -> IHtmlLocalizer: ...


class IHtmlLocalizer:
    @property
    def Item(self, name: str) -> LocalizedHtmlString: ...
    @property
    def Item(self, name: str, arguments: Set(Object)) -> LocalizedHtmlString: ...
    def GetAllStrings(self, includeParentCultures: bool) -> Iterable[LocalizedString]: ...
    @overload
    def GetString(self, name: str) -> LocalizedString: ...
    @overload
    def GetString(self, name: str, arguments: Set(Object)) -> LocalizedString: ...




class IHtmlLocalizerFactory:
    @overload
    def Create(self, resourceSource: Type) -> IHtmlLocalizer: ...
    @overload
    def Create(self, baseName: str, location: str) -> IHtmlLocalizer: ...


class IViewLocalizer:
    pass


class LocalizedHtmlString:
    @overload
    def __init__(self, name: str, value: str): ...
    @overload
    def __init__(self, name: str, value: str, isResourceNotFound: bool): ...
    @overload
    def __init__(self, name: str, value: str, isResourceNotFound: bool, arguments: Set(Object)): ...
    @property
    def IsResourceNotFound(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Value(self) -> str: ...
    def WriteTo(self, writer: TextWriter, encoder: HtmlEncoder) -> None: ...


class ViewLocalizer:
    def __init__(self, localizerFactory: IHtmlLocalizerFactory, hostingEnvironment: IWebHostEnvironment): ...
    def Contextualize(self, viewContext: ViewContext) -> None: ...
    @property
    def Item(self, key: str) -> LocalizedHtmlString: ...
    @property
    def Item(self, key: str, arguments: Set(Object)) -> LocalizedHtmlString: ...
    def GetAllStrings(self, includeParentCultures: bool) -> Iterable[LocalizedString]: ...
    @overload
    def GetString(self, name: str) -> LocalizedString: ...
    @overload
    def GetString(self, name: str, values: Set(Object)) -> LocalizedString: ...
