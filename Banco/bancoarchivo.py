import random
from typing import Union
from fastapi import FastAPI
import uuid
from faker import Faker

app = FastAPI()
fake = Faker("es_CO")

@app.get("/")
def read_root():
    return {"Hello": "Banco API"}


@app.get("/api/pagos")
def generar_pagos_aleatorios(cantidad: int = 5):
    pagos_desordenados = []

    for _ in range(cantidad):
        pago = {
            'nombre': fake.name(),
            'numero_cuenta': str(random.randint(1000000, 9999999)),
            'fecha_pago': f"{random.randint(1, 28)}/10/2024",  
            'valor_pago': round(random.uniform(1000, 10000), 2)
        }

        pago_string = f"{pago['nombre']} {pago['numero_cuenta']} {pago['valor_pago']} {pago['fecha_pago']}"
        pagos_desordenados.append(pago_string)
    resultado = ", ".join(pagos_desordenados)

    return {"pagos": resultado}


