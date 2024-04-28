from xerparser.src.validators import float_or_zero
class RSRCCURVDATA:
    """
    A class to represent P6 curve values.
    Used when a curve is applied to a TASKRSRC
    """
    
    def __init__(self, **data) -> None:
        #TODO change types to match once integration is complete
        self.uid: str = data["curv_id"]
        self.name: str = data[ "curv_name"]
        self.default_flag: str = data[ "default_flag"]
        self.curve_values = [
            float_or_zero(data["pct_usage_0"]),
            float_or_zero(data["pct_usage_1"]),
            float_or_zero(data["pct_usage_2"]),
            float_or_zero(data["pct_usage_3"]),
            float_or_zero(data["pct_usage_4"]),
            float_or_zero(data["pct_usage_5"]),
            float_or_zero(data["pct_usage_6"]),
            float_or_zero(data["pct_usage_7"]),
            float_or_zero(data["pct_usage_8"]),
            float_or_zero(data["pct_usage_9"]),
            float_or_zero(data["pct_usage_10"]),
            float_or_zero(data["pct_usage_11"]),
            float_or_zero(data["pct_usage_12"]),
            float_or_zero(data["pct_usage_13"]),
            float_or_zero(data["pct_usage_14"]),
            float_or_zero(data["pct_usage_15"]),
            float_or_zero(data["pct_usage_16"]),
            float_or_zero(data["pct_usage_17"]),
            float_or_zero(data["pct_usage_18"]),
            float_or_zero(data["pct_usage_19"]),
            float_or_zero(data["pct_usage_20"])
        ]
        
    def __str__(self) -> str:
        return f"{self.name}"
    
    def _convert_to_curve_data(self, **data) -> list[tuple[int, float]]:
        curve_values = []
        
        
        
    
