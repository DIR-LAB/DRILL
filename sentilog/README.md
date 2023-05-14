## Description of File ##
`filter`: this directory contains the scrubbed logs.

`preprocessor.py`: this file is for preprocessing the raw logs. It is not needed if you use the data we provide in `filter` as they are already preprocessed. However, if you want to preprocess your own logs, remember to change the "input_path" and "output_path" in the code to what you need.

`sentilog.ipynb`: this file is the evaluation part of the paper HotStorage'21 *SentiLog: Anomaly Detecting on Parallel File Systems via Log-based Sentiment Analysis.*

## Dependencies ##
pytorch: `pip3 install torch`
d2l: `pip3 install d2l`
jupyter notebook: `pip install notebook`

## How to Run ##

`jupyter notebook sentilog.ipynb`
