async function increase() {
    const resp = await fetch(`increase/${document.getElementById("increaseInput").value}`);
    let num = await resp.json();
    document.getElementById("number").innerText = num;
};
