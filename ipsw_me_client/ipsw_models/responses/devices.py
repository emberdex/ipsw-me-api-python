from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, Field, AliasChoices


class DeviceFirmware(BaseModel):
    identifier: str
    version: str

    build_id: Annotated[
        str,
        Field(
            validation_alias=AliasChoices('buildid')
        )
    ]

    sha1sum: str
    md5sum: str
    sha256sum: str

    file_size: Annotated[
        int,
        Field(
            validation_alias=AliasChoices('filesize')
        )
    ]

    url: str

    release_date: Annotated[
        datetime,
        Field(
            validation_alias=AliasChoices('releasedate')
        )
    ]

    upload_date: Annotated[
        datetime,
        Field(
            validation_alias=AliasChoices('uploaddate')
        )
    ]

    signed: bool


class DeviceBoard(BaseModel):
    board_config: Annotated[
        str,
        Field(
            validation_alias=AliasChoices('boardconfig')
        )
    ]

    platform: str
    cpid: int
    bdid: int


class DeviceCommonInfo(BaseModel):
    name: str
    identifier: str
    platform: str
    cpid: int
    bdid: int

    board_config: Annotated[
        str,
        Field(
            validation_alias=AliasChoices('boardconfig')
        )
    ]

class GetFirmwaresForDeviceResponse(DeviceCommonInfo):
    firmwares: list[DeviceFirmware]


class GetDeviceResponse(DeviceCommonInfo):
    boards: list[DeviceBoard]
