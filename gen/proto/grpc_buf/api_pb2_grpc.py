# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto.grpc_buf import api_pb2 as proto_dot_grpc__buf_dot_api__pb2


class ExampleApiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetExample = channel.unary_unary(
                '/grpc_buf.ExampleApi/GetExample',
                request_serializer=proto_dot_grpc__buf_dot_api__pb2.GetExampleRequest.SerializeToString,
                response_deserializer=proto_dot_grpc__buf_dot_api__pb2.GetExampleResponse.FromString,
                )
        self.CreateExample = channel.unary_unary(
                '/grpc_buf.ExampleApi/CreateExample',
                request_serializer=proto_dot_grpc__buf_dot_api__pb2.CreateExampleRequest.SerializeToString,
                response_deserializer=proto_dot_grpc__buf_dot_api__pb2.CreateExampleResponse.FromString,
                )


class ExampleApiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetExample(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateExample(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExampleApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetExample': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExample,
                    request_deserializer=proto_dot_grpc__buf_dot_api__pb2.GetExampleRequest.FromString,
                    response_serializer=proto_dot_grpc__buf_dot_api__pb2.GetExampleResponse.SerializeToString,
            ),
            'CreateExample': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateExample,
                    request_deserializer=proto_dot_grpc__buf_dot_api__pb2.CreateExampleRequest.FromString,
                    response_serializer=proto_dot_grpc__buf_dot_api__pb2.CreateExampleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc_buf.ExampleApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExampleApi(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetExample(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_buf.ExampleApi/GetExample',
            proto_dot_grpc__buf_dot_api__pb2.GetExampleRequest.SerializeToString,
            proto_dot_grpc__buf_dot_api__pb2.GetExampleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateExample(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc_buf.ExampleApi/CreateExample',
            proto_dot_grpc__buf_dot_api__pb2.CreateExampleRequest.SerializeToString,
            proto_dot_grpc__buf_dot_api__pb2.CreateExampleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
