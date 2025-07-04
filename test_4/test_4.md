Write an API server that meets the following requirements:
Login
POST /api/login
Inputs are username and password in JSON
Case insensitively validates usernames with at least 4 letters and the letters “a”, “b”, and “c” are in the username in that order. Please see the example below
abacca is validated
Cabbie is not validated since there is no c that comes after ab
Acaiberrycake is valid
Password will be valid if it is equal to the reverse of the username
List letters
GET /api/letters
Seed your database with the following data (you may use an in memory data or use a third party database application. If you do use an external database, make sure that it is included in the submission by submitting a docker image)
{“letter”:”A”, “value”:1, “strokes”:2, “vowel”:true},{“letter”:”B”, “value”:2, “strokes”:1, “vowel”:false}
You may represent the data in your database however you like as long as the expected API outputs are met
This should return a json of all unique letters in the database sorted by value in ascending order. Given the seed data, this should return {“letters”:[“A”, “B”]}
Add letter
POST /api/letter/add
Input is a json object containing the following fields:
Letter: string
Value: int - any random value
Strokes: int - any number that is not equal to value
Vowel: bool - if the letter is treated as a vowel or not
Letters must be unique and not limited to the latin alphabet
Hence a request with {“letter”:”A”, “value”:1, “strokes”:2, “vowel”:true} will fail
Return {‘status”:0} if the letter was added to the database otherwise return {“status”:1}
Get letter
GET /api/letter/<letter:str>
Returns the details of the letter in the URL
/api/letter/A will return {“letter”:”A”, “value”:1, “strokes”:2, “vowel”:true}
Shuffle letters
GET /api/letter/shuffle
Returns a string containing all the letters in the database without repetition but in a random order
Plus points will be given for implementing your own shuffle function
Filter letters
GET /api/letter/filter/<val:int>
Returns a list of letters whose value field is less than or equal to val ordered by when they were added to the database
On the original set, accessing /api/letter/filter/1 this should return {“letters”:[“A”]}
