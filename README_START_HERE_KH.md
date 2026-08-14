# AI KHEMRA BRO v6.7.1 — Clean Runtime Package

Package នេះមានតែឯកសារចាំបាច់សម្រាប់ដំណើរការ App។ មិនមាន test files, debug scripts, log files ឬ release notes ចាស់ៗនៅក្នុង runtime archive ទេ។

| ឯកសារ | ត្រូវប្រើសម្រាប់ |
|---|---|
| `app.py` | កម្មវិធី Streamlit សំខាន់។ |
| `requirements.txt` | Python packages ដែល App ត្រូវការ។ |
| `Dockerfile` | Build container ដែលមាន FFmpeg និង dependencies។ |
| `compose.yaml` | បើក App ជាមួយ persistent Docker volume។ |
| `.env.example` | Template សម្រាប់ Admin credentials និង secrets។ |
| `.gitignore` | ការពារ `.env`, database និង media មិនឱ្យ commit។ |

## ចាប់ផ្ដើមដោយ Docker

1. ចម្លង `.env.example` ទៅ `.env`។
2. កែ `ADMIN_USERNAME`, `ADMIN_PASSWORD`, `COOKIE_SECRET` និង `LICENSE_PEPPER` ជារបស់អ្នកផ្ទាល់។
3. រត់ `docker compose up -d --build`។
4. បើក `http://SERVER-IP:8501`។

> Access Code database ត្រូវរក្សាទុកក្នុង Docker volume `ai_khemra_data` តាម `/data`។ កុំលុប volume នេះ ប្រសិនបើចង់រក្សា Customer និង Access Code ចាស់។

## ចាប់ផ្ដើមដោយ Python ក្នុង local machine

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
export ADMIN_USERNAME=admin
export ADMIN_PASSWORD='choose-a-strong-password'
export COOKIE_SECRET='use-a-random-secret-at-least-32-characters'
export LICENSE_PEPPER='use-a-second-random-secret-at-least-32-characters'
export AI_KHEMRA_BRO_DATA_DIR="$PWD/data"
mkdir -p "$AI_KHEMRA_BRO_DATA_DIR"
streamlit run app.py
```

ត្រូវដំឡើង FFmpeg លើ local machine មុនប្រើ Video → SRT → MP3។
