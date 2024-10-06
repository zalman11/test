function addIframe() {
    const iframeInput = document.getElementById("iframeInput");
    const iframeCode = iframeInput.value;

    // Fetch the gallery.html content
    fetch("gallery.html")
        .then(response => response.text())
        .then(data => {
            // Find the gallery div
            const galleryDiv = document.querySelector("#gallery");

            // Add the iframe code to the gallery div
            galleryDiv.innerHTML += iframeCode;

            // Update the gallery.html file
            fetch("gallery.html", {
                method: "PUT",
                headers: {
                    "Content-Type": "text/html"
                },
                body: data + iframeCode
            })
            .then(response => {
                if (response.ok) {
                    console.log("Iframe added successfully!");
                } else {
                    console.error("Error adding iframe.");
                }
            })
            .catch(error => console.error(error));
        })
        .catch(error => console.error(error));
}