import unittest
from lib.Process import Process


class TestChallenge(unittest.TestCase):
    companies = [{'id': 1, 'name': 'Stark Industries', 'top_up': 100, 'email_status': False},
                 {'id': 2, 'name': 'Ghostbusters', 'top_up': 15, 'email_status': True}]

    users = [
        {'id': 9, 'first_name': 'Louise', 'last_name': 'Tully', 'email': 'louse.tully@demo.com',
         'company_id': 2, 'email_status': True, 'active_status': True, 'tokens': 10},
        {'id': 21, 'first_name': 'Lyanna', 'last_name': 'Stark', 'email': 'lyanna.stark@test.com',
         'company_id': 1, 'email_status': True, 'active_status': False, 'tokens': 43},
        {'id': 22, 'first_name': 'Peter', 'last_name': 'Venkman', 'email': 'slimer.ghost@notreal.com',
         'company_id': 2, 'email_status': True, 'active_status': False, 'tokens': 100},
        {'id': 22, 'first_name': 'Slimer', 'last_name': 'Ghost', 'email': 'slimer.ghost@notreal.com',
         'company_id': 2, 'email_status': False, 'active_status': True, 'tokens': 100}
    ]

    companies_no_names = [{'id': 1, 'top_up': 100, 'email_status': False},
                          {'id': 2, 'top_up': 15, 'email_status': True}]

    users_no_emails = [
        {'id': 9, 'first_name': 'Louise', 'last_name': 'Tully',
         'company_id': 2, 'email_status': True, 'active_status': True, 'tokens': 10},
        {'id': 21, 'first_name': 'Lyanna', 'last_name': 'Stark',
         'company_id': 1, 'email_status': True, 'active_status': False, 'tokens': 43},
        {'id': 22, 'first_name': 'Peter', 'last_name': 'Venkman',
         'company_id': 2, 'email_status': True, 'active_status': False, 'tokens': 100},
        {'id': 22, 'first_name': 'Slimer', 'last_name': 'Ghost',
         'company_id': 2, 'email_status': False, 'active_status': True, 'tokens': 100}
    ]

    users_with_non_existing_company_id = [
        {'id': 9, 'first_name': 'Louise', 'last_name': 'Tully', 'email': 'louse.tully@demo.com',
         'company_id': 1000, 'email_status': True, 'active_status': True, 'tokens': 10},
        {'id': 21, 'first_name': 'Lyanna', 'last_name': 'Stark', 'email': 'lyanna.stark@test.com',
         'company_id': 1000, 'email_status': True, 'active_status': False, 'tokens': 43},
        {'id': 22, 'first_name': 'Peter', 'last_name': 'Venkman', 'email': 'slimer.ghost@notreal.com',
         'company_id': 1000, 'email_status': True, 'active_status': False, 'tokens': 100},
        {'id': 22, 'first_name': 'Slimer', 'last_name': 'Ghost', 'email': 'slimer.ghost@notreal.com',
         'company_id': 1000, 'email_status': False, 'active_status': True, 'tokens': 100}
    ]

    def test_users_output(self):
        output = Process().start(self.users, self.companies)

        expected_result = f'\tCompany Id: 2\n' \
                          f'\tCompany Name: Ghostbusters\n' \
                          f'\tUsers Emailed:\n' \
                          f'\t\tTully, Louise, louse.tully@demo.com\n' \
                          f'\t\t    Previous Token Balance, 10\n' \
                          f'\t\t  New Token Balance 25\n' \
                          f'\t Users Not Emailed:\n' \
                          f'\t\tGhost, Slimer, slimer.ghost@notreal.com\n' \
                          f'\t\t    Previous Token Balance, 100\n' \
                          f'\t\t  New Token Balance 115\n' \
                          f'\t\t Total amount of top ups for Ghostbusters: 30\n' \
                          f'\n'

        self.assertEqual(expected_result.replace(' ', ''), output.replace(' ', ''),
                         'The output differs from expected result')

    def test_no_companies(self):
        output = Process().start(self.users, [])

        expected_result = ''

        self.assertEqual(expected_result, output,
                         'The output should be empty with 0 companies')

    def test_no_users(self):
        output = Process().start([], self.companies)

        expected_result = ''

        self.assertEqual(expected_result, output,
                         'The output should be empty with 0 users')

    def test_user_lacks_emails(self):
        output = Process().start(self.users_no_emails, self.companies)

        expected_result = ''

        self.assertEqual(expected_result, output,
                         'The output should be empty when users do not have emails')

    def test_company_lacks_names(self):
        output = Process().start(self.users, self.companies_no_names)

        expected_result = ''

        self.assertEqual(expected_result, output,
                         'The output should be empty when companies do not have names')

    def test_user_has_non_existing_company_id(self):
        output = Process().start(self.users_with_non_existing_company_id, self.companies)

        expected_result = ''

        self.assertEqual(expected_result, output,
                         'The output should be empty when users have company id that does not exist')


if __name__ == '__main__':
    unittest.main()
