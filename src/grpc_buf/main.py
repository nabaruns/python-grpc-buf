"""The Python AsyncIO implementation of the GRPC server."""

import asyncio
import logging
import os
import sys

import grpc

sys.path.append(os.path.join(os.path.dirname(__file__), "../../gen"))

from proto.grpc_buf.api_pb2_grpc import (
    ExampleApiServicer,
    add_ExampleApiServicer_to_server,
)
from proto.grpc_buf.api_pb2 import (
    CreateExampleRequest,
    CreateExampleResponse,
    Example,
    GetExampleRequest,
    GetExampleResponse,
)

storage: dict[str, Example] = {}

class ExampleApi(ExampleApiServicer):
    async def GetExample(
        self, request: GetExampleRequest, context: grpc.aio.ServicerContext
    ) -> GetExampleResponse:
        logging.info("GetExample called")
        result = storage.get(request.id, None)
        if result is None:
            await context.abort(grpc.StatusCode.NOT_FOUND, "Example not found")
        response = GetExampleResponse(example=result)
        return response

    async def CreateExample(
        self, request: CreateExampleRequest, context: grpc.aio.ServicerContext
    ) -> CreateExampleResponse:
        logging.info("CreateExample called")
        if request.example.id in storage:
            await context.abort(grpc.StatusCode.ALREADY_EXISTS, "Example already exists")
        storage[request.example.id] = request.example
        return CreateExampleResponse(example=request.example)


async def serve() -> None:
    """Start the GRPC server."""
    logging.info("Starting server")
    server = grpc.aio.server()
    add_ExampleApiServicer_to_server(ExampleApi(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
