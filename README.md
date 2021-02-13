# SSHuzz

## Setup
> All the experiments are conducted on Linux version 4.15.0-76-generic Ubuntu18.04 with RTX 2080ti, and the target programs are compiled using `afl-gcc`

```shell
# Compile SSHuzz
gcc -O3 -funroll-loops ./sshuzz.c -o sshuzz

# Static analysis of executable files to build control flow
python3 ./control_flow/flow.py program_path
```



## Perform Fuzzing

1. Execute the program smoothing part `nn.py` of SSHuzz

   ```shell
   # Neural network module
   CUDA_VISIBLE_DEVICES=cuda_device_num python2.7 nn.py program_path [params]
   ```

2. Start the fuzzing part `sshuzz`, defalut seed output directory is `./seeds`

   ```shell
   # Fuzzing module
   ./sshuzz -i in_dir -o out_dir -l max_file_size program_path [params] @@
   ```



## AccRatio Experimental Results

> To mearsure the effect of **accRatio** in Algorithm 2 (Candidate Edge Set Construction) on the edge coverage, experiments with different accRatio (0.1, 0.2, 0.4, 0.8, 1) are conducted, where six benchmarks are selected. Here are the corresponding experimental results. (results with accRatio=0.4 are shown in paper)

### Evaluation Results with accRatio=0.1

| Benchmark | Edge coverage | Rate gradient | Rate havoc |
| --------- | ------------- | ------------- | ---------- |
| readelf   | 38269         | 0.331         | 0.783      |
| obdjump   | 30391         | 0.167         | 11.558     |
| base64    | 1602          | 0.027         | 21.875     |
| md5sum    | 3138          | 0.045         | 36.083     |
| mp3gain   | 13065         | 0.049         | 0.280      |
| libpng    | 9948          | 0.022         | 2.368      |

### Evaluation Results with accRatio=0.2

| Benchmark | Edge coverage | Rate gradient | Rate havoc |
| --------- | ------------- | ------------- | ---------- |
| readelf   | 36030         | 0.328         | 1.117      |
| obdjump   | 32007         | 0.185         | 12.995     |
| base64    | 1632          | 0.027         | 29.0       |
| md5sum    | 3171          | 0.045         | 36.75      |
| mp3gain   | 13297         | 0.051         | 0.250      |
| libpng    | 7377          | 0.024         | 0.479      |

### Evaluation Results with accRatio=0.8

| Benchmark | Edge coverage | Rate gradient | Rate havoc |
| --------- | ------------- | ------------- | ---------- |
| readelf   | 39750         | 0.322         | 5.219      |
| obdjump   | 31041         | 0.176         | 14.060     |
| base64    | 1384          | 0.006         | 31.889     |
| md5sum    | 3077          | 0.044         | 49.556     |
| mp3gain   | 13603         | 0.050         | 8.996      |
| libpng    | 9614          | 0.020         | 3.698      |

### Evaluation Results with accRatio=1

| Benchmark | Edge coverage | Rate gradient | Rate havoc |
| --------- | ------------- | ------------- | ---------- |
| readelf   | 38269         | 0.341         | 7.042      |
| obdjump   | 30391         | 0.188         | 12.380     |
| base64    | 1602          | 0.006         | 31.0       |
| md5sum    | 3138          | 0.054         | 42.224     |
| mp3gain   | 13065         | 0.052         | 8.857      |
| libpng    | 9948          | 0.024         | 0.993      |

