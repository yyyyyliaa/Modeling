import numpy as np
import matplotlib.pyplot as plt

# Функция для генерации экспоненциального распределения
def exponential_distribution(lmbda, size):
    return np.random.exponential(scale=1/lmbda, size=size)

# Функция для генерации равномерного распределения
def uniform_distribution(a, b, size):
    return np.random.uniform(low=a, high=b, size=size)

# Функция для генерации распределения Эрланга порядка k
def erlang_distribution(k, lmbda, size):
    return np.random.gamma(shape=k, scale=1/lmbda, size=size)

# Функция для генерации нормального распределения
def normal_distribution(mu, sigma, size):
    return np.random.normal(loc=mu, scale=sigma, size=size)

# Функция для генерации распределения Пуассона
def poisson_distribution(mu, size):
    return np.random.poisson(lam=mu, size=size)

# Функция для вычисления среднего значения и дисперсии
def calculate_mean_and_variance(data):
    mean = np.mean(data)
    variance = np.var(data)
    return mean, variance

# Параметры для каждого распределения
lmbda_exp = 0.5
a_uniform = 0
b_uniform = 1
k_erlang = 1
mu_normal = 0
sigma_normal = 1
mu_poisson = 5

# Размер выборки
sample_size = 1000

# Генерация данных для каждого распределения
data_exp = exponential_distribution(lmbda_exp, sample_size)
data_uniform = uniform_distribution(a_uniform, b_uniform, sample_size)
data_erlang = erlang_distribution(k_erlang, lmbda_exp/k_erlang, sample_size)
data_normal = normal_distribution(mu_normal, sigma_normal, sample_size)
data_poisson = poisson_distribution(mu_poisson, sample_size)

# Построение гистограмм для каждого распределения
plt.figure(figsize=(8, 6))

plt.hist(data_exp, bins=30, density=True, color='skyblue', alpha=0.7)
plt.title('Экспоненциальное Распределение')
plt.xlabel('Значение')
plt.ylabel('Плотность')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(data_uniform, bins=30, density=True, color='salmon', alpha=0.7)
plt.title('Равномерное Распределение')
plt.xlabel('Значение')
plt.ylabel('Плотность')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(data_erlang, bins=30, density=True, color='green', alpha=0.7)
plt.title('Распределение Эрланга')
plt.xlabel('Значение')
plt.ylabel('Плотность')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(data_normal, bins=30, density=True, color='orange', alpha=0.7)
plt.title('Нормальное Распределение')
plt.xlabel('Значение')
plt.ylabel('Плотность')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(data_poisson, bins=30, density=True, color='purple', alpha=0.7)
plt.title('Распределение Пуассона')
plt.xlabel('Значение')
plt.ylabel('Плотность')
plt.show()

# Вычисление среднего значения и дисперсии для каждого распределения
mean_exp, var_exp = calculate_mean_and_variance(data_exp)
mean_uniform, var_uniform = calculate_mean_and_variance(data_uniform)
mean_erlang, var_erlang = calculate_mean_and_variance(data_erlang)
mean_normal, var_normal = calculate_mean_and_variance(data_normal)
mean_poisson, var_poisson = calculate_mean_and_variance(data_poisson)


# Вывод результатов
print("Экспоненциальное Распределение:")
print("Теоретическое Мат. Ожидание:", 1 / lmbda_exp)
print("Теоретическая Дисперсия:", 1 / (lmbda_exp ** 2))
print("Эмпирическое Мат. Ожидание:", mean_exp)
print("Эмпирическая Дисперсия:", var_exp)
print()
print("Равномерное Распределение:")
print("Теоретическое Мат. Ожидание:", (a_uniform + b_uniform) / 2)
print("Теоретическая Дисперсия:", ((b_uniform - a_uniform) ** 2) / 12)
print("Эмпирическое Мат. Ожидание:", mean_uniform)
print("Эмпирическая Дисперсия:", var_uniform)
print()
print("Распределение Эрланга:")
print("Теоретическое Мат. Ожидание:", k_erlang / lmbda_exp)
print("Теоретическая Дисперсия:", k_erlang / (lmbda_exp ** 2))
print("Эмпирическое Мат. Ожидание:", mean_erlang)
print("Эмпирическая Дисперсия:", var_erlang)
print()
print("Нормальное Распределение:")
print("Теоретическое Мат. Ожидание:", mu_normal)
print("Теоретическая Дисперсия:", sigma_normal ** 2)
print("Эмпирическое Мат. Ожидание:", mean_normal)
print("Эмпирическая Дисперсия:", var_normal)
print()
print("Распределение Пуассона:")
print("Теоретическое Мат. Ожидание:", mu_poisson)
print("Теоретическая Дисперсия:", mu_poisson)
print("Эмпирическое Мат. Ожидание:", mean_poisson)
print("Эмпирическая Дисперсия:", var_poisson)
