from decouple import config

from plusoft_api.helpers.api_endpoint import ApiEndpoint
from plusoft_api.scripts.consult import FutureProcessing
from plusoft_api.utils.aux_types import GroupsOptions, YesNo


class Users(ApiEndpoint):
    def __init__(
        self,
        username: str = config("PLUSOFT_USERNAME", default=None),
        password: str = config("PLUSOFT_PASSWORD", default=None),
        domain: str = config("PLUSOFT_ENVIRONMENT_DOMAIN", default=None),
    ):
        super().__init__(
            username=username,
            password=password,
            endpoint_path="/import/users",
            domain=domain,
        )

    def consult_user(self, login: str) -> dict:
        payload = {"login": login}
        return self.base_requests.post(path="/import/consult/user", json=payload)

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
        active: YesNo = None,
        cover: dict = None,
        terms: YesNo = None,
        groups: list[str] = None,
        groups_option: GroupsOptions = None,
        new_login: str = None,
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
                "novo_login": new_login,
            }
        ]
        return FutureProcessing(
            username=self.base_requests.username,
            password=self.base_requests.password,
            **self.base_requests.post(path=self.endpoint_path, json=payload)
        )

    def historic_user_access(
        self,
        login: str,
        login_data: str,
        remote_ip: str = None,
        operational_system: str = None,
        browser: str = None,
        browser_version: str = None,
        logout_data: str = None,
    ) -> FutureProcessing:
        self.endpoint_path = "/import/users/access"
        payload = [
            {
                "login": login,
                "data_login": login_data,
                "ip_remoto": remote_ip,
                "sistema_operacional": operational_system,
                "navegador": browser,
                "versao_navegador": browser_version,
                "data_logout": logout_data,
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
        edit_name: YesNo = None,
        edit_nickname: YesNo = None,
        edit_email: YesNo = None,
        change_password: YesNo = None,
        select_avatar: YesNo = None,
        select_cover: YesNo = None,
        upload_photo: YesNo = None,
        uplaad_cover: YesNo = None,
        default_cover_url: str = None,
        default_avatar_url: str = None,
        block_chat: YesNo = None,
        all_chat_users: YesNo = None,
        chat_group: YesNo = None,
        chat_supervisor: YesNo = None,
        chat_admin: YesNo = None,
        custom_layout: YesNo = None,
        dark_logo_url: str = None,
        light_logo_url: str = None,
        primary_color_dark: str = None,
        primary_color_light: str = None,
        main_page: dict = None,
        enable_notification_email: YesNo = None,
    ) -> FutureProcessing:
        self.endpoint_path = "/import/users/groups"
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
                "habilitar_notificacao_email": enable_notification_email,
            }
        ]
        return FutureProcessing(
            username=self.base_requests.__username,
            password=self.base_requests.__password,
            **self.base_requests.post(path=self.endpoint_path, json=payload)
        )

    def insert_users_avatars(
        self, avatar_title: str, published: YesNo, url_avatar_image: str
    ) -> FutureProcessing:
        self.endpoint_path = "/import/users/avatares"
        payload = [
            {
                "titulo_avatar": avatar_title,
                "publicado": published,
                "avatar_url": url_avatar_image,
            }
        ]
        return FutureProcessing(
            username=self.base_requests.__username,
            password=self.base_requests.__password,
            **self.base_requests.post(path=self.endpoint_path, json=payload)
        )

    def insert_users_covers(
        self, cover_title: str, published: YesNo, url_cover_image: str
    ) -> FutureProcessing:
        self.endpoint_path = "/import/users/capas"
        payload = [
            {
                "titulo_capa": cover_title,
                "publicado": published,
                "capa_url": url_cover_image,
            }
        ]
        return FutureProcessing(
            username=self.base_requests.__username,
            password=self.base_requests.__password,
            **self.base_requests.post(path=self.endpoint_path, json=payload)
        )
