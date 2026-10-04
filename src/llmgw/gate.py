class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if body.get("model") not in {"local-small", "local-large"}: failed.append("model_not_allowed")\n    if int(body.get("tokens") or 0) > int(body.get("budget") or 0): failed.append("over_budget")
    return {"passed": not failed, "failed": failed, "applied": False}
