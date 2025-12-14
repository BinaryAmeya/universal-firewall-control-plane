def safe_call(fn, fallback=None):
    try:
        return fn()
    except Exception as e:
        return fallback
