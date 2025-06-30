import pytest
from fastapi_backend.main import app
from httpx import AsyncClient
from httpx import ASGITransport  # 👈 important

@pytest.mark.asyncio
async def test_health_check():
    transport = ASGITransport(app=app)  # 👈 required for ASGI-based testing
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}