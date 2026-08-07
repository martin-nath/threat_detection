from monitor import ContinuousMonitor

monitor = ContinuousMonitor()

monitor.event_counts = {
    "Scream": 2,
    "Glass": 1
}

print("Monitor State:")
print(monitor.get_state())

print("\nThreat Signals:")
print(monitor.get_threat_signals())

print("\nContinuous Events:")
print(monitor.get_continuous_events())