import os
import subprocess

filename = "test.py"
bucket_nums = [80, 100]  # Add more values if required

for bucket_num in bucket_nums:
    cmd = f"pytest {filename} -v -vv --bucket={bucket_num}"
    print(f"Running tests with command: {cmd}")
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(f"Test output for bucket {bucket_num}:")
    print(result.stdout)
    print(result.stderr)
    print("=" * 80)