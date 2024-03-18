from plusoft_api.scripts.users import BasicAuth, Users


class PlusoftApi:
    def __init__(self, username: str, password: str, domain: str) -> None:
        self.__basic_auth = BasicAuth(username, password)
        self.__domain = domain
        self.__users: Users = None

    @property
    def users(self) -> Users:
        if not self.__users:
            self.__users = Users(basic_auth=self.__basic_auth, domain=self.__domain)

        return self.__users
