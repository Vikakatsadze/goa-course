document.getElementById("myForm").addEventListener("submit", function(e){
    e.preventDefault();

    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    let errorMessage = "";

    if (username === ""){
        errorMessage = "შეიყვანე სახელი!";
    }else if (!email.includes("@")){
        errorMessage = "Email არასწორია!";
    }else if (password.length < 6){
        errorMessage = "პაროლი უნდა იყოს მინიმუმ 6 სიმბოლო";
    }

    if (errorMessage){
        document.getElementById("error").textContent = errorMessage;
    }else {
        document.getElementById("error").textContent = "";
        alert("ფორმა სწორად შეივსო!");
        
        this.onsubmit();
    }
    
})