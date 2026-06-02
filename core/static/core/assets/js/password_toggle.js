document.querySelectorAll(".toggle-password").forEach(button => {

    button.addEventListener("click", function(){

        const input = this.previousElementSibling;

        if(input.type === "password"){
            input.type = "text";
            this.innerHTML = '<i class="fa fa-eye-slash"></i>';
        }
        else{
            input.type = "password";
            this.innerHTML = '<i class="fa fa-eye"></i>';
        }

    });

});
