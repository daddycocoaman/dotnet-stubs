from typing import Tuple, Set, Iterable, List


class AssemblyContextControlItem(ContextItem):
    def __init__(self): ...
    @property
    def AllAssemblyNamesInContext(self) -> Iterable[str]: ...
    @property
    def ItemType(self) -> Type: ...
    @property
    def LocalAssemblyName(self) -> AssemblyName: ...
    @property
    def ReferencedAssemblyNames(self) -> List[AssemblyName]: ...
    def GetAssembly(assemblyName: AssemblyName, multiTargetingService: IMultiTargetingSupportService) -> Assembly: ...
    def GetEnvironmentAssemblies(self, multiTargetingService: IMultiTargetingSupportService) -> Iterable[Assembly]: ...
    def GetEnvironmentAssemblyNames(self) -> Iterable[AssemblyName]: ...
    @LocalAssemblyName.setter
    def LocalAssemblyName(self, value: AssemblyName) -> None: ...
    @ReferencedAssemblyNames.setter
    def ReferencedAssemblyNames(self, value: List[AssemblyName]) -> None: ...


class CommandInfo(Object):
    @property
    def Command(self) -> ICommand: ...
    @property
    def IsBindingEnabledInDesigner(self) -> bool: ...
    @IsBindingEnabledInDesigner.setter
    def IsBindingEnabledInDesigner(self, value: bool) -> None: ...


class CommandValues(Object):
    pass


class ICommandService:
    def CanExecuteCommand(self, commandId: int) -> bool: ...
    def ExecuteCommand(self, commandId: int, parameters: Dictionary) -> None: ...
    def IsCommandSupported(self, commandId: int) -> bool: ...


class IDocumentPersistenceService:
    def Flush(self, documentRoot: Object) -> None: ...
    def Load(self, fileName: str) -> Object: ...
    def OnModelChanged(self, documentRoot: Object) -> None: ...


class ImportedNamespaceContextItem(ContextItem):
    def __init__(self): ...
    def EnsureInitialized(self, context: EditingContext) -> None: ...
    @property
    def ImportedNamespaces(self) -> Collection: ...
    @property
    def ItemType(self) -> Type: ...


class IMultiTargetingSupportService:
    def GetReflectionAssembly(self, targetAssemblyName: AssemblyName) -> Assembly: ...
    def GetRuntimeType(self, reflectionType: Type) -> Type: ...
    def IsSupportedType(self, type: Type) -> bool: ...


class IWorkflowCommandExtensionCallback:
    def OnWorkflowCommandLoaded(self, commandInfo: CommandInfo) -> None: ...


class MultiTargetingSupportService(Object):
    def GetReflectionAssembly(self, targetAssemblyName: AssemblyName) -> Assembly: ...
    def GetReflectionType(self, objectType: Type) -> Type: ...
    def GetRuntimeType(self, reflectionType: Type) -> Type: ...
    def IsSupportedType(self, type: Type) -> bool: ...


class ReadOnlyState(ContextItem):
    def __init__(self): ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def ItemType(self) -> Type: ...
    @IsReadOnly.setter
    def IsReadOnly(self, value: bool) -> None: ...


class WindowHelperService(Object):
    def __init__(self, hwnd: IntPtr): ...
    @property
    def ParentWindowHwnd(self) -> IntPtr: ...
    def RegisterWindowMessageHandler(self, callback: WindowMessage) -> bool: ...
    def TrySetWindowOwner(self, source: DependencyObject, target: Window) -> bool: ...
    def UnregisterWindowMessageHandler(self, callback: WindowMessage) -> bool: ...


class WindowMessage(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, msgId: int, parameter1: IntPtr, parameter2: IntPtr, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, msgId: int, parameter1: IntPtr, parameter2: IntPtr) -> None: ...


class WorkflowCommandExtensionItem(ContextItem):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, callback: IWorkflowCommandExtensionCallback): ...
    @property
    def ItemType(self) -> Type: ...
