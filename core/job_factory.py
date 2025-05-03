from .job_store import JobStore
from .job_queue import JobQueue
from .singleton import Singleton
from models.job import Job
from uuid import uuid4


class JobFactory(metaclass=Singleton):
    """
    JobFactory is a singleton class that manages the creation and storage of jobs.
    It provides methods to create, save, and retrieve jobs from the job store and queue.
    """

    def __init__(self):
        """
        Initialize the job factory with a job store and queue.
        """
        self.job_store = JobStore()
        self.job_queue = JobQueue()

    def create_job(self, task_name: str, args: list, kwargs: dict) -> str:
        """
        Create a new job with a unique ID and add it to the job store and queue.
        Args:
            task_name (str): The name of the task to be executed.
            args (list): The arguments for the task.
            kwargs (dict): The keyword arguments for the task.
        Returns:
            str: The unique ID of the created job.
        """
        job_id = str(uuid4())
        job = Job(id=job_id, task_name=task_name, args=args, kwargs=kwargs)
        self.job_store.save_job(job)
        self.job_queue.enqueue(job)
        return job_id
