from models.job import Job
from .singleton import Singleton


class JobQueue(metaclass=Singleton):
    """
    JobQueue is a singleton class that manages a queue of jobs.
    It provides methods to enqueue, dequeue, and check the size of the queue.
    """

    def __init__(self):
        """
        Initialize the job queue
        """
        self._queue = []

    def enqueue(self, job: Job) -> None:
        """
        Add a job to the queue
        Args:
            job (Job): The job to add to the queue.
        Raises:
            ValueError: If the job is invalid or already in the queue.
        """
        if not isinstance(job, Job):
            raise ValueError("Invalid job type.")
        if job in self._queue:
            raise ValueError("Job already in queue.")
        self._queue.append(job)

    def dequeue(self) -> Job:
        """
        Remove and return the next job from the queue
        Returns:
            Job: The next job in the queue.
        Raises:
            IndexError: If the queue is empty.
        """
        if not self._queue:
            raise IndexError("Queue is empty.")
        return self._queue.pop(0)

    def size(self) -> int:
        """
        Get the number of jobs in the queue
        Returns:
            int: The number of jobs in the queue.
        """
        return len(self._queue)
