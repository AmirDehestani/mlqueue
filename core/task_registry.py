from .singleton import Singleton


class TaskRegistry(metaclass=Singleton):
    """
    TaskRegistry is a singleton class that manages the registration and retrieval of tasks.
    It allows tasks to be registered with a name and provides methods to retrieve and list them.
    """

    def __init__(self):
        """
        Initialize the task registry
        """
        self._tasks = {}

    def register_task(self, name: str, func) -> None:
        """
        Register a task with a name and function
        Args:
            name (str): The name of the task.
            func (Callable): The function to register as a task.
        Raises:
            ValueError: If the task name is already registered.
        """
        if name in self._tasks:
            raise ValueError(f"Task '{name}' is already registered.")
        self._tasks[name] = func

    def get_task(self, name: str):
        """
        Retrieve a task by name
        Args:
            name (str): The name of the task to retrieve.
        Returns:
            Callable: The function associated with the task name.
        Raises:
            KeyError: If the task does not exist.
        """
        if name not in self._tasks:
            raise KeyError(f"Task '{name}' does not exist.")
        return self._tasks[name]

    def list_tasks(self) -> list[str]:
        """
        List all registered tasks
        Returns:
            List[str]: A list of task names.
        """
        return list(self._tasks.keys())


def task(func):
    """
    Decorator to register a function as a task.
    """
    TaskRegistry().register_task(func.__name__, func)
    return func
