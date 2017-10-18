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


class ContainerConfiguration(Model):
    """The configuration for container-enabled pools.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The container technology to be used. Values are:
     docker - Docker will be used to launch the containers. Default value:
     "docker" .
    :vartype type: str
    :param container_image_names: The collection of container image names.
     This is the full image reference, as would be specified to "docker pull".
     An image will be sourced from the default Docker registry unless the image
     is fully qualified with an alternative registry.
    :type container_image_names: list[str]
    :param container_registries: Additional private registries from which
     containers can be pulled. If any images must be downloaded from a private
     registry which requires credentials, then those credentials must be
     provided here.
    :type container_registries: list[~azure.batch.models.ContainerRegistry]
    """

    _validation = {
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'container_image_names': {'key': 'containerImageNames', 'type': '[str]'},
        'container_registries': {'key': 'containerRegistries', 'type': '[ContainerRegistry]'},
    }

    type = "docker"

    def __init__(self, container_image_names=None, container_registries=None):
        self.container_image_names = container_image_names
        self.container_registries = container_registries