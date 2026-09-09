function copyResult() {

    const result = document.getElementById("resultText");

    if (!result) {
        return;
    }

    navigator.clipboard.writeText(result.innerText);

    const button = document.querySelector(".copy-btn");

    button.innerText = "Copied!";

    setTimeout(() => {
        button.innerText = "Copy";
    }, 1500);
}