let socket = new WebSocket('ws://localhost:9999/');

socket.onopen = () => {
    // Tell the server who we are
    console.log("connected to socket")
    socket.send("browser")
}
socket.onmessage = (message) => {
    //Message handling
    console.log(message.data);
    if (message.data == "skip") {
        document.querySelector('.ytp-next-button').click();
    } else if (message.data == "back") {
        window.history.back();
    }
}