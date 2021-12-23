const table = document.getElementById("reimbursementTable");
const tableBody = document.getElementById("reimbursementBody");

async function updateReimbursement() {
    const requestId = document.getElementById("requestId").value;
    const userId = document.getElementById("userId").value;
    const expensename = document.getElementById("expenseName").value;
    const expenseamount = document.getElementById("expenseAmount").value;
    const expensedetail = document.getElementById("expenseDetail").value;
    const expensestatus = document.getElementById("expenseStatus").value;
    const usercomment = document.getElementById("userComment").value;
    
    let url = "http://127.0.0.1:5000/reimbursement/"
    let response = await fetch(url + requestId, {
        method:"PATCH",
        mode: "cors",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            "requestId": requestId,
            "userId": userId,
            "expenseName": expensename,
            "expenseAmount": expenseamount,
            "expenseDetail": expensedetail,
            "status": expensestatus,
            "userComment": usercomment})
    })
    
    if (response.status === 200) {
        let body = await response.json();
        alert("Request Updated Successful!") 
    } else {
        let body = await response.json;
        alert("Update Request Failed!")
    }
}


async function getAllReimbursementData(){
    let url = "http://127.0.0.1:5000/reimbursement";
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

getAllReimbursementData()

function Logout() {
    sessionStorage.clear()
    window.location.href = "login.html";
}
