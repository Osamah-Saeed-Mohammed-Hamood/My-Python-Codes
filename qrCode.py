# 

import qrcode

# النص أو الرابط الذي تريد تحويله إلى QR Code
#data = " https://youtube.com/playlist?list=PL86JZGzAEh4ud3JaPNvU3EFD_Z22peVSH&si=hZt3G9-ONt7IayZX"
#data = "https://waikato.github.io/weka-wiki/documentation/"
#data = "https://sourceforge.net/projects/weka/"
data = "https://youtu.be/sP4cQTZQenk?si=ZXQe7Fah4zUG-ZZM"

# إنشاء كائن QR Code
qr = qrcode.QRCode(
    version=1,  # حجم الـ QR (من 1 إلى 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # تصحيح الخطأ (L، M، Q، H)
    box_size=10,  # حجم كل مربع داخل الـ QR
    border=4,  # حجم الحافة البيضاء حول الـ QR
)

# إضافة البيانات
qr.add_data(data)
qr.make(fit=True)

# إنشاء الصورة
img = qr.make_image(fill_color="black", back_color="white")

# حفظ الصورة في ملف
img.save("WekaForWindows11.png")

print("✅ تم إنشاء QR Code وحفظه باسم 'my_qr_code.png'")
