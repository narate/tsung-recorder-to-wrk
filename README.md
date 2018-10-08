# tsung-recorder-to-wrk
Tsung Recorder session to wrk Lua Script converter.

## Example

Convert `tsung-recorder` file to JSON

```
python rec2wrk.py tsung_recorder.xml
```

Run `wrk` loadtest

```
wrk --latency -s load.lua -t 2 -c 100 -d 1m http://192.168.1.101:8000/

Running 1m test @ http://192.168.1.101:8000/
  2 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   460.80ms  526.77ms   2.00s    81.24%
    Req/Sec    76.81     57.11   353.00     73.43%
  Latency Distribution
     50%  166.49ms
     75%  832.36ms
     90%    1.26s
     99%    1.89s
  8751 requests in 1.00m, 147.09MB read
  Socket errors: connect 0, read 41, write 25, timeout 701
  Non-2xx or 3xx responses: 1160
Requests/sec:    145.70
Transfer/sec:      2.45MB

```