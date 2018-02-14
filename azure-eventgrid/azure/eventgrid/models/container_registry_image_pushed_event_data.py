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

from .container_registry_event_data import ContainerRegistryEventData


class ContainerRegistryImagePushedEventData(ContainerRegistryEventData):
    """Schema of the Data property of an EventGridEvent for a
    Microsoft.ContainerRegistry.ImagePushed event.

    :param id: The event ID.
    :type id: str
    :param timestamp: The time at which the event occurred.
    :type timestamp: datetime
    :param action: The action that encompasses the provided event.
    :type action: str
    :param target: The target of the event.
    :type target: ~azure.eventgrid.models.ContainerRegistryEventTarget
    :param request: The request that generated the event.
    :type request: ~azure.eventgrid.models.ContainerRegistryEventRequest
    :param actor: The agent that initiated the event. For most situations,
     this could be from the authorization context of the request.
    :type actor: ~azure.eventgrid.models.ContainerRegistryEventActor
    :param source: The registry node that generated the event. Put
     differently, while the actor initiates the event, the source generates it.
    :type source: ~azure.eventgrid.models.ContainerRegistryEventSource
    """

    def __init__(self, id=None, timestamp=None, action=None, target=None, request=None, actor=None, source=None):
        super(ContainerRegistryImagePushedEventData, self).__init__(id=id, timestamp=timestamp, action=action, target=target, request=request, actor=actor, source=source)
