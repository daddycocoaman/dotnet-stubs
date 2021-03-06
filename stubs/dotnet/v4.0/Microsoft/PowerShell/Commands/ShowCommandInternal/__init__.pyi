from typing import Tuple, Set, Iterable, List


class AllModulesControl:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class AllModulesViewModel:
    @overload
    def __init__(self, importedModules: Dictionary, commands: Iterable[ShowCommandCommandInfo]): ...
    @overload
    def __init__(self, importedModules: Dictionary, commands: Iterable[ShowCommandCommandInfo], noCommonParameter: bool): ...
    def add_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    def add_Refresh(self, value: EventHandler) -> None: ...
    def add_RunSelectedCommandInSelectedModule(self, value: EventHandler) -> None: ...
    def add_SelectedCommandInSelectedModuleNeedsHelp(self, value: EventHandler) -> None: ...
    def add_SelectedCommandInSelectedModuleNeedsImportModule(self, value: EventHandler) -> None: ...
    @property
    def CanCopy(self) -> bool: ...
    @property
    def CanRun(self) -> bool: ...
    @property
    def CommandNameFilter(self) -> str: ...
    @property
    def ExtraViewModel(self) -> Object: ...
    @property
    def MainGridDisplayed(self) -> bool: ...
    @property
    def MainGridVisibility(self) -> Visibility: ...
    @property
    def Modules(self) -> List: ...
    @property
    def NoCommonParameter(self) -> bool: ...
    @property
    def RefreshTooltip() -> str: ...
    @property
    def RefreshVisibility(self) -> Visibility: ...
    @property
    def SelectedModule(self) -> ModuleViewModel: ...
    @property
    def WaitMessageDisplayed(self) -> bool: ...
    @property
    def WaitMessageVisibility(self) -> Visibility: ...
    @property
    def ZoomLevel(self) -> float: ...
    def GetScript(self) -> str: ...
    def remove_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    def remove_Refresh(self, value: EventHandler) -> None: ...
    def remove_RunSelectedCommandInSelectedModule(self, value: EventHandler) -> None: ...
    def remove_SelectedCommandInSelectedModuleNeedsHelp(self, value: EventHandler) -> None: ...
    def remove_SelectedCommandInSelectedModuleNeedsImportModule(self, value: EventHandler) -> None: ...
    @CommandNameFilter.setter
    def CommandNameFilter(self, value: str) -> None: ...
    @ExtraViewModel.setter
    def ExtraViewModel(self, value: Object) -> None: ...
    @RefreshVisibility.setter
    def RefreshVisibility(self, value: Visibility) -> None: ...
    @SelectedModule.setter
    def SelectedModule(self, value: ModuleViewModel) -> None: ...
    @WaitMessageDisplayed.setter
    def WaitMessageDisplayed(self, value: bool) -> None: ...
    @ZoomLevel.setter
    def ZoomLevel(self, value: float) -> None: ...


class CmdletControl:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class CommandEventArgs:
    def __init__(self, command: CommandViewModel): ...
    @property
    def Command(self) -> CommandViewModel: ...


class CommandViewModel:
    def add_HelpNeeded(self, value: EventHandler) -> None: ...
    def add_ImportModule(self, value: EventHandler) -> None: ...
    def add_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    @property
    def AreCommonParametersExpanded(self) -> bool: ...
    @property
    def CommonParameters(self) -> ParameterSetViewModel: ...
    @property
    def CommonParametersHeight(self) -> GridLength: ...
    @property
    def CommonParameterVisibility(self) -> Visibility: ...
    @property
    def DetailsTitle(self) -> str: ...
    @property
    def ImportModuleMessage(self) -> str: ...
    @property
    def IsImported(self) -> bool: ...
    @property
    def ModuleName(self) -> str: ...
    @property
    def ModuleQualifyCommandName(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def NoParameterVisibility(self) -> Visibility: ...
    @property
    def NotImportedVisibility(self) -> Visibility: ...
    @property
    def ParameterSets(self) -> List: ...
    @property
    def ParameterSetTabControlVisibility(self) -> Visibility: ...
    @property
    def ParentModule(self) -> ModuleViewModel: ...
    @property
    def SelectedParameterSet(self) -> ParameterSetViewModel: ...
    @property
    def SelectedParameterSetAllMandatoryParametersHaveValues(self) -> bool: ...
    @property
    def SingleParameterSetControlVisibility(self) -> Visibility: ...
    @property
    def ToolTip(self) -> str: ...
    def GetScript(self) -> str: ...
    def OpenHelpWindow(self) -> None: ...
    def remove_HelpNeeded(self, value: EventHandler) -> None: ...
    def remove_ImportModule(self, value: EventHandler) -> None: ...
    def remove_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    @AreCommonParametersExpanded.setter
    def AreCommonParametersExpanded(self, value: bool) -> None: ...
    @CommonParametersHeight.setter
    def CommonParametersHeight(self, value: GridLength) -> None: ...
    @ModuleQualifyCommandName.setter
    def ModuleQualifyCommandName(self, value: bool) -> None: ...
    @SelectedParameterSet.setter
    def SelectedParameterSet(self, value: ParameterSetViewModel) -> None: ...
    @SelectedParameterSetAllMandatoryParametersHaveValues.setter
    def SelectedParameterSetAllMandatoryParametersHaveValues(self, value: bool) -> None: ...


class HelpNeededEventArgs:
    def __init__(self, commandName: str): ...
    @property
    def CommandName(self) -> str: ...


class ImageButton(ImageButtonBase):
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class ImageButtonBase:
    def __init__(self): ...
    @property
    def Command(self) -> RoutedUICommand: ...
    @property
    def DisabledImageSource(self) -> ImageSource: ...
    @property
    def EnabledImageSource(self) -> ImageSource: ...
    @Command.setter
    def Command(self, value: RoutedUICommand) -> None: ...
    @DisabledImageSource.setter
    def DisabledImageSource(self, value: ImageSource) -> None: ...
    @EnabledImageSource.setter
    def EnabledImageSource(self, value: ImageSource) -> None: ...


class ImageButtonToolTipConverter:
    def __init__(self): ...
    def Convert(self, value: Object, targetType: Type, parameter: Object, culture: CultureInfo) -> Object: ...
    def ConvertBack(self, value: Object, targetType: Type, parameter: Object, culture: CultureInfo) -> Object: ...


class ImageToggleButton(ImageButtonBase):
    def __init__(self): ...
    @property
    def IsChecked(self) -> bool: ...
    def InitializeComponent(self) -> None: ...
    @IsChecked.setter
    def IsChecked(self, value: bool) -> None: ...


class ImportModuleEventArgs:
    def __init__(self, commandName: str, parentModuleName: str, selectedModuleName: str): ...
    @property
    def CommandName(self) -> str: ...
    @property
    def ParentModuleName(self) -> str: ...
    @property
    def SelectedModuleName(self) -> str: ...


class ModuleViewModel:
    def __init__(self, name: str, importedModules: Dictionary): ...
    def add_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    def add_RunSelectedCommand(self, value: EventHandler) -> None: ...
    def add_SelectedCommandNeedsHelp(self, value: EventHandler) -> None: ...
    def add_SelectedCommandNeedsImportModule(self, value: EventHandler) -> None: ...
    @property
    def AllModules(self) -> AllModulesViewModel: ...
    @property
    def CommandControlVisibility(self) -> Visibility: ...
    @property
    def CommandRowHeight(self) -> GridLength: ...
    @property
    def Commands(self) -> List: ...
    @property
    def DisplayName(self) -> str: ...
    @property
    def FilteredCommands(self) -> ObservableCollection: ...
    @property
    def IsThereASelectedCommand(self) -> bool: ...
    @property
    def IsThereASelectedImportedCommandWhereAllMandatoryParametersHaveValues(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def SelectedCommand(self) -> CommandViewModel: ...
    def remove_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    def remove_RunSelectedCommand(self, value: EventHandler) -> None: ...
    def remove_SelectedCommandNeedsHelp(self, value: EventHandler) -> None: ...
    def remove_SelectedCommandNeedsImportModule(self, value: EventHandler) -> None: ...
    @IsThereASelectedCommand.setter
    def IsThereASelectedCommand(self, value: bool) -> None: ...
    @IsThereASelectedImportedCommandWhereAllMandatoryParametersHaveValues.setter
    def IsThereASelectedImportedCommandWhereAllMandatoryParametersHaveValues(self, value: bool) -> None: ...
    @SelectedCommand.setter
    def SelectedCommand(self, value: CommandViewModel) -> None: ...


class MultipleSelectionControl:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class MultipleSelectionDialog:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class NotImportedCmdletControl:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class ParameterSetControl:
    def __init__(self): ...
    def FocusFirstElement(self) -> None: ...
    def InitializeComponent(self) -> None: ...


class ParameterSetViewModel:
    def __init__(self, name: str, parameters: List): ...
    def add_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    @property
    def AllMandatoryParametersHaveValues(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Parameters(self) -> List: ...
    def GetIndividualParameterCount(self) -> int: ...
    def GetScript(self) -> str: ...
    def remove_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    @AllMandatoryParametersHaveValues.setter
    def AllMandatoryParametersHaveValues(self, value: bool) -> None: ...


class ParameterViewModel:
    def __init__(self, parameter: ShowCommandParameterInfo, parameterSetName: str): ...
    def add_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    @property
    def HasValue(self) -> bool: ...
    @property
    def IsInSharedParameterSet(self) -> bool: ...
    @property
    def IsMandatory(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def NameCheckLabel(self) -> str: ...
    @property
    def NameTextLabel(self) -> str: ...
    @property
    def Parameter(self) -> ShowCommandParameterInfo: ...
    @property
    def ParameterSetName(self) -> str: ...
    @property
    def ToolTip(self) -> str: ...
    @property
    def Value(self) -> Object: ...
    def remove_PropertyChanged(self, value: PropertyChangedEventHandler) -> None: ...
    @Value.setter
    def Value(self, value: Object) -> None: ...


class ShowAllModulesWindow:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class ShowCommandWindow:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...


class ShowModuleControl:
    def __init__(self): ...
    @property
    def Owner(self) -> Window: ...
    def InitializeComponent(self) -> None: ...
    @Owner.setter
    def Owner(self, value: Window) -> None: ...
