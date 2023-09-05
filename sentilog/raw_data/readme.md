The relevant research paper has been published at HotStorage'21. If you reference or use the dataset or the work in your research, please cite:

@inproceedings{zhang2021sentilog,
  title={SentiLog: Anomaly detecting on parallel file systems via log-based sentiment analysis},
  author={Zhang, Di and Dai, Dong and Han, Runzhou and Zheng, Mai},
  booktitle={Proceedings of the 13th ACM workshop on hot topics in storage and file systems},
  pages={86--93},
  year={2021}
}

`raw_test` contains the raw logs of beegfs, lustre. Notice, the hdfs is also evaluated in the paper Drill. However, the size of hdfs dataset is too large to be contained here, we recommend users to download it from the initial website: http://people.iiis.tsinghua.edu.cn/~weixu/sospdata.html  

`raw_train` contains the raw log statements in the source code of beegfs, lustre, gluster, orangefs, Ceph, daos, hbase, hive.

The suffix of filename indicates the label. For example, `beegfs-debug.txt` is considered positive while `beegfs-error.txt` is negative.