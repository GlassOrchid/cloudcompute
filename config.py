from project_secrets import SECRET_KEY

class Config:
    SECRET_KEY = SECRET_KEY
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}