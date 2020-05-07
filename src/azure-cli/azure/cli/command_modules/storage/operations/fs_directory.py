# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""Custom operations for storage file datalake"""

import os

from azure.core.exceptions import HttpResponseError
from azure.cli.core.profiles import ResourceType


def exists(cmd, client):
    try:
        client.get_directory_properties()
        return True
    except HttpResponseError as ex:
        from azure.cli.command_modules.storage.sdkutil import _dont_fail_on_exist
        StorageErrorCode = cmd.get_models("_shared.models#StorageErrorCode",
                                          resource_type=ResourceType.DATA_STORAGE_FILEDATALAKE)
        _dont_fail_on_exist(ex, StorageErrorCode.blob_not_found)
        return False


def list_fs_directories(client, path=None, recursive=True, num_results=None, timeout=None):
    generator = client.get_paths(path=path, recursive=recursive, timeout=timeout, max_results=num_results)

    return list(f for f in generator if f.is_directory)


def get_directory_properties(client):
    from knack.util import todict
    from .._transformers import transform_fs_access_output
    prop = todict(client.get_directory_properties())
    acl = transform_fs_access_output(client.get_access_control())
    result = dict(prop, **acl)
    return result
