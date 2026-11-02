# -*- coding: utf-8 -*-
"""Personal Agent Retinal Microvascular Caliper AR Ratio Skill.

Zero-dependency Central Retinal Arteriolar/Venular Equivalent (CRAE/CRVE) modeler,
Arteriolar-to-Venular Ratio (AVR) calculator, and cerebral microangiopathy velocity evaluator.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentRetinalMicrovascularCaliperArRatio:
    """Quantitative retinal fundus microvascular caliber and cerebral microcirculation engine
    based on the Parr-Hubbard-Knudtson formula and Atherosclerosis Risk in Communities (ARIC) studies."""

    def calculate_retinal_avr_and_microvascular_risk(
        self,
        crae_microns: float = 152.0,
        crve_microns: float = 210.0,
        age: int = 42,
        systolic_bp: float = 124.0
    ) -> Dict[str, Any]:
        """Calculates Arteriolar-to-Venular Ratio (AVR), arteriolar narrowing severity,
        venular dilation score, and systemic microangiopathy risk index (SMRI)."""
        crae = max(80.0, min(250.0, float(crae_microns)))
        crve = max(100.0, min(350.0, float(crve_microns)))
        a = max(18, int(age))
        sbp = max(80.0, float(systolic_bp))

        # Arteriolar-to-Venular Ratio: AVR = CRAE / CRVE
        avr = round(crae / crve, 3)

        # Microvascular Caliber Classification (ARIC Study & Blue Mountains Eye Study benchmarks)
        if avr >= 0.82:
            caliber_tier = "Optimal Retinal Microvascular Perfusion"
            microvascular_status = "Intact microvascular caliber; zero arteriolar sclerosis"
        elif avr >= 0.73:
            caliber_tier = "Normative Physiological Microvascular Ratio"
            microvascular_status = "Standard age-appropriate retinal arteriolar caliber"
        elif avr >= 0.65:
            caliber_tier = "Moderate Generalized Arteriolar Narrowing"
            microvascular_status = "Sub-clinical hypertensive remodeling; elevated cerebrovascular resistance"
        else:
            caliber_tier = "Severe Retinal Arteriolar Attenuation"
            microvascular_status = "Advanced microangiopathy; elevated hazard ratio for lacunar stroke and nephrosclerosis"

        # Venular Dilation Evaluation (Marker of Systemic Inflammation)
        venular_inflammation_flag = crve >= 225.0
        # Arteriolar Narrowing Evaluation (Marker of Chronic Hemodynamic Strain)
        arteriolar_attenuation_flag = crae <= 142.0

        # Systemic Microangiopathy Risk Index (SMRI: 0 - 100)
        # Based on deficit from optimal AVR (0.85) and hemodynamic load
        avr_deficit = max(0.0, 0.85 - avr)
        bp_load = max(0.0, sbp - 120.0) * 0.5
        smri = min(100.0, round((avr_deficit * 200.0) + bp_load, 1))

        return {
            "central_retinal_arteriolar_equivalent_crae_microns": crae,
            "central_retinal_venular_equivalent_crve_microns": crve,
            "arteriolar_to_venular_ratio_avr": avr,
            "microvascular_caliber_tier": caliber_tier,
            "microvascular_pathology_assessment": microvascular_status,
            "generalized_arteriolar_narrowing_present": arteriolar_attenuation_flag,
            "systemic_venular_inflammatory_dilation": venular_inflammation_flag,
            "systemic_microangiopathy_risk_index_smri": smri,
            "cerebral_microcirculation_surrogate_note": (
                "Retinal arterioles share embryological, anatomical, and physiological characteristics with "
                "cerebral penetrating arterioles, serving as an in vivo window into intracranial microvascular health."
            )
        }

    def evaluate_cerebral_microvascular_velocity(
        self,
        avr_ratio: float,
        pulse_pressure: float = 46.0
    ) -> Dict[str, Any]:
        """Correlates retinal AVR with cerebral microvascular pulsatility strain."""
        ratio = max(0.4, min(1.2, float(avr_ratio)))
        pp = max(20.0, float(pulse_pressure))

        # High pulsatility strain = high PP combined with low AVR
        pulsatility_strain = round((pp / 40.0) * (0.80 / ratio), 2)
        high_pulsatility_risk = pulsatility_strain >= 1.35

        return {
            "evaluated_avr_ratio": ratio,
            "pulse_pressure_mmHg": pp,
            "cerebral_microvascular_pulsatility_strain": pulsatility_strain,
            "high_pulsatility_end_organ_risk": high_pulsatility_risk,
            "clinical_recommendation": (
                "Optimize nocturnal blood pressure dipping and execute regular Zone 2 endurance training "
                "to enhance microvascular capillary density and reduce intracranial pulsatility strain."
                if high_pulsatility_risk else
                "Preserve current microvascular compliance and arterial elasticity."
            )
        }
