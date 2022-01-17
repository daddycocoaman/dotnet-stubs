from typing import Tuple, Set, Iterable, List


class BrowserFileExtensions:
    def RequestImageFileAsync(browserFile: IBrowserFile, format: str, maxWidth: int, maxHeight: int) -> ValueTask: ...


class EditContextFieldClassExtensions:
    @overload
    def FieldCssClass(editContext: EditContext, accessor: Expression) -> str: ...
    @overload
    def FieldCssClass(editContext: EditContext, fieldIdentifier: FieldIdentifier) -> Tuple[str, FieldIdentifier]: ...
    def SetFieldCssClassProvider(editContext: EditContext, fieldCssClassProvider: FieldCssClassProvider) -> None: ...


class EditForm(ComponentBase):
    def __init__(self): ...
    @property
    def AdditionalAttributes(self) -> IReadOnlyDictionary: ...
    @property
    def ChildContent(self) -> RenderFragment: ...
    @property
    def EditContext(self) -> EditContext: ...
    @property
    def Model(self) -> Object: ...
    @property
    def OnInvalidSubmit(self) -> EventCallback: ...
    @property
    def OnSubmit(self) -> EventCallback: ...
    @property
    def OnValidSubmit(self) -> EventCallback: ...
    @AdditionalAttributes.setter
    def AdditionalAttributes(self, value: IReadOnlyDictionary) -> None: ...
    @ChildContent.setter
    def ChildContent(self, value: RenderFragment) -> None: ...
    @EditContext.setter
    def EditContext(self, value: EditContext) -> None: ...
    @Model.setter
    def Model(self, value: Object) -> None: ...
    @OnInvalidSubmit.setter
    def OnInvalidSubmit(self, value: EventCallback) -> None: ...
    @OnSubmit.setter
    def OnSubmit(self, value: EventCallback) -> None: ...
    @OnValidSubmit.setter
    def OnValidSubmit(self, value: EventCallback) -> None: ...


class FieldCssClassProvider:
    def __init__(self): ...
    def GetFieldCssClass(self, editContext: EditContext, fieldIdentifier: FieldIdentifier) -> Tuple[str, FieldIdentifier]: ...


class IBrowserFile:
    @property
    def ContentType(self) -> str: ...
    @property
    def LastModified(self) -> DateTimeOffset: ...
    @property
    def Name(self) -> str: ...
    @property
    def Size(self) -> Int64: ...
    def OpenReadStream(self, maxAllowedSize: Int64, cancellationToken: CancellationToken) -> Stream: ...




class InputCheckbox:
    def __init__(self): ...
    @property
    def Element(self) -> Nullable: ...




class InputDateType:
    Date = 0
    DateTimeLocal = 1
    Month = 2
    Time = 3


class InputFile(ComponentBase):
    def __init__(self): ...
    @property
    def AdditionalAttributes(self) -> IDictionary: ...
    @property
    def Element(self) -> Nullable: ...
    @property
    def OnChange(self) -> EventCallback: ...
    @AdditionalAttributes.setter
    def AdditionalAttributes(self, value: IDictionary) -> None: ...
    @OnChange.setter
    def OnChange(self, value: EventCallback) -> None: ...


class InputFileChangeEventArgs:
    def __init__(self, files: IReadOnlyList): ...
    @property
    def File(self) -> IBrowserFile: ...
    @property
    def FileCount(self) -> int: ...
    def GetMultipleFiles(self, maximumFileCount: int) -> IReadOnlyList: ...










class InputText:
    def __init__(self): ...
    @property
    def Element(self) -> Nullable: ...


class InputTextArea:
    def __init__(self): ...
    @property
    def Element(self) -> Nullable: ...




class ValidationSummary(ComponentBase):
    def __init__(self): ...
    @property
    def AdditionalAttributes(self) -> IReadOnlyDictionary: ...
    @property
    def Model(self) -> Object: ...
    @AdditionalAttributes.setter
    def AdditionalAttributes(self, value: IReadOnlyDictionary) -> None: ...
    @Model.setter
    def Model(self, value: Object) -> None: ...
