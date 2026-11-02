# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Retinal Microvascular Caliper AR Ratio Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentRetinalMicrovascularCaliperArRatio

mcp = FastMCP("PersonalAgentRetinalMicrovascularCaliperArRatio")
client = PersonalAgentRetinalMicrovascularCaliperArRatio()

@mcp.tool()
def calculate_retinal_avr_and_microvascular_risk(
    crae_microns: float = 152.0,
    crve_microns: float = 210.0,
    age: int = 42,
    systolic_bp: float = 124.0
) -> str:
    """Calculates retinal Arteriolar-to-Venular Ratio (AVR), CRAE, CRVE, and systemic microangiopathy index."""
    import json
    return json.dumps(client.calculate_retinal_avr_and_microvascular_risk(
        crae_microns, crve_microns, age, systolic_bp
    ), indent=2)

@mcp.tool()
def evaluate_cerebral_microvascular_velocity(
    avr_ratio: float = 0.72,
    pulse_pressure: float = 46.0
) -> str:
    """Correlates retinal AVR with cerebral microvascular pulsatility strain and end-organ risk."""
    import json
    return json.dumps(client.evaluate_cerebral_microvascular_velocity(
        avr_ratio, pulse_pressure
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
