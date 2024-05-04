import random
import numpy as np
import matplotlib.pyplot as plt

# Данные для построения случайной величины
Xj = [-82.3, 4.3, 13.1, 28.2, 35.1, 55.3, 92.1]
Pj = [0.285, 0.152, 0.070, 0.056, 0.288, 0.126, 0.023]

np.random.seed(42)

# Генерация выборки из 500 значений дискретной случайной величины
sample = np.random.choice(Xj, size=500, p=Pj)

# Эмпирические оценки математического ожидания и дисперсии
empirical_mean = np.mean(sample)
empirical_variance = np.var(sample)

# Теоретические значения математического ожидания и дисперсии
theoretical_mean = np.sum(np.array(Xj) * np.array(Pj))
theoretical_variance = np.sum(np.array([(x - theoretical_mean) ** 2 for x in Xj]) * np.array(Pj))


# Построение гистограмм
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(sample, density=True, alpha=0.5, color='blue', label='Эмпирическое')
plt.title('Эмпирическое вероятностное распределение')
plt.xlabel('Значение')
plt.ylabel('Вероятность')

plt.subplot(1, 2, 2)
plt.bar(Xj, Pj,  alpha=0.5, color='red', label='Теоретическое')
plt.title('Теоретическое вероятностное распределение')
plt.xlabel('Значение')
plt.ylabel('Вероятность')

plt.legend()
plt.tight_layout()
plt.show()

print("Первые 30 значений выборки:", sample[:30])


# Вывод оценок
print("Эмпирическое среднее:", empirical_mean)
print("Эмпирическая дисперсия:", empirical_variance)
print("Теоретическое среднее:", theoretical_mean)
print("Теоретическая дисперсия:", theoretical_variance)
