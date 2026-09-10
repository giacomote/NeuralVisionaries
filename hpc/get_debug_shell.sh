#!/bin/bash

srun -Q -J debug \
    -w <node_name> \
    --immediate=20 \
    --partition=<partition_name> \
    --gres=gpu:1 \
    --time=00:10:00 \
    --account=<account_name> \
    --pty /bin/bash