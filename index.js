import {user}  from "user"

fetch('https://reqres.in/api/users')
.then(response => response.json())
.then(data => console.log(data))  




