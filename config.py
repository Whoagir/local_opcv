<<<<<<< HEAD
from dataclasses import dataclass, field
from typing import List, Dict

# Настройка времени старта нарезки
start_time = 30  # Нарезка начинается с 30-й секунды


@dataclass
class IndicatorArea:
    frame: int  # Номер кадра
    x: int  # Координата X
    y: int  # Координата Y
    width: int  # Ширина области
    height: int  # Высота области
    rotation: int  # Угол поворота
    label: str  # Название индикатора


@dataclass
class IndicatorSection:
    areas: List[IndicatorArea] = field(default_factory=list)  # Список областей в секции


# Создание секций с группировкой данных
indicator_sections: Dict[str, IndicatorSection] = {
    "Table_1": IndicatorSection(
        areas=[
            IndicatorArea(0, 285, 412, 110, 30, 0, "Player_1"),
            IndicatorArea(0, 737, 337, 110, 30, 0, "Player_2"),
            IndicatorArea(0, 1172, 425, 110, 30, 0, "Player_3"),
            IndicatorArea(0, 252, 767, 110, 30, 0, "Player_4"),
            IndicatorArea(0, 747, 915, 110, 30, 0, "Player_5"),
            IndicatorArea(0, 1217, 766, 110, 30, 0, "Player_6"),
            IndicatorArea(0, 538, 480, 97, 130, 0, "Card_1"),
            IndicatorArea(0, 645, 480, 97, 130, 0, "Card_2"),
            IndicatorArea(0, 750, 480, 97, 130, 0, "Card_3"),
            IndicatorArea(0, 855, 480, 97, 130, 0, "Card_4"),
            IndicatorArea(0, 955, 480, 97, 130, 0, "Card_5"),
            IndicatorArea(0, 825, 457, 80, 20, 0, "Commonbank"),
        ]
    ),
    "Table_2": IndicatorSection(
        areas=[
            IndicatorArea(0, 1492 + 10, 428, 110, 30, 0, "Player_1"),
            IndicatorArea(0, 1907 + 15, 344, 110, 30, 0, "Player_2"),
            IndicatorArea(0, 2323 + 18, 418, 110, 30, 0, "Player_3"),
            IndicatorArea(0, 1457 + 20, 766, 110, 30, 0, "Player_4"),
            IndicatorArea(0, 1907 + 20, 906, 110, 30, 0, "Player_5"),
            IndicatorArea(0, 2363 + 20, 756, 110, 30, 0, "Player_6"),
            IndicatorArea(0, 1733, 492, 92, 130, 0, "Card_1"),
            IndicatorArea(0, 1837, 492, 92, 130, 0, "Card_2"),
            IndicatorArea(0, 1940, 492, 92, 130, 0, "Card_3"),
            IndicatorArea(0, 2044, 492, 92, 130, 0, "Card_4"),
            IndicatorArea(0, 2143, 492, 92, 130, 0, "Card_5"),
            IndicatorArea(0, 2003, 457, 80, 20, 0, "Commonbank"),
        ]
    ),
    "Table_3": IndicatorSection(
        areas=[
            IndicatorArea(0, 2654 + 20, 409, 110, 30, 0, "Player_1"),
            IndicatorArea(0, 3089 + 20, 307, 110, 30, 0, "Player_2"),
            IndicatorArea(0, 3547 + 20, 369, 110, 30, 0, "Player_3"),
            IndicatorArea(0, 2620 + 20, 750, 110, 30, 0, "Player_4"),
            IndicatorArea(0, 3085 + 20, 892, 110, 30, 0, "Player_5"),
            IndicatorArea(0, 3587 + 20, 730, 110, 30, 0, "Player_6"),
            IndicatorArea(0, 1733, 492, 92, 130, 0, "Card_1"),
            IndicatorArea(0, 1837, 492, 92, 130, 0, "Card_2"),
            IndicatorArea(0, 1940, 492, 92, 130, 0, "Card_3"),
            IndicatorArea(0, 2044, 492, 92, 130, 0, "Card_4"),
            IndicatorArea(0, 2143, 492, 92, 130, 0, "Card_5"),
            IndicatorArea(0, 2003, 457, 80, 20, 0, "Commonbank"),
        ]
    ),
    "Table_4": IndicatorSection(
        areas=[
            IndicatorArea(0, 290 + 20, 1294, 110, 30, 0, "Player_1"),
            IndicatorArea(0, 737 + 20, 1198, 110, 30, 0, "Player_2"),
            IndicatorArea(0, 1173 + 20, 1271, 110, 30, 0, "Player_3"),
            IndicatorArea(0, 254 + 20, 1644, 110, 30, 0, "Player_4"),
            IndicatorArea(0, 740 + 20, 1771, 110, 30, 0, "Player_5"),
            IndicatorArea(0, 1225, 1604, 110, 30, 0, "Player_6"),
            IndicatorArea(0, 1733, 492, 92, 130, 0, "Card_1"),
            IndicatorArea(0, 1837, 492, 92, 130, 0, "Card_2"),
            IndicatorArea(0, 1940, 492, 92, 130, 0, "Card_3"),
            IndicatorArea(0, 2044, 492, 92, 130, 0, "Card_4"),
            IndicatorArea(0, 2143, 492, 92, 130, 0, "Card_5"),
            IndicatorArea(0, 2003, 457, 80, 20, 0, "Commonbank"),
        ]
    ),
    "Table_5": IndicatorSection(
        areas=[
            IndicatorArea(0, 1515, 1264, 110, 30, 0, "Player_1"),
            IndicatorArea(0, 1925, 1180, 110, 30, 0, "Player_2"),
            IndicatorArea(0, 2345, 1255, 110, 30, 0, "Player_3"),
            IndicatorArea(0, 1480, 1596, 110, 30, 0, "Player_4"),
            IndicatorArea(0, 1930, 1735, 110, 30, 0, "Player_5"),
            IndicatorArea(0, 2378, 1590, 110, 30, 0, "Player_6"),
            IndicatorArea(0, 1736, 1325, 92, 130, 0, "Card_1"),
            IndicatorArea(0, 1840, 1325, 92, 130, 0, "Card_2"),
            IndicatorArea(0, 1935, 1325, 92, 130, 0, "Card_3"),
            IndicatorArea(0, 2035, 1325, 92, 130, 0, "Card_4"),
            IndicatorArea(0, 2135, 1325, 92, 130, 0, "Card_5"),
            IndicatorArea(0, 2010, 1290, 80, 20, 0, "Commonbank"),
        ]
    ),
    "Table_6": IndicatorSection(
        areas=[
            IndicatorArea(0, 2674, 1255, 110, 30, 0, "Player_1"),
            IndicatorArea(0, 3105, 1175, 110, 30, 0, "Player_2"),
            IndicatorArea(0, 3565, 1265, 110, 30, 0, "Player_3"),
            IndicatorArea(0, 2650, 1590, 110, 30, 0, "Player_4"),
            IndicatorArea(0, 3110, 1755, 110, 30, 0, "Player_5"),
            IndicatorArea(0, 3605, 1625, 110, 30, 0, "Player_6"),
            IndicatorArea(0, 2910, 1325, 92, 130, 0, "Card_1"),
            IndicatorArea(0, 3015, 1325, 92, 130, 0, "Card_2"),
            IndicatorArea(0, 3120, 1325, 92, 130, 0, "Card_3"),
            IndicatorArea(0, 3225, 1325, 92, 130, 0, "Card_4"),
            IndicatorArea(0, 3330, 1325, 92, 130, 0, "Card_5"),
            IndicatorArea(0, 3195, 1295, 80, 20, 0, "Commonbank"),
        ]
    ),
}
=======

# Настройка тайминга старта нарезки (в секундах)
start_time = 30  # Нарезка начинается с 10-й секунды

indicator_areas = [
    [0, 285,  412, 110, 30,  0, "tb_1_pl_1"],
    [0, 737,  337, 110, 30,  0, "tb_1_pl_2"],
    [0, 1172, 425, 110, 30,  0, "tb_1_pl_3"],
    [0, 252,  767, 110, 30,  0, "tb_1_pl_4"],
    [0, 747,  915, 110, 30,  0, "tb_1_pl_5"],
    [0, 1217, 766, 110, 30,  0, "tb_1_pl_6"],
    [0, 538,  480, 97,  130, 0, "tb_1_card_1"],
    [0, 645,  480, 97,  130, 0, "tb_1_card_2"],
    [0, 750,  480, 97,  130, 0, "tb_1_card_3"],
    [0, 855,  480, 97,  130, 0, "tb_1_card_4"],
    [0, 955,  480, 97,  130, 0, "tb_1_card_5"],
    [0, 825,  457, 80,  20,  0, "tb_1_commonbank"],

    [0, 1492 + 10, 428, 110, 30,  0, "tb_2_pl_1"],
    [0, 1907 + 15, 344, 110, 30,  0, "tb_2_pl_2"],
    [0, 2323 + 18, 418, 110, 30,  0, "tb_2_pl_3"],
    [0, 1457 + 20, 766, 110, 30,  0, "tb_2_pl_4"],
    [0, 1907 + 20, 906, 110, 30,  0, "tb_2_pl_5"],
    [0, 2363 + 20, 756, 110, 30,  0, "tb_2_pl_6"],
    [0, 1733, 492, 92,  130, 0, "tb_2_card_1"],
    [0, 1837, 492, 92,  130, 0, "tb_2_card_2"],
    [0, 1940, 492, 92,  130, 0, "tb_2_card_3"],
    [0, 2044, 492, 92,  130, 0, "tb_2_card_4"],
    [0, 2143, 492, 92,  130, 0, "tb_2_card_5"],
    [0, 2003, 457, 80,  20,  0, "tb_2_commonbank"],

    [0, 2654 + 20, 409, 110, 30, 0, "tb_3_pl_1"],
    [0, 3089 + 20, 307, 110, 30, 0, "tb_3_pl_2"],
    [0, 3547 + 20, 369, 110, 30, 0, "tb_3_pl_3"],
    [0, 2620 + 20, 750, 110, 30, 0, "tb_3_pl_4"],
    [0, 3085 + 20, 892, 110, 30, 0, "tb_3_pl_5"],
    [0, 3587 + 20, 730, 110, 30, 0, "tb_3_pl_6"],
    [0, 1733, 492, 92, 130, 0, "tb_2_card_1"],
    [0, 1837, 492, 92, 130, 0, "tb_2_card_2"],
    [0, 1940, 492, 92, 130, 0, "tb_2_card_3"],
    [0, 2044, 492, 92, 130, 0, "tb_2_card_4"],
    [0, 2143, 492, 92, 130, 0, "tb_2_card_5"],
    [0, 2003, 457, 80, 20, 0, "tb_2_commonbank"],

    [0, 290  + 20, 1294, 110, 30, 0, "tb_4_pl_1"],
    [0, 737  + 20, 1198, 110, 30, 0, "tb_4_pl_2"],
    [0, 1173 + 20, 1271, 110, 30, 0, "tb_4_pl_3"],
    [0, 254  + 20, 1644, 110, 30, 0, "tb_4_pl_4"],
    [0, 740  + 20, 1771, 110, 30, 0, "tb_4_pl_5"],
    [0, 1225, 1604, 110, 30, 0, "tb_4_pl_6"],
    [0, 1733, 492, 92, 130, 0, "tb_2_card_1"],
    [0, 1837, 492, 92, 130, 0, "tb_2_card_2"],
    [0, 1940, 492, 92, 130, 0, "tb_2_card_3"],
    [0, 2044, 492, 92, 130, 0, "tb_2_card_4"],
    [0, 2143, 492, 92, 130, 0, "tb_2_card_5"],
    [0, 2003, 457, 80, 20, 0, "tb_2_commonbank"],
]
>>>>>>> main
