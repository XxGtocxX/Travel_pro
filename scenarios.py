from typing import Tuple, Dict, Any
from enum import Enum
from travel_pro.models import UserGoal

class ScenarioLevel(Enum):
    HAPPY_PATH = 1
    ADVERSARIAL = 2
    CHAOS = 3

class ScenarioManager:
    """Manages environment scenarios and entropy profiles."""
    
    @staticmethod
    def get_scenario(level: int) -> Tuple[UserGoal, Dict[str, Any]]:
        """
        Returns (UserGoal, EnvConfig) based on the entropy level.
        
        Level 1 (HAPPY_PATH): Generates a UserGoal with a $5,000 budget and high availability.
        
        Level 2 (ADVERSARIAL): Injects FLIGHT_CRUNCH (high prices) or HOTEL_STRIKE (no hotels). 
        Strict constraints (e.g., 'Must be 4+ stars' with a low $1,200 budget).
        
        Level 3 (CHAOS): Activates 'Stale Data' mode. Prices are initialized but flagged 
        for dynamic updates in the environment state.
        """
        if level == ScenarioLevel.HAPPY_PATH.value:
            user_goal = UserGoal(
                destination="Paris",
                budget=5000.0,
                max_steps=15
            )
            env_config = {
                "availability": "high",
                "pricing": "standard",
                "stale_data": False,
                "flags": ["HIGH_AVAILABILITY"]
            }
            return user_goal, env_config
        
        elif level == ScenarioLevel.ADVERSARIAL.value:
            import random
            adversary_type = random.choice(["FLIGHT_CRUNCH", "HOTEL_STRIKE"])
            
            user_goal = UserGoal(
                destination="Tokyo",
                budget=1200.0,
                min_hotel_rating=4.0,
                is_direct_flight_required=True,
                max_steps=10
            )
            
            env_config = {
                "adversary": adversary_type,
                "availability": "none" if adversary_type == "HOTEL_STRIKE" else "low",
                "pricing": "premium" if adversary_type == "FLIGHT_CRUNCH" else "standard",
                "stale_data": False,
                "flags": [adversary_type, "STRICT_CONSTRAINTS"]
            }
            return user_goal, env_config
        
        elif level == ScenarioLevel.CHAOS.value:
            user_goal = UserGoal(
                destination="London",
                budget=2000.0,
                max_steps=20
            )
            env_config = {
                "stale_data": True,
                "dynamic_updates": True,
                "volatility": "extreme",
                "flags": ["STALE_DATA_ENABLED", "DYNAMIC_PRICING"]
            }
            return user_goal, env_config
        
        else:
            raise ValueError(f"Unsupported scenario level: {level}")
