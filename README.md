# Django Custom User Model — Todos API

## Loyiha haqida

Django REST Framework asosida yozilgan To-do boshqaruv tizimi.
Foydalanuvchilar ro'yxatdan o'tib, o'z vazifalarini yaratishi, ko'rishi, tahrirlashi va o'chirishi mumkin.

---

## Texnologiyalar

- Python 3.14
- Django
- Django REST Framework
- SQLite (ma'lumotlar bazasi)
- uv (paket menejeri)

---

## Loyiha tuzilmasi

| Papka / Fayl   | Vazifasi                              |
| -------------- | ------------------------------------- |
| config/        | Loyiha sozlamalari (settings, urls)   |
| users/         | Foydalanuvchi modeli va ro'yxatdan o'tish |
| manage.py      | Django boshqaruv skripti              |
| pyproject.toml | Loyiha bog'liqliklari                 |

---

## Ma'lumotlar modellari

### User (Foydalanuvchi)

Django ning standart `AbstractUser` modelidan meros olingan. Qo'shimcha maydon:

| Maydon      | Turi    | Izoh                              |
| ----------- | ------- | --------------------------------- |
| is_verified | Boolean | Foydalanuvchi tasdiqlangan yoki yo'q |

### Task (Vazifa)

| Maydon       | Turi       | Izoh                        |
| ------------ | ---------- | --------------------------- |
| id           | Integer    | Avtomatik birlamchi kalit   |
| title        | String     | Vazifa sarlavhasi           |
| description  | Text       | Vazifa tavsifi              |
| is_completed | Boolean    | Bajarilganlik holati        |
| user         | ForeignKey | Vazifa egasi (User)         |
| created_at   | DateTime   | Yaratilgan vaqt             |
| updated_at   | DateTime   | Yangilangan vaqt            |

---

## API Endpointlar

### Foydalanuvchi

| Metod | URL                      | Vazifasi                              |
| ----- | ------------------------ | ------------------------------------- |
| POST  | /api/v1/users/register/  | Yangi foydalanuvchi ro'yxatdan o'tkazish |

### Vazifalar (Todos)

| Metod  | URL                  | Vazifasi                                    |
| ------ | -------------------- | ------------------------------------------- |
| POST   | /api/v1/todos/       | Yangi vazifa yaratish                       |
| GET    | /api/v1/todos/       | Barcha vazifalarni ko'rish (filter bilan)   |
| GET    | /api/v1/todos/{id}/  | Bitta vazifani ko'rish                      |
| PUT    | /api/v1/todos/{id}/  | Vazifani to'liq yangilash                   |
| DELETE | /api/v1/todos/{id}/  | Vazifani o'chirish                          |

#### Sana bo'yicha filtrlash

Vazifalar ro'yxatini ko'rishda quyidagi query parametrlardan foydalanish mumkin:

- `start_date` — boshlanish sanasi (format: DD.MM.YYYY)
- `end_date` — tugash sanasi (format: DD.MM.YYYY)

Misol: `/api/v1/todos/?start_date=12.11.2025&end_date=21.05.2026`

---

## O'rnatish va ishga tushirish

1. Repozitoriyani klonlash
2. Virtual muhit yaratish va bog'liqliklarni o'rnatish
3. Ma'lumotlar bazasini migratsiya qilish
4. Serverni ishga tushirish

---

## Loyiha maqsadi

Bu loyiha **NajotTalim SN04** o'quv dasturining 74-darsi uchun yozilgan.
Maqsad — Django da maxsus foydalanuvchi modeli (Custom User Model) va REST API yaratishni o'rganish.
