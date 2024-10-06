from dagster import job, op

@op
def hello_op():
    return "Hello, Dagster!"

@op
def greet_op(name: str):
    return f"Greetings, {name}!"

@job
def hello_job():
    name = hello_op()
    greet_op(name)