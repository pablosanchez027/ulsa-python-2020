import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

rawData = pd.read_csv('StudentsPerformance.csv')

#print(rawData)

dataInfo = rawData.info()

#print(dataInfo)

dataNeeded = pd.read_csv('StudentsPerformance.csv', usecols=['gender', 'math score'])

femaleFilter = dataNeeded['gender'].isin(['female'])
maleFilter = dataNeeded['gender'].isin(['male'])

#print(dataNeeded)

femaleData = dataNeeded[femaleFilter]
maleData = dataNeeded[maleFilter]

femaleMathScore = femaleData['math score']
maleMathScore = maleData['math score']

femaleMathScoreAverage = np.average(femaleMathScore)
maleMathScoreAverage = np.average(maleMathScore)

#print(maleData)
#print(femaleData)

#print(femaleMathScoreAverage)
#print(maleMathScoreAverage)

plt.title('Promedio de pruebas de matemáticas por genero')

plt.bar([1], [maleMathScoreAverage], color = 'blue')
plt.bar([2], [femaleMathScoreAverage], color = 'pink')

plt.legend(['Hombres', 'Mujeres'])

plt.xlabel('Gender')
plt.ylabel('Score')

plt.show()