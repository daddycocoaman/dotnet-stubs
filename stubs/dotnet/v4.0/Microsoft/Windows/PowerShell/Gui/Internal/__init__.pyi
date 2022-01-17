from typing import Tuple, Set, Iterable, List


class AccessibleMenuItem:
    def __init__(self): ...


class AddOnToolTabControl:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class App:
    def InitializeComponent(self) -> None: ...


class AutomationNames:
    def StripUnderscores(uiString: str) -> str: ...


class ColorNames:
    pass


class ColorPicker:
    def __init__(self): ...
    def add_ColorChanged(self, value: EventHandler) -> None: ...
    @property
    def CurrentColor(self) -> Color: ...
    def InitializeComponent(self) -> None: ...
    def remove_ColorChanged(self, value: EventHandler) -> None: ...
    @CurrentColor.setter
    def CurrentColor(self, value: Color) -> None: ...


class ContextMenuOnlyCustomCommands:
    @property
    def DisableBreakpoint() -> RoutedUICommand: ...
    @property
    def EnableBreakpoint() -> RoutedUICommand: ...


class ControlTexts:
    pass


class CustomCommands:
    @property
    def AboutAddOnTools() -> RoutedUICommand: ...
    @property
    def ApplicationExit() -> RoutedUICommand: ...
    @property
    def BreakAllDebugger() -> RoutedUICommand: ...
    @property
    def ClearOutput() -> RoutedUICommand: ...
    @property
    def CloseRunspaceCmd() -> RoutedUICommand: ...
    @property
    def CloseScript() -> RoutedUICommand: ...
    @property
    def Copy() -> RoutedUICommand: ...
    @property
    def CustomScriptCmd() -> RoutedUICommand: ...
    @property
    def Cut() -> RoutedUICommand: ...
    @property
    def DisableAllBreakpoints() -> RoutedUICommand: ...
    @property
    def EnableAllBreakpoints() -> RoutedUICommand: ...
    @property
    def Find() -> RoutedUICommand: ...
    @property
    def FindNext() -> RoutedUICommand: ...
    @property
    def FindPrevious() -> RoutedUICommand: ...
    @property
    def GetCallStack() -> RoutedUICommand: ...
    @property
    def GoToConsolePane() -> RoutedUICommand: ...
    @property
    def GoToEditor() -> RoutedUICommand: ...
    @property
    def GoToLine() -> RoutedUICommand: ...
    @property
    def GoToMatch() -> RoutedUICommand: ...
    @property
    def GoToSelectedHorizontalAddOnTool() -> RoutedUICommand: ...
    @property
    def GoToSelectedVerticalAddOnTool() -> RoutedUICommand: ...
    @property
    def Help() -> RoutedUICommand: ...
    @property
    def HideHorizontalAddOnTool() -> RoutedUICommand: ...
    @property
    def HideVerticalAddOnTool() -> RoutedUICommand: ...
    @property
    def ListBreakpoints() -> RoutedUICommand: ...
    @property
    def ModuleBrowserAddOnCommand() -> RoutedUICommand: ...
    @property
    def MoveHorizontalAddOnToolToVertical() -> RoutedUICommand: ...
    @property
    def MoveScriptToTopOrRightCmd() -> RoutedUICommand: ...
    @property
    def MoveVerticalAddOnToolToHorizontal() -> RoutedUICommand: ...
    @property
    def NewRemotePowerShellTab() -> RoutedUICommand: ...
    @property
    def NewRunspaceCmd() -> RoutedUICommand: ...
    @property
    def NewScript() -> RoutedUICommand: ...
    @property
    def OpenMruFile() -> RoutedUICommand: ...
    @property
    def OpenOptionsDialog() -> RoutedUICommand: ...
    @property
    def OpenScript() -> RoutedUICommand: ...
    @property
    def Paste() -> RoutedUICommand: ...
    @property
    def Redo() -> RoutedUICommand: ...
    @property
    def RemoveAllBreakpoints() -> RoutedUICommand: ...
    @property
    def Replace() -> RoutedUICommand: ...
    @property
    def ReplaceAllCmd() -> RoutedUICommand: ...
    @property
    def ResumeDebugger() -> RoutedUICommand: ...
    @property
    def RunScript() -> RoutedUICommand: ...
    @property
    def RunSelection() -> RoutedUICommand: ...
    @property
    def SaveScript() -> RoutedUICommand: ...
    @property
    def SaveScriptAs() -> RoutedUICommand: ...
    @property
    def ScriptAnalyzerAddOnCommand() -> RoutedUICommand: ...
    @property
    def ScriptBrowserAddOnCommand() -> RoutedUICommand: ...
    @property
    def SelectAll() -> RoutedUICommand: ...
    @property
    def ShowAndSelectAddOnTool() -> RoutedUICommand: ...
    @property
    def ShowPopupCommand() -> RoutedUICommand: ...
    @property
    def ShowRunspaceCmd() -> RoutedUICommand: ...
    @property
    def ShowScriptCmd() -> RoutedUICommand: ...
    @property
    def ShowScriptPaneMaximized() -> RoutedUICommand: ...
    @property
    def ShowScriptPaneRight() -> RoutedUICommand: ...
    @property
    def ShowScriptPaneTop() -> RoutedUICommand: ...
    @property
    def ShowSnippet() -> RoutedUICommand: ...
    @property
    def StartIntellisense() -> RoutedUICommand: ...
    @property
    def StartPowerShell() -> RoutedUICommand: ...
    @property
    def StepInto() -> RoutedUICommand: ...
    @property
    def StepOut() -> RoutedUICommand: ...
    @property
    def StepOver() -> RoutedUICommand: ...
    @property
    def StopDebugger() -> RoutedUICommand: ...
    @property
    def StopExecution() -> RoutedUICommand: ...
    @property
    def ToggleBreakpoint() -> RoutedUICommand: ...
    @property
    def ToggleEmbeddedCommands() -> RoutedUICommand: ...
    @property
    def ToggleHorizontalAddOnPane() -> RoutedUICommand: ...
    @property
    def ToggleOutliningExpandCollapseAll() -> RoutedUICommand: ...
    @property
    def ToggleScriptingPane() -> RoutedUICommand: ...
    @property
    def ToggleShowLineNumbers() -> RoutedUICommand: ...
    @property
    def ToggleShowOutlining() -> RoutedUICommand: ...
    @property
    def ToggleToolBar() -> RoutedUICommand: ...
    @property
    def ToggleVerticalAddOnPane() -> RoutedUICommand: ...
    @property
    def Undo() -> RoutedUICommand: ...
    @property
    def UpdateHelp() -> RoutedUICommand: ...
    @property
    def ZoomIn() -> RoutedUICommand: ...
    @property
    def ZoomOut() -> RoutedUICommand: ...


class EditorTabControl:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class FindAndReplaceDialog:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...
    def SetFindMode(self, findMode: bool) -> None: ...


class HostGuiAutomationNames:
    pass


class HostGuiNLStrings:
    pass


class HostGuiStrings:
    pass


class HostTextWriter:
    @property
    def Encoding(self) -> Encoding: ...
    def RegisterHost(host: PSHostUserInterface) -> None: ...
    @overload
    def Write(self, value: str) -> None: ...
    @overload
    def WriteLine(self, value: str) -> None: ...


class InternalPropertyBindingConverter:
    def __init__(self): ...
    def Convert(self, value: Object, targetType: Type, parameter: Object, culture: CultureInfo) -> Object: ...
    def ConvertBack(self, value: Object, targetType: Type, parameter: Object, culture: CultureInfo) -> Object: ...


class MainWindow:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...
    def OnDismissTooltipTimer_Tick(self, sender: Object, e: EventArgs) -> None: ...
    def showToolTip(self, sender: Object, e: KeyboardFocusChangedEventArgs) -> None: ...


class ManageThemesWindow:
    def InitializeComponent(self) -> None: ...


class NewRemotePowerShellTabDialog:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class OptionsGuiStrings:
    pass


class OptionsWindow:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, initialOptions: ISEOptions): ...
    def InitializeComponent(self) -> None: ...


class OutputControl:
    def __init__(self): ...
    @property
    def Content(self) -> Object: ...
    def InitializeComponent(self) -> None: ...
    @Content.setter
    def Content(self, value: Object) -> None: ...


class Program:
    def Initialize() -> int: ...
    def OpenFiles(fileNames: List) -> None: ...
    def ShowMainWindow(filesToOpen: List, mta: bool, noProfile: bool, loadedCallback: SendOrPostCallback) -> None: ...


class ProgressBarInformation:
    def __init__(self, sourceId: Int64, progressRecord: ProgressRecord): ...
    def add_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    @property
    def Description(self) -> str: ...
    @property
    def FontSize(self) -> int: ...
    @property
    def PercentComplete(self) -> int: ...
    @property
    def ProgressMargin(self) -> Thickness: ...
    @property
    def ProgressRecord(self) -> ProgressRecord: ...
    @property
    def TextMargin(self) -> Thickness: ...
    def remove_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...


class ProgressControl:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class PromptForChoiceDialog:
    @property
    def Result(self) -> int: ...
    def InitializeComponent(self) -> None: ...


class ReadLineDialog:
    @property
    def IsSecure(self) -> bool: ...
    @property
    def ResultObject(self) -> Object: ...
    @property
    def TargetType(self) -> Type: ...
    def InitializeComponent(self) -> None: ...


class RunspaceControl:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class RunspaceTabControl:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class ScriptExpander:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class ShowCommandAddOnControl:
    def __init__(self): ...
    @property
    def HostObject(self) -> ObjectModelRoot: ...
    def InitializeComponent(self) -> None: ...
    @HostObject.setter
    def HostObject(self, value: ObjectModelRoot) -> None: ...


class SkippableMessageBox:
    def InitializeComponent(self) -> None: ...


class StatusAndSizingBar:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class StorableColorTheme:
    def __init__(self): ...
    def Equals(self, obj: Object) -> bool: ...
    @property
    def FontFamily(self) -> str: ...
    @property
    def FontSize(self) -> int: ...
    @property
    def Item(self, key: str) -> Color: ...
    @property
    def Item(self, key: str, defaultColor: Color) -> Color: ...
    @property
    def Keys(self) -> Collection: ...
    @property
    def Name(self) -> str: ...
    @property
    def Values(self) -> Collection: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(left: StorableColorTheme, right: StorableColorTheme) -> bool: ...
    def op_Inequality(left: StorableColorTheme, right: StorableColorTheme) -> bool: ...
    @FontFamily.setter
    def FontFamily(self, value: str) -> None: ...
    @FontSize.setter
    def FontSize(self, value: int) -> None: ...
    @Item.setter
    def Item(self, key: str, value: Color) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...


class ToolTipStrings:
    pass


class ZoomSlider:
    def __init__(self): ...
