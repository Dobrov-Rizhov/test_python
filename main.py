def discriminant(nu_a, nu_b, nu_c):
    num_d = nu_b**2 - 4 * nu_a * nu_c
    print(num_d)
    if num_d > 0:
        x1 = ((-nu_b)+(num_d**0.5))/2 * nu_a
        x2 = ((-nu_b)-(num_d**0.5))/2 * nu_a
        print(f'Уравнение имеет два корня x1 = {x1} и x2 = {x2}')
    elif num_d == 0:
        x1 = -(nu_b/(2*nu_a))
        print(f'Уравнение имеет один корень x = {x1}')
    else:
        print("Корней нет")


if __name__ == '__main__':
    num_a = int(input("a: "))
    num_b = int(input("b: "))
    num_c = int(input("c: "))
    discriminant(num_a, num_b, num_c)
