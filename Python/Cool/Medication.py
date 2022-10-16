#!/bin/env python3
from dataclasses import dataclass


@dataclass
class Medication:
    patient_id: int = 0
    units: int = 0
    meal: str = "nothing to eat"



