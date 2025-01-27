import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1080,
            "height": 720,
        }
    }

    browser_context.set_default_timeout(0)
