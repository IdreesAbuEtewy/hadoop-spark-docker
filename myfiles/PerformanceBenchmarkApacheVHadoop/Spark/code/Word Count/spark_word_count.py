# spark_word_count.py
#Import libraries
from pyspark import SparkContext, SparkConf
import time

#Configuring the setup
conf = SparkConf().setAppName("WordCount").setMaster('local')
sc = SparkContext(conf=conf)

#Read the text file
text_file = sc.textFile("dataset_wordcount/input_300000.txt")

#Main code -> It splits the line into words and it counts the words
word_counts = text_file \
    .flatMap(lambda line: line.split()) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)

#Saves the output in a text file
word_counts.saveAsTextFile("word_count_output_300000")
time.sleep(60)
sc.stop()

