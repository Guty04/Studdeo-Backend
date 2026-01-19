class TeacherNotFound(Exception):
    def __init__(self, message: str = "Teacher not found.") -> None:
        super().__init__(message)
