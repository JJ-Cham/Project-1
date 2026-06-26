import pytest
from unittest.mock import patch

from game.actions import perform_action

# Test: transport modes use carbon_saved
@patch("game.actions.sprout_feedback")
@patch("game.actions.get_weather")
@patch("game.actions.get_plant")
@patch("game.actions.update_plant_progression")
@patch("game.actions.log_action")
@patch("game.actions.carbon_saved")
def test_perform_action_transport_modes(
    mock_carbon,
    mock_log,
    mock_update,
    mock_get_plant,
    mock_weather,
    mock_feedback
):
    mock_carbon.return_value = 10.5
    mock_get_plant.return_value = {"stage": 2}
    mock_weather.return_value = {"description": "Sunny"}
    mock_feedback.return_value = "ok"

    result = perform_action(
        user_id=1,
        action_type="bike",
        distance=5,
        city="Atlanta"
    )

    mock_carbon.assert_called_once_with("bike", 5)
    mock_log.assert_called_once_with(1, "bike", 10.5)

    # safer check
    mock_update.assert_called_once()
    update_args = mock_update.call_args[0]

    assert update_args[0] == 1          # user_id
    assert update_args[1] == 10         # weather_bonus = int(saved)
    assert update_args[2] == 0          # carbon_penalty default

    mock_feedback.assert_called_once()
    assert result == "ok"


# Test: invalid action defaults carbon to 0.5
@patch("game.actions.sprout_feedback")
@patch("game.actions.get_weather")
@patch("game.actions.get_plant")
@patch("game.actions.update_plant_progression")
@patch("game.actions.log_action")
@patch("game.actions.carbon_saved")
def test_perform_action_invalid_action(
    mock_carbon,
    mock_log,
    mock_update,
    mock_get_plant,
    mock_weather,
    mock_feedback
):
    mock_get_plant.return_value = {"stage": 1}
    mock_weather.return_value = {"description": "Rainy"}
    mock_feedback.return_value = "ok"

    result = perform_action(
        user_id=2,
        action_type="gaming",
        distance=0,
        city="Atlanta"
    )

    mock_carbon.assert_not_called()
    mock_log.assert_called_once_with(2, "gaming", 0.5)

    update_args = mock_update.call_args[0]
    assert update_args[1] == 0  # int(0.5)

    assert result == "ok"


# Test: weather fallback
@patch("game.actions.sprout_feedback")
@patch("game.actions.get_weather")
@patch("game.actions.get_plant")
@patch("game.actions.update_plant_progression")
@patch("game.actions.log_action")
@patch("game.actions.carbon_saved")
def test_weather_fallback(
    mock_carbon,
    mock_log,
    mock_update,
    mock_get_plant,
    mock_weather,
    mock_feedback
):
    mock_carbon.return_value = 3
    mock_get_plant.return_value = {"stage": 4}
    mock_weather.return_value = None
    mock_feedback.return_value = "ok"

    perform_action(
        user_id=3,
        action_type="walk",
        distance=2,
        city="UnknownCity"
    )

    args = mock_feedback.call_args[0]
    assert args[-1] == "Unknown"

# Test: feedback input correctness
@patch("game.actions.sprout_feedback")
@patch("game.actions.get_weather")
@patch("game.actions.get_plant")
@patch("game.actions.update_plant_progression")
@patch("game.actions.log_action")
@patch("game.actions.carbon_saved")
def test_feedback_input_values(
    mock_carbon,
    mock_log,
    mock_update,
    mock_get_plant,
    mock_weather,
    mock_feedback
):
    mock_carbon.return_value = 8
    mock_get_plant.return_value = {"stage": 3}
    mock_weather.return_value = {"description": "Cloudy"}
    mock_feedback.return_value = "good"

    perform_action(
        user_id=99,
        action_type="bus",
        distance=10,
        city="Atlanta"
    )

    mock_feedback.assert_called_once()

    args = mock_feedback.call_args[0]

    assert args[0] == "bus"
    assert args[1] == 8
    assert args[2] == 3
    assert args[3] == "Cloudy"