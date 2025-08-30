# Performance Benchmark ⚡ Hadoop MapReduce vs Apache Spark

A comparative study and performance benchmark of two powerful big data frameworks — **Hadoop MapReduce** and **Apache Spark** — across various data processing tasks.

## Project Overview

This project analyzes and compares:

- **Architecture and characteristics**
- **Ease of use, performance, fault tolerance**
- **Real-world experiments** using:
  - Word Count
  - Join operations
  - PageRank algorithm

Implemented using:

- `Python (Hadoop Streaming)` for MapReduce
- `PySpark` for Spark jobs

## Key Experiments & Results

| Task                    | MapReduce Time | Spark Time   |
| ----------------------- | -------------- | ------------ |
| Word Count (300k words) | 31 sec         | **2.66 sec** |
| Join Ops (100 rows)     | 31 sec         | **5.46 sec** |
| PageRank (300k nodes)   | **47 sec**     | 234 sec      |

- **Spark outperformed MapReduce** in Word Count and Join tasks.
- **MapReduce handled PageRank** more efficiently for very large data.

## Conclusion

- **Spark** is ideal for fast, iterative tasks and large-scale analytics.
- **MapReduce** remains stable for complex, resource-intensive jobs like PageRank.
- The choice depends on **task type**, **data volume**, and **system resources**.

---


## Project Architecture

The benchmark suite is organized into two main components:

```
Performance Benchmark ApacheVHadoop/
├── Spark/
│   ├── README.md                    # Spark execution guide
│   ├── spark_word_count.py         # Spark word count implementation
│   ├── spark_join.py               # Spark join implementation
│   └── spark_pagerank.py           # Spark PageRank implementation
└── Mapreduce/
    ├── README.md                    # MapReduce execution guide
    └── codes/
        ├── word_count/
        │   ├── word_count_map.py
        │   ├── word_count_reduce.py
        │   └── input.txt
        ├── join/
        │   ├── join_map.py
        │   ├── join_reduce.py
        │   ├── General_ledger_dataset.txt
        │   └── Vendors_dataset.txt
        └── pagerank/
            ├── pagerank_map.py
            ├── pagerank_reduce.py
            └── graph.txt
```

## Getting Started

### Prerequisites

1. **Start the Docker Cluster**:
   ```bash
   docker compose up
   ```

2. **Access the Cluster Master Node**:
   ```bash
   docker exec -it spark-master bash
   ```

3. **Navigate to the Benchmark Directory**:
   ```bash
   cd /myfiles/PerformanceBenchmarkApacheVHadoop/
   ```

## Benchmark Programs

This suite implements three classic big data algorithms in both Spark and MapReduce:

### 1. Word Count
- **Purpose**: Text processing and frequency analysis
- **Input**: Text files with various content
- **Output**: Word frequency counts
- **Use Case**: Log analysis, text mining, document processing

### 2. Join Operations
- **Purpose**: Data joining between multiple datasets
- **Input**: Structured datasets (General Ledger & Vendors)
- **Output**: Joined records based on common keys
- **Use Case**: Data warehousing, ETL operations, relational data processing

### 3. PageRank Algorithm
- **Purpose**: Graph-based ranking algorithm
- **Input**: Graph structure with nodes and edges
- **Output**: Ranking scores for each node
- **Use Case**: Web page ranking, social network analysis, recommendation systems

## Execution Guides

### For Spark Programs
Refer to the comprehensive Spark execution guide:
- **Location**: `Spark/README.md`
- **Key Features**: 
  - Pre-configured Spark 3.5.6 environment
  - Real-time job monitoring via Spark UI
  - Integration with YARN resource manager

### For MapReduce Programs
Refer to the detailed MapReduce execution guide:
- **Location**: `Mapreduce/README.md`
- **Key Features**:
  - Hadoop 3.4.1 streaming framework
  - Python-based mapper and reducer implementations
  - HDFS integration for distributed storage

## Cluster Monitoring & Management

### Web Interfaces

| Service | URL | Purpose |
|---------|-----|----------|
| **Spark History Server** | `http://localhost:18080` | View completed Spark jobs |
| **MapReduce Job History** | `http://localhost:19888` | View completed MapReduce jobs |
| **YARN ResourceManager** | `http://localhost:8088` | Cluster resource management |
| **HDFS Web UI** | `http://localhost:9870` | Distributed file system status |
| **Spark Job UI** | `http://localhost:4040` | Real-time Spark job monitoring |
| **JupyterLab** | `http://localhost:8888` | Interactive development environment |

### Performance Comparison

This benchmark suite enables direct performance comparison between:
- **Spark**: In-memory processing, iterative algorithms, interactive analytics
- **MapReduce**: Batch processing, fault tolerance, large-scale data processing

## Best Practices

1. **Resource Monitoring**: Use YARN UI to monitor cluster resources during execution
2. **Data Management**: Leverage HDFS for distributed data storage and access
3. **Job Optimization**: Analyze job performance through respective history servers
4. **Error Handling**: Check logs and monitoring interfaces for troubleshooting

## Quick Start Commands

```bash
# Access cluster
docker exec -it spark-master bash

# Navigate to benchmark directory
cd /myfiles/PerformanceBenchmarkApacheVHadoop/

# Run Spark word count
cd Spark/
spark-submit spark_word_count.py

# Run MapReduce word count
cd ../Mapreduce/codes/word_count/
# Follow detailed instructions in Mapreduce/README.md
```

> [!NOTE]\
> For detailed execution instructions, refer to the respective README files in the Spark and Mapreduce directories.

---

**Happy Benchmarking!** 🚀