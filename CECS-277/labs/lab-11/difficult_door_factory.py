from door_factory import DoorFactory
from door import Door
from combo_door import ComboDoor
from deadbolt_door import DeadboltDoor
from code_door import CodeDoor
from random import choice


class DifficultDoorFactory(DoorFactory):
    def create_door(self) -> Door:
        return choice([CodeDoor(), DeadboltDoor(), ComboDoor()])
