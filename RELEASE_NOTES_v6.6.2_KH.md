# AI KHEMRA BRO v6.6.2 — Story-Faithful Translation និង Strict SRT Timing

## គោលបំណង

កំណែនេះកែលម្អការបកប្រែ និងការបញ្ចេញសំឡេង Khmer សម្រាប់ video/SRT dubbing។ គោលដៅគឺរក្សា **សាច់រឿង ន័យ អារម្មណ៍ និង timestamp ដើម** ដោយមិនឱ្យសំឡេងចាប់ផ្តើមមុន cue ឬបន្តលើសចុង cue។

| ផ្នែក | ការកែលម្អ v6.6.2 |
|---|---|
| សាច់រឿង | Prompt បង្ខំឱ្យយល់ cause-and-effect, ទំនាក់ទំនងតួអង្គ និងអារម្មណ៍ មុនបកប្រែ។ |
| ន័យសំខាន់ | ហាមសង្ខេប កាត់បន្ថយ បង្កើតថ្មី ឬប្តូរ clue, promise, warning, condition, negation, name និង number។ |
| SRT timing | ID, cue count, cue order, start និង end timestamp ត្រូវបាន lock មិនឱ្យផ្លាស់ប្តូរ។ |
| Audio fitting | សំឡេងចាប់ផ្តើមតាម cue start និងត្រូវបញ្ចប់នៅ/មុន cue end។ មិនបន្ថែម milliseconds សិប្បនិម្មិត ឬ tail 350 ms បន្ទាប់ពី cue ចុងក្រោយទៀត។ |
| សំឡេងធម្មជាតិ | រក្សា tempo អតិបរមា 1.10× ដើម្បីមិនបង្ខំឱ្យភាសាខ្មែររត់លឿន ឬស្ងួតៗ។ |
| Cue វែងពេក | App បង្ហាញ error ច្បាស់ៗ ជំនួសឱ្យកាត់ចុងសំឡេង ឬអូសសំឡេងលើសវីដេអូ។ |

> ប្រសិនបើ cue មួយមានពាក្យច្រើនពេកសម្រាប់ timestamp ដើម App នឹងមិនកាត់ពាក្យ ឬកាត់សំឡេងស្ងាត់ៗទេ។ សូមប្រើ Khmer ដែលខ្លីធម្មជាតិដោយរក្សាន័យគ្រប់យ៉ាង ឬបន្ថែមពេល cue ក្នុង SRT ដើម។

## របៀបប្រើ

សម្រាប់ Video → SRT និង AI Subtitle Translator សូមរក្សា video/SRT ដែលមាន timestamp ត្រឹមត្រូវ។ បន្ទាប់ពីបាន Khmer SRT អ្នកអាចពិនិត្យអត្ថបទក្នុង SRT Editor មុនចុចបង្កើត MP3។ ប្រសិនបើ App រាយការណ៍ថា cue វែងពេក សូមកាត់តែរចនាសម្ព័ន្ធពាក្យឱ្យខ្លី ដោយមិនលុបន័យ ឬពង្រីក timestamp cue នោះ។

## ការផ្ទៀងផ្ទាត់

បាន pass Python syntax, static analysis, Edge TTS, FFmpeg audio ducking, SRT-to-MP3, video extraction, privacy isolation និង regression test ថ្មី `test_v662_story_and_strict_timing.py` ដែលវាស់ថា output MP3 មិនបង្កើត tail លើស SRT ចុងក្រោយ។
