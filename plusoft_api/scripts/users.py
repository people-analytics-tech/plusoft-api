from plusoft_api.helpers.api_endpoint import ApiEndpoint
from plusoft_api.scripts.consult import FutureProcessing
from decouple import config
from typing import Literal
from enum import Enum


class GroupsOptions(int, Enum):
      ADD_GROUPS = 1
      FULL_UPDATE = 2
      REMOVE_GROUPS = 3
      REMOVE_ALL_GROUPS = 4


class Users(ApiEndpoint):
    
    def __init__(
            self,
            username: str = config("PLUSOFT_USERNAME"),
            password: str = config("PLUSOFT_PASSWORD")
        ):
            super().__init__(username=username, password=password, endpoint_path="/import/user")
    
    def insert_user(
            self,
            login: str,
            name: str,
            email: str,
            password: str = None,
            nickname: str = None,
            biography: str = None,
            telephone: str = None,
            team: str = None,
            position: str = None,
            login_manager: str = None,
            name_manager: str = None,
            position_manager: str = None,
            photo: dict = None,
            language: dict = None,
            active: Literal["sim", "nao"] = None,
            cover: dict = None,
            terms: Literal["sim", "nao"] = None,
            groups: list[str] = None,
            groups_option: GroupsOptions = None,
            new_login: str = None
        ) -> FutureProcessing:
            payload = [
                {
                    "login": login,
                    "nome": name,
                    "senha": password,
                    "email": email,
                    "apelido": nickname,
                    "biografia": biography,
                    "telefone": telephone,
                    "time": team,
                    "cargo": position,
                    "login_supervisor": login_manager,
                    "nome_supervisor": name_manager,
                    "cargo_supervisor": position_manager,
                    "foto": photo,
                    "linguagem": language,
                    "ativo": active,
                    "capa": cover,
                    "termos": terms,
                    "grupos": groups,
                    "grupos_opcao": groups_option,
                    "novo_login": new_login
                }
            ]
            return FutureProcessing(
                   username=self.base_requests.__username,
                   password=self.base_requests.__password,
                   **self.base_requests.post(path=self.endpoint_path, json=payload)
            )