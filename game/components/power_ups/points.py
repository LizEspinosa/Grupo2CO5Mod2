from game.components.power_ups.power_up import PowerUp
from game.utils.constants import  POINTS, POINTS_TYPE


class Points(PowerUp):
    def __init__(self):
        super().__init__(POINTS, POINTS_TYPE)
        