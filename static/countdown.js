function updateCountdown() {
    const deadline = new Date("January 31, 2026 23:59:59").getTime()
    const now = new Date().getTime()
    const diff = deadline - now

    if (diff <= 0) {
        document.getElementById("timer").innerHTML = "CLOSED"
        return
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24))
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60))
    const seconds = Math.floor((diff % (1000 * 60)) / 1000)

    const format = (num) => num.toString().padStart(2, '0')

    document.getElementById("timer").innerHTML =
        `${format(days)}:${format(hours)}:${format(minutes)}:${format(seconds)}`
}

setInterval(updateCountdown, 1000)
updateCountdown()