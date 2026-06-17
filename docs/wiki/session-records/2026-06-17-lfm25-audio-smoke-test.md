# 2026-06-17 LFM2.5 Audio Smoke Test

Status: generated on phone

Purpose: Test whether the older LFM2 Android ARM64 runner can load the LFM2.5 model, mmproj, and vocoder.

Exit code: 134

## Log tail

```text
llama_model_loader: - kv   5:                            general.license str              = other
llama_model_loader: - kv   6:                       general.license.name str              = lfm1.0
llama_model_loader: - kv   7:                       general.license.link str              = LICENSE
llama_model_loader: - kv   8:                   general.base_model.count u32              = 1
llama_model_loader: - kv   9:                  general.base_model.0.name str              = LFM2 1.2B
llama_model_loader: - kv  10:          general.base_model.0.organization str              = LiquidAI
llama_model_loader: - kv  11:              general.base_model.0.repo_url str              = https://huggingface.co/LiquidAI/LFM2-...
llama_model_loader: - kv  12:                               general.tags arr[str,7]       = ["liquid", "lfm2", "audio", "lfm2-aud...
llama_model_loader: - kv  13:                          general.languages arr[str,1]       = ["en"]
llama_model_loader: - kv  14:                           lfm2.block_count u32              = 16
llama_model_loader: - kv  15:                        lfm2.context_length u32              = 128000
llama_model_loader: - kv  16:                      lfm2.embedding_length u32              = 2048
llama_model_loader: - kv  17:                   lfm2.feed_forward_length u32              = 8192
llama_model_loader: - kv  18:                  lfm2.attention.head_count u32              = 32
llama_model_loader: - kv  19:               lfm2.attention.head_count_kv arr[i32,16]      = [0, 0, 8, 0, 0, 8, 0, 0, 8, 0, 8, 0, ...
llama_model_loader: - kv  20:                        lfm2.rope.freq_base f32              = 1000000.000000
llama_model_loader: - kv  21:      lfm2.attention.layer_norm_rms_epsilon f32              = 0.000010
llama_model_loader: - kv  22:                            lfm2.vocab_size u32              = 65536
llama_model_loader: - kv  23:                     lfm2.shortconv.l_cache u32              = 3
llama_model_loader: - kv  24:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  25:                         tokenizer.ggml.pre str              = lfm2
llama_model_loader: - kv  26:                      tokenizer.ggml.tokens arr[str,65536]   = ["<|pad|>", "<|startoftext|>", "<|end...
llama_model_loader: - kv  27:                  tokenizer.ggml.token_type arr[i32,65536]   = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ...
llama_model_loader: - kv  28:                      tokenizer.ggml.merges arr[str,63683]   = ["Ċ Ċ", "Ċ ĊĊ", "ĊĊ Ċ", "Ċ �...
llama_model_loader: - kv  29:                tokenizer.ggml.bos_token_id u32              = 1
llama_model_loader: - kv  30:                tokenizer.ggml.eos_token_id u32              = 7
llama_model_loader: - kv  31:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  32:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  33:               tokenizer.ggml.add_sep_token bool             = false
llama_model_loader: - kv  34:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  35:                    tokenizer.chat_template str              = {{- bos_token -}}{%- set system_promp...
llama_model_loader: - kv  36:               general.quantization_version u32              = 2
llama_model_loader: - kv  37:                          general.file_type u32              = 2
llama_model_loader: - type  f32:   55 tensors
llama_model_loader: - type q4_0:   92 tensors
llama_model_loader: - type q6_K:    1 tensors
print_info: file format = GGUF V3 (latest)
print_info: file type   = Q4_0
print_info: file size   = 661.25 MiB (4.74 BPW) 
load: printing all EOG tokens:
load:   - 2 ('<|endoftext|>')
load:   - 7 ('<|im_end|>')
load: special tokens cache size = 507
load: token to piece cache size = 0.3756 MB
print_info: arch             = lfm2
print_info: vocab_only       = 0
print_info: n_ctx_train      = 128000
print_info: n_embd           = 2048
print_info: n_layer          = 16
print_info: n_head           = 32
print_info: n_head_kv        = [0, 0, 8, 0, 0, 8, 0, 0, 8, 0, 8, 0, 8, 0, 8, 0]
print_info: n_rot            = 64
print_info: n_swa            = 0
print_info: is_swa_any       = 0
print_info: n_embd_head_k    = 64
print_info: n_embd_head_v    = 64
print_info: n_gqa            = [0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0]
print_info: n_embd_k_gqa     = [0, 0, 512, 0, 0, 512, 0, 0, 512, 0, 512, 0, 512, 0, 512, 0]
print_info: n_embd_v_gqa     = [0, 0, 512, 0, 0, 512, 0, 0, 512, 0, 512, 0, 512, 0, 512, 0]
print_info: f_norm_eps       = 0.0e+00
print_info: f_norm_rms_eps   = 1.0e-05
print_info: f_clamp_kqv      = 0.0e+00
print_info: f_max_alibi_bias = 0.0e+00
print_info: f_logit_scale    = 0.0e+00
print_info: f_attn_scale     = 0.0e+00
print_info: n_ff             = 8192
print_info: n_expert         = 0
print_info: n_expert_used    = 0
print_info: causal attn      = 1
print_info: pooling type     = 0
print_info: rope type        = 2
print_info: rope scaling     = linear
print_info: freq_base_train  = 1000000.0
print_info: freq_scale_train = 1
print_info: n_ctx_orig_yarn  = 128000
print_info: rope_finetuned   = unknown
print_info: model type       = 1.2B
print_info: model params     = 1.17 B
print_info: general.name     = LFM2.5 Audio 1.5B
print_info: vocab type       = BPE
print_info: n_vocab          = 65536
print_info: n_merges         = 63683
print_info: BOS token        = 1 '<|startoftext|>'
print_info: EOS token        = 7 '<|im_end|>'
print_info: EOT token        = 2 '<|endoftext|>'
print_info: PAD token        = 0 '<|pad|>'
print_info: LF token         = 708 'Ċ'
print_info: EOG token        = 2 '<|endoftext|>'
print_info: EOG token        = 7 '<|im_end|>'
print_info: max token length = 30
load_tensors: loading model tensors, this can take a while... (mmap = true)
load_tensors:   CPU_REPACK model buffer size =   555.75 MiB
load_tensors:   CPU_Mapped model buffer size =   652.25 MiB
......................................................................
llama_context: constructing llama_context
llama_context: n_seq_max     = 1
llama_context: n_ctx         = 4096
llama_context: n_ctx_per_seq = 4096
llama_context: n_batch       = 2048
llama_context: n_ubatch      = 512
llama_context: causal_attn   = 1
llama_context: flash_attn    = auto
llama_context: kv_unified    = false
llama_context: freq_base     = 1000000.0
llama_context: freq_scale    = 1
llama_context: n_ctx_per_seq (4096) < n_ctx_train (128000) -- the full capacity of the model will not be utilized
llama_context:        CPU  output buffer size =     0.26 MiB
llama_kv_cache:        CPU KV buffer size =    48.00 MiB
llama_kv_cache: size =   48.00 MiB (  4096 cells,   6 layers,  1/1 seqs), K (f16):   24.00 MiB, V (f16):   24.00 MiB
llama_memory_recurrent:        CPU RS buffer size =     0.16 MiB
llama_memory_recurrent: size =    0.16 MiB (     1 cells,  16 layers,  1 seqs), R (f32):    0.16 MiB, S (f32):    0.00 MiB
llama_context: Flash Attention was auto, set to enabled
llama_context:        CPU compute buffer size =   132.00 MiB
llama_context: graph nodes  = 549
llama_context: graph splits = 1
common_init_from_params: added <|endoftext|> logit bias = -inf
common_init_from_params: added <|im_end|> logit bias = -inf
common_init_from_params: setting dry_penalty_last_n to ctx_size = 4096
common_init_from_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
libc++abi: terminating due to uncaught exception of type std::runtime_error: weight tensor not found: decoder.layers.0.conv.weight
```

## Output file

No output WAV produced.

## Interpretation

The old LFM2 Android ARM64 runner is executable inside the Pixel Debian Termux environment, but it does not appear compatible with the LFM2.5 audio stack.

The smoke test began loading the LFM2.5 main model and identified it as LFM2.5 Audio 1.5B.

It then aborted with this key error:

weight tensor not found: decoder.layers.0.conv.weight

Interpretation: the older runner likely expects the older LFM2 audiodecoder tensor layout, while LFM2.5 uses a different vocoder stack.

Conclusion: generic llama-server works for local text inference, and the old LFM2 audio runner executes, but LFM2.5 full audio likely requires the proper Liquid LFM2.5 runner or newer custom llama.cpp support.
