from abc import ABC, abstractmethod
from typing import List, Callable
from models.job import Job
from models.status import Status

# --- Job Store Interface ---


class JobStoreInterface(ABC):
    @abstractmethod
    def save_job(self, job: Job) -> None:
        """
        Save a job to the store
        Args:
            job (Job): The job to save.
        Raises:
            ValueError: If the job is invalid or already exists.
        """
        pass

    @abstractmethod
    def get_job(self, job_id: str) -> Job:
        """
        Retrieve a job by its ID
        Args:
            job_id (str): The ID of the job to retrieve.
        Returns:
            Job: The job instance.
        Raises:
            KeyError: If the job does not exist.
        """
        pass

    @abstractmethod
    def update_job(self, job: Job) -> None:
        """
        Update an existing job
        Args:
            job (Job): The job to update.
        Raises:
            ValueError: If the job is invalid or does not exist.
        """
        pass

    @abstractmethod
    def list_jobs(self, status: Status = None) -> List[Job]:
        """
        List jobs with optional status filter
        Args:
            status (Status, optional): The status to filter jobs by.
        Returns:
            List[Job]: A list of jobs matching the status.
        """
        pass


# --- Task Registry Interface ---


class TaskRegistryInterface(ABC):
    @abstractmethod
    def register_task(self, name: str, func: Callable) -> None:
        """
        Register a task with a name and function
        Args:
            name (str): The name of the task.
            func (Callable): The function to register as a task.
        Raises:
            ValueError: If the task name is already registered.
        """
        pass

    @abstractmethod
    def get_task(self, name: str) -> Callable:
        """
        Retrieve a task by name
        Args:
            name (str): The name of the task to retrieve.
        Returns:
            Callable: The function associated with the task name.
        Raises:
            KeyError: If the task does not exist.
        """
        pass

    @abstractmethod
    def list_tasks(self) -> List[str]:
        """
        List all registered tasks
        Returns:
            List[str]: A list of task names.
        """
        pass


# --- Queue Interface ---


class JobQueueInterface(ABC):
    @abstractmethod
    def enqueue(self, job: Job) -> None:
        """
        Add a job to the queue
        Args:
            job (Job): The job to add to the queue.
        Raises:
            ValueError: If the job is invalid or already in the queue.
        """
        pass

    @abstractmethod
    def dequeue(self) -> Job:
        """
        Remove and return the next job from the queue
        Returns:
            Job: The next job in the queue.
        Raises:
            IndexError: If the queue is empty.
        """
        pass

    @abstractmethod
    def size(self) -> int:
        """
        Get the number of jobs in the queue
        Returns:
            int: The number of jobs in the queue.
        """
        pass
