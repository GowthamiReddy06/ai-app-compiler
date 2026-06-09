from fastapi import FastAPI

from intent_extractor import extract_intent
from system_designer import design_system
from schema_generator import generate_schema
from validator import validate_schema
from repair_engine import repair_schema

app = FastAPI(
    title="AI App Compiler"
)


@app.get("/")
def home():

    return {
        "message":
        "AI App Compiler Running"
    }


@app.post("/generate")
def generate(data: dict):

    prompt = data["prompt"]

    intent = extract_intent(prompt)

    design = design_system(intent)

    schema = generate_schema(design)

    errors = validate_schema(schema)

    repaired = False

    if errors:

        schema = repair_schema(
            schema,
            errors
        )

        repaired = True

    return {
        "intent": intent,
        "design": design,
        "schema": schema,
        "errors": errors,
        "repaired": repaired
    }