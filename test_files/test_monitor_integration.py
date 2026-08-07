from monitor import ContinuousMonitor

monitor = ContinuousMonitor()

test_data = [
    [{"label": "Scream", "confidence": 0.90}],
    [{"label": "Scream", "confidence": 0.85}],
    [{"label": "Glass", "confidence": 0.80}],
]

for accepted_predictions in test_data:

    monitor.update(accepted_predictions)

    print("\nMonitor State:")
    print(monitor.get_state())

    print("\nThreat Signals:")
    print(monitor.get_threat_signals())

    print("\nContinuous Events:")
    print(monitor.get_continuous_events())