# 1. انتخاب image پایه‌ی Python
FROM python:3.13.6-slim

# 2. تنظیم دایرکتوری کاری داخل container
WORKDIR /app

# 3. کپی فایل requirements.txt به داخل container
COPY requirements.txt .

# 4. نصب پکیج‌ها
RUN pip install --no-cache-dir -r requirements.txt

# 5. کپی کل پروژه به داخل container
COPY . .

# 6. باز کردن پورت 8000 برای Django
EXPOSE 8000

# 7. دستور پیش‌فرض برای اجرای سرور توسعه Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
