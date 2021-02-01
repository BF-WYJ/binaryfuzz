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

