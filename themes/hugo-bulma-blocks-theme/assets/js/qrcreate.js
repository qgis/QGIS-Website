const qrCodeElements = document.querySelectorAll('.qr-code');
qrCodeElements.forEach(renderQr);    


// Creates a single QR Code, then appends it to the document.
function renderQr(container) {
    // See https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes
    text = container.dataset.url;
    const errCorLvl = qrcodegen.QrCode.Ecc.LOW;  // Error correction level
    const qr = qrcodegen.QrCode.encodeText(text, errCorLvl);  // Make the QR Code symbol
    drawCanvas(qr, 5, 4, "#FFFFFF", "#000000", container);  // Draw it on screen
}

// Draws the given QR Code, with the given module scale and border modules, onto the given HTML
// canvas element. The canvas's width and height is resized to (qr.size + border * 2) * scale.
// The drawn image is purely dark and light, and fully opaque.
// The scale must be a positive integer and the border must be a non-negative integer.
function drawCanvas(qr, scale, border, lightColor, darkColor, canvas) {
    if (scale <= 0 || border < 0)
        throw new RangeError("Value out of range");
    const width = (qr.size + border * 2) * scale;
    canvas.width = width;
    canvas.height = width;
    let ctx = canvas.getContext("2d");
    for (let y = -border; y < qr.size + border; y++) {
        for (let x = -border; x < qr.size + border; x++) {
            ctx.fillStyle = qr.getModule(x, y) ? darkColor : lightColor;
            ctx.fillRect((x + border) * scale, (y + border) * scale, scale, scale);
        }
    }
}