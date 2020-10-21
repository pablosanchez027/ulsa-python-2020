import matplotlib.pyplot as plt

years = [1950, 1970, 1990, 2010] #X

population = [2.519, 3.692, 5.263, 6.972] #Y
deaths = [0.519, 1.692, 10.263, 2.972] #Y

plt.title('Población anual')

plt.xlabel('año')
plt.ylabel('Población')

#plt.legend(['crecimiento poblacional'])

plt.plot(years, population, 'r')
plt.plot(years, deaths, 'g')
plt.scatter(years, population, color = 'r')
plt.scatter(years, deaths, color = 'g')
plt.legend(['crecimiento', 'muertes'])

plt.show()