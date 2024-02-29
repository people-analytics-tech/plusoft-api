"""This module provide a base to use requests for api"""

import base64
from typing import Any, Literal

import requests

from plusoft_api.utils.aux_functions import remove_none_fields


class BaseRequests:
    """Aux class to communicate with mindsight api"""

    def __init__(self, username: str, password: str, domain: str):
        self.username = username
        self.password = password
        self.headers = None
        self.base_path = f"https://{domain}.edusense.app/api"

    @property
    def basic_authorization_token(self) -> bytes:
        return base64.b64encode(
            f"{self.username}:{self.password}".encode("utf-8")
        ).decode("ascii")

    def __default_header(self) -> dict:
        return {
            "Authorization": f"Basic {self.basic_authorization_token}",
            "Content-Type": "application/json; charset=utf-8",
        }

    def __request_helper(
        self,
        path: str,
        method: Literal["get", "post", "put", "patch", "delete"],
        headers: dict = None,
        parameters: dict = None,
        data: Any = None,
        json: Any = None,
    ):
        if not headers:
            headers = {}

        request_url = f"{self.base_path}{path}"
        self.headers = {**self.__default_header(), **headers}

        response = None
        method = method.lower()

        if method == "get":
            response = requests.get(
                url=request_url,
                headers=self.headers,
                params=parameters,
                data=data,
            )

        elif method == "post":
            response = requests.post(
                url=request_url,
                headers=self.headers,
                params=parameters,
                data=data,
                json=json,
            )

        elif method == "put":
            response = requests.put(
                url=request_url,
                headers=self.headers,
                params=parameters,
                data=data,
                json=json,
            )

        elif method == "patch":
            response = requests.patch(
                url=request_url,
                headers=self.headers,
                params=parameters,
                data=data,
                json=json,
            )

        elif method == "delete":
            response = requests.delete(
                url=request_url,
                headers=self.headers,
                params=parameters,
                data=data,
                json=json,
            )

        # Check response
        response.raise_for_status()
        response_json = response.json()

        return response_json

    def get(
        self,
        path: str,
        headers: dict = None,
        parameters: dict = None,
        json: dict = None,
    ) -> Any:
        """Use GET method on Rest API"""
        return self.__request_helper(
            path=path, method="get", headers=headers, parameters=parameters, json=json
        )

    def post(
        self,
        path: str,
        headers: dict = None,
        parameters: dict = None,
        data: Any = None,
        json: Any = None,
    ) -> Any:
        """Use POST method on Rest API"""
        return self.__request_helper(
            path=path,
            method="post",
            headers=headers,
            parameters=parameters,
            data=data,
            json=json,
        )

    def put(
        self,
        path: str,
        headers: dict = None,
        parameters: dict = None,
        data: Any = None,
        json: Any = None,
    ):
        """Use PUT method on Rest API"""
        return self.__request_helper(
            path=path,
            method="put",
            headers=headers,
            parameters=parameters,
            data=data,
            json=json,
        )

    def patch(
        self,
        path: str,
        headers: dict = None,
        parameters: dict = None,
        data: Any = None,
        json: Any = None,
    ):
        """Use PATCH method on Rest API"""
        return self.__request_helper(
            path=path,
            method="patch",
            headers=headers,
            parameters=parameters,
            data=remove_none_fields(data) if data else None,
            json=remove_none_fields(json) if json else None,
        )

    def delete(
        self,
        path: str,
        headers: dict = None,
        parameters: dict = None,
        data: Any = None,
    ):
        """Use DELETE method on Rest API"""
        return self.__request_helper(
            path=path,
            method="delete",
            headers=headers,
            parameters=parameters,
            data=data,
        )
