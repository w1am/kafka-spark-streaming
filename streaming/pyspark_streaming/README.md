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