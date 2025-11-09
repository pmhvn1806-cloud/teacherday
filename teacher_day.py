from flask import Flask, request
from markupsafe import Markup

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    teacher_name = "Thầy/Cô kính mến"
    default_message = "Chúc mừng Ngày Nhà giáo Việt Nam 20/11! Kính chúc Thầy/Cô luôn mạnh khỏe, hạnh phúc và thành công trong sự nghiệp trồng người!"
    message = default_message
    if request.method == "POST":
        message = default_message

    html = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Chúc mừng Ngày Nhà giáo Việt Nam</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{height:100%;font-family:Segoe UI,Roboto,Arial,sans-serif;}}
body{{background:linear-gradient(180deg,#fff8f0,#fff0f6);color:#222;overflow-x:hidden;}}
#fireworks-canvas{{position:fixed;inset:0;pointer-events:none;z-index:0;}}
.container{{position:relative;z-index:5;max-width:1000px;margin:40px auto;padding:20px;text-align:center;}}
.marquee{{display:inline-block;font-size:22px;font-weight:700;padding:8px 20px;border-radius:999px;background:rgba(255,255,255,0.85);box-shadow:0 8px 30px rgba(0,0,0,0.08);animation:slide 10s linear infinite;white-space:nowrap;}}
@keyframes slide{{0%{{transform:translateX(0)}}50%{{transform:translateX(-20px)}}100%{{transform:translateX(0)}}}}
.teacher{{margin-top:12px;color:#6b2c91;font-weight:700}}
.card{{margin-top:18px;display:flex;gap:20px;align-items:center;justify-content:center;background:rgba(255,255,255,0.9);border-radius:14px;padding:18px;box-shadow:0 10px 30px rgba(102,51,
