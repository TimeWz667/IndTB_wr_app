# Diagnosis and treatment


care-seeking


``` js
fetch('http://example.com/users/1', {
  method: 'PUT',
  body: JSON.stringify({
    name: 'John Doe',
    age: 27,
  }),
  headers: {
    'Content-type': 'application/json',
  },
})
  .then((response) => response.json())
  .then((json) => console.log(json));
```
