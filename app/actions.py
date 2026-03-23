def trigger_action(is_valid, data):
    if is_valid:
        return "stored_and_api_triggered"
    else:
        return "sent_to_manual_review"