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
    def historic_user_access(
                  self,
                  login: str,
                  login_data: str,
                  remote_ip: str =  None,
                  operational_system: str = None,
                  browser: str = None,
                  browser_version: str = None,
                  logout_data: str = None                  
    ) -> FutureProcessing:
           payload = [
                  {
                         "login": login,
                         "data_login": login_data,
                         "ip_remoto": remote_ip,
                         "sistema_operacional": operational_system,
                         "navegador": browser,
                         "versao_navegador": browser_version,
                         "data_logout": logout_data
                  }
           ]
           return FutureProcessing(
                  username=self.base_requests.__username,
                  password=self.base_requests.__password,
                  **self.base_requests.post(path=self.endpoint_path, json=payload)
           )
    def insert_users_group(
                  self,
                  group_title: str,
                  edit_name: Literal["sim", "não"] = None,
                  edit_nickname: Literal["sim", "não"] = None,
                  edit_email: Literal["sim", "não"] = None,
                  change_password: Literal["sim", "não"] = None,
                  select_avatar: Literal["sim", "não"] = None,
                  select_cover: Literal["sim", "não"] = None,
                  upload_photo: Literal["sim", "não"] = None,
                  uplaad_cover: Literal["sim", "não"] = None,
                  default_cover_url: str = None,
                  default_avatar_url: str = None,
                  block_chat: Literal["sim", "não"] = None,
                  all_chat_users: Literal["sim", "não"] = None,
                  chat_group: Literal["sim", "não"] = None,
                  chat_supervisor: Literal["sim", "não"] = None,
                  chat_admin: Literal["sim", "não"] = None,
                  custom_layout: Literal["sim", "não"] = None,
                  dark_logo_url: str = None,
                  light_logo_url: str = None,
                  primary_color_dark: str = None,
                  primary_color_light: str = None,
                  main_page: dict = None,
                  enable_notification_email: Literal["sim", "não"] = None,
    ) -> FutureProcessing:
           payload = [
                  {
                         "titulo_grupo": group_title,
                         "editar_nome": edit_name,
                         "editar_apelido": edit_nickname,
                         "editar_email": edit_email,
                         "trocar_senha": change_password,
                         "upload_capa": uplaad_cover,
                         "selecionar_avatar": select_avatar,
                         "selecionar_capa": select_cover,
                         "upload_foto": upload_photo,
                         "capa_padrao_url": default_cover_url,
                         "avatar_padrao_url": default_avatar_url,
                         "bloquear_chat": block_chat,
                         "chat_todos_usuarios": all_chat_users,
                         "chat_grupo": chat_group,
                         "chat_supervisor": chat_supervisor,
                         "chat_admin": chat_admin,
                         "layout_customizado": custom_layout,
                         "logo_escuro_url": dark_logo_url,
                         "logo_claro_url": light_logo_url,
                         "cor_primaria_escuro": primary_color_dark,
                         "cor_primaria_claro": primary_color_light,
                         "pagina_principal": main_page,
                         "habilitar_notificacao_email": enable_notification_email
                  }
           ]
           return FutureProcessing(
                  username=self.base_requests.__username,
                  password=self.base_requests.__password,
                  **self.base_requests.post(path=self.endpoint_path, json=payload)
           )
    
    def insert_users_avatars(
                  self,
                  avatar_title: str,
                  published: Literal["sim", "não"],
                  url_avatar_image: str
    ) -> FutureProcessing:
           payload = [
                  {
                        "titulo_avatar": avatar_title,
                        "publicado": published,
                        "avatar_url": url_avatar_image
                  }
           ]
           return FutureProcessing(
                  username=self.base_requests.__username,
                  password=self.base_requests.__password,
                  **self.base_requests.post(path=self.endpoint_path, json=payload)
           )
    
    def insert_users_covers(
                  self,
                  cover_title: str,
                  published: Literal["sim", "não"],
                  url_cover_image: str
    ) -> FutureProcessing:
           payload = [
                  {
                        "titulo_capa": cover_title,
                        "publicado": published,
                        "capa_url": url_cover_image
                  }
           ]
           return FutureProcessing(
                  username=self.base_requests.__username,
                  password=self.base_requests.__password,
                  **self.base_requests.post(path=self.endpoint_path, json=payload)
           )
    