import model


class StorageException(Exception):
    pass


class LocalStorage:
    def __init__(self):
        self.storage = {}

    def create(self, event: model.Event):
        try:
            self.storage[event.event_id] = event
        except Exception as ex:
            return StorageException(f"failed CREATE operation with: {ex}")

    def list(self):
        try:
            return self.storage.values()
        except Exception as ex:
            return StorageException(f"failed LIST operation with: {ex}")

    def read(self, event_id: str):
        if event_id not in self.storage:
            raise StorageException(f"{event_id} not found in storage")
        return self.storage[event_id]

    def update(self, event_id: str, event: model.Event):
        if event_id not in self.storage:
            raise StorageException(f"{event_id} not found in storage")
        event_id = id
        self.storage[event_id] = event

    def delete(self, event_id: str):
        if event_id not in self.storage:
            raise StorageException(f"{event_id} not found in storage")
        del self.storage[event_id]
