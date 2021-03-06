# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def network_client_factory(cli_ctx, **kwargs):
    from .profiles import CUSTOM_IP_GROUPS
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    return get_mgmt_service_client(cli_ctx, CUSTOM_IP_GROUPS, **kwargs)


def cf_ip_groups(cli_ctx, _):
    return network_client_factory(cli_ctx).ip_groups
