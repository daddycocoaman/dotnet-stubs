__all__ = ['WebControls']
from typing import Tuple, Set, Iterable, List


class AsyncPostBackTriggerControlIDConverter(StringConverter):
    def __init__(self): ...
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool: ...
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool: ...


class AsyncPostBackTriggerEventNameConverter(StringConverter):
    def __init__(self): ...
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool: ...
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool: ...


class CollectionEditorBase(CollectionEditor):
    def __init__(self, type: Type): ...


class ExtenderControlDesigner(ControlDesigner):
    def __init__(self): ...
    @overload
    def GetDesignTimeHtml(self) -> str: ...
    def Initialize(self, component: IComponent) -> None: ...


class ExtenderControlToolboxItem(WebControlToolboxItem):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, type: Type): ...
    def GetTargetControlTypes(self, host: IDesignerHost) -> ReadOnlyCollection: ...
    def Initialize(self, type: Type) -> None: ...


class PostBackTriggerControlIDConverter(StringConverter):
    def __init__(self): ...
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool: ...
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool: ...


class QueryExtenderDesigner(ControlDesigner):
    def __init__(self): ...
    @overload
    def GetDesignTimeHtml(self) -> str: ...


class ScriptManagerDesigner(ControlDesigner):
    def __init__(self): ...
    def GetApplicationServices(scriptManager: ScriptManager, proxies: Iterable[ScriptManagerProxy]) -> str: ...
    @overload
    def GetDesignTimeHtml(self) -> str: ...
    def GetProxyScript(scriptManager: ScriptManager, serviceReference: ServiceReference) -> str: ...
    def GetProxyUrl(scriptManager: ScriptManager, serviceReference: ServiceReference) -> str: ...
    def GetScriptFromWebResource(assembly: Assembly, resourceName: str, culture: CultureInfo) -> str: ...
    def GetScriptReferences(scriptManager: ScriptManager, proxies: Iterable[ScriptManagerProxy]) -> ReadOnlyCollection: ...
    def GetServiceReferences(scriptManager: ScriptManager, proxies: Iterable[ScriptManagerProxy]) -> ReadOnlyCollection: ...
    def Initialize(self, component: IComponent) -> None: ...


class ScriptManagerProxyDesigner(ControlDesigner):
    def __init__(self): ...
    @overload
    def GetDesignTimeHtml(self) -> str: ...
    def Initialize(self, component: IComponent) -> None: ...


class ServiceReferenceCollectionEditor(CollectionEditorBase):
    def __init__(self, type: Type): ...


class TimerDesigner(ControlDesigner):
    def __init__(self): ...
    @overload
    def GetDesignTimeHtml(self) -> str: ...


class UpdatePanelDesigner(ControlDesigner):
    def __init__(self): ...
    @overload
    def GetDesignTimeHtml(self, regions: DesignerRegionCollection) -> str: ...
    def GetEditableDesignerRegionContent(self, region: EditableDesignerRegion) -> str: ...
    def Initialize(self, component: IComponent) -> None: ...
    def OnComponentChanged(self, sender: Object, ce: ComponentChangedEventArgs) -> None: ...
    def SetEditableDesignerRegionContent(self, region: EditableDesignerRegion, content: str) -> None: ...


class UpdatePanelTriggerCollectionEditor(CollectionEditorBase):
    def __init__(self, type: Type): ...
    @overload
    def EditValue(self, context: ITypeDescriptorContext, provider: IServiceProvider, value: Object) -> Object: ...


class UpdateProgressAssociatedUpdatePanelIDConverter(StringConverter):
    def __init__(self): ...
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
    @overload
    def GetStandardValuesExclusive(self, context: ITypeDescriptorContext) -> bool: ...
    @overload
    def GetStandardValuesSupported(self, context: ITypeDescriptorContext) -> bool: ...


class UpdateProgressDesigner(ControlDesigner):
    def __init__(self): ...
    @overload
    def GetDesignTimeHtml(self, regions: DesignerRegionCollection) -> str: ...
    def GetEditableDesignerRegionContent(self, region: EditableDesignerRegion) -> str: ...
    def SetEditableDesignerRegionContent(self, region: EditableDesignerRegion, content: str) -> None: ...
