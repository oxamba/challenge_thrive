from lib.Company import Company


class Process:
    @classmethod
    def start(cls, users_data, companies_data):
        # Sort received users by their last name ASC
        sorted_users_data = sorted(users_data, key=lambda d: d['last_name'])

        # Sort received companies by their id ASC
        sorted_companies_data = sorted(companies_data, key=lambda d: d['id'])
        companies_dict = cls.create_company_dict(sorted_companies_data)
        cls.add_filtered_users_to_companies(sorted_users_data, companies_dict)
        return cls.form_output(companies_dict)

    # Iterates through a list of dictionaries containing company data,
    # creating a new dictionary with the following format:
    # - The company_id serves as the key - to easily get access to company by ID
    # - The corresponding value is a company object representing the company with that ID.
    # Additionally, this process involves filtering out companies with missing ID or name fields.
    @classmethod
    def create_company_dict(cls, sorted_companies_data):
        return {
            company['id']: Company(company['id'], company['name'], company['top_up'], company['email_status'])
            for company in sorted_companies_data
            if 'id' and 'name' in company.keys()}

    # Adds users to their corresponding company and skips users with a non-existing company ID
    @classmethod
    def add_filtered_users_to_companies(cls, sorted_users_data, companies_dict):
        for user in sorted_users_data:
            if user['company_id'] not in companies_dict.keys():
                continue
            company = companies_dict[user['company_id']]
            company.add_user(user)

    # Forms output, if there are no active users in the company output is empty
    @classmethod
    def form_output(cls, companies_dict):
        output = ''
        for company_id, company in companies_dict.items():
            if len(company.get_users_emailed()) + len(company.get_users_not_emailed()) == 0:
                continue

            output += f'\tCompany Id: {company_id}\n' \
                      f'\tCompany Name: {company.name}\n' \
                      f'\tUsers Emailed:\n{company.print_users(company.get_users_emailed())}' \
                      f'\tUsers Not Emailed:\n{company.print_users(company.get_users_not_emailed())}' \
                      f'\t{company.print_company_balance()}\n' \
                      f'\n'

        return output
