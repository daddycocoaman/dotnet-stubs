from typing import Tuple, Set, Iterable, List


class April(CalendarMonth):
    def __init__(self): ...


class August(CalendarMonth):
    def __init__(self): ...


class BootCollectionGPOSetting(ScheduledTaskCommonTriggers):
    def __init__(self): ...
    @property
    def Delay(self) -> str: ...
    @Delay.setter
    def Delay(self, value: str) -> None: ...


class CalendarCollectionGPOSetting(ScheduledTaskCommonTriggers):
    def __init__(self): ...
    @property
    def RandomDelay(self) -> str: ...
    @property
    def ScheduleByDay(self) -> CalendarDailyGPOSetting: ...
    @property
    def ScheduleByMonth(self) -> CalendarMonthlyGPOSetting: ...
    @property
    def ScheduleByMonthDayOfWeek(self) -> CalendarMonthlyByDayOfWeekGPOSetting: ...
    @property
    def ScheduleByWeek(self) -> CalendarWeeklyGPOSetting: ...
    @RandomDelay.setter
    def RandomDelay(self, value: str) -> None: ...
    @ScheduleByDay.setter
    def ScheduleByDay(self, value: CalendarDailyGPOSetting) -> None: ...
    @ScheduleByMonth.setter
    def ScheduleByMonth(self, value: CalendarMonthlyGPOSetting) -> None: ...
    @ScheduleByMonthDayOfWeek.setter
    def ScheduleByMonthDayOfWeek(self, value: CalendarMonthlyByDayOfWeekGPOSetting) -> None: ...
    @ScheduleByWeek.setter
    def ScheduleByWeek(self, value: CalendarWeeklyGPOSetting) -> None: ...


class CalendarDailyGPOSetting(ScheduledTaskCommonTriggers):
    def __init__(self): ...
    @property
    def DaysInterval(self) -> str: ...
    @DaysInterval.setter
    def DaysInterval(self, value: str) -> None: ...


class CalendarMonth(PolicyMakerElement):
    def __init__(self): ...


class CalendarMonthlyByDayOfWeekGPOSetting(ScheduledTaskCommonTriggers):
    def __init__(self): ...
    @property
    def DaysOfWeek(self) -> Collection: ...
    @property
    def Months(self) -> Collection: ...
    @property
    def Weeks(self) -> Collection: ...


class CalendarMonthlyGPOSetting(ScheduledTaskCommonTriggers):
    def __init__(self): ...
    @property
    def CalendarMonthly(self) -> Collection: ...
    @property
    def DaysOfMonth(self) -> Collection: ...


class CalendarWeeklyGPOSetting(ScheduledTaskCommonTriggers):
    def __init__(self): ...
    @property
    def DaysOfWeek(self) -> Collection: ...
    @property
    def WeeksInterval(self) -> str: ...
    @WeeksInterval.setter
    def WeeksInterval(self, value: str) -> None: ...


class December(CalendarMonth):
    def __init__(self): ...


class EventCollectionGPOSetting(ScheduledTaskCommonTriggers):
    def __init__(self): ...
    @property
    def Delay(self) -> str: ...
    @property
    def Subscription(self) -> str: ...
    @Delay.setter
    def Delay(self, value: str) -> None: ...
    @Subscription.setter
    def Subscription(self, value: str) -> None: ...


class ExecActionGPOSetting(PolicyMakerElement):
    @property
    def Arguments(self) -> str: ...
    @property
    def Command(self) -> str: ...
    @property
    def WorkingDirectory(self) -> str: ...
    @Arguments.setter
    def Arguments(self, value: str) -> None: ...
    @Command.setter
    def Command(self, value: str) -> None: ...
    @WorkingDirectory.setter
    def WorkingDirectory(self, value: str) -> None: ...


class February(CalendarMonth):
    def __init__(self): ...


class Friday(WeekDay):
    def __init__(self): ...


class IdleCollectionGPOSetting(ScheduledTaskCommonTriggers):
    def __init__(self): ...
    @property
    def Delay(self) -> str: ...
    @Delay.setter
    def Delay(self, value: str) -> None: ...


class ImmediateTaskGPOSetting(ScheduledTasksGPOSettingBase):
    def __init__(self): ...


class ImmediateTaskV2GPOSetting(ScheduledTasksGPOSettingBase):
    def __init__(self): ...


class January(CalendarMonth):
    def __init__(self): ...


class July(CalendarMonth):
    def __init__(self): ...


class June(CalendarMonth):
    def __init__(self): ...


class LogonCollectionGPOSetting(ScheduledTaskCommonTriggers):
    def __init__(self): ...
    @property
    def Delay(self) -> str: ...
    @property
    def UserId(self) -> str: ...
    @Delay.setter
    def Delay(self, value: str) -> None: ...
    @UserId.setter
    def UserId(self, value: str) -> None: ...


class March(CalendarMonth):
    def __init__(self): ...


class May(CalendarMonth):
    def __init__(self): ...


class Monday(WeekDay):
    def __init__(self): ...


class November(CalendarMonth):
    def __init__(self): ...


class October(CalendarMonth):
    def __init__(self): ...


class RegistrationCollectionGPOSetting(ScheduledTaskCommonTriggers):
    def __init__(self): ...
    @property
    def Delay(self) -> str: ...
    @Delay.setter
    def Delay(self, value: str) -> None: ...


class Saturday(WeekDay):
    def __init__(self): ...


class ScheduledTaskCommonRepetition(PolicyMakerElement):
    def __init__(self): ...
    @property
    def Duration(self) -> str: ...
    @property
    def Interval(self) -> str: ...
    @property
    def StopAtDurationEnd(self) -> str: ...
    @Duration.setter
    def Duration(self, value: str) -> None: ...
    @Interval.setter
    def Interval(self, value: str) -> None: ...
    @StopAtDurationEnd.setter
    def StopAtDurationEnd(self, value: str) -> None: ...


class ScheduledTaskCommonTriggers(PolicyMakerElement):
    def __init__(self): ...
    @property
    def Enabled(self) -> str: ...
    @property
    def EndBoundary(self) -> str: ...
    @property
    def ExecutionTimeLimit(self) -> str: ...
    @property
    def Repetition(self) -> ScheduledTaskCommonRepetition: ...
    @property
    def StartBoundary(self) -> str: ...
    @Enabled.setter
    def Enabled(self, value: str) -> None: ...
    @EndBoundary.setter
    def EndBoundary(self, value: str) -> None: ...
    @ExecutionTimeLimit.setter
    def ExecutionTimeLimit(self, value: str) -> None: ...
    @Repetition.setter
    def Repetition(self, value: ScheduledTaskCommonRepetition) -> None: ...
    @StartBoundary.setter
    def StartBoundary(self, value: str) -> None: ...


class ScheduledTaskProperties(PolicyMakerProperties):
    @property
    def Task(self) -> TaskCollectionGPOSetting: ...
    @property
    def Triggers(self) -> Collection: ...
    @property
    def Version(self) -> str: ...
    @Task.setter
    def Task(self, value: TaskCollectionGPOSetting) -> None: ...
    @Version.setter
    def Version(self, value: str) -> None: ...


class ScheduledTasksGPOSetting(ScheduledTasksGPOSettingBase):
    def __init__(self): ...


class ScheduledTasksGPOSettingBase:
    def GetHashKey(self) -> str: ...


class ScheduledTasksGPOSettings(PolicyMakerElement):
    def __init__(self): ...
    @property
    def ScheduledTasksSettingsList(self) -> Collection: ...
    @ScheduledTasksSettingsList.setter
    def ScheduledTasksSettingsList(self, value: Collection) -> None: ...


class ScheduledTasksRsopSetting(PolicyMakerRsopSetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, managementObject: ManagementObject): ...
    def GetHashKey(self) -> str: ...
    def GetItemSubInstanceAttributeName(self) -> str: ...


class ScheduledTasksSettings(PolicyMakerSettings):
    def __init__(self): ...
    @property
    def ScheduledTasksGPOSettings(self) -> ScheduledTasksGPOSettings: ...
    @property
    def ScheduledTasksRsopSettings(self) -> Collection: ...
    def GetGPOSettings(self) -> ICollection: ...
    def GetRsopSettings(self) -> ICollection: ...
    def Initialize(self, context: ReportingContext) -> None: ...
    @ScheduledTasksGPOSettings.setter
    def ScheduledTasksGPOSettings(self, value: ScheduledTasksGPOSettings) -> None: ...
    @ScheduledTasksRsopSettings.setter
    def ScheduledTasksRsopSettings(self, value: Collection) -> None: ...


class ScheduledTasksV2GPOSetting(ScheduledTasksGPOSettingBase):
    def __init__(self): ...


class ScheduledTasksV2GPOSettingBase:
    def GetHashKey(self) -> str: ...


class ScheduledTaskV2IdleSettings(PolicyMakerElement):
    @property
    def Duration(self) -> str: ...
    @property
    def RestartOnIdle(self) -> str: ...
    @property
    def StopOnIdleEnd(self) -> str: ...
    @property
    def WaitTimeout(self) -> str: ...
    @Duration.setter
    def Duration(self, value: str) -> None: ...
    @RestartOnIdle.setter
    def RestartOnIdle(self, value: str) -> None: ...
    @StopOnIdleEnd.setter
    def StopOnIdleEnd(self, value: str) -> None: ...
    @WaitTimeout.setter
    def WaitTimeout(self, value: str) -> None: ...


class ScheduledTaskV2NetworkSettings(PolicyMakerElement):
    @property
    def Id(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @Id.setter
    def Id(self, value: str) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...


class ScheduledTaskV2Principal(PolicyMakerElement):
    @property
    def DisplayName(self) -> str: ...
    @property
    def GroupId(self) -> str: ...
    @property
    def LogonType(self) -> str: ...
    @property
    def RunLevel(self) -> str: ...
    @property
    def UserId(self) -> str: ...
    @DisplayName.setter
    def DisplayName(self, value: str) -> None: ...
    @GroupId.setter
    def GroupId(self, value: str) -> None: ...
    @LogonType.setter
    def LogonType(self, value: str) -> None: ...
    @RunLevel.setter
    def RunLevel(self, value: str) -> None: ...
    @UserId.setter
    def UserId(self, value: str) -> None: ...


class ScheduledTaskV2RegistrationInfo(PolicyMakerElement):
    @property
    def Author(self) -> str: ...
    @property
    def Date(self) -> str: ...
    @property
    def Description(self) -> str: ...
    @property
    def Documentation(self) -> str: ...
    @property
    def SecurityDescriptor(self) -> str: ...
    @property
    def Source(self) -> str: ...
    @property
    def URI(self) -> str: ...
    @Author.setter
    def Author(self, value: str) -> None: ...
    @Date.setter
    def Date(self, value: str) -> None: ...
    @Description.setter
    def Description(self, value: str) -> None: ...
    @Documentation.setter
    def Documentation(self, value: str) -> None: ...
    @SecurityDescriptor.setter
    def SecurityDescriptor(self, value: str) -> None: ...
    @Source.setter
    def Source(self, value: str) -> None: ...
    @URI.setter
    def URI(self, value: str) -> None: ...


class ScheduledTaskV2RestartOnFailure(PolicyMakerElement):
    @property
    def Count(self) -> str: ...
    @property
    def Interval(self) -> str: ...
    @Count.setter
    def Count(self, value: str) -> None: ...
    @Interval.setter
    def Interval(self, value: str) -> None: ...


class ScheduledTaskV2Settings(PolicyMakerElement):
    @property
    def AllowHardTerminate(self) -> str: ...
    @property
    def AllowStartOnDemand(self) -> str: ...
    @property
    def DeleteExpiredTaskAfter(self) -> str: ...
    @property
    def DisallowStartIfOnBatteries(self) -> str: ...
    @property
    def Enabled(self) -> str: ...
    @property
    def ExecutionTimeLimit(self) -> str: ...
    @property
    def Hidden(self) -> str: ...
    @property
    def IdleSettings(self) -> ScheduledTaskV2IdleSettings: ...
    @property
    def MultipleInstancesPolicy(self) -> str: ...
    @property
    def NetworkProfileName(self) -> str: ...
    @property
    def NetworkSettings(self) -> ScheduledTaskV2NetworkSettings: ...
    @property
    def Priority(self) -> str: ...
    @property
    def RestartOnFailure(self) -> ScheduledTaskV2RestartOnFailure: ...
    @property
    def RunOnlyIfIdle(self) -> str: ...
    @property
    def RunOnlyIfNetworkAvailable(self) -> str: ...
    @property
    def StartWhenAvailable(self) -> str: ...
    @property
    def StopIfGoingOnBatteries(self) -> str: ...
    @property
    def WakeToRun(self) -> str: ...
    @AllowHardTerminate.setter
    def AllowHardTerminate(self, value: str) -> None: ...
    @AllowStartOnDemand.setter
    def AllowStartOnDemand(self, value: str) -> None: ...
    @DeleteExpiredTaskAfter.setter
    def DeleteExpiredTaskAfter(self, value: str) -> None: ...
    @DisallowStartIfOnBatteries.setter
    def DisallowStartIfOnBatteries(self, value: str) -> None: ...
    @Enabled.setter
    def Enabled(self, value: str) -> None: ...
    @ExecutionTimeLimit.setter
    def ExecutionTimeLimit(self, value: str) -> None: ...
    @Hidden.setter
    def Hidden(self, value: str) -> None: ...
    @IdleSettings.setter
    def IdleSettings(self, value: ScheduledTaskV2IdleSettings) -> None: ...
    @MultipleInstancesPolicy.setter
    def MultipleInstancesPolicy(self, value: str) -> None: ...
    @NetworkProfileName.setter
    def NetworkProfileName(self, value: str) -> None: ...
    @NetworkSettings.setter
    def NetworkSettings(self, value: ScheduledTaskV2NetworkSettings) -> None: ...
    @Priority.setter
    def Priority(self, value: str) -> None: ...
    @RestartOnFailure.setter
    def RestartOnFailure(self, value: ScheduledTaskV2RestartOnFailure) -> None: ...
    @RunOnlyIfIdle.setter
    def RunOnlyIfIdle(self, value: str) -> None: ...
    @RunOnlyIfNetworkAvailable.setter
    def RunOnlyIfNetworkAvailable(self, value: str) -> None: ...
    @StartWhenAvailable.setter
    def StartWhenAvailable(self, value: str) -> None: ...
    @StopIfGoingOnBatteries.setter
    def StopIfGoingOnBatteries(self, value: str) -> None: ...
    @WakeToRun.setter
    def WakeToRun(self, value: str) -> None: ...


class SendMailActionGPOSetting(PolicyMakerElement):
    @property
    def Attachments(self) -> Collection: ...
    @property
    def Bcc(self) -> str: ...
    @property
    def Body(self) -> str: ...
    @property
    def Cc(self) -> str: ...
    @property
    def From(self) -> str: ...
    @property
    def ReplyTo(self) -> str: ...
    @property
    def Server(self) -> str: ...
    @property
    def Subject(self) -> str: ...
    @property
    def To(self) -> str: ...
    @Bcc.setter
    def Bcc(self, value: str) -> None: ...
    @Body.setter
    def Body(self, value: str) -> None: ...
    @Cc.setter
    def Cc(self, value: str) -> None: ...
    @From.setter
    def From(self, value: str) -> None: ...
    @ReplyTo.setter
    def ReplyTo(self, value: str) -> None: ...
    @Server.setter
    def Server(self, value: str) -> None: ...
    @Subject.setter
    def Subject(self, value: str) -> None: ...
    @To.setter
    def To(self, value: str) -> None: ...


class September(CalendarMonth):
    def __init__(self): ...


class SessionCollectionGPOSetting(ScheduledTaskCommonTriggers):
    def __init__(self): ...
    @property
    def Delay(self) -> str: ...
    @property
    def StateChange(self) -> str: ...
    @property
    def UserId(self) -> str: ...
    @Delay.setter
    def Delay(self, value: str) -> None: ...
    @StateChange.setter
    def StateChange(self, value: str) -> None: ...
    @UserId.setter
    def UserId(self, value: str) -> None: ...


class ShowMessageActionGPOSetting(PolicyMakerElement):
    @property
    def Body(self) -> str: ...
    @property
    def Title(self) -> str: ...
    @Body.setter
    def Body(self, value: str) -> None: ...
    @Title.setter
    def Title(self, value: str) -> None: ...


class Sunday(WeekDay):
    def __init__(self): ...


class TaskCollectionGPOSetting(PolicyMakerElement):
    def __init__(self): ...
    @property
    def Actions(self) -> Collection: ...
    @property
    def Principal(self) -> Collection: ...
    @property
    def Registrationinfo(self) -> ScheduledTaskV2RegistrationInfo: ...
    @property
    def Settings(self) -> ScheduledTaskV2Settings: ...
    @property
    def Triggers(self) -> Collection: ...
    @property
    def version(self) -> str: ...
    @Registrationinfo.setter
    def Registrationinfo(self, value: ScheduledTaskV2RegistrationInfo) -> None: ...
    @Settings.setter
    def Settings(self, value: ScheduledTaskV2Settings) -> None: ...
    @version.setter
    def version(self, value: str) -> None: ...


class Thursday(WeekDay):
    def __init__(self): ...


class TimeCollectionGPOSetting(ScheduledTaskCommonTriggers):
    def __init__(self): ...
    @property
    def RandomDelay(self) -> str: ...
    @RandomDelay.setter
    def RandomDelay(self, value: str) -> None: ...


class TriggerCollectionGPOSetting(ScheduledTaskCommonTriggers):
    def __init__(self): ...


class Tuesday(WeekDay):
    def __init__(self): ...


class Wednesday(WeekDay):
    def __init__(self): ...


class WeekDay(PolicyMakerElement):
    def __init__(self): ...
