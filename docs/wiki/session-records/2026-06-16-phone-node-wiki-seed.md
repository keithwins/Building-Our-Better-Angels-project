# BOBA Phone Node Wiki Seed

Status: phone-local staging note

## Purpose

This note captures the BOBA phone-node wiki direction until the full repo wiki can be created.

## Core Primitive

Bounded consequential agency: the right of a system to do real work with real effects inside tested limits, with logs, reversibility, escalation, and domain-specific earned trust.

## Governance Primitive

Trust Envelope Ledger: a durable record of what authority each system component has, who or what granted it, what evidence supports the grant, what limits apply, and how the authority can be revoked.

## Oversight Primitive

No agent is the sole witness to its own authority.

Orthogonal oversight agents test not whether an acting agent is capable, but whether its consequences remain inside the authority it has earned.

## Pixel Phone Node Current State

Confirmed:

- Termux + Debian PRoot works.
- Liquid model bundle exists on phone.
- llama.cpp llama-server compiled successfully.
- Working binary exists at ~/bin/llama-server.
- Liquid LFM2.5-Audio model loads.
- mmproj loads.
- HTTP inference works on 127.0.0.1:8080.
- Basic semantic probes work.
- Audio/vocoder path not yet proven.

## Intended Architecture

Phone sensory stream
  -> ASR / audio understanding
  -> local triage LLM
  -> action policy / trust gate
  -> local actions, memory cards, repo/corpus sync, Hermes escalation
  -> optional TTS response

## Next Repo Destination

Eventually move this into the BOBA repo as a wiki:

docs/wiki/

Suggested pages:

- docs/wiki/index.md
- docs/wiki/concepts/bounded-consequential-agency.md
- docs/wiki/concepts/trust-envelope-ledger.md
- docs/wiki/concepts/orthogonal-oversight-agents.md
- docs/wiki/systems/pixel-phone-node.md
- docs/wiki/protocols/agency-promotion-protocol.md
- docs/wiki/session-records/2026-06-16-pixel-liquid-phone-node.md

## Next Technical Question

Find the correct way to invoke the full Liquid audio stack, especially the vocoder file, and determine whether generic llama-server is sufficient or whether a Liquid-specific runner is required.
