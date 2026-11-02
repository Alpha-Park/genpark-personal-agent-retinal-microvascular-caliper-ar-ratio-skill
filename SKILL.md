---
name: genpark-personal-agent-retinal-microvascular-caliper-ar-ratio-skill
version: "1.0.0"
description: "Zero-dependency Central Retinal Arteriolar/Venular Equivalent (CRAE/CRVE) modeler, Arteriolar-to-Venular Ratio (AVR) calculator, and cerebral microangiopathy velocity evaluator."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Retinal Microvascular Caliper AR Ratio Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI health assistants to evaluate retinal microvascular caliber morphology, compute Central Retinal Arteriolar Equivalent (CRAE) and Central Retinal Venular Equivalent (CRVE), determine the Arteriolar-to-Venular Ratio ($AVR = CRAE / CRVE$) via the Parr-Hubbard-Knudtson formula, and evaluate cerebral penetrating microvessel pulsatility strain.

## Agent In-Context Capabilities

- **In Vivo Microvascular Window**: Evaluates retinal fundus calibers as a direct anatomical surrogate for cerebral and renal microcirculation.
- **Parr-Hubbard AVR Formulation**: Differentiates between arteriolar narrowing (chronic hypertensive remodeling) and venular widening (systemic endothelial inflammation).
- **Cerebral Pulsatility Strain**: Correlates arterial Pulse Pressure with narrowed microvascular beds to predict intracranial end-organ stress.

## Tools Summary

1. `calculate_retinal_avr_and_microvascular_risk`: Returns CRAE, CRVE, AVR, and the Systemic Microangiopathy Risk Index (SMRI).
2. `evaluate_cerebral_microvascular_velocity`: Projects cerebral penetrating arteriole pulsatility strain and end-organ risk.
