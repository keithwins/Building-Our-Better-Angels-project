# Exp 0 — Static-Encoder Baseline (result)
- Date: 2026-06-06
- Encoder: facebook/vjepa2-vitl-fpc64-256 (V-JEPA 2.0 ViT-L, frozen, 326M)
- Stack: torch 2.12.0+cu130, sm_120, WSL2 GPU passthrough, driver CUDA 13.3
- Data: aisuko/ucf101-subset (10 classes; 300 train / 30 val), 64 frames/clip, mean-pooled tokens
- Probe: StandardScaler + LogisticRegression on frozen embeddings
- **Baseline: 96.7% val accuracy**
- Frozen forward peak mem: 0.91 GB / 16.3 GB (fp16 smoke test)
