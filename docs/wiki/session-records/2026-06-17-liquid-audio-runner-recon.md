# Liquid Audio Runner Recon

Created: 2026-06-17T12:23:03

## Local binary

```text
version: 9672 (74ade5274)
built with GNU 14.2.0 for Linux aarch64
```

## Local server help: audio-related flags

```text
mmproj is also downloaded automatically if available. to disable, add
                                        --no-mmproj
-hfv,  -hfrv, --hf-repo-v <user>/<model>[:quant]
                                        Hugging Face model repository for the vocoder model (default: unused)
-hffv, --hf-file-v FILE                 Hugging Face model file for the vocoder model (default: unused)
-np,   --parallel N                     number of server slots (default: -1, -1 = auto)
-mm,   --mmproj FILE                    path to a multimodal projector file. see tools/mtmd/README.md
                                        (env: LLAMA_ARG_MMPROJ)
-mmu,  --mmproj-url URL                 URL to a multimodal projector file. see tools/mtmd/README.md
                                        (env: LLAMA_ARG_MMPROJ_URL)
--mmproj-auto, --no-mmproj, --no-mmproj-auto
                                        (env: LLAMA_ARG_MMPROJ_AUTO)
--mmproj-offload, --no-mmproj-offload   whether to enable GPU offloading for multimodal projector (default:
                                        (env: LLAMA_ARG_MMPROJ_OFFLOAD)
--mtmd-batch-max-tokens N               maximum number of image tokens per batch when encoding images
                                        (env: LLAMA_ARG_MTMD_BATCH_MAX_TOKENS)
                                        int16, 1=taxicab, 2=euclidean, >2=p-norm)
--api-prefix PREFIX                     prefix path the server serves from, without the trailing slash
--rerank, --reranking                   enable reranking endpoint on server (default: disabled)
-to,   --timeout N                      server read/write timeout in seconds (default: 3600)
--sse-ping-interval N                   server SSE ping interval in seconds (-1 = disabled, default: 30)
--models-dir PATH                       directory containing models for the router server (default: disabled)
--models-preset PATH                    path to INI file containing model presets for the router server
--models-max N                          for router server, maximum number of models to load simultaneously
                                        for router server, whether to automatically load models (default:
--sleep-idle-seconds SECONDS            number of seconds of idleness after which the server will sleep
-mv,   --model-vocoder FNAME            vocoder model for audio generation (default: unused)
--tts-use-guide-tokens                  Use guide tokens to improve TTS word recall
```

## Local llama.cpp liquid/audio files

```text
/root/llama.cpp/tools/mtmd/mtmd-audio.cpp
/root/llama.cpp/tools/mtmd/mtmd-audio.h
/root/llama.cpp/tools/ui/src/lib/components/app/chat/ChatAttachments/ChatAttachmentsPreview/ChatAttachmentsPreviewCurrentItem/ChatAttachmentsPreviewCurrentItemAudio.svelte
/root/llama.cpp/tools/ui/src/lib/utils/audio-recording.ts
/root/llama.cpp/vendor/miniaudio
/root/llama.cpp/vendor/miniaudio/miniaudio.h
/root/llama.cpp/build/tools/mtmd/CMakeFiles/mtmd.dir/mtmd-audio.cpp.o
/root/llama.cpp/build/tools/mtmd/CMakeFiles/mtmd.dir/mtmd-audio.cpp.o.d
```

## Hugging Face file scan: LiquidAI/LFM2.5-Audio-1.5B-GGUF

```text
runners
LFM2.5-Audio-1.5B-F16.gguf
LFM2.5-Audio-1.5B-Q4_0.gguf
LFM2.5-Audio-1.5B-Q8_0.gguf
liquid_audio_chat.py
mmproj-LFM2.5-Audio-1.5B-F16.gguf
mmproj-LFM2.5-Audio-1.5B-Q4_0.gguf
mmproj-LFM2.5-Audio-1.5B-Q8_0.gguf
runners/llama-liquid-audio-android-arm64.zip
runners/llama-liquid-audio-macos-arm64.zip
runners/llama-liquid-audio-ubuntu-arm64.zip
runners/llama-liquid-audio-ubuntu-x64.zip
tokenizer-LFM2.5-Audio-1.5B-F16.gguf
tokenizer-LFM2.5-Audio-1.5B-Q4_0.gguf
tokenizer-LFM2.5-Audio-1.5B-Q8_0.gguf
vocoder-LFM2.5-Audio-1.5B-F16.gguf
vocoder-LFM2.5-Audio-1.5B-Q4_0.gguf
vocoder-LFM2.5-Audio-1.5B-Q8_0.gguf
```

## Hugging Face file scan: LiquidAI/LFM2-Audio-1.5B-GGUF

```text
runners
runners/android-arm64
runners/macos-arm64
runners/ubuntu-arm64
runners/ubuntu-x64
LFM2-Audio-1.5B-F16.gguf
LFM2-Audio-1.5B-Q8_0.gguf
audiodecoder-LFM2-Audio-1.5B-F16.gguf
audiodecoder-LFM2-Audio-1.5B-Q8_0.gguf
mmproj-audioencoder-LFM2-Audio-1.5B-F16.gguf
mmproj-audioencoder-LFM2-Audio-1.5B-Q8_0.gguf
runners/android-arm64/lfm2-audio-android-arm64.zip
runners/macos-arm64/lfm2-audio-macos-arm64.zip
runners/ubuntu-arm64/lfm2-audio-ubuntu-arm64.zip
runners/ubuntu-x64/lfm2-audio-ubuntu-x64.zip
```
