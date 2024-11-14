from door_factory import DoorFactory
from door import Door
from basic_door import BasicDoor
from locked_door import LockedDoor
from combo_door import ComboDoor
from random import choice


class EasyDoorFactory(DoorFactory):
    def create_door(self) -> Door:
        return choice([BasicDoor(), LockedDoor(), ComboDoor()])
