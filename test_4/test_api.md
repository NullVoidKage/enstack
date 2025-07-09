

## 🔧 Postman Collection: `LetterAPI`

### 🌐 Base URL

```
http://localhost:5001
```

---

### 1. ✅ `POST /api/login`

**Description:** Validates login using a username (must contain 'a', 'b', 'c' in order) and reverse string as password.

#### 📤 Request

```
POST /api/login
Content-Type: application/json
```

```json
{
  "username": "abcde",
  "password": "edcba"
}
```

#### 📥 Success Response

```json
{
  "message": "Login successful"
}
```

#### ❌ Failure Response (e.g., invalid username or wrong password)

```json
{
  "error": "Invalid credentials"
}
```

Status: `401 Unauthorized`

---

### 2. ✅ `GET /api/letters`

**Description:** Returns sorted unique letters by their values.

#### 📤 Request

```
GET /api/letters
```

#### 📥 Response

```json
{
  "letters": ["A", "B"]
}
```

---

### 3. ✅ `POST /api/letter/add`

**Description:** Adds a new letter entry.

#### 📤 Request

```
POST /api/letter/add
Content-Type: application/json
```

```json
{
  "letter": "C",
  "value": 3,
  "strokes": 2,
  "vowel": false
}
```

#### 📥 Success Response

```json
{
  "status": 0
}
```

#### ❌ Failure Response (e.g., duplicate, type error, strokes = value)

```json
{
  "status": 1
}
```

---

### 4. ✅ `GET /api/letter/{letter}`

**Description:** Get details of a specific letter.

#### 📤 Request

```
GET /api/letter/A
```

#### 📥 Success Response

```json
{
  "letter": "A",
  "value": 1,
  "strokes": 2,
  "vowel": true
}
```

#### ❌ Failure Response

```json
{
  "error": "Letter not found"
}
```

Status: `404 Not Found`

---

### 5. ✅ `GET /api/letter/shuffle`

**Description:** Returns a shuffled string of all unique letters.

#### 📤 Request

```
GET /api/letter/shuffle
```

#### 📥 Response

```
"BAC" // Randomized output
```

---

### 6. ✅ `GET /api/letter/filter/{val}`

**Description:** Returns letters where value ≤ `val`.

#### 📤 Request

```
GET /api/letter/filter/2
```

#### 📥 Response

```json
{
  "letters": ["A", "B"]
}
```

---
