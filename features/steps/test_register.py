from pytest_bdd import given, then, when, scenario
from pages.actions.register_actions import RegisterActions


@scenario("register.feature","Register User with valid credentials")
def test_register_user():
    pass

@given('the User goes to the Website')
def step_open_web(driver) -> None:
    register = RegisterActions(driver)
    register.load("https://testertestarudo.com/sandbox-para-pruebas-automatizadas/")


@when('the User enters with valid credentials')
def step_register_user(driver) -> None:
    register = RegisterActions(driver)
    register.type_user("Manuel")
    register.type_email("email@testertestarudo.com")
    register.type_age("36")
    register.click_to_register()

@then('the User is registered successfully')
def step_user_is_registered_successfully(driver) -> None:
    register = RegisterActions(driver)
    register.user_is_logged()
