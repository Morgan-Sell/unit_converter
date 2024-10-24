from abc import ABC, abstractmethod

from src.config import LENGTH_CONVERSION_FACTORS, WEIGHT_CONVERSION_FACTORS


class ConversionStrategy(ABC):
    @abstractmethod
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        pass


class LengthConversionStrategy(ConversionStrategy):
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        # if units are the same, no conversion is required.
        if from_unit == to_unit:
            return value
        # perform conversions
        if (from_unit, to_unit) in LENGTH_CONVERSION_FACTORS:
            return value * LENGTH_CONVERSION_FACTORS[(from_unit, to_unit)]
        else:
            raise ValueError(f"No conversion available {from_unit} to {to_unit}.")


class WeightConversionStrategy(ConversionStrategy):
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        # if units are the same, no conversion is required.
        if from_unit == to_unit:
            return value
        # perform conversions
        if (from_unit, to_unit) in WEIGHT_CONVERSION_FACTORS:
            return value * WEIGHT_CONVERSION_FACTORS[(from_unit, to_unit)]
        else:
            raise ValueError(f"No conversion available {from_unit} to {to_unit}.")


class TemperatureConversionStrategy(ConversionStrategy):
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        pass


class UnitConverter:
    def __init__(self, strategy: ConversionStrategy):
        self.strategy = strategy

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        return self.strategy.convert(value, from_unit, to_unit)
