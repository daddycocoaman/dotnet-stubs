from typing import Tuple, Set, Iterable, List


class ActivityScheduledQueryElement(TrackingQueryElement):
    def __init__(self): ...
    @property
    def ActivityName(self) -> str: ...
    @property
    def ChildActivityName(self) -> str: ...
    @ActivityName.setter
    def ActivityName(self, value: str) -> None: ...
    @ChildActivityName.setter
    def ChildActivityName(self, value: str) -> None: ...


class ActivityScheduledQueryElementCollection:
    def __init__(self): ...


class ActivityStateQueryElement(TrackingQueryElement):
    def __init__(self): ...
    @property
    def ActivityName(self) -> str: ...
    @property
    def Arguments(self) -> ArgumentElementCollection: ...
    @property
    def States(self) -> StateElementCollection: ...
    @property
    def Variables(self) -> VariableElementCollection: ...
    @ActivityName.setter
    def ActivityName(self, value: str) -> None: ...


class ActivityStateQueryElementCollection:
    def __init__(self): ...


class AnnotationElement(TrackingConfigurationElement):
    def __init__(self): ...
    @property
    def ElementKey(self) -> Object: ...
    @property
    def Name(self) -> str: ...
    @property
    def Value(self) -> str: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Value.setter
    def Value(self, value: str) -> None: ...


class AnnotationElementCollection:
    def __init__(self): ...


class ArgumentElement(TrackingConfigurationElement):
    def __init__(self): ...
    @property
    def ElementKey(self) -> Object: ...
    @property
    def Name(self) -> str: ...
    @Name.setter
    def Name(self, value: str) -> None: ...


class ArgumentElementCollection:
    def __init__(self): ...


class BookmarkResumptionQueryElement(TrackingQueryElement):
    def __init__(self): ...
    @property
    def Name(self) -> str: ...
    @Name.setter
    def Name(self, value: str) -> None: ...


class BookmarkResumptionQueryElementCollection:
    def __init__(self): ...


class CancelRequestedQueryElement(TrackingQueryElement):
    def __init__(self): ...
    @property
    def ActivityName(self) -> str: ...
    @property
    def ChildActivityName(self) -> str: ...
    @ActivityName.setter
    def ActivityName(self, value: str) -> None: ...
    @ChildActivityName.setter
    def ChildActivityName(self, value: str) -> None: ...


class CancelRequestedQueryElementCollection:
    def __init__(self): ...


class CustomTrackingQueryElement(TrackingQueryElement):
    def __init__(self): ...
    @property
    def ActivityName(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @ActivityName.setter
    def ActivityName(self, value: str) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...


class CustomTrackingQueryElementCollection:
    def __init__(self): ...


class FaultPropagationQueryElement(TrackingQueryElement):
    def __init__(self): ...
    @property
    def FaultHandlerActivityName(self) -> str: ...
    @property
    def FaultSourceActivityName(self) -> str: ...
    @FaultHandlerActivityName.setter
    def FaultHandlerActivityName(self, value: str) -> None: ...
    @FaultSourceActivityName.setter
    def FaultSourceActivityName(self, value: str) -> None: ...


class FaultPropagationQueryElementCollection:
    def __init__(self): ...


class ProfileElement(TrackingConfigurationElement):
    def __init__(self): ...
    @property
    def ElementKey(self) -> Object: ...
    @property
    def ImplementationVisibility(self) -> ImplementationVisibility: ...
    @property
    def Name(self) -> str: ...
    @property
    def Workflows(self) -> ProfileWorkflowElementCollection: ...
    @ImplementationVisibility.setter
    def ImplementationVisibility(self, value: ImplementationVisibility) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...


class ProfileElementCollection:
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType: ...


class ProfileWorkflowElement(TrackingConfigurationElement):
    def __init__(self): ...
    @property
    def ActivityDefinitionId(self) -> str: ...
    @property
    def ActivityScheduledQueries(self) -> ActivityScheduledQueryElementCollection: ...
    @property
    def ActivityStateQueries(self) -> ActivityStateQueryElementCollection: ...
    @property
    def BookmarkResumptionQueries(self) -> BookmarkResumptionQueryElementCollection: ...
    @property
    def CancelRequestedQueries(self) -> CancelRequestedQueryElementCollection: ...
    @property
    def CustomTrackingQueries(self) -> CustomTrackingQueryElementCollection: ...
    @property
    def ElementKey(self) -> Object: ...
    @property
    def FaultPropagationQueries(self) -> FaultPropagationQueryElementCollection: ...
    @property
    def StateMachineStateQueries(self) -> StateMachineStateQueryElementCollection: ...
    @property
    def WorkflowInstanceQueries(self) -> WorkflowInstanceQueryElementCollection: ...
    @ActivityDefinitionId.setter
    def ActivityDefinitionId(self, value: str) -> None: ...


class ProfileWorkflowElementCollection:
    def __init__(self): ...


class StateElement(TrackingConfigurationElement):
    def __init__(self): ...
    @property
    def ElementKey(self) -> Object: ...
    @property
    def Name(self) -> str: ...
    @Name.setter
    def Name(self, value: str) -> None: ...


class StateElementCollection:
    def __init__(self): ...


class StateMachineStateQueryElement(TrackingQueryElement):
    def __init__(self): ...
    @property
    def ActivityName(self) -> str: ...
    @ActivityName.setter
    def ActivityName(self, value: str) -> None: ...


class StateMachineStateQueryElementCollection:
    def __init__(self): ...




class TrackingConfigurationElement(ConfigurationElement):
    @property
    def ElementKey(self) -> Object: ...


class TrackingQueryElement(TrackingConfigurationElement):
    @property
    def Annotations(self) -> AnnotationElementCollection: ...
    @property
    def ElementKey(self) -> Object: ...


class TrackingSection(ConfigurationSection):
    def __init__(self): ...
    @property
    def Profiles(self) -> ProfileElementCollection: ...
    @property
    def TrackingProfiles(self) -> Collection: ...


class VariableElement(TrackingConfigurationElement):
    def __init__(self): ...
    @property
    def ElementKey(self) -> Object: ...
    @property
    def Name(self) -> str: ...
    @Name.setter
    def Name(self, value: str) -> None: ...


class VariableElementCollection:
    def __init__(self): ...


class WorkflowInstanceQueryElement(TrackingQueryElement):
    def __init__(self): ...
    @property
    def States(self) -> StateElementCollection: ...


class WorkflowInstanceQueryElementCollection:
    def __init__(self): ...
