
from task26.pom_file import InputFieldPage
def test_enter_name(browser):
    name_field = InputFieldPage(browser)
    name_field.SetNameInput("Tom Cruise")

def test_enter_birthdate(browser):
    birthdate_field = InputFieldPage(browser)
    birthdate_field.SetBirthDate("01/01/1950", "01/01/2024")

def test_enter_birthday(browser):
    birthday_field = InputFieldPage(browser)
    birthday_field.SetBirthday("01-01")

def test_select_awards(browser):
    awards_field = InputFieldPage(browser)
    awards_field.SelectAwards()

def test_select_pagetopics(browser):
    pagetopics_field = InputFieldPage(browser)
    pagetopics_field.SelectPageTopic("Quotes")

def test_select_gender(browser):
    gender_field = InputFieldPage(browser)
    gender_field.SelectGender()
