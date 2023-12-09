# python-grpc-buf

1. Generate proto files

    ```bash
    buf generate
    ```

2. Activate virtual environment

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Run server

    ```bash
    python3 src/grpc_buf/main.py
    ```

5. Test server
    a. GetExample API

    ```bash
    grpcurl -proto proto/grpc_buf/api.proto -d @ -plaintext localhost:50051 grpc_buf.ExampleApi.GetExample <<EOM
    {
      "id": "1"
    }
    EOM
    ```

    b. CreateExample API

    ```bash
    grpcurl -proto proto/grpc_buf/api.proto -d @ -plaintext localhost:50051 grpc_buf.ExampleApi.CreateExample <<EOM
    {
      "example": {
        "id": "1",
        "name": "anim et ut eu"
      }
    }
    EOM
    ```
