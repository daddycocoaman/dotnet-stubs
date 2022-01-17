from typing import Tuple, Set, Iterable, List


class WindowsFormsApplicationBase(ConsoleApplicationBase):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, authenticationMode: AuthenticationMode): ...
    def add_ApplyApplicationDefaults(self, obj: ApplyApplicationDefaultsEventHandler) -> None: ...
    def add_NetworkAvailabilityChanged(self, value: NetworkAvailableEventHandler) -> None: ...
    def add_Shutdown(self, obj: ShutdownEventHandler) -> None: ...
    def add_Startup(self, obj: StartupEventHandler) -> None: ...
    def add_StartupNextInstance(self, obj: StartupNextInstanceEventHandler) -> None: ...
    def add_UnhandledException(self, value: UnhandledExceptionEventHandler) -> None: ...
    def DoEvents(self) -> None: ...
    @property
    def ApplicationContext(self) -> ApplicationContext: ...
    @property
    def MinimumSplashScreenDisplayTime(self) -> int: ...
    @property
    def OpenForms(self) -> FormCollection: ...
    @property
    def SaveMySettingsOnExit(self) -> bool: ...
    @property
    def SplashScreen(self) -> Form: ...
    def remove_ApplyApplicationDefaults(self, obj: ApplyApplicationDefaultsEventHandler) -> None: ...
    def remove_NetworkAvailabilityChanged(self, value: NetworkAvailableEventHandler) -> None: ...
    def remove_Shutdown(self, obj: ShutdownEventHandler) -> None: ...
    def remove_Startup(self, obj: StartupEventHandler) -> None: ...
    def remove_StartupNextInstance(self, obj: StartupNextInstanceEventHandler) -> None: ...
    def remove_UnhandledException(self, value: UnhandledExceptionEventHandler) -> None: ...
    def Run(self, commandLine: Set(str)) -> None: ...
    @MinimumSplashScreenDisplayTime.setter
    def MinimumSplashScreenDisplayTime(self, value: int) -> None: ...
    @SaveMySettingsOnExit.setter
    def SaveMySettingsOnExit(self, value: bool) -> None: ...
    @SplashScreen.setter
    def SplashScreen(self, value: Form) -> None: ...
