from monitor import ContinuousMonitor

monitor = ContinuousMonitor()

test_cases = [

    # Test 1
    [
        {"label": "Scream", "confidence": 0.90}
    ],

    # Test 2
    [
        {"label": "Scream", "confidence": 0.88}
    ],

    # Test 3
    [
        {"label": "Glass", "confidence": 0.85}
    ],

    # Test 4
    [
        {"label": "Explosion", "confidence": 0.92}
    ],

    # Test 5
    [
        {"label": "Gunshot, gunfire", "confidence": 0.95}
    ]

]

for i, accepted_predictions in enumerate(test_cases, start=1):

    print("\n" + "=" * 50)
    print(f"TEST {i}")
    print("=" * 50)

    monitor.update(accepted_predictions)

    print("\nMonitor State:")
    print(monitor.get_state())

    print("\nThreat Signals:")
    print(monitor.get_threat_signals())

    print("\nContinuous Events:")
    print(monitor.get_continuous_events())