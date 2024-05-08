from lib.User import User


class Company:
    # If company does not have top_up value is 0
    # If company does not have email_status value is false
    def __init__(self, company_id, name, top_up=0, email_status=False):
        self.company_id = company_id
        self.name = name
        self.top_up = top_up
        self.email_status = email_status
        self.users_emailed = []
        self.users_not_emailed = []

    def get_company_id(self):
        return self.company_id

    def get_name(self):
        return self.name

    def get_top_up(self):
        return self.top_up

    def get_users_emailed(self):
        return self.users_emailed

    def get_users_not_emailed(self):
        return self.users_not_emailed

    def print_users(self, users):
        resulting_string = ''
        for user in users:
            resulting_string += f'{user.get_user_data()}\n' \
                                f'  {user.get_user_token_data()}\n' \
                                f'\t\t  New Token Balance {user.tokens + self.top_up}\n '
        return resulting_string

    def get_company_top_up_balance(self):
        return (len(self.get_users_emailed()) + len(self.get_users_not_emailed())) * self.top_up

    def print_company_balance(self):
        return f'\tTotal amount of top ups for {self.name}: ' \
               f'{self.get_company_top_up_balance()}'

    def add_user(self, user_data):
        user_keys = {'id', 'first_name', 'last_name', 'email', 'company_id'}

        # Checks that user has all required keys, taking into account that if it lacks
        # email_status, active_status, tokens - they are set to 0/false
        if (user_data.keys()) >= user_keys:
            new_user = User(user_data['id'], user_data['first_name'], user_data['last_name'],
                            user_data['email'], user_data['company_id'], user_data['email_status'],
                            user_data['active_status'], user_data['tokens'])

            if not new_user.get_active_status():
                return

            if not self.email_status:
                self.users_not_emailed.append(new_user)
                return

            if new_user.get_email_status():
                self.users_emailed.append(new_user)
            else:
                self.users_not_emailed.append(new_user)

        else:
            return
