let body = document.body
let parentDiv = document.createElement("div")
let h1 = document.createElement("h1")
let p = document.createElement("p")
body.appendChild(parentDiv)
body.appendChild(h1)
body.appendChild(p)

h1.textContent = "Heading"
p.textContent = "Hello world"

parentDiv.style.height = "200px"
parentDiv.style.width = "200px"
parentDiv.style.backgroundColor = "green"

document.title = "My Website"
