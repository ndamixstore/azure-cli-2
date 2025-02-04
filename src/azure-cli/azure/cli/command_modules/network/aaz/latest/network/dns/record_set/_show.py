# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class Show(AAZCommand):
    """Get a record set.
    """

    _aaz_info = {
        "version": "2018-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/dnszones/{}/{}/{}", "2018-05-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.record_type = AAZStrArg(
            options=["--record-type"],
            help="The type of DNS record in this record set.",
            required=True,
            id_part="child_type_1",
            enum={"A": "A", "AAAA": "AAAA", "CAA": "CAA", "CNAME": "CNAME", "MX": "MX", "NS": "NS", "PTR": "PTR", "SOA": "SOA", "SRV": "SRV", "TXT": "TXT"},
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the record set, relative to the name of the zone.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.zone_name = AAZStrArg(
            options=["-z", "--zone-name"],
            help="Name of the DNS zone.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.RecordSetsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class RecordSetsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "recordType", self.ctx.args.record_type,
                    required=True,
                ),
                **self.serialize_url_param(
                    "relativeRecordSetName", self.ctx.args.name,
                    skip_quote=True,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "zoneName", self.ctx.args.zone_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2018-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType()
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.aaaa_records = AAZListType(
                serialized_name="AAAARecords",
            )
            properties.a_records = AAZListType(
                serialized_name="ARecords",
            )
            properties.cname_record = AAZObjectType(
                serialized_name="CNAMERecord",
            )
            properties.mx_records = AAZListType(
                serialized_name="MXRecords",
            )
            properties.ns_records = AAZListType(
                serialized_name="NSRecords",
            )
            properties.ptr_records = AAZListType(
                serialized_name="PTRRecords",
            )
            properties.soa_record = AAZObjectType(
                serialized_name="SOARecord",
            )
            properties.srv_records = AAZListType(
                serialized_name="SRVRecords",
            )
            properties.ttl = AAZIntType(
                serialized_name="TTL",
            )
            properties.txt_records = AAZListType(
                serialized_name="TXTRecords",
            )
            properties.caa_records = AAZListType(
                serialized_name="caaRecords",
            )
            properties.fqdn = AAZStrType(
                flags={"read_only": True},
            )
            properties.metadata = AAZDictType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.target_resource = AAZObjectType(
                serialized_name="targetResource",
            )

            aaaa_records = cls._schema_on_200.properties.aaaa_records
            aaaa_records.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.aaaa_records.Element
            _element.ipv6_address = AAZStrType(
                serialized_name="ipv6Address",
            )

            a_records = cls._schema_on_200.properties.a_records
            a_records.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.a_records.Element
            _element.ipv4_address = AAZStrType(
                serialized_name="ipv4Address",
            )

            cname_record = cls._schema_on_200.properties.cname_record
            cname_record.cname = AAZStrType()

            mx_records = cls._schema_on_200.properties.mx_records
            mx_records.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.mx_records.Element
            _element.exchange = AAZStrType()
            _element.preference = AAZIntType()

            ns_records = cls._schema_on_200.properties.ns_records
            ns_records.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.ns_records.Element
            _element.nsdname = AAZStrType()

            ptr_records = cls._schema_on_200.properties.ptr_records
            ptr_records.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.ptr_records.Element
            _element.ptrdname = AAZStrType()

            soa_record = cls._schema_on_200.properties.soa_record
            soa_record.email = AAZStrType()
            soa_record.expire_time = AAZIntType(
                serialized_name="expireTime",
            )
            soa_record.host = AAZStrType()
            soa_record.minimum_ttl = AAZIntType(
                serialized_name="minimumTTL",
            )
            soa_record.refresh_time = AAZIntType(
                serialized_name="refreshTime",
            )
            soa_record.retry_time = AAZIntType(
                serialized_name="retryTime",
            )
            soa_record.serial_number = AAZIntType(
                serialized_name="serialNumber",
            )

            srv_records = cls._schema_on_200.properties.srv_records
            srv_records.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.srv_records.Element
            _element.port = AAZIntType()
            _element.priority = AAZIntType()
            _element.target = AAZStrType()
            _element.weight = AAZIntType()

            txt_records = cls._schema_on_200.properties.txt_records
            txt_records.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.txt_records.Element
            _element.value = AAZListType()

            value = cls._schema_on_200.properties.txt_records.Element.value
            value.Element = AAZStrType()

            caa_records = cls._schema_on_200.properties.caa_records
            caa_records.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.caa_records.Element
            _element.flags = AAZIntType()
            _element.tag = AAZStrType()
            _element.value = AAZStrType()

            metadata = cls._schema_on_200.properties.metadata
            metadata.Element = AAZStrType()

            target_resource = cls._schema_on_200.properties.target_resource
            target_resource.id = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
