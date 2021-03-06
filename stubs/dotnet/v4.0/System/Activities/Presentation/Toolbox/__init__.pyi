from typing import Tuple, Set, Iterable, List


class ActivityTemplateFactory(Object):
    def Create(self, target: DependencyObject) -> Activity: ...




class ActivityTemplateFactoryBuilder(Object):
    def __init__(self): ...
    @property
    def Implementation(self) -> Object: ...
    @property
    def Name(self) -> str: ...
    @property
    def TargetType(self) -> Type: ...
    @Implementation.setter
    def Implementation(self, value: Object) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @TargetType.setter
    def TargetType(self, value: Type) -> None: ...


class ToolboxCategory(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str): ...
    def add_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    def Add(self, tool: ToolboxItemWrapper) -> None: ...
    @property
    def CategoryName(self) -> str: ...
    @property
    def Item(self, index: int) -> ToolboxItemWrapper: ...
    @property
    def Tools(self) -> ICollection: ...
    def remove_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    def Remove(self, tool: ToolboxItemWrapper) -> bool: ...
    @CategoryName.setter
    def CategoryName(self, value: str) -> None: ...


class ToolboxCategoryItems(Object):
    def __init__(self): ...
    def Add(self, item: ToolboxCategory) -> None: ...
    def Clear(self) -> None: ...
    def Contains(self, item: ToolboxCategory) -> bool: ...
    def CopyTo(self, array: Set(ToolboxCategory), arrayIndex: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Item(self, index: int) -> ToolboxCategory: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Remove(self, item: ToolboxCategory) -> bool: ...


class ToolboxControl(Control):
    def __init__(self): ...
    def add_ToolCreated(self, value: ToolCreatedEventHandler) -> None: ...
    def add_ToolSelected(self, value: RoutedEventHandler) -> None: ...
    @property
    def AssociatedDesigner(self) -> WorkflowDesigner: ...
    @property
    def Categories(self) -> ToolboxCategoryItems: ...
    @property
    def CategoryItemStyle(self) -> Style: ...
    @property
    def CategoryTemplate(self) -> DataTemplate: ...
    @property
    def SelectedTool(self) -> ToolboxItem: ...
    @property
    def ToolboxFile(self) -> str: ...
    @property
    def ToolItemStyle(self) -> Style: ...
    @property
    def ToolTemplate(self) -> DataTemplate: ...
    def OnApplyTemplate(self) -> None: ...
    def remove_ToolCreated(self, value: ToolCreatedEventHandler) -> None: ...
    def remove_ToolSelected(self, value: RoutedEventHandler) -> None: ...
    @AssociatedDesigner.setter
    def AssociatedDesigner(self, value: WorkflowDesigner) -> None: ...
    @Categories.setter
    def Categories(self, value: ToolboxCategoryItems) -> None: ...
    @CategoryItemStyle.setter
    def CategoryItemStyle(self, value: Style) -> None: ...
    @CategoryTemplate.setter
    def CategoryTemplate(self, value: DataTemplate) -> None: ...
    @ToolboxFile.setter
    def ToolboxFile(self, value: str) -> None: ...
    @ToolItemStyle.setter
    def ToolItemStyle(self, value: Style) -> None: ...
    @ToolTemplate.setter
    def ToolTemplate(self, value: DataTemplate) -> None: ...


class ToolboxItemWrapper(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, toolType: Type): ...
    @overload
    def __init__(self, toolType: Type, displayName: str): ...
    @overload
    def __init__(self, toolType: Type, bitmapName: str, displayName: str): ...
    @overload
    def __init__(self, toolName: str, assemblyName: str, bitmapName: str, displayName: str): ...
    def add_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    @property
    def AssemblyName(self) -> str: ...
    @property
    def Bitmap(self) -> Bitmap: ...
    @property
    def BitmapName(self) -> str: ...
    @property
    def DisplayName(self) -> str: ...
    @property
    def IsValid(self) -> bool: ...
    @property
    def ToolName(self) -> str: ...
    @property
    def Type(self) -> Type: ...
    def remove_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    @AssemblyName.setter
    def AssemblyName(self, value: str) -> None: ...
    @BitmapName.setter
    def BitmapName(self, value: str) -> None: ...
    @DisplayName.setter
    def DisplayName(self, value: str) -> None: ...
    @ToolName.setter
    def ToolName(self, value: str) -> None: ...
    def ToString(self) -> str: ...


class ToolCreatedEventArgs(RoutedEventArgs):
    @property
    def Components(self) -> Set(IComponent): ...


class ToolCreatedEventHandler(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, sender: Object, e: ToolCreatedEventArgs, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, e: ToolCreatedEventArgs) -> None: ...
