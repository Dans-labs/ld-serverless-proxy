from fastapi import APIRouter

from ld_proxy.core.models.output import OutputExample
from ld_proxy.core.models.input import InputExample

router = APIRouter()


@router.get("/example", tags=["example get"])
def example_get():
    """
    API V1
    Say hej!

    This will greet you properly

    And this path operation will:
    * return "hej!"
    """
    return {"msg": "Hej!"}


@router.post("/example", response_model=OutputExample, tags=["example post"])
def example_endpoint(inputs: InputExample):
    """
    Multiply two values

    This will multiply two inputs.

    And this path operation will:
    * return a*b
    """
    return {"a": inputs.a, "b": inputs.b, "result": inputs.a * inputs.b}
