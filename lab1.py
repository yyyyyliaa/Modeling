import numpy as np
import matplotlib.pyplot as plt


def generate_random(seed, T, n):
    np.random.seed(seed)
    random_numbers = []
    a = seed
    b = seed + 1  # Используем соседние значения для начальных чисел
    for _ in range(n):
        # Умножаем два числа и используем только последние T разрядов
        product = a * b
        zi = product % T
        random_numbers.append(zi / T)
        # Переходим к следующим числам
        a = (a + 1) % T  # Изменяем a для увеличения разнообразия последовательности
        b = (b + 1) % T  # Изменяем b для увеличения разнообразия последовательности
    return random_numbers


T = 10000

random_numbers = generate_random(seed=42, T=T, n=T)

M = np.mean(random_numbers)
D = np.var(random_numbers)

print(f"Математическое ожидание: {M}")
print(f"Дисперсия: {D}")

plt.hist(random_numbers, bins=10, density=True)
plt.show()

start_pow, end_pow = 4, 21
pow_count = (end_pow - start_pow) + 1
T_values = np.logspace(start_pow, end_pow, num=pow_count, base=2, dtype=int)

for s in [2, 5, 10]:
    corr_values = []
    for T in T_values:
        random_numbers = generate_random(seed=42, T=T, n=T)
        R = np.corrcoef(random_numbers[:-s], random_numbers[s:])[0, 1]
        corr_values.append(R)

    plt.plot(T_values, corr_values, label=f's={s}')

plt.xscale('log')
plt.xlabel('T')
plt.ylabel('corr')
plt.legend()
plt.show()
