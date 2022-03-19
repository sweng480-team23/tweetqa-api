def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    config.addinivalue_line(
        "markers", "qa_model: mark a test that is a part of the QAModel stack"
    )
    config.addinivalue_line(
        "markers", "data: mark a test that is a part of the Data stack"
    )
    config.addinivalue_line(
        "markers", "account: mark a test that is a part of the Account stack"
    )
    config.addinivalue_line(
        "markers", "visitor: mark a test that is a part of the Visitor stack"
    )
    config.addinivalue_line(
        "markers", "predicition: mark a test that is a part of the Predicition stack"
    )


def pytest_unconfigure(config):
    """
    called before test process is exited.
    """
    pass
