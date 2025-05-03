from .interfaces import TaskRegistryInterface
from singleton import Singleton

class TaskRegistry(TaskRegistryInterface, metaclass=Singleton):
    def __init__(self):
        self._tasks = {}

    def register_task(self, name: str, func) -> None:
        if name in self._tasks:
            raise ValueError(f"Task '{name}' is already registered.")
        self._tasks[name] = func

    def get_task(self, name: str):
        if name not in self._tasks:
            raise KeyError(f"Task '{name}' does not exist.")
        return self._tasks[name]

    def list_tasks(self) -> list[str]:
        return list(self._tasks.keys())
    
def task(func):
    """
    Decorator to register a function as a task.
    """
    TaskRegistry().register_task(func.__name__, func)
    return func