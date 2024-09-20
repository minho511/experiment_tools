import random
import os
import numpy as np
import torch

def seed_torch(seed=42):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.enabled = False
    
    # 아래의 코드를 써야할 때도 있음
    # os.environ['CUBLAS_WORKSPACE_CONFIG'] = ':4096:8'
    # torch.use_deterministic_algorithms(True, warn_only=True)