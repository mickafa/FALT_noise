import math
mg = 1.0    # пусть масса коптера 0.1 кг
c = 340.0   # скорость звука
rho = 1.225 # плотность воздуха

# по заданной длине лопасти найдем все параметры
def noise ( r ):
    s = math.pi * r*r          # площадь, ометаемая винтом
    dp = mg / s                # избыточное давление
    i = dp*dp / (2.0*rho*c)    # шум
    v = math.sqrt ( dp / rho ) # скорость воздуха = скорость лопасти
    n = mg * v                 # мощность
    omega = v / r              # частота вращения
    return i, omega, n


i0, omega0, n0 = noise ( 1.0 ) # начальные параметры
r = 1.0                        # пусть длина лопасти = 1 м
i, omega, n = 1., 1., 1.       # инициализация 

# отвечаем на вопрос №2
while ( i0 / i < 3.0 ):         # подбираем длину лопасти
    r += 1e-7                   # пока не достигнем нужного шума
    i, omega, n = noise ( r )
print ( "Ответ №2: отнощение частот вращения = ", omega0 / omega )

# отвечаем на вопрос №3
r = 1.0
i = 1.
while ( i0 / i < 2.0 ):         # подбираем длину лопасти
    r += 1e-7                   # пока не достигнем нужного шума
    i, omega, n = noise ( r )
print ( "Ответ №3: отнощение мощностей = ", n0 / n )
