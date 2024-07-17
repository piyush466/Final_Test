import pytest

from test_cases.baseclass import Baseclass


class Test_login(Baseclass):

    def test_01_login_with_valid_creds(self):
        self.login.do_login("student", "Password123")
        Expected_result = "Logged In Successfully | Practice Test Automation"
        assert self.base.get_title() == Expected_result

    def test_02_login_with_invalid_password(self):
        self.login.do_login("student", "Password")
        Expecter_result = "Your password is invalid!"
        assert self.base.get_text(self.login.Invalid_creds) == Expecter_result

    def test_03_login_with_invalid_username(self):
        self.login.do_login("stud", "Password@123")
        Expecter_result = "Your username is invalid!"
        assert self.base.get_text(self.login.Invalid_creds) == Expecter_result

    @pytest.mark.skip
    def test_04_login_with_invalid_creds(self):
        self.login.do_login("stud", "Pass")
        Expecter_result = "Your username is invalid!"
        assert self.base.get_text(self.login.Invalid_creds) == Expecter_result


