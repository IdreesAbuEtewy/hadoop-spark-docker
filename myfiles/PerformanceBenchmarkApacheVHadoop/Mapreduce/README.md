# MapReduce Execution Documentation

This guide provides step-by-step instructions for executing MapReduce programs within the Hadoop-Spark Docker cluster.

## Prerequisites

Before running MapReduce programs, ensure you have:
1. Started the Docker cluster using `docker compose up`
2. Accessed the cluster master node using:
   ```bash
   docker exec -it spark-master bash
   ```
3. Navigate to the MapReduce codes directory:
   ```bash
   cd /myfiles/PerformanceBenchmarkApacheVHadoop/Mapreduce/codes/
   ```

## Architecture Overview

The MapReduce programs are organized into three main categories:
- **Word Count**: Text processing and frequency analysis
- **Join**: Data joining operations between datasets
- **PageRank**: Graph algorithm implementation

Each program consists of separate mapper and reducer Python scripts that work together in the Hadoop streaming framework.

## 1. Word Count Program

### Program Structure
- **Mapper**: `word_count/word_count_map.py`
- **Reducer**: `word_count/word_count_reduce.py`
- **Input**: `word_count/input.txt`

### Execution Steps

#### a. Navigate to the word count directory
```bash
cd word_count/
```

#### b. Prepare HDFS input directory
```bash
hdfs dfs -mkdir -p /input/wordcount
hdfs dfs -put input.txt /input/wordcount/
```

#### c. Run the MapReduce job
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files word_count_map.py,word_count_reduce.py \
  -mapper word_count_map.py \
  -reducer word_count_reduce.py \
  -input /input/wordcount/input.txt \
  -output /output/wordcount
```

#### d. View the output
```bash
hdfs dfs -cat /output/wordcount/part-00000
```

#### e. Copy output to local directory (optional)
```bash
hdfs dfs -get /output/wordcount/part-00000 ./wc_output.txt
```

## 2. Join Program

### Program Structure
- **Mapper**: `join/join_map.py`
- **Reducer**: `join/join_reduce.py`
- **Input Files**: 
  - `join/General_ledger_dataset.txt`
  - `join/Vendors_dataset.txt`

### Execution Steps

#### a. Navigate to the join directory
```bash
cd ../join/
```

#### b. Prepare HDFS input directory
```bash
hdfs dfs -mkdir -p /input/join
hdfs dfs -put General_ledger_dataset.txt /input/join/
hdfs dfs -put Vendors_dataset.txt /input/join/
```

#### c. Run the MapReduce job
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files join_map.py,join_reduce.py \
  -mapper join_map.py \
  -reducer join_reduce.py \
  -input /input/join/ \
  -output /output/join
```

#### d. View the output
```bash
hdfs dfs -cat /output/join/part-00000
```

#### e. Copy output to local directory (optional)
```bash
hdfs dfs -get /output/join/part-00000 ./join_output.txt
```

## 3. PageRank Program

### Program Structure
- **Mapper**: `pagerank/pagerank_map.py`
- **Reducer**: `pagerank/pagerank_reduce.py`
- **Input**: `pagerank/graph.txt`

### Execution Steps

#### a. Navigate to the pagerank directory
```bash
cd ../pagerank/
```

#### b. Prepare HDFS input directory
```bash
hdfs dfs -mkdir -p /input/pagerank
hdfs dfs -put graph.txt /input/pagerank/
```

#### c. Run the MapReduce job
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files pagerank_map.py,pagerank_reduce.py \
  -mapper pagerank_map.py \
  -reducer pagerank_reduce.py \
  -input /input/pagerank/graph.txt \
  -output /output/pagerank
```

#### d. View the output
```bash
hdfs dfs -cat /output/pagerank/part-00000
```

#### e. Copy output to local directory (optional)
```bash
hdfs dfs -get /output/pagerank/part-00000 ./pagerank_output.txt
```

## Monitoring and Management

### MapReduce Job History Server
View completed MapReduce jobs and their details:
- **URL**: `http://localhost:19888`
- **Purpose**: Historical job analysis and performance monitoring

### YARN ResourceManager
Monitor cluster resources and running applications:
- **URL**: `http://localhost:8088`
- **Purpose**: Cluster resource management and application tracking

### HDFS Web UI
View distributed file system status:
- **URL**: `http://localhost:9870`
- **Purpose**: File system monitoring and data management

## Useful HDFS Commands

### List HDFS directories
```bash
hdfs dfs -ls /
hdfs dfs -ls /input
hdfs dfs -ls /output
```

### Remove output directories (before re-running jobs)
```bash
hdfs dfs -rm -r /output/wordcount
hdfs dfs -rm -r /output/join
hdfs dfs -rm -r /output/pagerank
```

### Check HDFS disk usage
```bash
hdfs dfs -du -h /
```

## Tips for Optimal Performance

1. **Data Preparation**: Ensure input data is properly formatted and accessible in HDFS
2. **Resource Monitoring**: Use YARN UI to monitor job progress and resource utilization
3. **Output Management**: Clean up output directories between runs to avoid conflicts
4. **Error Handling**: Check job logs through the Job History Server for debugging

## Troubleshooting

- **Permission Issues**: Ensure Python scripts have execute permissions (`chmod +x *.py`)
- **HDFS Errors**: Verify input files exist in HDFS before running jobs
- **Output Conflicts**: Remove existing output directories before re-running jobs
- **Job Failures**: Check YARN logs and Job History Server for detailed error information
- **Python Path**: Ensure Python scripts use the correct shebang (`#!/usr/bin/python3`)

> [!NOTE]\
> All MapReduce jobs use Hadoop Streaming to execute Python scripts. The cluster comes with Hadoop 3.4.1 pre-configured and ready to use.