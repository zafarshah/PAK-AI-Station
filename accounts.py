import os, sqlite3, hashlib, secrets, hmac
from pathlib import Path
DB=Path(os.environ.get('PAK_AI_DB',str(Path(__file__).with_name('accounts.sqlite3'))))
def connect():
 db=sqlite3.connect(DB,timeout=15);db.execute('PRAGMA journal_mode=WAL');db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT UNIQUE NOT NULL, salt TEXT NOT NULL, pw_hash TEXT NOT NULL, credits INTEGER NOT NULL DEFAULT 20)');db.execute('CREATE TABLE IF NOT EXISTS ledger (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, delta INTEGER NOT NULL, reason TEXT NOT NULL, reference TEXT UNIQUE, created_at TEXT DEFAULT CURRENT_TIMESTAMP)');db.commit();return db
def digest(password,salt):return hashlib.pbkdf2_hmac('sha256',password.encode(),bytes.fromhex(salt),260000).hex()
def register(email,password):
 email=email.strip().lower()
 if '@' not in email or len(password)<10:raise ValueError('Enter a valid email and a password of at least 10 characters.')
 salt=secrets.token_hex(16)
 with connect() as db:
  try:
   db.execute('INSERT INTO users(email,salt,pw_hash) VALUES(?,?,?)',(email,salt,digest(password,salt)))
   uid=db.execute('SELECT id FROM users WHERE email=?',(email,)).fetchone()[0]
   db.execute('INSERT INTO ledger(user_id,delta,reason,reference) VALUES(?,?,?,?)',(uid,20,'Welcome credits','welcome:'+str(uid)))
  except sqlite3.IntegrityError:raise ValueError('Account already exists.')
 return uid
def login(email,password):
 with connect() as db:r=db.execute('SELECT id,salt,pw_hash FROM users WHERE email=?',(email.strip().lower(),)).fetchone()
 return r[0] if r and hmac.compare_digest(digest(password,r[1]),r[2]) else None
def balance(uid):
 with connect() as db:
  r=db.execute('SELECT credits FROM users WHERE id=?',(uid,)).fetchone()
 return r[0] if r else 0
def change(uid,delta,reason,reference):
 with connect() as db:
  db.execute('BEGIN IMMEDIATE')
  if reference and db.execute('SELECT 1 FROM ledger WHERE reference=?',(reference,)).fetchone():return False
  if db.execute('UPDATE users SET credits=credits+? WHERE id=? AND credits+?>=0',(delta,uid,delta)).rowcount!=1:return False
  db.execute('INSERT INTO ledger(user_id,delta,reason,reference) VALUES(?,?,?,?)',(uid,delta,reason,reference));return True
