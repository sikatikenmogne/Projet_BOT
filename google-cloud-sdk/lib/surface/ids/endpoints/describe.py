# -*- coding: utf-8 -*- #
# Copyright 2021 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""'ids endpoints describe' command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base
from googlecloudsdk.api_lib.ids import ids_api
from googlecloudsdk.command_lib.ids import flags

DETAILED_HELP = {
    'DESCRIPTION':
        """
          Describe a Cloud IDS endpoint.
        """,
    'EXAMPLES':
        """
          To get a description of a endpoint called `my-ep` in
          project `my-project` and zone `us-central1-a`, run:

          $ {command} my-ep --project=my-project --zone=us-central1-a

          OR

          $ {command} projects/myproject/locations/us-central1-a/endpoints/my-ep
    """,
}


@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA,
                    base.ReleaseTrack.GA)
class Describe(base.DescribeCommand):
  """Describe a Cloud IDS endpoint."""

  @staticmethod
  def Args(parser):
    flags.AddEndpointResource(parser)

  def Run(self, args):
    endpoint = args.CONCEPTS.endpoint.Parse()

    client = ids_api.Client(self.ReleaseTrack())
    return client.DescribeEndpoint(endpoint.RelativeName())


Describe.detailed_help = DETAILED_HELP
