from abc import ABC, ABCMeta, abstractmethod, abstractproperty


class Movable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def move(self):
        """
        Moving~
        """
        raise NotImplementedError

    @abstractproperty
    def speed(cls):
        """
        Speed equal to
        :return:
        """
        raise NotImplementedError