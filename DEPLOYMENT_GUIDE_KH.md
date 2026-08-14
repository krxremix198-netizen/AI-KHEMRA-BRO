# AI KHEMRA BRO v6.6.1 — មគ្គុទ្ទេសក៍ដាក់ឱ្យប្រើប្រាស់

## គោលបំណងនៃកំណែនេះ

កំណែនេះជួសជុលបញ្ហាដែលរារាំងការដំណើរការ និងរៀបចំកម្មវិធីសម្រាប់ចែកចាយជាសាធារណៈតាម URL មួយ។ អ្នកប្រើអាចចូលពី iPhone, Android ឬ browser ផ្សេងទៀតបានដោយប្រើ **Access Code** ដែលអ្នកគ្រប់គ្រងផ្តល់ឱ្យ។ កូដមួយអាចប្រើលើឧបករណ៍ច្រើនក្នុងពេលតែមួយ ហើយកម្មវិធីមិនចងកូដនោះជាមួយ device, IP ឬ fingerprint ឡើយ។

> **សុវត្ថិភាពសំខាន់៖** កុំប្រើ Streamlit Community Cloud សម្រាប់គ្រប់គ្រង Access Code លក់/ចែកចាយ ប្រសិនបើអ្នកមិនមាន persistent storage។ ឯកសារ `licenses.db` ត្រូវតែស្ថិតលើ persistent volume មួយ ដើម្បីមិនបាត់អតិថិជន កូដ និងកំណត់ត្រាពេល server restart ឬ deploy កំណែថ្មី។

| ធាតុ | ស្ថានភាព v6.6.1 |
|---|---|
| ចូលពីទូរស័ព្ទច្រើន | បានគាំទ្រ; មិនមាន device lock ឬ single-session lock |
| Access Code | អ្នកគ្រប់គ្រងបង្កើត និងផ្តល់ជូនដោយដៃ |
| Admin | ត្រូវកំណត់ `ADMIN_USERNAME` និង `ADMIN_PASSWORD` ផ្ទាល់ខ្លួន |
| Cookies/API key | ត្រូវការសោ `COOKIE_SECRET` ដែលអ្នកគ្រប់គ្រងកំណត់; មិនមាន hard-coded key សម្រាប់ deploy ថ្មី |
| License database | កំណត់ទៅ persistent `/data/licenses.db` ក្នុង Docker |
| FFmpeg | ដំឡើងក្នុង container សម្រាប់ video/audio/MP3 |
| Whisper model cache | រក្សាទុកក្នុង `/data/huggingface` ដើម្បីកុំទាញម្តងទៀតរាល់ restart |

## ការរៀបចំមុន Deploy

សូមកុំផ្ញើលេខសម្ងាត់ Admin ឬ API key មកក្នុង chat ឬ commit ទៅ Git។ នៅក្នុងថតគម្រោង សូមចម្លង `.env.example` ទៅជា `.env` ហើយកែតម្លៃ placeholder ទាំងអស់។ `COOKIE_SECRET` និង `LICENSE_PEPPER` គួរជាតម្លៃចៃដន្យវែងៗ និងខុសគ្នាពីគ្នា។

```bash
cp .env.example .env
```

| តម្លៃ | ត្រូវកំណត់ | មូលហេតុ |
|---|---:|---|
| `ADMIN_USERNAME` | បាទ/ចាស | ឈ្មោះចូល Admin របស់ម្ចាស់កម្មវិធី |
| `ADMIN_PASSWORD` | បាទ/ចាស | ពាក្យសម្ងាត់ Admin ដែលមិនមានក្នុង source code |
| `COOKIE_SECRET` | បាទ/ចាស | អ៊ិនគ្រីប cookies សម្រាប់ session និង Gemini API key ក្នុង browser |
| `LICENSE_PEPPER` | បាទ/ចាស | បំប្លែង Access Code មុនរក្សាទុកក្នុង database |
| `GEMINI_API_KEYS` | ជម្រើស | ប្រើតែបើអ្នកចង់ផ្តល់ Gemini key ពី server; បើមិនដូច្នោះ អ្នកប្រើអាចបញ្ចូល key ផ្ទាល់ខ្លួន |

## របៀប Deploy ជាមួយ Docker

Docker គឺជាជម្រើសដែលបានរៀបចំក្នុង folder នេះ ព្រោះវារក្សា FFmpeg, Python packages, database និង Whisper cache ឱ្យស្ថិតស្ថេរ។ ម៉ាស៊ីន host ត្រូវមាន Docker និង Docker Compose រួចជាស្រេច។

```bash
cp .env.example .env
# កែ .env ដោយមិនដាក់វាទៅ Git
sudo docker compose up -d --build
sudo docker compose logs -f
```

បន្ទាប់ពី service ដំណើរការ សូមបើក `http://SERVER-IP:8501` ឬភ្ជាប់ domain/TLS តាម reverse proxy របស់អ្នក។ ក្នុង deployment ជាក់ស្តែង សូមប្រើ HTTPS និង firewall ដែលបើកតែ port ដែលត្រូវការ។ Volume `ai_khemra_data` ត្រូវបានកំណត់ក្នុង `compose.yaml`; វាជាទីតាំងរក្សា `licenses.db` និង Whisper model cache ដើម្បីឱ្យទិន្នន័យនៅសល់ក្រោយ restart ឬ update កម្មវិធី។

## ការចូល Admin និងចែក Access Code

លើទំព័រ Login ចុចសញ្ញា `✦` ខាងលើស្តាំ **៥ ដង** ដើម្បីបើកផ្ទាំង Admin។ បញ្ចូល `ADMIN_USERNAME` និង `ADMIN_PASSWORD` ដែលអ្នកបានកំណត់ក្នុង `.env`។ ពីផ្ទាំងនេះ អ្នកអាចបង្កើត Access Code មួយៗ បិទ/បើក code បន្តថ្ងៃប្រើ និងលុប code ដែលមិនត្រូវការបាន។

| សកម្មភាព | លទ្ធផល |
|---|---|
| បង្កើត Access Code | ផ្តល់ code ដោយផ្ទាល់ទៅអតិថិជន/អ្នកប្រើ |
| អ្នកប្រើ Login | អាចចូលបានពី phone ឬ browser ច្រើនដោយ code ដដែល |
| Logout ពី phone មួយ | បិទតែ session នៅ browser នោះ; មិនបិទ device ផ្សេង |
| បិទ Access Code | រារាំង code នោះពីគ្រប់ device បន្ទាប់ពី refresh/login |
| បន្តថ្ងៃប្រើ | បន្ថែមសិទ្ធិប្រើដោយមិនបង្កើត code ថ្មី |

## ចំណាំអំពី Gemini API Key

Gemini API key ដែលអ្នកប្រើបញ្ចូលត្រូវរក្សាទុក **តែក្នុង browser របស់អ្នកប្រើនោះ** ប៉ុណ្ណោះ ដោយអ៊ិនគ្រីបតាម `COOKIE_SECRET`។ Key មិនត្រូវបានចែករំលែកទៅទូរស័ព្ទផ្សេង ឬទៅអ្នកប្រើផ្សេងទេ។ ប្រសិនបើអ្នកប្រើលុប browser data ឬប្តូរ browser គាត់ត្រូវបញ្ចូល key ម្តងទៀត។

## Backup និង Update

មុន update កំណែថ្មី សូម backup volume ដែលមាន `/data/licenses.db`។ សម្រាប់ Docker volume ក្នុង `compose.yaml` អ្នកអាច export backup ដូចខាងក្រោម៖

```bash
sudo docker run --rm \
  -v ai_khemra_bro_repair_ai_khemra_data:/data:ro \
  -v "$PWD":/backup \
  alpine tar czf /backup/ai-khemra-data-backup.tgz -C /data .
```

ឈ្មោះ volume អាចខុសគ្នាតាមឈ្មោះ folder របស់អ្នក។ សូមពិនិត្យជាមួយ `sudo docker volume ls` មុន run command។ កុំ commit `licenses.db`, `.env`, backup ឬ API key ទៅ repository ទេ។

## ការត្រួតពិនិត្យក្រោយ Deploy

សាកល្បងចូលពីទូរស័ព្ទពីរដោយ Access Code ដូចគ្នា។ ទាំងពីរគួរចូលបាន។ បន្ទាប់មក restart container ម្តង ហើយចូល Admin ពិនិត្យថា Access Code នៅដដែល។ សាកបង្កើត MP3 មួយក្នុង Text → Speech ដើម្បីបញ្ជាក់ថា Edge TTS និង FFmpeg ដំណើរការ។

> កុំបើកផ្ទាំង Admin ឬផ្តល់ `.env` ឱ្យអ្នកដទៃ។ អ្នកប្រើទូទៅត្រូវទទួលតែ Access Code ដែលអ្នកសម្រេចចិត្តផ្តល់ប៉ុណ្ណោះ។
