from abc import ABC, abstractmethod


class ConversionStrategy(ABC):
    @abstractmethod
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        pass


class LengthConversionStrategy(ConversionStrategy):
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        pass


class WeightConversionStrategy(ConversionStrategy):
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        pass


class TemperatureConversionStrategy(ConversionStrategy):
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        pass


class UnitConverter:
    def __init__(self, strategy: ConversionStrategy):
        self.strategy = strategy

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        return self.strategy.convert(value, from_unit, to_unit)
