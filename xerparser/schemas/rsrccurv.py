class RSRCCURVDATA:
    """
    A class to represent P6 curve values.
    Used when a curve is applied to a TASKRSRC
    """
    
    def __init__(self, **data) -> None:
        #TODO change types to match once integration is complete
        self.curv_id: str = data["curv_id"]
        self.curv_name: str = data[ "curv_name"]
        self.default_flag: str = data[ "default_flag"]
        self.pct_usage_0: str = data[ "pct_usage_0"]
        self.pct_usage_1: str = data[ "pct_usage_1"]
        self.pct_usage_2: str = data[ "pct_usage_2"]
        self.pct_usage_3: str = data[ "pct_usage_3"]
        self.pct_usage_4: str = data[ "pct_usage_4"]
        self.pct_usage_5: str = data[ "pct_usage_5"]
        self.pct_usage_6: str = data[ "pct_usage_6"]
        self.pct_usage_7: str = data[ "pct_usage_7"]
        self.pct_usage_8: str = data[ "pct_usage_8"]
        self.pct_usage_9: str = data[ "pct_usage_9"]
        self.pct_usage_10: str = data[ "pct_usage_10"]
        self.pct_usage_11: str = data[ "pct_usage_11"]
        self.pct_usage_12: str = data[ "pct_usage_12"]
        self.pct_usage_13: str = data[ "pct_usage_13"]
        self.pct_usage_14: str = data[ "pct_usage_14"]
        self.pct_usage_15: str = data[ "pct_usage_15"]
        self.pct_usage_16: str = data[ "pct_usage_16"]
        self.pct_usage_17: str = data[ "pct_usage_17"]
        self.pct_usage_18: str = data[ "pct_usage_18"]
        self.pct_usage_19: str = data[ "pct_usage_19"]
        self.pct_usage_20: str = data[ "pct_usage_20"]
