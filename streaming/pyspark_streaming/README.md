# Streaming

## Required versions
```
PATH="$PATH:/Users/will/kafka_2.13-3.4.0/bin"

export HADOOP_HOME=/Users/will/server/hadoop-3.3.4

export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-18.jdk/Contents/Home/
export SPARK_HOME=/Users/will/server/spark-3.3.2-bin-hadoop3
export SBT_HOME=/Users/will/server/sbt
export SCALA_HOME=/Users/will/server/scala-2.12.15

export PATH=$JAVA_HOME/bin:$SBT_HOME/bin:$SBT_HOME/lib:$SCALA_HOME/bin:$SCALA_HOME/lib:$PATH
export PATH=$JAVA_HOME/bin:$SPARK_HOME:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
export PYSPARK_PYTHON=python3
```

## Different ways to start a Spark Streaming application
`StreamingContext` and `spark.readStream` are two different APIs in PySpark that are
used for processing streaming data, but they have some key differences.

`StreamingContext` is a high-level API in PySpark that provides a complete
framework for building and managing streaming applications. It allows you to
create and manage streaming applications that can consume data in real-time from
various sources like Kafka, Flume, and HDFS. With `StreamingContext`, you can
create input DStreams, apply transformations to these DStreams, and output the
results to various data sinks.

On the other hand, `spark.readStream` is a lower-level API in PySpark that
provides a way to read streaming data from a source and create a streaming
DataFrame. It is primarily used for creating a streaming DataFrame from a
structured streaming source, such as Kafka, Kinesis, or file-based sources like
directories and files. Once you have created the streaming DataFrame, you can
apply transformations to it using the DataFrame API.

In summary, `StreamingContext` provides a complete framework for building
streaming applications, while spark.readStream is focused on creating a
streaming DataFrame from a structured streaming source. The choice between the
two APIs depends on the specific requirements of your streaming application. If
you need a complete framework for building a streaming application,
`StreamingContext` is the way to go. If you need to process structured streaming
data and want to use DataFrame API for transformations, then spark.readStream is
more suitable.