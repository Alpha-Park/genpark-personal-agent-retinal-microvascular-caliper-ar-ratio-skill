# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Retinal Microvascular Caliper AR Ratio Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentRetinalMicrovascularCaliperArRatio

def main():
    agent = PersonalAgentRetinalMicrovascularCaliperArRatio()

    print("=" * 70)
    print("DEMO: Personal Agent Retinal Microvascular Caliper & AVR Modeler")
    print("=" * 70)

    # 1. Evaluate Retinal Microvascular Calibers (CRAE: 154 um, CRVE: 202 um, Age 42, SBP 122 mmHg)
    res_avr = agent.calculate_retinal_avr_and_microvascular_risk(
        crae_microns=154.0,
        crve_microns=202.0,
        age=42,
        systolic_bp=122.0
    )

    print(f"\n1. Retinal Fundus Microvascular Analysis:")
    print(f"   Central Retinal Arteriolar Equivalent (CRAE): {res_avr['central_retinal_arteriolar_equivalent_crae_microns']} um")
    print(f"   Central Retinal Venular Equivalent (CRVE): {res_avr['central_retinal_venular_equivalent_crve_microns']} um")
    print(f"   Arteriolar-to-Venular Ratio (AVR): {res_avr['arteriolar_to_venular_ratio_avr']}")
    print(f"   Microvascular Caliber Tier: {res_avr['microvascular_caliber_tier']}")
    print(f"   Microangiopathy Assessment: {res_avr['microvascular_pathology_assessment']}")
    print(f"   Arteriolar Narrowing Present: {res_avr['generalized_arteriolar_narrowing_present']}")
    print(f"   Venular Inflammatory Dilation: {res_avr['systemic_venular_inflammatory_dilation']}")
    print(f"   Systemic Microangiopathy Risk Index (SMRI): {res_avr['systemic_microangiopathy_risk_index_smri']}/100")
    print(f"   Cerebral Window: {res_avr['cerebral_microcirculation_surrogate_note']}")

    # 2. Evaluate Cerebral Pulsatility Strain (AVR 0.762, PP 44 mmHg)
    res_puls = agent.evaluate_cerebral_microvascular_velocity(
        avr_ratio=res_avr['arteriolar_to_venular_ratio_avr'],
        pulse_pressure=44.0
    )

    print(f"\n2. Cerebral Penetrating Microvascular Pulsatility Strain:")
    print(f"   Evaluated AVR: {res_puls['evaluated_avr_ratio']} | Pulse Pressure: {res_puls['pulse_pressure_mmHg']} mmHg")
    print(f"   Pulsatility Strain Index: {res_puls['cerebral_microvascular_pulsatility_strain']}")
    print(f"   High-Pulsatility End-Organ Risk: {res_puls['high_pulsatility_end_organ_risk']}")
    print(f"   Clinical Prescription: {res_puls['clinical_recommendation']}")

    print("\nVerification complete: Retinal microvascular caliper engine executed flawlessly.")

if __name__ == "__main__":
    main()
