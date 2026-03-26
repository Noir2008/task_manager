def validate_tasks(status: str) -> bool:
    return status in ["new", "in_progress", "done"]