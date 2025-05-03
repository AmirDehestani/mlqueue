from interfaces import JobStoreInterface
from models.job import Job
from models.status import Status
from database.mongodb import MongoDB
from singleton import Singleton

class JobStore(JobStoreInterface, metaclass=Singleton):
    def __init__(self):
        self.jobs_collection = MongoDB().get_collection("jobs")

    def save_job(self, job: Job) -> None:
        if self.jobs_collection.find_one({"id": job.id}):
            raise ValueError(f"Job with ID '{job.id}' already exists.")
        self.jobs_collection.insert_one(job.to_dict())

    def get_job(self, job_id: str) -> Job:
        job_dict = self.jobs_collection.find_one({"id": job_id})
        if not job_dict:
            raise KeyError(f"Job with ID '{job_id}' does not exist.")
        return Job.from_dict(job_dict)

    def update_job(self, job: Job) -> None:
        if not self.jobs_collection.find_one({"id": job.id}):
            raise KeyError(f"Job with ID '{job.id}' does not exist.")
        self.jobs_collection.replace_one({"id": job.id}, job.to_dict())

    def list_jobs(self, status: Status = None) -> list[Job]:
        query = {}
        if status is not None:
            query["status"] = str(status)
        return [Job.from_dict(doc) for doc in self.jobs_collection.find(query)]
