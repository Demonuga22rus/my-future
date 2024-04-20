def main():
    x, y = 300, 400
    width, height = 200, 300
    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    Нарисовать домик ширины width и height от опорной точки (x, y),
    которая находиться в середине нижней точки фундамента.
    х : координата х середины домика
    y : кордината у низа фундамента
    width : полная ширина домика (фундамент или вылет крыши включены)
    height: полная высота домика
    """
    print('Типа рисую домик...', x, y, width, height)
    foundation_height = 0.05 * height
    walls_widht = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height,
                     walls_widht, walls_height)
    draw_house_roof(x, y - foundation_height -
                    walls_height, width, roof_height)


def draw_house_foundation(x, y, width, height):
    """
    Нарисовать домик ширины width и height от опорной точки (x, y),
    которая находиться в середине нижней точки фундамента.
    х : координата х середины фундамента
    y : кордината у низа фундамента
    width : полная ширина фундамента
    height: полная высота фундамента
    """
    print('Типа рисую основание...', x, y, width, height)
    pass


def draw_house_walls(x, y, width, height):
    """
    Нарисовать домик ширины width и height от опорной точки (x, y),
    которая находиться в середине нижней точки фундамента.
    х : координата х середины стены
    y : кордината у низа стен
    width : полная ширина стен
    height: полная высота стен
    """
    print('Типа рисую стены...', x, y, width, height)
    pass


def draw_house_roof(x, y, width, height):
    """
    Нарисовать домик ширины width и height от опорной точки (x, y),
    которая находиться в середине нижней точки фундамента.
    х : координата х середины крыши
    y : кордината у низа крыши
    width : полная ширина крыши
    height: полная высота крыши
    """
    print('Типа рисую крышу...', x, y, width, height)
    pass
if __name__ == "__main__":
    main()
