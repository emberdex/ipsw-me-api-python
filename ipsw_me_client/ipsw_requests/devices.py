from typing import Literal
from ipsw_me_client.ipsw_http import HTTPClient
from ipsw_me_client.ipsw_models.responses.devices import GetFirmwaresForDeviceResponse, GetDeviceResponse

http_client = HTTPClient()


async def get_firmwares_for_device(
        identifier: str,
        firmware_type: Literal['ipsw', 'ota'] = 'ipsw'
) -> GetFirmwaresForDeviceResponse:
    """
    Get a list of firmwares for a given Device Identifier.

    The device identifier can be a model identifier, e.g. iPhone8,1, or a board identifier, e.g. N71AP.
    It is recommended to search by the board identifier, as the same device can have multiple boards.

    :param identifier: The Device Identifier to fetch firmwares for.
    :param firmware_type: The type of firmwares to search for ('ipsw' or 'ota'). If not specified, defaults to 'ipsw'.
    :return: A list of firmwares for the given device.
    """
    return await http_client.get_firmwares_for_device(identifier, firmware_type)


async def get_devices(keys_only: bool = False) -> list[GetDeviceResponse]:
    """
    Get a list of all known devices.
    :param keys_only: Filter results to devices which have firmware keys.
    :return: A list of devices.
    """
    return await http_client.get_devices(keys_only=keys_only)
