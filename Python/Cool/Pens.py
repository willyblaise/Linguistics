#!/bin /env python3
from dataclasses import dataclass


@dataclass
class Pens:
    id: int = 0
    pharmacy: str = "no place added"
    price: float = "0.0"
