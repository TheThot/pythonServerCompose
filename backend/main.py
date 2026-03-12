from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
app = FastAPI()
# @app.get("/", response_class=HTMLResponse)
# async def read_root():
#     html_content = """
#         <!DOCTYPE html>
#         <html>
#             <head>
#                 <title>Simple Page</title>
#             </head>
#             <body>
#                 <div class="container">
#                     <h1>Hello from Effective Mobile!</h1>
#                 </div>
#             </body>
#         </html>
#         """
#     return html_content
@app.get("/")
async def read_root():
    return "Hello from Effective Mobile!"

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )