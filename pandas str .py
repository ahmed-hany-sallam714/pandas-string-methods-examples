# 📌 استيراد مكتبة الباندا
import pandas as pd

# 🧾 مجموعة بيانات نصية متنوعة (أسماء، أرقام، حروف، مسافات...)
data = ["AHMED", "Ahmed", "ahmed", "kjh", "345", "    "]

# 🧵 تحويل القائمة إلى Series للتعامل مع الدوال النصية
series = pd.Series(data)

# 🧪 اختبارات على السلسلة النصية باستخدام دوال pandas.str
print("🔄 Swapcase:\n", series.str.swapcase())       # تحويل الأحرف: الكابتل تصبح سمول والعكس
print("\n🔡 Lower:\n", series.str.lower())           # تحويل كل النص إلى أحرف صغيرة
print("\n🔠 Capitalize:\n", series.str.capitalize()) # أول حرف كابتل والباقي سمول
print("\n🔼 Upper:\n", series.str.upper())           # تحويل كل النص إلى كابتل

print("\n🔍 islower:\n", series.str.islower())       # هل النص كله سمول؟
print("\n🔍 istitle:\n", series.str.istitle())       # هل النص مكتوب بصيغة عنوان (أول حرف كابتل والباقي سمول)؟
print("\n🔍 isspace:\n", series.str.isspace())       # هل النص عبارة عن مسافات فقط؟
print("\n🔍 isdigit:\n", series.str.isdigit())       # هل النص يحتوي على أرقام فقط؟
print("\n🔍 isalpha:\n", series.str.isalpha())       # هل النص يحتوي على حروف فقط؟
print("\n🔍 isalnum:\n", series.str.isalnum())       # هل النص يحتوي على حروف وأرقام فقط؟
print("\n🔍 isdecimal:\n", series.str.isdecimal())   # هل النص عبارة عن أرقام عشرية فقط؟
print("\n🔍 isnumeric:\n", series.str.isnumeric())   # هل النص أرقام (تشمل الرموز الرقمية)؟
print("\n🔍 isupper:\n", series.str.isupper())       # هل النص كله كابتل؟

# 🎨 تنسيقات نصية
print("\n🧊 zfill(20):\n", series.str.zfill(20))     # إضافة أصفار من اليسار حتى يصل الطول إلى 20
print("\n🎯 center(20):\n", series.str.center(20))   # توسيط النص داخل مساحة 20 حرف
print("\n⬅️ ljust(20):\n", series.str.ljust(20))     # محاذاة لليسار
print("\n➡️ rjust(20):\n", series.str.rjust(20))     # محاذاة لليمين

# 🔎 البحث عن الحرف "e"
print("\n📍 rfind('e'):\n", series.str.rfind("e"))   # آخر موقع للحرف "e"
print("\n📍 find('e'):\n", series.str.find("e"))     # أول موقع للحرف "e"

# ✅ هل تنتهي أو تبدأ بشكل معين؟
print("\n❓ endswith('5'):\n", series.str.endswith("5"))
print("\n❓ startswith('A'):\n", series.str.startswith("A"))

# 🧮 طول كل عنصر
print("\n📏 Length:\n", series.str.len())
