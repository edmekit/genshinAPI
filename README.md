# Genshin Character API

A free and open-source REST API that provides recommended builds for Genshin Impact characters, including stat goals, artifacts, weapons, and team compositions.

**Base URL**

```
https://genshinapi-0vzb.onrender.com
```

---

## How to Use

### Get a Character

```
GET /character/{character_name}
```

Example

```http
GET https://genshinapi-0vzb.onrender.com/character/chasca
```

or simply visit

```
https://genshinapi-0vzb.onrender.com/character/chasca
```

### Example Response

```json
{
  "info": "...",
  "recommended": {
    "atk": "2000 - 3000",
    "critdmg": "200% - 250%"
  },
  "premium": {
    "weapon": [
      "Astral Vulture's Crimson Plumage"
    ]
  },
  "f2p": {
    "weapon": "Chain Breaker"
  }
}
```

---

## Character Naming

Character names should be lowercase.

Examples

```
/character/furina
/character/nahida
/character/chasca
```

---

## Contributing

Want to add a missing character or improve existing data?

1. Fork this repository.
2. Add a new JSON file inside the `char/` folder.
3. Name the file using the character's lowercase name.

Example

```
char/
├── chasca.json
├── furina.json
├── nahida.json
```

Use the following schema:

```json
{
  "info": "",

  "recommended": {
    "hp": "",
    "atk": "",
    "def": "",
    "critdmg": "",
    "critrt": "",
    "em": "",
    "artifact": [
      ""
    ]
  },

  "premium": {
    "weapon": [
      ""
    ],
    "team": [
      ["", "", "", ""]
    ]
  },

  "f2p": {
    "weapon": "",
    "team": [
      ["", "", "", ""]
    ]
  }
}
```

After adding your character, submit a Pull Request.

---

## Run Locally

Clone the repository

```bash
git clone https://github.com/<your-username>/<repo>.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start the server

```bash
uvicorn main:app --reload
```

Visit

```
http://127.0.0.1:8000/docs
```

to test the API locally.

---

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn

Install all dependencies using

```bash
pip install -r requirements.txt
```

---

## License

This project is open source. Contributions are welcome!