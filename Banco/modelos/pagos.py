from pydantic import BaseModel
from typing import Optional

class Pago(BaseModel):
    numero_cuenta: str
    nombre: str
    valor_pago: float
    fecha_pago: str
