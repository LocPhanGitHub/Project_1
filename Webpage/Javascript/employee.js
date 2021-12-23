const table = document.getElementById("reimbursementTable");
const tableBody = document.getElementById("reimbursementBody");

async function createReimbursement() {
    const userId = document.getElementById("userId").value;
    const expensename = document.getElementById("expenseName").value;
    const expenseamount = document.getElementById("expenseAmount").value;
    const expensedetail = document.getElementById("expenseDetail").value;
    const expensestatus = document.getElementById("expenseStatus").value;
    const usercomment = document.getElementById("userComment").value;
    
    let response = await fetch("http://127.0.0.1:5000/reimbursement", {
        method:"POST",
        mode: "cors",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            "userId": userId,
            "expenseName": expensename,
            "expenseAmount": expenseamount,
            "expenseDetail": expensedetail,
            "status": expensestatus,
            "userComment": usercomment})
    }
    )
    if (response.status === 200) {
        let body = await response.json();
        alert("Request Submitted Successful!") 
    } else {
        let body = await response.json;
        alert("Request Failed!")
    }
}

async function getMyReimbursementData(){
    let url = "http://127.0.0.1:5000/reimbursement/user/3";
    let response = await fetch(url);

    if (response.status === 200) {
        let body = await response.json();
        populateData(body);
    } else {
        alert("There was a problem trying to get the reimbursement information!")
    }
}

function populateData(responseBody) {
    for (let reimbursement of responseBody) {
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${reimbursement.requestId}</td>
                                <td>${reimbursement.userId}</td>
                                <td>${reimbursement.expenseName}</td>
                                <td>${reimbursement.expenseAmount}</td>
                                <td>${reimbursement.expenseDetail}</td>
                                <td>${reimbursement.status}</td>
                                <td>${reimbursement.userComment}</td>`
        tableBody.appendChild(tableRow)
    }
}

getMyReimbursementData()

function Logout() {
    sessionStorage.clear()
    window.location.href = "login.html";
}

