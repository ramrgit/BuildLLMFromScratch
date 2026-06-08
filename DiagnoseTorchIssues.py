import os
os.add_dll_directory(r'C:\github\BuildLLMFromScratch\.bldllmfs\Lib\site-packages\torch\lib')
import torch
print(torch.__version__)