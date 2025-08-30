# spark_pagerank.py
from pyspark import SparkConf, SparkContext
import time

# Step 1: Set up SparkConf and SparkContext
conf = SparkConf().setAppName("PageRank")
sc = SparkContext(conf=conf)


import ast

file_path = "pagerank_dataset/graph1.5.txt" 

with open(file_path, "r") as file:
    content = file.read()
    link_data = ast.literal_eval(content)

ranks = sc.parallelize(link_data.keys()).map(lambda x : (x, 1.))
links = sc.parallelize(link_data.items()).cache()

sorted(links.join(ranks).collect())
def computeContribs(node_urls_rank):
    """
    This function takes elements from the joined dataset above and
    computes the contribution to each outgoing link based on the
    current rank.
    """
    _, (urls, rank) = node_urls_rank
    nb_urls = len(urls)
    for url in urls:
        yield url, rank / nb_urls

c = links.join(ranks).flatMap(computeContribs)
print(c.toDebugString().decode("utf8"))

from operator import add

for iteration in range(10):
    # compute contributions of each node where it links to
    contribs = links.join(ranks).flatMap(computeContribs)

    # use a full outer join to make sure, that not well connected nodes aren't dropped
    contribs = links.fullOuterJoin(contribs).mapValues(lambda x : x[1] or 0.0)

    # Sum up all contributions per link
    ranks = contribs.reduceByKey(add)

    # Re-calculate ranks
    ranks = ranks.mapValues(lambda rank: rank * 0.85 + 0.15)
    
# Collects all ranks
for (link, rank) in sorted(ranks.collect()):
    print("%s has rank: %s." % (link, rank / len(link_data)))

# Step 5: Save the final PageRank values to an output file
ranks.saveAsTextFile("pagerank_output_100")

# Step 6: Stop the SparkContext
time.sleep(60)
sc.stop()
