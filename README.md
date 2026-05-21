# Django Custom User Model — Todos API

Django REST Framework asosida yozilgan foydalanuvchi va vazifalar boshqaruv tizimi.

---

## Texnologiyalar

- Python 3.14
- Django
- Django REST Framework
- SQLite
- uv (paket menejeri)

---

## Loyiha tuzilmasi

```text
config/        — sozlamalar (settings, urls)
users/         — foydalanuvchi modeli va endpointlar
manage.py      — Django boshqaruv skripti
pyproject.toml — bog'liqliklar
```

---

## Modellar

### User

`AbstractUser` dan meros olingan. Qo'shimcha maydon:

| Maydon      | Turi    | Izoh                          |
| ----------- | ------- | ----------------------------- |
| is_verified | Boolean | Foydalanuvchi tasdiqlanganmi  |

### Todo (Vazifa)

| Maydon       | Turi       | Izoh                      |
| ------------ | ---------- | ------------------------- |
| id           | Integer    | Birlamchi kalit           |
| title        | String     | Vazifa sarlavhasi         |
| description  | Text       | Vazifa tavsifi            |
| is_completed | Boolean    | Bajarilganlik holati      |
| user         | ForeignKey | Vazifa egasi              |
| created_at   | DateTime   | Yaratilgan vaqt           |
| updated_at   | DateTime   | Yangilangan vaqt          |

---

## API Endpointlar

### Foydalanuvchi

| Metod | URL                     | Vazifasi                    |
| ----- | ----------------------- | --------------------------- |
| POST  | /api/users/register/    | Yangi foydalanuvchi yaratish |

### Vazifalar

Foydalanuvchi URL parametridan olinadi (`user_id`).

| Metod  | URL                              | Vazifasi              |
| ------ | -------------------------------- | --------------------- |
| GET    | /api/users/{user_id}/todos/      | Barcha vazifalar      |
| POST   | /api/users/{user_id}/todos/      | Yangi vazifa yaratish |
| GET    | /api/users/{user_id}/todos/{id}/ | Bitta vazifa          |
| PUT    | /api/users/{user_id}/todos/{id}/ | Vazifani yangilash    |
| DELETE | /api/users/{user_id}/todos/{id}/ | Vazifani o'chirish    |

---

## O'rnatish

```bash
# Reponi klonlash
git clone <repo-url>
cd django-custom-user-model

# Virtual muhit va bog'liqliklar
uv sync

# Migratsiya
python manage.py migrate

# Serverni ishga tushirish
python manage.py runserver
```

---

## Loyiha maqsadi

**NajotTalim SN04** — 74-dars. Django da Custom User Model va DRF yordamida REST API yaratish.
