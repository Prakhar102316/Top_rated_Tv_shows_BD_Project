# Top Rated TV Show Analysis using Hadoop MapReduce

## Project Overview
This project analyzes a Top Rated TV Shows dataset using Hadoop MapReduce.  
The objective is to classify TV shows into rating categories based on their vote average and count the number of shows in each category using distributed processing.

This project uses:
- HDFS for distributed storage
- Hadoop Streaming for MapReduce execution
- Python for Mapper and Reducer implementation

---

## Problem Statement
Large volumes of TV show rating data are generated through digital entertainment platforms. Traditional processing methods may be inefficient for large datasets.

This project uses Hadoop MapReduce to analyze a TV show dataset and classify shows into:

- HighRated (vote_average ≥ 8.5)
- MediumRated (vote_average < 8.5)

The number of shows in each category is then calculated.

---

## Objectives
- Store dataset in HDFS
- Process data using Hadoop MapReduce
- Classify TV shows based on ratings
- Count number of shows in each category

---

## Dataset
Dataset File:

top_rated_tv.csv

Attributes include:
- First Air Date
- TV Show Name
- Overview
- Popularity
- Vote Average
- Vote Count
- Adult Flag

The Vote Average field is used for analysis.

---

## Project Files
Repository contains:

- Project-Report.pdf
- mapper.py
- reducer.py
- top_rated_tv.csv
- README.md

---

## Mapper Logic
The mapper reads each record and emits:

(HighRated,1)

or

(MediumRated,1)

Example:

HighRated 1  
MediumRated 1

---

## Reducer Logic
Reducer aggregates total counts for each category.

Example output:

HighRated Total_Count  
MediumRated Total_Count

---

## HDFS Commands

Create HDFS directory:

```bash
hdfs dfs -mkdir /tvproject
```

Upload dataset:

```bash id="qbjlwm"
hdfs dfs -put top_rated_tv.csv /tvproject/
```

Check dataset:

```bash id="jlwm14"
hdfs dfs -ls /tvproject
```

---

## MapReduce Execution

Run Hadoop Streaming:

```bash id="xjlwm15"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-mapper "python mapper.py" \
-reducer "python reducer.py" \
-input /tvproject/top_rated_tv.csv \
-output /output_tv
```

View output:

```bash id="6jlwm16"
hdfs dfs -cat /output_tv/part-00000
```

---

## Sample Output
Example:

HighRated 45  
MediumRated 2363

(Replace with actual output from your execution)

---

## System Workflow

Dataset  
↓  
HDFS Storage  
↓  
Mapper  
↓  
Shuffle and Sort  
↓  
Reducer  
↓  
Final Output

---

## Technologies Used
- Hadoop
- HDFS
- MapReduce
- Python
- Cloudera Quickstart VM

---

## Conclusion
This project demonstrates the use of Hadoop MapReduce for analyzing TV show rating data.  
The dataset was processed in a distributed environment and TV shows were classified successfully into rating categories.

---

## Future Scope
This project can be extended using:
- Apache Hive
- Recommendation Systems
- Machine Learning Models
- Visualization Dashboards
