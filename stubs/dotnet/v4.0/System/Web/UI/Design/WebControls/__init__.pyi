from typing import Tuple, Set, Iterable, List


class DataPagerDesigner(ControlDesigner):
    def __init__(self): ...
    @property
    def ActionLists(self) -> DesignerActionListCollection: ...
    @property
    def PagedControlID(self) -> str: ...
    @property
    def TemplateGroups(self) -> TemplateGroupCollection: ...
    @overload
    def GetDesignTimeHtml(self) -> str: ...
    def Initialize(self, component: IComponent) -> None: ...
    @PagedControlID.setter
    def PagedControlID(self, value: str) -> None: ...


class DataPagerFieldTypeEditor(UITypeEditor):
    def __init__(self): ...
    @overload
    def EditValue(self, context: ITypeDescriptorContext, provider: IServiceProvider, value: Object) -> Object: ...
    @overload
    def GetEditStyle(self, context: ITypeDescriptorContext) -> UITypeEditorEditStyle: ...


class LinqDataSourceDesigner(DataSourceDesigner):
    def __init__(self): ...
    def Configure(self) -> None: ...
    @property
    def ActionLists(self) -> DesignerActionListCollection: ...
    @property
    def CanConfigure(self) -> bool: ...
    @property
    def CanRefreshSchema(self) -> bool: ...
    @property
    def ContextTypeName(self) -> str: ...
    @property
    def Delete(self) -> str: ...
    @property
    def EnableDelete(self) -> bool: ...
    @property
    def EnableInsert(self) -> bool: ...
    @property
    def EnableUpdate(self) -> bool: ...
    @property
    def GroupBy(self) -> str: ...
    @property
    def Insert(self) -> str: ...
    @property
    def OrderBy(self) -> str: ...
    @property
    def OrderGroupsBy(self) -> str: ...
    @property
    def Select(self) -> str: ...
    @property
    def ServiceProvider(self) -> IServiceProvider: ...
    @property
    def TableName(self) -> str: ...
    @property
    def Update(self) -> str: ...
    @property
    def Where(self) -> str: ...
    def GetView(self, viewName: str) -> DesignerDataSourceView: ...
    def GetViewNames(self) -> Set(str): ...
    def Initialize(self, component: IComponent) -> None: ...
    def RefreshSchema(self, preferSilent: bool) -> None: ...
    @ContextTypeName.setter
    def ContextTypeName(self, value: str) -> None: ...
    @Delete.setter
    def Delete(self, value: str) -> None: ...
    @EnableDelete.setter
    def EnableDelete(self, value: bool) -> None: ...
    @EnableInsert.setter
    def EnableInsert(self, value: bool) -> None: ...
    @EnableUpdate.setter
    def EnableUpdate(self, value: bool) -> None: ...
    @GroupBy.setter
    def GroupBy(self, value: str) -> None: ...
    @Insert.setter
    def Insert(self, value: str) -> None: ...
    @OrderBy.setter
    def OrderBy(self, value: str) -> None: ...
    @OrderGroupsBy.setter
    def OrderGroupsBy(self, value: str) -> None: ...
    @Select.setter
    def Select(self, value: str) -> None: ...
    @TableName.setter
    def TableName(self, value: str) -> None: ...
    @Update.setter
    def Update(self, value: str) -> None: ...
    @Where.setter
    def Where(self, value: str) -> None: ...


class LinqDesignerDataSourceView(DesignerDataSourceView):
    def __init__(self, owner: LinqDataSourceDesigner): ...
    @property
    def CanDelete(self) -> bool: ...
    @property
    def CanInsert(self) -> bool: ...
    @property
    def CanPage(self) -> bool: ...
    @property
    def CanSort(self) -> bool: ...
    @property
    def CanUpdate(self) -> bool: ...
    @property
    def IsDataContext(self) -> bool: ...
    @property
    def IsTableTypeTable(self) -> bool: ...
    @property
    def Schema(self) -> IDataSourceViewSchema: ...
    def GetDesignTimeData(self, minimumRows: int) -> Tuple[IEnumerable, bool]: ...


class ListViewDesigner(DataBoundControlDesigner):
    def __init__(self): ...
    @property
    def ActionLists(self) -> DesignerActionListCollection: ...
    @overload
    def GetDesignTimeHtml(self) -> str: ...
    @overload
    def GetDesignTimeHtml(self, regions: DesignerRegionCollection) -> str: ...
    def GetEditableDesignerRegionContent(self, region: EditableDesignerRegion) -> str: ...
    def Initialize(self, component: IComponent) -> None: ...
    def OnComponentChanged(self, sender: Object, ce: ComponentChangedEventArgs) -> None: ...
    def SetEditableDesignerRegionContent(self, region: EditableDesignerRegion, content: str) -> None: ...
