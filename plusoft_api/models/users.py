from datetime import date
from typing import Literal, Union

from typing_extensions import override

from plusoft_api.models.aux import PayloadDataClass, dataclass
from plusoft_api.utils.aux_types import GroupsOptions, YesNoEnum


@dataclass
class FileMetadata:
    name: str
    contentType: str
    b64: str


@dataclass
class Language:
    language: str
    idioma: str
    languem: str


@dataclass
class UserModel(PayloadDataClass):
    login: str
    nome: str
    email: str
    senha: str = None
    apelido: str = None
    biografia: str = None
    telefone: str = None
    time: str = None
    cargo: str = None
    login_supervisor: str = None
    nome_supervisor: str = None
    cargo_supervisor: str = None
    foto: FileMetadata = None
    linguagem: Language = None
    ativo: Literal["sim", "nao"] = None
    capa: FileMetadata = (None,)
    termos: Literal["sim", "nao"] = None
    grupos: list[str] = None
    grupos_opcao: GroupsOptions = None
    novo_login: str = None
    custom_fields: dict = None

    def __formated_custom_fields(self) -> Union[dict, None]:
        formated = {}
        if self.custom_fields:
            for key, value in self.custom_fields.items():
                if isinstance(value, date):
                    formated[key] = value.strftime("%Y-%m-%d")

                else:
                    formated[key] = value

            return formated

        else:
            return None

    @override
    @property
    def as_dict(self) -> dict:
        payload = super().as_dict
        payload.pop("custom_fields")
        custom_fields = self.__formated_custom_fields()
        if not custom_fields:
            custom_fields = {}

        return dict(**payload, **custom_fields)


class UserAccessHistoricModel(PayloadDataClass):
    login: str
    ip_remoto: str = None
    sistema_operacional: str = None
    navegador: str = None
    versao_navegador: str = None
    data_login: str
    data_logout: str = None


class UserGroupModel(PayloadDataClass):
    titulo_grupo: str
    editar_nome: YesNoEnum = None
    editar_apelido: YesNoEnum = None
    editar_email: YesNoEnum = None
    trocar_senha: YesNoEnum = None
    selecionar_avatar: YesNoEnum = None
    selecionar_capa: YesNoEnum = None
    upload_foto: YesNoEnum = None
    upload_capa: YesNoEnum = None
    capa_padrao_url: str = None
    avatar_padrao_url: str = None
    bloquear_chat: YesNoEnum = None
    chat_todos_usuarios: YesNoEnum = None
    chat_grupo: YesNoEnum = None
    chat_supervisor: YesNoEnum = None
    chat_admin: YesNoEnum = None
    layout_customizado: YesNoEnum = None
    logo_escuro_url: str = None
    logo_claro_url: str = None
    cor_primaria_escuro: str = None
    cor_primaria_claro: str = None
    pagina_principal: str = None
    habilitar_notificacao_email: YesNoEnum = None


class UserAvatarModel(PayloadDataClass):
    titulo_avatar: str
    publicado: YesNoEnum
    avatar_url: str


class UserCoverModel(PayloadDataClass):
    titulo_capa: str
    publicado: YesNoEnum
    capa_url: str
