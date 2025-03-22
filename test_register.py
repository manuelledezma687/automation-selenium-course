from pages.actions.register_actions import RegisterActions

def test_fill_form(browser):
    register = RegisterActions(browser)
    register.load("https://testertestarudo.com/sandbox-para-pruebas-automatizadas/")
    register.type_user("Manuel")
    register.type_email("email@testertestarudo.com")
    register.type_age("36")
    register.click_to_register()
    register.user_is_logged()