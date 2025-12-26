def validate_faq_count(faqs: dict) -> bool:
    return sum(len(v) for v in faqs.values()) >= 15
