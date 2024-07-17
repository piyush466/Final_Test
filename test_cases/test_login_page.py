import pytest

from test_cases.baseclass import Baseclass


class Test_login(Baseclass):

    def test_01_login_with_valid_creds(self):
        self.login.do_login("student", "Password123")
        self.base.assertion(self.base.get_title(), "Logged In Successfully | Practice Test Automation")

    def test_02_login_with_invalid_password(self):
        self.login.do_login("student", "Password")
        self.base.assertion(self.base.get_text(self.login.Invalid_creds), "Your password is invalid!")

    def test_03_login_with_invalid_username(self):
        self.login.do_login("stud", "Password@123")
        self.base.assertion(self.base.get_text(self.login.Invalid_creds), "Your username is invalid!")

    # @pytest.mark.skip
    def test_04_login_with_invalid_creds(self):
        self.login.do_login("stud", "Pass")
        self.base.assertion(self.base.get_text(self.login.Invalid_creds), "Your username is invalid!")



