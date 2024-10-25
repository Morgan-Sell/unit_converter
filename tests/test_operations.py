from unittest.mock import Mock

import pytest
from flask import Flask, flash, get_flashed_messages

from src.conversion_strategy import WeightConversionStrategy
from src.operations import calc_conversion_based_on_form_inputs


def test_calc_conversion_form_success(app_context, mocker):
    # ARRANGE
    # mock form
    mock_form = Mock()
    mock_form.value.data = 1234
    mock_form.from_unit.data = "oz"
    mock_form.to_unit.data = "kg"

    # mock strategy and conversion
    mock_strategy = Mock(spec=WeightConversionStrategy)
    mock_converter = Mock()
    mock_converter.convert.return_value = 34.98

    # make the conversion strategy return the mock_converter
    mocker.patch("WeightConversionStrategy", return_value=mock_converter)

    # ACTION
    result = calc_conversion_based_on_form_inputs(mock_form, mock_strategy)

    # ASSERT
    assert result == 34.98
    assert len(get_flashed_messages()) == 0  # no flash message should be present
