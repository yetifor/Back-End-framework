class SoftAssert:
    def __init__(self):
        self.warnings = []

    def soft_assert(self, actual, expected, msg=""):
        if actual != expected:
            error_msg = (f"Message: {msg}\n"
                         f"Wrong result actual: {actual}\n"
                         f"Expected result: {expected}")
            self.warnings.append(error_msg)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.warnings:
            raise AssertionError("\n".join(self.warnings))
