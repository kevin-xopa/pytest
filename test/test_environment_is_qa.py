from pytest import mark

# @mark.skip(reason='broken by last deployed some number')
# def test_environment_is_qa(app_config):
#     # assert env == 'qa'
#     base_url = app_config.base_url
#     port = app_config.app_port
#     assert base_url == 'https://myqa-env.com'
#     assert port == 80


@mark.xfail(reason='Env was not QA')
def test_environment_is_qa(app_config):
    # assert env == 'qa'
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80


def test_environment_is_dev(app_config):
    # assert env == 'dev'
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://mydev-env.com'
    assert port == 8080


@mark.skip(reason='Not staging environment')
def test_environment_is_staging(app_config):
    base_url = app_config.base_url
    assert base_url == 'staging'


def test_this_should_always_pass():
    assert True


@mark.skip(reason='Broken, fixing next sprint')
def test_this_needs_work():
    assert False


@mark.xfail(reason='This feature should have been deprecated')
def test_this_should_always_fail():
    assert False