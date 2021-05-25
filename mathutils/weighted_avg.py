from decimal import *

class WeightedAvg:
    
    def __init__(self, size_):
        self.size = size_
        self.weightedValues = []
        self.weights = []
        self.factorTotalWeightedValues = Decimal(0)
        self.factorTotalWeights = Decimal(0)

    def add(self, value, weight):
        removedWeightedValue = Decimal(0)
        removedWeight = Decimal(0)

        #limit array size
        if len(self.weightedValues) == self.size:
            removedWeightedValue = self.weightedValues[0]
            self.weightedValues = self.weightedValues[1:]

            removedWeight = self.weights[0]
            self.weights = self.weights[1:]

        #append values
        mr = Decimal(value) * Decimal(weight)
        self.weightedValues.append(mr)
        self.weights.append(weight)

        #pre calculated factors are used for optimization purposes
        #remove outgoing elements and add the newest elements to the total
        self.factorTotalWeightedValues = self.factorTotalWeightedValues - removedWeightedValue + mr
        self.factorTotalWeights = self.factorTotalWeights - removedWeight + weight

    def avg(self):
        return self.factorTotalWeightedValues / self.factorTotalWeights


