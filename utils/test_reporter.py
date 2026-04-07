import os
import json
from datetime import datetime

class TestReporter:
    def __init__(self, scenario_name):
        self.scenario_name = scenario_name
        self.results_dir = os.path.join(os.getcwd(), "test_results")
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.report_path = os.path.join(self.results_dir, f"test_run_{timestamp}.json")
        self.steps = []
        self.start_time = datetime.now().isoformat()

    def log_step(self, step_name, status, details=""):
        """Logs a test step with its status and optional details."""
        step_info = {
            "step": step_name,
            "status": status,
            "timestamp": datetime.now().isoformat(),
            "details": details
        }
        self.steps.append(step_info)
        print(f"[{status}] {step_name}: {details}")

    def finalize_report(self, overall_status):
        """Finalizes the test run and saves the results to a JSON file."""
        report_data = {
            "scenario": self.scenario_name,
            "overall_status": overall_status,
            "start_time": self.start_time,
            "end_time": datetime.now().isoformat(),
            "steps": self.steps
        }
        
        with open(self.report_path, "w") as f:
            json.dump(report_data, f, indent=4)
        
        print(f"\nTest report saved to: {self.report_path}")
        return self.report_path
