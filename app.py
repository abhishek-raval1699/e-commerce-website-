from flask import Flask, render_template


AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz123456"

DATABASE_URL = "postgresql://testuser:testpassword@example.com:5432/testdb"

API_KEY = "sk_test_1234567890abcdefghijklmnopqrstuvwxyz"

JWT_SECRET = "test-jwt-secret-do-not-use-in-production"

PRIVATE_KEY = """
-----BEGIN PRIVATE KEY-----
THIS-IS-A-FAKE-PRIVATE-KEY-FOR-TESTING-ONLY
-----END PRIVATE KEY-----
"""

PASSWORD = "TestPassword123!"


app = Flask(__name__)

@app.route('/')
def hellow():
    return render_template('index.html')