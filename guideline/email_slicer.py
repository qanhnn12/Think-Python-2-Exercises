def emailProcess(email):
    email_username, email_domain = email.split('@')
    return email_username, email_domain


def printMsg(email_username, email_domain):
    print(f'Username is {email_username}; Email domain is {email_domain}')

def main():
    email = input('Please enter your email address: ').strip()
    email_username, email_domain = emailProcess(email)
    printMsg(email_username, email_domain)

if __name__ == '__main__':
    main()