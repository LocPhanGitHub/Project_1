const username = document.getElementById("userName")
const password = document.getElementById("userPassword")
const userrole = document.getElementById("userRole")

async function login(){
    let response = await fetch(
        "http://127.0.0.1:5000/login", {
            method:"POST",
            mode:"cors",
            headers: {"Content-Type": "application/json"}, 
            body: JSON.stringify({"userName": username.value, "userPassword": password.value, "userRole": userrole.value})
        }
    )
    if (response.status === 200){
        let body = await response.json()
        console.log(body)
        if (body["validated"]) {
            sessionStorage.setItem("validated", true)
            if (userrole.value === "manager"){
            window.location.href = "manager_homepage.html"
            } else {window.location.href = "employee_homepage.html"}
        } else {
                alert("Login Failed: Please Try Again!")
            }
    } else {
        alert("The Request Failed")
    }
}

