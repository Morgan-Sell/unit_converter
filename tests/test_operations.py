from unittest.mock import Mock

import pytest
from flask import Flask, flash, get_flashed_messages

from src.conversion_strategy import WeightConversionStrategy
from src.operations import calc_conversion_based_on_form_inputs


def test_calc_conversion_form_success(app_context, mocker):
    # Arrange
    mock_form = Mock()
    mock_form.value.data = 1234
    mock_form.from_unit.data = "oz"
    mock_form.to_unit.data = "kg"

    mock_converter = Mock()
    mock_converter.convert.return_value = 34.98
    mocker.patch("src.conversion_strategy.UnitConverter", return_value=mock_converter)

    # Action
    result = calc_conversion_based_on_form_inputs(mock_form, WeightConversionStrategy())
    result_rounded = round(result, 2)

    # Assert
    assert result_rounded == 34.98
    assert len(get_flashed_messages()) == 0  # no flash message should be present


def test_calc_conversion_form_raises_error(app_context, mocker):
    # Arrange
    mock_form = Mock()
    mock_form.value.data = 1234
    mock_form.from_unit.data = "oz"
    mock_form.to_unit.data = "invalid_unit"

    mock_converter = Mock()
    mock_converter.convert.side_effect = ValueError("Invalid conversion units")
    mocker.patch("src.conversion_strategy.UnitConverter", return_value=mock_converter)

    # Action
    result = calc_conversion_based_on_form_inputs(mock_form, WeightConversionStrategy())

    # Assert
    assert result is None
    assert get_flashed_messages(with_categories=True) == [
        ("danger", "Unsupported conversion from oz to invalid_unit.")
    ]
