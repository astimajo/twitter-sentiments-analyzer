import csv
from collections import Counter
from collections import defaultdict

def compute(filename):
    # Initialize variables for counter.
    Positive = 0
    Negative = 0
    Neutral = 0

    # Iterations to retrieve sentiments in row 7 note: 0-indexing
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_words = row[6].split(' ')
            for i in csv_words:
                if "Positive_Tweet" in csv_words:
                    #Positive.append(i)
                    Positive += 1
                elif "Negative_Tweet" in csv_words:
                    #Negative.append(i)
                    Negative += 1
                elif "Neutral_Tweet" in csv_words:
                    #Neutral.append(i)
                    Neutral += 1

    # Initializing the Variables for percentage computations.
    Total = Positive + Negative + Neutral

    pos = (Positive / Total) * 100
    neg = (Negative / Total) * 100
    neut = (Neutral / Total) * 100

    return [pos, neg, neut]














