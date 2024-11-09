import abc


class Task(abc.ABC): ...


class Future(abc.ABC): ...


class MyAsync(abc.ABC):
    def __init__(self) -> None:
        self.loop = []
        self.fututres = []
        self.tasks = []

    @abc.abstractmethod
    def create_task(task: Task) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def ensure_future(fututre: Future) -> Future:
        raise NotImplementedError
