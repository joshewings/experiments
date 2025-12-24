# experiments
My experiments

## Run the webpage
1. Start the web server:
   ```bash
   python app.py
   ```
2. Open `http://localhost:8000` in your browser.

## Deploy to PythonAnywhere
1. **Create or log in to your PythonAnywhere account.**
2. **Start a Bash console** from the dashboard.
3. **Clone this repository** into your home directory:
   ```bash
   git clone https://github.com/joshewings/experiments.git
   cd experiments
   ```
4. **Create a virtual environment** (replace `3.11` with your preferred Python version if needed) and activate it:
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```
5. **Install dependencies** (there are no external dependencies for this project, but this keeps the environment ready if you add some later):
   ```bash
   pip install -r requirements.txt  # safe to run even if the file is empty or missing
   ```
6. **Create a WSGI entrypoint** so PythonAnywhere can serve the page. In the Bash console, open your WSGI configuration file (linked from the "Web" tab) and replace its contents with:
   ```python
   import pathlib

   HTML = """
   <!doctype html>
   <html lang="en">
     <head>
       <meta charset="utf-8" />
       <title>Happy Holidays</title>
       <style>
         :root {
           color-scheme: light;
         }

         body {
           margin: 0;
           min-height: 100vh;
           font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
           color: #fff7f0;
           background: radial-gradient(circle at top, #2d6a4f 0%, #1b4332 55%, #081c15 100%);
           display: flex;
           align-items: center;
           justify-content: center;
         }

         .card {
           background: rgba(255, 255, 255, 0.08);
           border: 1px solid rgba(255, 255, 255, 0.2);
           border-radius: 24px;
           padding: 48px 56px;
           max-width: 520px;
           box-shadow: 0 20px 45px rgba(0, 0, 0, 0.35);
           text-align: center;
           position: relative;
           overflow: hidden;
         }

         .card::before,
         .card::after {
           content: "";
           position: absolute;
           width: 140px;
           height: 140px;
           border-radius: 50%;
           background: rgba(255, 255, 255, 0.12);
           top: -60px;
           right: -40px;
         }

         .card::after {
           width: 180px;
           height: 180px;
           top: auto;
           bottom: -70px;
           left: -60px;
         }

         h1 {
           font-size: 2.6rem;
           margin-bottom: 16px;
           letter-spacing: 1px;
         }

         p {
           font-size: 1.1rem;
           margin-bottom: 28px;
           line-height: 1.6;
         }

         .details {
           display: flex;
           gap: 16px;
           justify-content: center;
           flex-wrap: wrap;
         }

         .badge {
           background: #d00000;
           color: #fff7f0;
           padding: 10px 18px;
           border-radius: 999px;
           font-weight: 600;
           text-transform: uppercase;
           letter-spacing: 1px;
           box-shadow: 0 8px 18px rgba(208, 0, 0, 0.35);
         }

         .badge.alt {
           background: #ffd166;
           color: #432818;
           box-shadow: 0 8px 18px rgba(255, 209, 102, 0.35);
         }
       </style>
     </head>
     <body>
       <main class="card">
         <h1>Happy Holidays!</h1>
         <p>
           We're decking the halls with a fresh Christmas vibe. Enjoy the warm
           glow, festive colors, and a little holiday cheer on our main page.
         </p>
         <div class="details">
           <span class="badge">Season's Greetings</span>
           <span class="badge alt">Winter Magic</span>
         </div>
       </main>
     </body>
   </html>
   """


   def application(environ, start_response):
       start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
       return [HTML.encode("utf-8")]
   ```
   (If you later convert `app.py` to a WSGI framework like Flask, update this section to import and expose your Flask `app` instead.)
7. **Back on the "Web" tab**, set the virtualenv path (e.g., `/home/your-username/experiments/venv`) and point the code directory to `/home/your-username/experiments`.
8. **Reload the web app**. Visit your `https://<your-username>.pythonanywhere.com` domain to see the holiday page.
9. **Update code later** by pulling the latest changes and reloading the web app:
   ```bash
   cd ~/experiments
   git pull
   touch /var/www/<your-username>_pythonanywhere_com_wsgi.py  # if you edited the WSGI file
   ```
