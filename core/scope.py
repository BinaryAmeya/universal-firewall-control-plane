def scoped_action(action):
    if action is None:
        return None
    return f"{action}_LIMITED_SCOPE"
