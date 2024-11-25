const button = document.querySelector(".button")
console.log(button)

button.addEventListener("click", sendData)
function sendData() {

    console.log('Работает')

    const dataStr = {
        'name': 'Чесалка для животных',
        'price': '200.0',
        'image': '/media/image_comb.png'
    }

    console.log(dataStr)

    fetch("http://127.0.0.1:8000/api/products/",
        {
            method: "POST",
            body: JSON.stringify(dataStr),
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            }
        }
    )
    .then(resp => resp.json())
    .then(data => {
        // console.log(data)
    })
}