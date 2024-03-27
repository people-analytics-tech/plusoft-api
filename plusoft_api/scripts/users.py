from typing import Literal

from typing_extensions import override

from plusoft_api.helpers.api_endpoint import BaseApiEndpoint, BasicAuth, ImportEndpoint
from plusoft_api.models.users import (
    FileMetadata,
    Language,
    UserAccessHistoricModel,
    UserAvatarModel,
    UserCoverModel,
    UserGroupModel,
    UserModel,
)
from plusoft_api.scripts.payloads import BaseImportsPayload
from plusoft_api.utils.aux_types import GroupsOptions


class InsertUsersFactory(BaseImportsPayload):
    def __init__(self, endpoint: BaseApiEndpoint) -> None:
        super().__init__(endpoint=endpoint, path="", payload_factory=UserModel)

    @override
    def add_to_payload(
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
        photo: FileMetadata = None,
        language: Language = None,
        active: Literal["sim", "nao"] = None,
        cover: FileMetadata = None,
        terms: Literal["sim", "nao"] = None,
        groups: list[str] = None,
        groups_option: GroupsOptions = None,
        new_login: str = None,
        extra_fields: dict = None,
        primary_key: str = "login",
    ) -> "InsertUsersFactory":
        """Add user to staged payload before upload.

        Parameters:
            login (str, Mandatory): User login. This is the primary key of user.
            name (str, Mandatory): Name of user.
            email (str, Mandatory): Email of user.
            password (str, Optional): Password of user.
            nickname (str, Optional): Nickname of user.
            biography (str, Optional): Biography of user.
            telephone (str, Optional): Telephone number of user.
            team (str, Optional): Team name of user.
            position (str, Optional): Position name of user.
            login_manager (str, Optional): Login of manager. Same defined in manager user record.
            name_manager (str, Optional): Name of manager.
            position_manager (str, Optional): Position of manager.
            photo (FileMetadata, Optional): Photo file. Import the FileMetadata object to send in this field.
            language (Language, Optional): Language to user. Import the Language object to send in this field.
            active (Literal["sim", "nao"], Optional): This define if the user is active on the system.
            cover (FileMetadata, Optional): Cover image. Import the FileMetadata object to send in this field.
            terms (Literal["sim", "nao"], Optional): Terms accepted.
            groups (list[str], , Optional): Groups of user. Use the group primary key to send in this list.
            groups_option (GroupsOptions, Optional): Action to execute with groups list. Send 1 to only add the groups to user, 2 to overwrite user groups, 3 to remove groups of user, 4 to remove all groups of user.
            new_login (str, Optional): New login information to update in system.
            extra_fields (dict, Optional): Extra fields values to send in requisition. Format: {"extra_field_name": "value"}
            primary_key (str, Optional): If you want to verify if a user already exist in staged payload, use this parameter to pass what the field you want to verify. Default = "login"
        """
        defult_payload = {
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
        super().add_to_payload(
            **defult_payload, custom_fields=extra_fields, primary_key=primary_key
        )
        return self


class InsertUsersAccessHistoricFactory(BaseImportsPayload):
    def __init__(self, endpoint: BaseApiEndpoint) -> None:
        super().__init__(
            endpoint=endpoint, path="/access", payload_factory=UserAccessHistoricModel
        )

    @override
    def add_to_payload(
        self,
        login: str,
        login_data: str,
        remote_ip: str = None,
        operational_system: str = None,
        browser: str = None,
        browser_version: str = None,
        logout_data: str = None,
    ) -> "InsertUsersAccessHistoricFactory":
        payload = {
            "login": login,
            "data_login": login_data,
            "ip_remoto": remote_ip,
            "sistema_operacional": operational_system,
            "navegador": browser,
            "versao_navegador": browser_version,
            "data_logout": logout_data,
        }
        self._payload.add_to_payload(**payload)
        return self


class InsertUsersGroupsFactory(BaseImportsPayload):
    def __init__(self, endpoint: BaseApiEndpoint) -> None:
        super().__init__(
            endpoint=endpoint, path="/groups", payload_factory=UserGroupModel
        )

    @override
    def add_to_payload(
        self,
        group_title: str,
        edit_name: Literal["sim", "nao"] = None,
        edit_nickname: Literal["sim", "nao"] = None,
        edit_email: Literal["sim", "nao"] = None,
        change_password: Literal["sim", "nao"] = None,
        select_avatar: Literal["sim", "nao"] = None,
        select_cover: Literal["sim", "nao"] = None,
        upload_photo: Literal["sim", "nao"] = None,
        uplaad_cover: Literal["sim", "nao"] = None,
        default_cover_url: str = None,
        default_avatar_url: str = None,
        block_chat: Literal["sim", "nao"] = None,
        all_chat_users: Literal["sim", "nao"] = None,
        chat_group: Literal["sim", "nao"] = None,
        chat_supervisor: Literal["sim", "nao"] = None,
        chat_admin: Literal["sim", "nao"] = None,
        custom_layout: Literal["sim", "nao"] = None,
        dark_logo_url: str = None,
        light_logo_url: str = None,
        primary_color_dark: str = None,
        primary_color_light: str = None,
        main_page: dict = None,
        enable_notification_email: Literal["sim", "nao"] = None,
    ) -> "InsertUsersGroupsFactory":
        payload = {
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
        self._payload.add_to_payload(**payload)
        return self


class InsertUsersAvatarsFactory(BaseImportsPayload):
    def __init__(self, endpoint: BaseApiEndpoint) -> None:
        super().__init__(
            endpoint=endpoint, path="/avatares", payload_factory=UserAvatarModel
        )

    @override
    def add_to_payload(
        self, avatar_title: str, published: Literal["sim", "nao"], url_avatar_image: str
    ) -> "InsertUsersAvatarsFactory":
        payload = {
            "titulo_avatar": avatar_title,
            "publicado": published,
            "avatar_url": url_avatar_image,
        }
        self._payload.add_to_payload(**payload)
        return self


class InsertUsersCoversFactory(BaseImportsPayload):
    def __init__(self, endpoint: BaseApiEndpoint) -> None:
        super().__init__(
            endpoint=endpoint, path="/avatares", payload_factory=UserCoverModel
        )

    @override
    def add_to_payload(
        self, cover_title: str, published: Literal["sim", "nao"], url_cover_image: str
    ) -> "InsertUsersCoversFactory":
        payload = {
            "titulo_capa": cover_title,
            "publicado": published,
            "capa_url": url_cover_image,
        }
        self._payload.add_to_payload(**payload)
        return self


class Users(ImportEndpoint):
    def __init__(
        self,
        basic_auth: BasicAuth,
        domain: str,
    ):
        super().__init__(
            basic_auth=basic_auth,
            endpoint_path="/users",
            domain=domain,
        )

        self.__insert_users: InsertUsersFactory = None
        self.__insert_user_access_historic: InsertUsersAccessHistoricFactory = None
        self.__insert_users_group: InsertUsersGroupsFactory = None
        self.__insert_users_avatars: InsertUsersAvatarsFactory = None
        self.__insert_users_covers: InsertUsersCoversFactory = None

    def consult_user(self, login: str) -> dict:
        payload = {"login": login}
        return ImportEndpoint(
            basic_auth=self._basic_auth, domain=self.domain
        ).base_requests.post(path="/consult/user", json=payload)

    @property
    def insert_users(self) -> InsertUsersFactory:
        if not self.__insert_users:
            self.__insert_users = InsertUsersFactory(endpoint=self)

        return self.__insert_users

    @property
    def insert_user_access_historic(self) -> InsertUsersAccessHistoricFactory:
        if not self.__insert_user_access_historic:
            self.__insert_user_access_historic = InsertUsersAccessHistoricFactory(
                endpoint=self
            )

        return self.__insert_user_access_historic

    @property
    def insert_users_group(self) -> InsertUsersGroupsFactory:
        if not self.__insert_users_group:
            self.__insert_users_group = InsertUsersGroupsFactory(self)

        return self.__insert_users_group

    @property
    def insert_users_avatars(self) -> InsertUsersAvatarsFactory:
        if not self.__insert_users_avatars:
            self.__insert_users_avatars = InsertUsersAvatarsFactory(self)

        return self.__insert_users_avatars

    @property
    def insert_users_covers(self) -> InsertUsersCoversFactory:
        if not self.__insert_users_covers:
            self.__insert_users_covers = InsertUsersCoversFactory(self)

        return self.__insert_users_covers
