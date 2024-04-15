from sanic import Sanic
from sanic.response import text, json, JSONResponse
from sanic_ext import validate
from api_benchmark.model.response import ArrayValueResponse, ErrorResponse
from api_benchmark.model.request import GetValueRequest
from api_benchmark.data.array_data import test_array


app = Sanic(name="SanicBenchmarkApp")


@app.get("/items/<row_n:int>/<column_n:int>/")
async def read_item(request, row_n: int, column_n: int):
    try:
        value = test_array[row_n, column_n]
    except IndexError as ex:
        return JSONResponse(
            body=ErrorResponse(reason=str(ex)).model_dump(mode="json"),
            status=500,
        )

    return JSONResponse(
        body=ArrayValueResponse(
            value=value,
        ).model_dump(mode="json"),
    )


@app.post("/items")
@validate(json=GetValueRequest)
async def read_root(request, body: GetValueRequest):
    try:
        value = test_array[body.row, body.column]
    except IndexError as ex:
        return JSONResponse(
            body=ErrorResponse(reason=str(ex)).model_dump(mode="json"),
            status=500,
        )

    if body.multiplier:
        value = value * body.multiplier

    return JSONResponse(
        body=ArrayValueResponse(
            value=value,
        ).model_dump(mode="json"),
    )


# sanic server
