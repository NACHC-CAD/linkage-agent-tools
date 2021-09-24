import time
import os
import shutil
from match import match

output = []
for file in os.listdir("benchmark/sized"):
    try:
        os.remove("benchmark/inbox/x.zip")
        os.remove("benchmark/inbox/y.zip")
    except OSError:
        pass
    size = int(file[:-4])
    print(f"Testing {size} patients...")
    shutil.copy("benchmark/sized/" + file, "benchmark/inbox/x.zip")
    shutil.copy("benchmark/sized/" + file, "benchmark/inbox/y.zip")
    start = time.time()
    match()
    end = time.time()
    output.append((size, end - start))
    print(f"{size} patients took {end - start} seconds")
