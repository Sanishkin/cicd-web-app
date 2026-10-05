def test_application_title():
    with open("app/index.html", "r") as file:
        content = file.read()

    assert "CI/CD Web Application" in content


def test_application_status():
    with open("app/index.html", "r") as file:
        content = file.read()

    assert "APPLICATION DEPLOYED SUCCESSFULLY" in content