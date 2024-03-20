from fastapi import FastAPI
from routers import rotas_auth, rotas_familia, rotas_conta, rotas_renda

app = FastAPI()

app.include_router(rotas_familia.router, prefix=('/familia'))
app.include_router(rotas_conta.router, prefix=('/conta'))
app.include_router(rotas_renda.router, prefix=('/renda'))
app.include_router(rotas_auth.router, prefix=('/auth'))