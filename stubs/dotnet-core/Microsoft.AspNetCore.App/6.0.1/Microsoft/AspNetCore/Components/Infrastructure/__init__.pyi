from typing import Tuple, Set, Iterable, List


class ComponentStatePersistenceManager:
    def __init__(self, logger: ILogger): ...
    @property
    def State(self) -> PersistentComponentState: ...
    def PersistStateAsync(self, store: IPersistentComponentStateStore, renderer: Renderer) -> Task: ...
    def RestoreStateAsync(self, store: IPersistentComponentStateStore) -> Task: ...
