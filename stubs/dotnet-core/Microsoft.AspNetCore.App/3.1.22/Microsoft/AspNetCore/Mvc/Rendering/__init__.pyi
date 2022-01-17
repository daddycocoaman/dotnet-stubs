from typing import Tuple, Set, Iterable, List


class ViewContext(ActionContext):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, viewContext: ViewContext, view: IView, viewData: ViewDataDictionary, writer: TextWriter): ...
    @overload
    def __init__(self, actionContext: ActionContext, view: IView, viewData: ViewDataDictionary, tempData: ITempDataDictionary, writer: TextWriter, htmlHelperOptions: HtmlHelperOptions): ...
    @property
    def ClientValidationEnabled(self) -> bool: ...
    @property
    def ExecutingFilePath(self) -> str: ...
    @property
    def FormContext(self) -> FormContext: ...
    @property
    def Html5DateRenderingMode(self) -> Html5DateRenderingMode: ...
    @property
    def TempData(self) -> ITempDataDictionary: ...
    @property
    def ValidationMessageElement(self) -> str: ...
    @property
    def ValidationSummaryMessageElement(self) -> str: ...
    @property
    def View(self) -> IView: ...
    @property
    def ViewBag(self) -> Object: ...
    @property
    def ViewData(self) -> ViewDataDictionary: ...
    @property
    def Writer(self) -> TextWriter: ...
    def GetFormContextForClientValidation(self) -> FormContext: ...
    @ClientValidationEnabled.setter
    def ClientValidationEnabled(self, value: bool) -> None: ...
    @ExecutingFilePath.setter
    def ExecutingFilePath(self, value: str) -> None: ...
    @FormContext.setter
    def FormContext(self, value: FormContext) -> None: ...
    @Html5DateRenderingMode.setter
    def Html5DateRenderingMode(self, value: Html5DateRenderingMode) -> None: ...
    @TempData.setter
    def TempData(self, value: ITempDataDictionary) -> None: ...
    @ValidationMessageElement.setter
    def ValidationMessageElement(self, value: str) -> None: ...
    @ValidationSummaryMessageElement.setter
    def ValidationSummaryMessageElement(self, value: str) -> None: ...
    @View.setter
    def View(self, value: IView) -> None: ...
    @ViewData.setter
    def ViewData(self, value: ViewDataDictionary) -> None: ...
    @Writer.setter
    def Writer(self, value: TextWriter) -> None: ...
