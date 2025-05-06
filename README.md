# coding-dojo-backend

# 🐍 API Heapsort com Flask

Este projeto é uma API em Python feita com o framework Flask que implementa o algoritmo de ordenação **Heapsort** manualmente (sem bibliotecas externas). A API recebe uma lista de números via requisição HTTP POST e devolve a lista ordenada.

---

## 🚀 Como funciona?

A API possui uma única rota:

### `POST /heapsort`

- Recebe um JSON com uma lista de números inteiros ou decimais.
- Ordena a lista usando o algoritmo **Heapsort**.
- Retorna um JSON com a lista ordenada.

---

## 📦 Exemplo de Requisição

### 🔸 Requisição:
```json
POST /heapsort
Content-Type: application/json

{
  "array": [10, 3, 5, 1, 8]
}
