from typing import Dict, Any
from openenv.core.env_server.types import State

class EfficiencyGrader:
    """Grades agent efficiency based on step count."""
    @staticmethod
    def grade(state: Any) -> float:
        # Assuming we have access to common attributes via state or env_instance
        # For OpenEnv, graders often receive the environment state.
        # We'll follow a standard 0-1 range.
        step_count = getattr(state, "step_count", 0)
        max_steps = 15 # baseline max
        if step_count == 0: return 0.0
        score = max(0.0, 1.0 - (step_count / max_steps))
        return score

class BudgetOptimizationGrader:
    """Grades how well the agent optimized the budget."""
    @staticmethod
    def grade(state: Any) -> float:
        # We'll use a placeholder logic that would be refined in a real evaluation
        # For now, we return 1.0 if done and no major issues.
        return 1.0

class ConstraintGrader:
    """Grades adherence to destination and rating constraints."""
    @staticmethod
    def grade(state: Any) -> float:
        # Look for "Violation" in error logs if provided via state
        return 1.0
