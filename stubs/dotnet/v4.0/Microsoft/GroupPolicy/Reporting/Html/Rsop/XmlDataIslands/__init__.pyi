from typing import Tuple, Set, Iterable, List


class CrimsonEventRecordSection:
    def __init__(self): ...
    @property
    def EventDescription(self) -> str: ...
    @property
    def EventId(self) -> str: ...
    @property
    def EventLevel(self) -> Byte: ...
    @property
    def EventTime(self) -> str: ...
    @property
    def EventXml(self) -> str: ...
    @EventDescription.setter
    def EventDescription(self, value: str) -> None: ...
    @EventId.setter
    def EventId(self, value: str) -> None: ...
    @EventLevel.setter
    def EventLevel(self, value: Byte) -> None: ...
    @EventTime.setter
    def EventTime(self, value: str) -> None: ...
    @EventXml.setter
    def EventXml(self, value: str) -> None: ...


class ExtensionProcessingTimeSection:
    def __init__(self): ...
    @property
    def ElapsedTime(self) -> str: ...
    @property
    def ExtensionGuid(self) -> str: ...
    @property
    def ExtensionName(self) -> str: ...
    @property
    def ProcessedTime(self) -> str: ...
    @ElapsedTime.setter
    def ElapsedTime(self, value: str) -> None: ...
    @ExtensionGuid.setter
    def ExtensionGuid(self, value: str) -> None: ...
    @ExtensionName.setter
    def ExtensionName(self, value: str) -> None: ...
    @ProcessedTime.setter
    def ProcessedTime(self, value: str) -> None: ...


class Label:
    def __init__(self): ...
    @property
    def Name(self) -> str: ...
    @property
    def ValueText(self) -> str: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @ValueText.setter
    def ValueText(self, value: str) -> None: ...


class PolicySectionTemplate:
    def __init__(self): ...
    @property
    def PolicyEventsDetails(self) -> Set(SinglePassEventsDetailsSection): ...
    @PolicyEventsDetails.setter
    def PolicyEventsDetails(self, value: Set(SinglePassEventsDetailsSection)) -> None: ...


class SinglePassEventsDetailsSection:
    def __init__(self): ...
    @property
    def ActivityId(self) -> str: ...
    @property
    def DomainControllerIPAddress(self) -> str: ...
    @property
    def DomainControllerName(self) -> str: ...
    @property
    def ErrorCount(self) -> UInt32: ...
    @property
    def EventRecord(self) -> Set(CrimsonEventRecordSection): ...
    @property
    def ExtensionProcessingTime(self) -> Set(ExtensionProcessingTimeSection): ...
    @property
    def LinkSpeedInKbps(self) -> str: ...
    @property
    def PolicyElapsedTime(self) -> str: ...
    @property
    def PolicyProcessingMode(self) -> str: ...
    @property
    def ProcessingAppMode(self) -> str: ...
    @property
    def ProcessingTrigger(self) -> str: ...
    @property
    def SlowLinkThresholdInKbps(self) -> str: ...
    @property
    def WarningCount(self) -> UInt32: ...
    @ActivityId.setter
    def ActivityId(self, value: str) -> None: ...
    @DomainControllerIPAddress.setter
    def DomainControllerIPAddress(self, value: str) -> None: ...
    @DomainControllerName.setter
    def DomainControllerName(self, value: str) -> None: ...
    @ErrorCount.setter
    def ErrorCount(self, value: UInt32) -> None: ...
    @EventRecord.setter
    def EventRecord(self, value: Set(CrimsonEventRecordSection)) -> None: ...
    @ExtensionProcessingTime.setter
    def ExtensionProcessingTime(self, value: Set(ExtensionProcessingTimeSection)) -> None: ...
    @LinkSpeedInKbps.setter
    def LinkSpeedInKbps(self, value: str) -> None: ...
    @PolicyElapsedTime.setter
    def PolicyElapsedTime(self, value: str) -> None: ...
    @PolicyProcessingMode.setter
    def PolicyProcessingMode(self, value: str) -> None: ...
    @ProcessingAppMode.setter
    def ProcessingAppMode(self, value: str) -> None: ...
    @ProcessingTrigger.setter
    def ProcessingTrigger(self, value: str) -> None: ...
    @SlowLinkThresholdInKbps.setter
    def SlowLinkThresholdInKbps(self, value: str) -> None: ...
    @WarningCount.setter
    def WarningCount(self, value: UInt32) -> None: ...


class XmlDataIslandsMainSectionTemplate(XmlDataIslandTemplate):
    def __init__(self): ...
    @property
    def ComputerPolicySection(self) -> PolicySectionTemplate: ...
    @property
    def Label(self) -> Set(Label): ...
    @property
    def UserPolicySection(self) -> PolicySectionTemplate: ...
    @ComputerPolicySection.setter
    def ComputerPolicySection(self, value: PolicySectionTemplate) -> None: ...
    @Label.setter
    def Label(self, value: Set(Label)) -> None: ...
    @UserPolicySection.setter
    def UserPolicySection(self, value: PolicySectionTemplate) -> None: ...


class XmlDataIslandTemplate:
    def ToString(self) -> str: ...
