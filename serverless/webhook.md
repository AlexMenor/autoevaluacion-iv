# Configuración de webhook entre dev.to y vercel

- Crear webhook en vercel: https://vercel.com/docs/more/deploy-hooks
- Hacer curl a la api de dev.to para crear ese webhook:
```
curl -v -X POST -H "Content-Type: application/json" \
  -H "api-key: API_KEY" \
  -d '{"webhook_endpoint":{"target_url":"https://example.org/webhooks/webhook1","source":"rhymes","events":["article_created"]}}' \
  https://dev.to/api/webhooks
```

[Repositorio funcionando](https://github.com/AlexMenor/jamstack-portfolio)

