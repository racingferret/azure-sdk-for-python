# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineScaleSetSkuCapacity(Model):
    """Describes scaling information of a sku.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar minimum: The minimum capacity.
    :vartype minimum: long
    :ivar maximum: The maximum capacity that can be set.
    :vartype maximum: long
    :ivar default_capacity: The default capacity.
    :vartype default_capacity: long
    :ivar scale_type: The scale type applicable to the sku. Possible values
     include: 'Automatic', 'None'
    :vartype scale_type: str or
     ~azure.mgmt.compute.v2017_03_30.models.VirtualMachineScaleSetSkuScaleType
    """

    _validation = {
        'minimum': {'readonly': True},
        'maximum': {'readonly': True},
        'default_capacity': {'readonly': True},
        'scale_type': {'readonly': True},
    }

    _attribute_map = {
        'minimum': {'key': 'minimum', 'type': 'long'},
        'maximum': {'key': 'maximum', 'type': 'long'},
        'default_capacity': {'key': 'defaultCapacity', 'type': 'long'},
        'scale_type': {'key': 'scaleType', 'type': 'VirtualMachineScaleSetSkuScaleType'},
    }

    def __init__(self):
        self.minimum = None
        self.maximum = None
        self.default_capacity = None
        self.scale_type = None