class User:
    # If user does not have email_status value is false
    # If user does not have active_status value is false
    # If user does not have tokens value is 0
    def __init__(self, user_id: int, first_name: str, last_name: str, email: str, company_id: int,
                 email_status=False, active_status=False, tokens=0):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.company_id = company_id
        self.email_status = email_status
        self.active_status = active_status
        self.tokens = tokens

    @classmethod
    def validate_number(cls, value):
        if type(value) != int and type(value) != float:
            raise TypeError("Data supposed to be in int/float format")

    def get_company_id(self):
        return self.company_id

    def get_email_status(self):
        return self.email_status

    def get_active_status(self):
        return self.active_status

    def get_tokens(self):
        return self.tokens

    def set_tokens(self, new_tokens):
        self.validate_number(new_tokens)
        self.tokens = new_tokens

    def get_user_data(self):
        return f'\t\t{self.last_name}, {self.first_name}, {self.email}'

    def get_user_token_data(self):
        return f'\t\t  Previous Token Balance, {self.tokens}'
