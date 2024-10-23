import httpx

from typing import Literal
from pydantic import TypeAdapter

from ipsw_me_client.ipsw_models.errors import NotFoundError, APIServerError
from ipsw_me_client.ipsw_models.responses.devices import GetFirmwaresForDeviceResponse, GetDeviceResponse


class HTTPClient:
    def __init__(
            self,
            base_url='https://api.ipsw.me/v4'
    ):
        self._common_headers = {
            'Accept': 'application/json'
        }

        self._http_client_kwargs = {
            'base_url': base_url,
            'headers': self._common_headers
        }

    async def get_firmwares_for_device(
            self,
            identifier: str,
            firmware_type: Literal['ipsw', 'ota'] = 'ipsw'
    ) -> GetFirmwaresForDeviceResponse:
        async with httpx.AsyncClient(**self._http_client_kwargs) as http_client:
            resp = await http_client.get(
                f'/device/{identifier}?type={firmware_type}'
            )

            self.handle_http_status(resp.status_code)

            if resp.status_code == 404:
                raise NotFoundError(f'device firmwares for identifier "{identifier}"')

            return GetFirmwaresForDeviceResponse.model_validate(resp.json())

    async def get_devices(
            self,
            keys_only: bool = False
    ) -> list[GetDeviceResponse]:
        async with httpx.AsyncClient(**self._http_client_kwargs) as http_client:
            resp = await http_client.get(
                '/devices',
                params={'keys_only': keys_only}
            )

            self.handle_http_status(resp.status_code)

            return TypeAdapter(list[GetDeviceResponse]).validate_python(resp.json())

    @staticmethod
    def handle_http_status(http_status: int):
        if 500 < http_status <= 599:
            raise APIServerError(http_status)
