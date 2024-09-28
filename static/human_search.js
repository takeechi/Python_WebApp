function check_input(){
    const searchHeight = document.getElementById("searchHeight");
    const searchWeight = document.getElementById("searchWeight");
    console.log(searchHeight.value);
    console.log(searchWeight.value);
    if(searchHeight.value !== "" && searchWeight.value !== ""){
        return true;
    } else {
        alert("身長または体重が入力されていません")
        return false;
    }
}