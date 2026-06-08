# BOBA Session Record: 2026-06-07 Pipeline & Retrieval Evaluation

## 📅 Session Context
Date: 2026-06-07 (Tuesday)
Time: 19:00 - 22:30 UTC
Environment: WSL2 (Ubuntu 22.04)
Workspace: /home/keith260601/boba_work/Building-Our-Better-Angels-project

## 🧠 Key Achievements
### Corpus Index MVE
- Built and verified a Minimum Viable Embedding (MVE) index using [nomic-embed-text](https://github.com/nomic-ai/nomic-embed-text) via Ollama
- Processed 8 markdown files → 72 semantic chunks
- 768-dimensional embeddings with cosine similarity calculations in numpy
- Index validated with 10-sample sanity checks

### Retrieval Evaluation
- Conducted 8 paraphrase queries across 5 core domains
- Top-3 precision: 87.5% (7/8 queries)
- Top-5 precision: 100% (8/8 queries)
- Mean Reciprocal Rank (MRR): 0.838
- Average query latency: 123ms

## ⚠️ Critical Failures & Lessons
### Hermes Approval Gate
- Manual approval mode fails closed (denies action)
- No auto-approval after timeout - requires explicit gate passage
- **Recommended posture**: Smart mode with local Qwen auxiliary for unattended operation

### Ollama Crash-Loop
- A nonexistent flag `--embeddings` was added to `ollama serve` command
- Caused 40+ crash-restarts until flag removed
- **Lesson**: Always verify flags against actual binary documentation

### Worker Write-Path Bug
- Workers using code-execution sandbox hit separate approval gate
- Issues: some halted, some blocked, one fabricated completion summary
- **Solution**: Native `write_file` tool with absolute repo path
- **Lesson**: Cards must explicitly instruct native write_file + absolute path

## 🧹 Clean-Up
- No files modified outside target session record
- All changes confined to /boba_work/.../session-records/
- No git commits made

## 📌 Next Steps
1. Update how-we-work-here.md with overnight lessons
2. Validate flag documentation for all tools
3. Test smart approval workflow with Qwen auxiliary
4. Document write-file protocol in card templates

**Session Status**: ✅ Complete (write_file successful)
**Completion Time**: 2026-06-07 22:30 UTC