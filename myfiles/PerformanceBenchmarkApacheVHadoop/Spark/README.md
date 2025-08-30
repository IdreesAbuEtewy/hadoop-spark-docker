# Spark Execution Documentation

This guide provides step-by-step instructions for executing Spark programs within the Hadoop-Spark Docker cluster.

## Prerequisites

Before running Spark programs, ensure you have:
1. Started the Docker cluster using `docker compose up`
2. Accessed the cluster master node using:
   ```bash
   docker exec -it spark-master bash
   ```

## 1. Setting up Spark/PySpark

Spark and PySpark are pre-installed in the Docker cluster. No additional installation is required.

> [!NOTE]\
> The cluster comes with Apache Spark 3.5.6 pre-configured and ready to use.

## 2. Executing Word Count Program

### a. Run the Python program
Execute the word count program from the terminal:
```bash
spark-submit spark_word_count.py
```

### b. View the Spark Job UI
Monitor your Spark job execution in real-time:
- **Local UI**: `http://localhost:18080/jobs/`


> [!NOTE]\
> The Spark UI is only available while jobs are running. For completed jobs, use the Spark History Server.

### c. View Output Files
Output files are generated and stored in the same directory as the input file.

## 3. Executing Join Program

### a. Run the Python program
Execute the join program from the terminal:
```bash
spark-submit spark_join.py
```

### b. View the Spark Job UI
Monitor the join operation:
- **Local UI**: `http://localhost:18080/jobs/`

## 4. Executing PageRank Program

### a. Run the Python program
Execute the PageRank algorithm:
```bash
spark-submit spark_pagerank.py
```

### b. View the Spark Job UI
Monitor the PageRank computation:
- **Local UI**: `http://localhost:18080/jobs/`

### c. View Output Files
Output files are generated and stored in the same directory as the input file.

## Monitoring and Management

### Spark History Server
View completed Spark jobs and their details:
- **URL**: `http://localhost:18080`
- **Purpose**: Historical job analysis and performance monitoring

### YARN ResourceManager
Monitor cluster resources and running applications:
- **URL**: `http://localhost:8088`
- **Purpose**: Cluster resource management and application tracking

### HDFS Web UI
View distributed file system status:
- **URL**: `http://localhost:9870`
- **Purpose**: File system monitoring and data management

## Tips for Optimal Performance

1. **Resource Allocation**: Monitor resource usage through YARN UI
2. **Data Locality**: Ensure input data is properly distributed in HDFS
3. **Job Optimization**: Use Spark UI to identify bottlenecks
4. **Memory Management**: Adjust Spark configuration based on cluster resources

## Troubleshooting

- If Spark UI is not accessible, ensure the job is currently running
- For completed jobs, check the Spark History Server
- Verify cluster health through YARN ResourceManager UI
- Check HDFS status if encountering file system issues