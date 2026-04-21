# إعداد اللغات
LANGUAGES = [
    ('ar', 'Arabic'),
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
]

# تفعيل نظام الترجمة
USE_I18N = True
LOCALE_PATHS = [BASE_DIR / 'locale'] # المجلد الذي ستوضع فيه ملفات الترجمة
