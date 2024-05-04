# clouthes-back/src/app.py
from fastapi import FastAPI, Request, HTTPException
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
from .routes import auth_routes, catalog_routes, order_routes, user_routes, returns_routes
from .middlewares.auth_middleware import verify_jwt_token
from .database.db import init_db

# Configuração de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("clouthes-back")

# Função para gerenciar eventos de ciclo de vida
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicialização do banco de dados
    init_db()
    yield
    # Código de encerramento, se necessário

# Criação da aplicação FastAPI
app = FastAPI(title="Clouthes Back", version="1.0.0", lifespan=lifespan)

# Configuração de CORS
origins = ["http://localhost:3000", "https://meu-site.com"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Middleware de autenticação
@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if request.url.path not in ["/auth/login", "/auth/register"]:
        token = request.headers.get("Authorization")
        if token:
            if not verify_jwt_token(token):
                return JSONResponse(status_code=401, content={"message": "Invalid or expired token"})
        else:
            return JSONResponse(status_code=401, content={"message": "Missing Authorization Header"})
    response = await call_next(request)
    return response

# Tratamento de exceções globais
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

# Rotas
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(catalog_routes.router, prefix="/catalog", tags=["catalog"])
app.include_router(order_routes.router, prefix="/orders", tags=["orders"])
app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(returns_routes.router, prefix="/returns", tags=["returns"])

# Endpoint básico para saúde da aplicação
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
