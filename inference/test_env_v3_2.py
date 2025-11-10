"""验证 DeepSeek-V3.2 环境"""
import sys

print("=" * 60)
print("Environment Check for DeepSeek-V3.2")
print("=" * 60)

# 1. Python 版本
print(f"Python: {sys.version}")

# 2. PyTorch
try:
    import torch
    print(f"✓ PyTorch: {torch.__version__}")
    print(f"  - CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"  - CUDA version: {torch.version.cuda}")
        print(f"  - GPU count: {torch.cuda.device_count()}")
        print(f"  - GPU name: {torch.cuda.get_device_name(0)}")
except Exception as e:
    print(f"✗ PyTorch: {e}")

# 3. Transformers
try:
    import transformers
    print(f"✓ Transformers: {transformers.__version__}")
except Exception as e:
    print(f"✗ Transformers: {e}")

# 4. SafeTensors
try:
    import safetensors
    print(f"✓ SafeTensors: {safetensors.__version__}")
except Exception as e:
    print(f"✗ SafeTensors: {e}")

# 5. Fast Hadamard Transform
try:
    import fast_hadamard_transform
    print(f"✓ Fast Hadamard Transform: installed")
except Exception as e:
    print(f"✗ Fast Hadamard Transform: {e}")

# 6. TileLang
try:
    import tilelang
    print(f"✓ TileLang: {tilelang.__version__}")
except Exception as e:
    print(f"✗ TileLang: {e}")

print("=" * 60)