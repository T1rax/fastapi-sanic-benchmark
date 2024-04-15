from fastapi import FastAPI, Response
from api_benchmark.model.response import ArrayValueResponse, ErrorResponse
from api_benchmark.model.request import GetValueRequest
from api_benchmark.data.array_data import test_array


app = FastAPI(title="FastAPI BenchmarkApp")


@app.get(
    "/items/{row_n}/{column_n}/",
    response_model=ArrayValueResponse,
)
async def read_item(row_n: int, column_n: int):
    try:
        value = test_array[row_n, column_n]
    except IndexError:
        return Response(
            content=ErrorResponse,
            status_code=500,
        )

    return ArrayValueResponse(
            value=value,
        )


@app.post(
    "/items",
    response_model=ArrayValueResponse,
)
async def read_root(get_value_request: GetValueRequest):
    try:
        value = test_array[get_value_request.row, get_value_request.column]
    except IndexError:
        return Response(
            content=ErrorResponse,
            status_code=500,
        )

    if get_value_request.multiplier:
        value = value * get_value_request.multiplier

    return ArrayValueResponse(
            value=value,
        )

# uvicorn main:app --reload
