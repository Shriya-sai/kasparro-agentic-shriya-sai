from typing import TypedDict, Dict, List, Optional

class AgentState(TypedDict):
    product: Dict
    faqs: Optional[Dict]
    product_page: Optional[Dict]
    comparison_page: Optional[Dict]
    errors: List[str]
