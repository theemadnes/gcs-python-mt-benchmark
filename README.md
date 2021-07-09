# gcs-python-mt-benchmark
Compare performance between serial transfers, multi-threaded transfers, and multi-process transfers using the Python GCS client

#### Examples

Serial:

```
$ python gcs-xfer-serial.py 
uploading dummyfile1.bin
File dummyfile1.bin uploaded to 1625811635/dummyfile1.bin.
uploading dummyfile2.bin
File dummyfile2.bin uploaded to 1625811635/dummyfile2.bin.
uploading dummyfile3.bin
File dummyfile3.bin uploaded to 1625811635/dummyfile3.bin.
Execution time in seconds: 8.505363941192627
```

Multi-threading:

```
$ python gcs-xfer-mt.py 
uploading dummyfile1.bin
uploading dummyfile2.bin
uploading dummyfile3.bin
File dummyfile2.bin uploaded to 1625811720/dummyfile2.bin.
File dummyfile1.bin uploaded to 1625811720/dummyfile1.bin.
File dummyfile3.bin uploaded to 1625811720/dummyfile3.bin.
Execution time in seconds: 4.809969186782837
```

Multi-processing:

```
$ python gcs-xfer-mp.py 
uploading dummyfile1.bin
uploading dummyfile2.bin
uploading dummyfile3.bin
File dummyfile1.bin uploaded to 1625811756/dummyfile1.bin.
File dummyfile2.bin uploaded to 1625811756/dummyfile2.bin.
File dummyfile3.bin uploaded to 1625811756/dummyfile3.bin.
Execution time in seconds: 4.610538005828857
```