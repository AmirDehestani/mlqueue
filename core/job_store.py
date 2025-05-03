from models.job import Job
from models.status import Status
from database.mongodb import MongoDB
from .singleton import Singleton


class JobStore(metaclass=Singleton):
    """
    JobStore is a singleton class that manages job storage in a MongoDB collection.
    It provides methods to save, retrieve, update, and list jobs.
    """

    def __init__(self):
        """
        Initialize the job store with a MongoDB collection.
        """
        self.jobs_collection = MongoDB().get_collection("jobs")

    def save_job(self, job: Job) -> None:
        """
        Save a job to the store
        Args:
            job (Job): The job to save.
        Raises:
            ValueError: If the job is invalid or already exists.
        """
        if self.jobs_collection.find_one({"id": job.id}):
            raise ValueError(f"Job with ID '{job.id}' already exists.")
        self.jobs_collection.insert_one(job.to_dict())

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
        job_dict = self.jobs_collection.find_one({"id": job_id})
        if not job_dict:
            raise KeyError(f"Job with ID '{job_id}' does not exist.")
        return Job.from_dict(job_dict)

    def update_job(self, job: Job) -> None:
        """
        Update an existing job
        Args:
            job (Job): The job to update.
        Raises:
            KeyError: If the job does not exist.
        """
        if not self.jobs_collection.find_one({"id": job.id}):
            raise KeyError(f"Job with ID '{job.id}' does not exist.")
        self.jobs_collection.replace_one({"id": job.id}, job.to_dict())

    # TODO: Add pagination and sorting options.
    def list_jobs(self, status: Status = None) -> list[Job]:
        """
        List jobs with optional status filter
        Args:
            status (Status, optional): The status to filter jobs by.
        Returns:
            List[Job]: A list of jobs matching the status.
        """
        query = {}
        if status is not None:
            query["status"] = str(status)
        return [Job.from_dict(doc) for doc in self.jobs_collection.find(query)]
