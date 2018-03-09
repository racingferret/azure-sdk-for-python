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


class PerformanceTierServiceLevelObjectives(Model):
    """Service level objectives for performance tier.

    :param id: ID for the service level objective.
    :type id: str
    :param edition: Edition of the performance tier.
    :type edition: str
    :param v_core: vCore associated with the service level objective
    :type v_core: int
    :param hardware_generation: Hardware generation associated with the
     service level objective
    :type hardware_generation: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'edition': {'key': 'edition', 'type': 'str'},
        'v_core': {'key': 'vCore', 'type': 'int'},
        'hardware_generation': {'key': 'hardwareGeneration', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, edition: str=None, v_core: int=None, hardware_generation: str=None, **kwargs) -> None:
        super(PerformanceTierServiceLevelObjectives, self).__init__(**kwargs)
        self.id = id
        self.edition = edition
        self.v_core = v_core
        self.hardware_generation = hardware_generation
