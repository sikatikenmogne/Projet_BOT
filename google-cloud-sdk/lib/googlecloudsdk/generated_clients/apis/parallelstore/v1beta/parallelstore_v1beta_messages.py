"""Generated message classes for parallelstore version v1beta.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'parallelstore'


class CancelOperationRequest(_messages.Message):
  r"""The request message for Operations.CancelOperation."""


class DestinationGcsBucket(_messages.Message):
  r"""Google Cloud Storage as a destination.

  Fields:
    uri: Required. URI to a Cloud Storage object in format: 'gs:///'.
  """

  uri = _messages.StringField(1)


class DestinationParallelstore(_messages.Message):
  r"""Parallelstore as a destination.

  Fields:
    path: Optional. Root directory path to the Paralellstore filesystem,
      starting with '/'. Defaults to '/' if unset.
  """

  path = _messages.StringField(1)


class ExportDataRequest(_messages.Message):
  r"""Message representing the request exporting data from Cloud Storage to
  parallelstore.

  Fields:
    destinationGcsBucket: Cloud Storage destination.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and t he request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
    sourceParallelstore: Parallelstore source.
  """

  destinationGcsBucket = _messages.MessageField('DestinationGcsBucket', 1)
  requestId = _messages.StringField(2)
  sourceParallelstore = _messages.MessageField('SourceParallelstore', 3)


class GoogleProtobufEmpty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }
  """



class ImportDataRequest(_messages.Message):
  r"""Message representing the request importing data from parallelstore to
  Cloud Storage.

  Fields:
    destinationParallelstore: Parallelstore destination.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and t he request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
    serviceAccount: Optional. User-specified Service Account (SA) credentials
      to be used when performing the transfer. Format:
      `projects/{project_id}/serviceAccounts/{service_account}` If
      unspecified, the Parallelstore service agent is used: service-@gcp-sa-
      parallelstore.iam.gserviceaccount.com)
    sourceGcsBucket: Cloud Storage source.
  """

  destinationParallelstore = _messages.MessageField('DestinationParallelstore', 1)
  requestId = _messages.StringField(2)
  serviceAccount = _messages.StringField(3)
  sourceGcsBucket = _messages.MessageField('SourceGcsBucket', 4)


class Instance(_messages.Message):
  r"""A Parallelstore instance.

  Enums:
    StateValueValuesEnum: Output only. The instance state.

  Messages:
    LabelsValue: Optional. Cloud Labels are a flexible and lightweight
      mechanism for organizing cloud resources into groups that reflect a
      customer's organizational needs and deployment strategies. Cloud Labels
      can be used to filter collections of resources. They can be used to
      control how resource metrics are aggregated. And they can be used as
      arguments to policy management rules (e.g. route, firewall, load
      balancing, etc.). * Label keys must be between 1 and 63 characters long
      and must conform to the following regular expression: `a-z{0,62}`. *
      Label values must be between 0 and 63 characters long and must conform
      to the regular expression `[a-z0-9_-]{0,63}`. * No more than 64 labels
      can be associated with a given resource. See https://goo.gl/xmQnxf for
      more information on and examples of labels. If you plan to use labels in
      your own code, please note that additional characters may be allowed in
      the future. Therefore, you are advised to use an internal label
      representation, such as JSON, which doesn't rely upon specific
      characters being disallowed. For example, representing labels as the
      string: name + "_" + value would prove problematic if we were to allow
      "_" in a future release.

  Fields:
    accessPoints: Output only. List of access_points. Contains a list of IPv4
      addresses used for client side configuration.
    capacityGib: Required. Immutable. Storage capacity of Parallelstore
      instance in Gibibytes (GiB).
    createTime: Output only. The time when the instance was created.
    daosVersion: Output only. The version of DAOS software running in the
      instance
    description: Optional. The description of the instance. 2048 characters or
      less.
    effectiveReservedIpRange: Output only. Immutable. Contains the id of the
      allocated IP address range associated with the private service access
      connection for example, "test-default" associated with IP range
      10.0.0.0/29. This field is populated by the service and and contains the
      value currently used by the service.
    labels: Optional. Cloud Labels are a flexible and lightweight mechanism
      for organizing cloud resources into groups that reflect a customer's
      organizational needs and deployment strategies. Cloud Labels can be used
      to filter collections of resources. They can be used to control how
      resource metrics are aggregated. And they can be used as arguments to
      policy management rules (e.g. route, firewall, load balancing, etc.). *
      Label keys must be between 1 and 63 characters long and must conform to
      the following regular expression: `a-z{0,62}`. * Label values must be
      between 0 and 63 characters long and must conform to the regular
      expression `[a-z0-9_-]{0,63}`. * No more than 64 labels can be
      associated with a given resource. See https://goo.gl/xmQnxf for more
      information on and examples of labels. If you plan to use labels in your
      own code, please note that additional characters may be allowed in the
      future. Therefore, you are advised to use an internal label
      representation, such as JSON, which doesn't rely upon specific
      characters being disallowed. For example, representing labels as the
      string: name + "_" + value would prove problematic if we were to allow
      "_" in a future release.
    name: Identifier. The resource name of the instance, in the format
      `projects/{project}/locations/{location}/instances/{instance_id}`
    network: Optional. Immutable. The name of the Google Compute Engine [VPC
      network](https://cloud.google.com/vpc/docs/vpc) to which the instance is
      connected.
    reservedIpRange: Optional. Immutable. Contains the id of the allocated IP
      address range associated with the private service access connection for
      example, "test-default" associated with IP range 10.0.0.0/29. If no
      range id is provided all ranges will be considered.
    state: Output only. The instance state.
    updateTime: Output only. The time when the instance was updated.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. The instance state.

    Values:
      STATE_UNSPECIFIED: Not set.
      CREATING: The instance is being created.
      ACTIVE: The instance is available for use.
      DELETING: The instance is being deleted.
      FAILED: The instance is not usable.
    """
    STATE_UNSPECIFIED = 0
    CREATING = 1
    ACTIVE = 2
    DELETING = 3
    FAILED = 4

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Optional. Cloud Labels are a flexible and lightweight mechanism for
    organizing cloud resources into groups that reflect a customer's
    organizational needs and deployment strategies. Cloud Labels can be used
    to filter collections of resources. They can be used to control how
    resource metrics are aggregated. And they can be used as arguments to
    policy management rules (e.g. route, firewall, load balancing, etc.). *
    Label keys must be between 1 and 63 characters long and must conform to
    the following regular expression: `a-z{0,62}`. * Label values must be
    between 0 and 63 characters long and must conform to the regular
    expression `[a-z0-9_-]{0,63}`. * No more than 64 labels can be associated
    with a given resource. See https://goo.gl/xmQnxf for more information on
    and examples of labels. If you plan to use labels in your own code, please
    note that additional characters may be allowed in the future. Therefore,
    you are advised to use an internal label representation, such as JSON,
    which doesn't rely upon specific characters being disallowed. For example,
    representing labels as the string: name + "_" + value would prove
    problematic if we were to allow "_" in a future release.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  accessPoints = _messages.StringField(1, repeated=True)
  capacityGib = _messages.IntegerField(2)
  createTime = _messages.StringField(3)
  daosVersion = _messages.StringField(4)
  description = _messages.StringField(5)
  effectiveReservedIpRange = _messages.StringField(6)
  labels = _messages.MessageField('LabelsValue', 7)
  name = _messages.StringField(8)
  network = _messages.StringField(9)
  reservedIpRange = _messages.StringField(10)
  state = _messages.EnumField('StateValueValuesEnum', 11)
  updateTime = _messages.StringField(12)


class ListInstancesResponse(_messages.Message):
  r"""Message for response to listing Instances

  Fields:
    instances: The list of Parallelstore Instances
    nextPageToken: A token identifying a page of results the server should
      return.
    unreachable: Locations that could not be reached.
  """

  instances = _messages.MessageField('Instance', 1, repeated=True)
  nextPageToken = _messages.StringField(2)
  unreachable = _messages.StringField(3, repeated=True)


class ListLocationsResponse(_messages.Message):
  r"""The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class Location(_messages.Message):
  r"""A resource that represents a Google Cloud location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal, successful response of the operation. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal, successful response of the operation. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation. It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata. Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal, successful response of the operation. If the original
    method returns no data on success, such as `Delete`, the response is
    `google.protobuf.Empty`. If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource. For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name. For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OperationMetadata(_messages.Message):
  r"""Represents the metadata of the long-running operation.

  Fields:
    apiVersion: Output only. API version used to start the operation.
    createTime: Output only. The time the operation was created.
    endTime: Output only. The time the operation finished running.
    requestedCancellation: Output only. Identifies whether the user has
      requested cancellation of the operation. Operations that have been
      cancelled successfully have Operation.error value with a
      google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.
    statusMessage: Output only. Human-readable status of the operation, if
      any.
    target: Output only. Server-defined resource path for the target of the
      operation.
    verb: Output only. Name of the verb executed by the operation.
  """

  apiVersion = _messages.StringField(1)
  createTime = _messages.StringField(2)
  endTime = _messages.StringField(3)
  requestedCancellation = _messages.BooleanField(4)
  statusMessage = _messages.StringField(5)
  target = _messages.StringField(6)
  verb = _messages.StringField(7)


class ParallelstoreProjectsLocationsGetRequest(_messages.Message):
  r"""A ParallelstoreProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class ParallelstoreProjectsLocationsInstancesCreateRequest(_messages.Message):
  r"""A ParallelstoreProjectsLocationsInstancesCreateRequest object.

  Fields:
    instance: A Instance resource to be passed as the request body.
    instanceId: Required. The logical name of the Parallelstore instance in
      the user project with the following restrictions: * Must contain only
      lowercase letters, numbers, and hyphens. * Must start with a letter. *
      Must be between 1-63 characters. * Must end with a number or a letter. *
      Must be unique within the customer project / location
    parent: Required. The instance's project and location, in the format
      `projects/{project}/locations/{location}`. Locations map to Google Cloud
      zones, for example **us-west1-b**.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and t he request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
  """

  instance = _messages.MessageField('Instance', 1)
  instanceId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)
  requestId = _messages.StringField(4)


class ParallelstoreProjectsLocationsInstancesDeleteRequest(_messages.Message):
  r"""A ParallelstoreProjectsLocationsInstancesDeleteRequest object.

  Fields:
    name: Required. Name of the resource
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes after the first
      request. For example, consider a situation where you make an initial
      request and t he request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
  """

  name = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)


class ParallelstoreProjectsLocationsInstancesExportDataRequest(_messages.Message):
  r"""A ParallelstoreProjectsLocationsInstancesExportDataRequest object.

  Fields:
    exportDataRequest: A ExportDataRequest resource to be passed as the
      request body.
    name: Required. Name of the resource.
  """

  exportDataRequest = _messages.MessageField('ExportDataRequest', 1)
  name = _messages.StringField(2, required=True)


class ParallelstoreProjectsLocationsInstancesGetRequest(_messages.Message):
  r"""A ParallelstoreProjectsLocationsInstancesGetRequest object.

  Fields:
    name: Required. The instance resource name, in the format
      `projects/{project_id}/locations/{location}/instances/{instance_id}`.
  """

  name = _messages.StringField(1, required=True)


class ParallelstoreProjectsLocationsInstancesImportDataRequest(_messages.Message):
  r"""A ParallelstoreProjectsLocationsInstancesImportDataRequest object.

  Fields:
    importDataRequest: A ImportDataRequest resource to be passed as the
      request body.
    name: Required. Name of the resource.
  """

  importDataRequest = _messages.MessageField('ImportDataRequest', 1)
  name = _messages.StringField(2, required=True)


class ParallelstoreProjectsLocationsInstancesListRequest(_messages.Message):
  r"""A ParallelstoreProjectsLocationsInstancesListRequest object.

  Fields:
    filter: Optional. Filtering results
    orderBy: Optional. Hint for how to order the results
    pageSize: Optional. Requested page size. Server may return fewer items
      than requested. If unspecified, server will pick an appropriate default.
    pageToken: Optional. A token identifying a page of results the server
      should return.
    parent: Required. The project and location for which to retrieve instance
      information, in the format `projects/{project_id}/locations/{location}`.
      For Parallelstore locations map to Google Cloud zones, for example **us-
      central1-a**. To retrieve instance information for all locations, use
      "-" for the `{location}` value.
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)


class ParallelstoreProjectsLocationsInstancesPatchRequest(_messages.Message):
  r"""A ParallelstoreProjectsLocationsInstancesPatchRequest object.

  Fields:
    instance: A Instance resource to be passed as the request body.
    name: Identifier. The resource name of the instance, in the format
      `projects/{project}/locations/{location}/instances/{instance_id}`
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and t he request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
    updateMask: Required. Mask of fields to update .Field mask is used to
      specify the fields to be overwritten in the Instance resource by the
      update. At least one path must be supplied in this field. The fields
      specified in the update_mask are relative to the resource, not the full
      request.
  """

  instance = _messages.MessageField('Instance', 1)
  name = _messages.StringField(2, required=True)
  requestId = _messages.StringField(3)
  updateMask = _messages.StringField(4)


class ParallelstoreProjectsLocationsListRequest(_messages.Message):
  r"""A ParallelstoreProjectsLocationsListRequest object.

  Fields:
    filter: A filter to narrow down results to a preferred subset. The
      filtering language accepts strings like `"displayName=tokyo"`, and is
      documented in more detail in [AIP-160](https://google.aip.dev/160).
    name: The resource that owns the locations collection, if applicable.
    pageSize: The maximum number of results to return. If not set, the service
      selects a default.
    pageToken: A page token received from the `next_page_token` field in the
      response. Send that page token to receive the subsequent page.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class ParallelstoreProjectsLocationsOperationsCancelRequest(_messages.Message):
  r"""A ParallelstoreProjectsLocationsOperationsCancelRequest object.

  Fields:
    cancelOperationRequest: A CancelOperationRequest resource to be passed as
      the request body.
    name: The name of the operation resource to be cancelled.
  """

  cancelOperationRequest = _messages.MessageField('CancelOperationRequest', 1)
  name = _messages.StringField(2, required=True)


class ParallelstoreProjectsLocationsOperationsDeleteRequest(_messages.Message):
  r"""A ParallelstoreProjectsLocationsOperationsDeleteRequest object.

  Fields:
    name: The name of the operation resource to be deleted.
  """

  name = _messages.StringField(1, required=True)


class ParallelstoreProjectsLocationsOperationsGetRequest(_messages.Message):
  r"""A ParallelstoreProjectsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class ParallelstoreProjectsLocationsOperationsListRequest(_messages.Message):
  r"""A ParallelstoreProjectsLocationsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class SourceGcsBucket(_messages.Message):
  r"""Google Cloud Storage as a source.

  Fields:
    uri: Required. URI to a Cloud Storage object in format: 'gs:///'.
  """

  uri = _messages.StringField(1)


class SourceParallelstore(_messages.Message):
  r"""Pa as a source.

  Fields:
    path: Optional. Root directory path to the Paralellstore filesystem,
      starting with '/'. Defaults to '/' if unset.
  """

  path = _messages.StringField(1)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details. You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details. There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
