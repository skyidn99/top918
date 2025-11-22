
# Domain Checker API (Self-Hosted)

A FastAPI-based service to check whether a domain is listed in the Indonesian TrustPositif/Nawala blocklist (via Skiddle-ID/blocklist).

## Deploy on Railway

1. Create a new Railway project
2. Select "Deploy from GitHub"
3. Push this repo to GitHub
4. Railway will auto-detect FastAPI

### Start Command
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

## API Endpoint

```
GET /check?domain=example.com
```

Response:
```
{
  "domain": "example.com",
  "blocked": false,
  "source": "Skiddle-ID/blocklist"
}
```
