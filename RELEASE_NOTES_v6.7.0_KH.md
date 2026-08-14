# AI KHEMRA BRO v6.7.0 — Ordered Workflow និង Google AI Stable Fallback

## គោលបំណង

កំណែនេះរក្សា **UI ដដែល** ប៉ុន្តែកែលម្អលំហូរខាងក្នុងសម្រាប់ Video → Khmer SRT → MP3 ដើម្បីមិនរំលង cue, រក្សាលំដាប់សាច់រឿង និងធ្វើ fallback ទៅ Google AI Studio Gemini ម៉ូឌែល stable ថ្មីៗដោយស្វ័យប្រវត្តិ។

| ផ្នែក | ការកែលម្អ |
|---|---|
| លំដាប់បកប្រែ | បែងជា batch 30 cue, រក្សា context 8 cue មុន និងមិន return មុនគ្រប់ batch។ |
| មិនរំលងបន្ទាត់ | កូដផ្ទៀងផ្ទាត់ថា cue គ្រប់ ID មានការបកប្រែ មុនបង្កើត SRT។ បើខ្វះ App បង្ហាញ error ជំនួសឱ្យបង្កើត SRT ខ្វះ cue។ |
| សាច់រឿង | Repair prompt រក្សា clue, command, condition, negation, name, number និងអារម្មណ៍ ដោយមិនសង្ខេប ឬបន្ថយន័យ។ |
| Khmer-only | Repair និង SRT refinement បដិសេធអក្សរបរទេស មិនមែនតែ Chinese characters ប៉ុណ្ណោះ។ |
| Google AI Studio | Fallback ខាងក្នុងប្រើ stable IDs `gemini-3.7-flash`, `gemini-3.6-flash`, `gemini-3.5-flash`, និង `gemini-3.5-flash-lite`។ UI model selector មិនត្រូវបានប្តូរ។ |
| Video → MP3 | Workflow “Khmer SRT + MP3 តែម្តង” នៅដដែល; Whisper timestamps ត្រូវប្រើម្តង ហើយបន្តទៅ translation/audio ដោយមិនធ្វើ ASR ម្តងទៀត។ |
| សំឡេង | រក្សា strict SRT timing និង natural audio master ពី v6.6.2 ដើម្បីកុំឱ្យសំឡេងលើសវីដេអូ ឬកាត់ចុងពាក្យស្ងាត់ៗ។ |

## ចំណាំសម្រាប់ការប្រើប្រាស់ 24 ម៉ោង

កូដអាចត្រៀមរួចសម្រាប់ run 24 ម៉ោង ប៉ុន្តែការរត់ public 24/7 ត្រូវការម៉ាស៊ីន ឬ cloud host ដែលបើកជានិច្ច។ ការធ្វើឱ្យមនុស្សគ្រប់គ្នាប្រើដោយសេរីត្រូវមាន CPU/RAM គ្រប់គ្រាន់សម្រាប់ FFmpeg និង Whisper។ Access Code មិនចង device រួចហើយ ប៉ុន្តែ public server ឥតគិតថ្លៃភាគច្រើនមិនធានា uptime ឬធនធានសម្រាប់ video/audio jobs ច្រើនពេលតែមួយទេ។

## ការផ្ទៀងផ្ទាត់

បាន pass syntax, static analysis, Edge TTS, FFmpeg audio ducking, SRT-to-MP3, video extraction, privacy isolation, strict timing, Google AI fallback និង ordered-batch regression tests។

## ប្រភព Google AI

Google Gemini model catalog: <https://ai.google.dev/gemini-api/docs/models>

Google Gemini API release notes: <https://ai.google.dev/gemini-api/docs/changelog>
