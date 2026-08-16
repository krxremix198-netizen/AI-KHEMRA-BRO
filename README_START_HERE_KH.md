# AI KHEMRA BRO v6.9.0 — Clean Runtime Package

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

## ផ្ទៃថ្មីសាមញ្ញ (Minimal Mobile Workspace)

កំណែ **v6.9.0** រៀបចំផ្ទៃកម្មវិធីឡើងវិញ សម្រាប់ទូរស័ព្ទ និង browser ដោយកាត់បន្ថយមុខងារដែលបង្ហាញនៅពេលតែមួយ។ ទំព័រចូលប្រើ Customer និង Owner មានតែវាលចាំបាច់ ប៊ូតុងសកម្មភាពសំខាន់មួយ និងតំណទំនាក់ទំនងសង្ខេប។

ផ្ទាំងការងារសំខាន់ត្រូវបានបង្រួមជា **4 ផ្ទាំង**៖ **បកប្រែវីដេអូ**, **កែ SRT**, **បង្កើតសំឡេង**, និង **ក្រុម**។ មុខងារ SRT → Speech និង Text → Speech ត្រូវបានដាក់ជាក្រុមនៅក្នុងផ្ទាំង **បង្កើតសំឡេង** ដើម្បីកាត់បន្ថយភាពរញ៉េរញ៉ៃ។

## ការងារក្រុម (Shared Team Workspace)

កំណែ **v6.8.0** បានបន្ថែមផ្ទាំង **«👥 ការងារក្រុម»** សម្រាប់រៀបចំការបកប្រែរឿងរួមគ្នា។ សមាជិកដែលចូលប្រើដោយ **Access Code ដូចគ្នា** អាចមើល និងកែគម្រោងរួមដូចគ្នាបាន។

| មុខងារ | របៀបប្រើ |
|---|---|
| គម្រោងរឿង/ជំពូក | បង្កើតគម្រោងថ្មី ហើយកំណត់ឈ្មោះរឿង ឬភាគ។ |
| ស្ថានភាព និងអ្នកទទួលបន្ទុក | កំណត់ជា កំពុងបកប្រែ, ត្រូវពិនិត្យ, រួចរាល់ ឬផ្អាក ហើយបញ្ចូលឈ្មោះអ្នកទទួលបន្ទុក។ |
| SRT និងចំណាំរួម | រក្សាទុក SRT និងចំណាំសម្រាប់សមាជិកក្រុម។ អាចនាំ SRT ចូល ឬចេញពី Editor សំខាន់បាន។ |
| ប្រវត្តិកំណែ | រាល់ការរក្សាទុកបង្កើតកំណែថ្មី និងកំណត់ហេតុសកម្មភាព។ កម្មវិធីការពារកុំឱ្យសមាជិកពីរនាក់សរសេរជាន់គ្នា។ |
| ឯកជនភាព | API Key និងវីដេអូដែលបានអាប់ឡូតនៅតែឯកជនក្នុង browser របស់សមាជិកនីមួយៗ។ មានតែគម្រោង SRT/ចំណាំដែលបានរក្សាទុកប៉ុណ្ណោះដែលចែករំលែក។ |

> ប្រសិនបើ Owner លុប Access Code មួយ កម្មវិធីនឹងលុបគម្រោងក្រុមដែលភ្ជាប់នឹង Code នោះផងដែរ ដើម្បីការពារទិន្នន័យមិនឱ្យបង្ហាញពេលមានការប្រើ Code ឡើងវិញ។

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
