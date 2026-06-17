# 2026-06-17 Liquid LFM2 Android Runner Inspection

Status: phone-generated inspection

Finding: older Liquid LFM2 Android ARM64 runner can execute inside Debian PRoot on Pixel phone.

Relevant help lines:

```text
load_backend: loaded CPU backend from /tmp/liquid_lfm2_runner_recon/lfm2-audio-android-arm64/libggml-cpu-android_armv8.6_1.so
-h,    --help, --usage                  print usage and exit
                                        mmproj is also downloaded automatically if available. to disable, add
                                        --no-mmproj
                                        Hugging Face model repository for the vocoder model (default: unused)
-hffv, --hf-file-v FILE                 Hugging Face model file for the vocoder model (default: unused)
                                        'auto' enables colors when output is to a terminal
--mmproj FILE                           path to a multimodal projector file. see tools/mtmd/README.md
                                        (env: LLAMA_ARG_MMPROJ)
--mmproj-url URL                        URL to a multimodal projector file. see tools/mtmd/README.md
                                        (env: LLAMA_ARG_MMPROJ_URL)
--no-mmproj                             explicitly disable multimodal projector, useful when using -hf
                                        (env: LLAMA_ARG_NO_MMPROJ)
--no-mmproj-offload                     do not offload multimodal projector to GPU
                                        (env: LLAMA_ARG_NO_MMPROJ_OFFLOAD)
--image, --audio FILE                   path to an image or audio file. use with multimodal models, can be
-o,    --output, --output-file FNAME    output file (default: '')
-mv,   --model-vocoder FNAME            vocoder model for audio generation (default: unused)
Experimental CLI for LFM2-Audio-1.5B
Usage: ./llama-lfm2-audio [options] -m <model> --mmproj <mmproj> --image <image> --audio <audio> -p <prompt>
  -m, --mmproj, -mv are required
  --audio, -p, --output are required depending on -sys
```

Interpretation:

- The runner supports --audio input.
- The runner supports --model-vocoder / -mv.
- The runner supports --mmproj.
- It is labeled experimental for LFM2-Audio-1.5B, not necessarily LFM2.5.
- Compatibility with LFM2.5 remains unproven.
