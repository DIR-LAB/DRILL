# DRILL
Log-based Anomaly Detection for Unseen Logs via Source Code Feature Extraction

## Description of File ##

`Drill.ipynb`: this file is the evaluation part of the paper IPDPS'23 *Log-based Anomaly Detection for Unseen Logs via Source Code Feature Extraction*

`features.pkl`: this file is the sentiment and context features of HDFS log statements. 

`data`: this directory contains the log sessions of HDFS, the corresponding log templates of log indices are described in `Drill.ipynb`.

`figures.ipynb`: this file displays the figures in the paper.

`sentilog`: this directory contains the code of paper HotStorage'21 *SentiLog: Anomaly Detecting on Parallel File Systems via Log-based Sentiment Analysis.*, which shows how we extract the sentiment features in Drill.

## Dependencies ##

pytorch: `pip3 install torch`

d2l: `pip3 install d2l`

sklearn: `pip3 install scikit-learn`

jupyter notebook: `pip3 install notebook`

## How to Run ##

`jupyter notebook Drill.ipynb`

