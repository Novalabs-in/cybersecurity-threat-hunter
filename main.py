from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyThreatHunter:
    """
    Cybersecurity Telemetry Anomaly Detector
    Utilizes Isolation Forests to analyze connection frequency and byte transfer rates for intrusions.
    """
    def __init__(self):
        self.detector = IsolationForest(contamination=0.05, random_state=42)

    def train(self, normal_traffic_features):
        self.detector.fit(normal_traffic_features)
        print("Threat hunting anomaly detector trained on baseline network profile.")

    def inspect_traffic(self, live_traffic):
        # 1 = Normal connection, -1 = Anomalous threat flagged
        signals = self.detector.predict(live_traffic)
        return np.where(signals == -1, "SUSPICIOUS THREAT FLAGGED", "SAFE CONNECTION")

if __name__ == "__main__":
    baseline = np.random.normal(50, 5, (100, 2)) # 100 safe connections with low duration & byte transfers
    hunter = AnomalyThreatHunter()
    hunter.train(baseline)
    
    live_checks = np.array([
        [48.0, 52.0],  # Normal traffic
        [999.0, 999.0] # Massive out-of-bound byte transfer
    ])
    print("Live Network Scan Results:")
    print(hunter.inspect_traffic(live_checks))
