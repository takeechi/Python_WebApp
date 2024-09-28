// let colorChanged = false;
let selectedColor = "red";
function change_by_select(){
    const selectObj = document.getElementById('select_id');
    selectedColor = selectObj.value;
}
function change_table(){
    const tableObj = document.getElementById('table_id');
    tableObj.style.backgroundColor = selectedColor;
}