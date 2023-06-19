from auth.domain.dto import LoginDto


def login(login_data: LoginDto, repository):
    return repository.login(login_data)


def process_token(token: str, repository):
    return repository.verify_token(token)
