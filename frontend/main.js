window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount();
})

const functionApi = 'http://localhost:7071/api/Http_trigger_v2';
const functionApiAzure = "__FUNCTION_URL__"; // This will be replaced during GitHub Actions workflow

const getVisitCount = () => {
    let count = 30;
    fetch(functionApiAzure).then(response => {
        return response.json()
    }).then(response =>{
        console.log("Website called function API.");
        count = response.count;
        document.getElementById("counter").innerText = count;
    }).catch(function(error){
        console.log(error);
    });
    return count;
}


