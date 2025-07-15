# bg-remover-api
A lightweight background remover API built using Python and Flask, deployed on Render.com. Perfect for image editing, SaaS tools, and automation.
# 🖼️ Background Remover API (Python + Flask)

This is a simple and fast background remover API built using *Python, **OpenCV, and **Flask*. It accepts an image via POST request and returns the image with the background removed.

🚀 *Live Demo:*  
[https://your-api.onrender.com](https://your-api.onrender.com)

---

## 🔧 Features

- Upload image via POST /remove
- Removes background using OpenCV logic (can be swapped with AI models)
- Deployed on *Render.com* (Free Tier)
- Can be used as backend for your own tools or websites

---

## 📦 Requirements

- Python 3.x
- Flask
- OpenCV (cv2)
- NumPy
- Render.com account (Free)

Install dependencies:

```bash
pip install -r requirements.txt
