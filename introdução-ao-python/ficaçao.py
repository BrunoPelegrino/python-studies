def triangulo(x, y, z):
    is_triangle = (
        x + y > z and
        x + z > y and
        z + y > x
    )

    if not is_triangle:
        return "naõ é um triângulo"

    elif x == z == y:
        return "triangulo equilatero"
    elif x == z or x == y or z == y:
        return "triangulo isoceles"
    else:
        return "escaleno"
