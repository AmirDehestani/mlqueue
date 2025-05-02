from .status import Status
from dataclasses import dataclass, field
from typing import Dict, Any, List
from datetime import datetime


@dataclass
class Job:
    id: str
    task_name: str
    args: List[Any] = field(default_factory=list)
    kwargs: Dict[str, Any] = field(default_factory=dict)
    status: Status = Status.PENDING
    created_at: str = datetime.now().isoformat()
    updated_at: str = datetime.now().isoformat()

    def update_status(self, new_status: Status) -> None:
        """
        Update the job status and timestamp.
        Args:
            new_status (Status): The new status to set.
        Raises:
            ValueError: If new_status is not an instance of Status.
        """
        if not isinstance(new_status, Status):
            raise ValueError("new_status must be an instance of Status")
        self.status = new_status
        self.updated_at = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the job to a dictionary for serialization.
        Returns:
            dict: A dictionary representation of the job.
        """
        return {
            "id": self.id,
            "task_name": self.task_name,
            "args": self.args,
            "kwargs": self.kwargs,
            "status": str(self.status),
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Job":
        """
        Create a Job instance from a dictionary.
        Args:
            data (dict): A dictionary containing job data.
        Returns:
            Job: A Job instance.
        Raises:
            KeyError: If required keys are missing in the data.
        """
        return cls(
            id=data["id"],
            task_name=data["task_name"],
            args=data.get("args", []),
            kwargs=data.get("kwargs", {}),
            status=Status[data.get("status", "PENDING").upper()],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
        )
