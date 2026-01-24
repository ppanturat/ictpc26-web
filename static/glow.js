document.querySelectorAll('.menu-container .box').forEach(el => {
    el.addEventListener('mousemove', e => {
        const rect = el.getBoundingClientRect()
        el.style.setProperty('--x', e.clientX - rect.left)
        el.style.setProperty('--y', e.clientY - rect.top)
    })

    el.addEventListener('mouseleave', () => {
        el.style.setProperty('--x', '-9999px')
        el.style.setProperty('--y', '-9999px')
    })
})

document.querySelectorAll('.menu-container .spanning-flexboxes').forEach(el => {
    el.addEventListener('mousemove', e => {
        const rect = el.getBoundingClientRect()
        el.style.setProperty('--x', e.clientX - rect.left)
        el.style.setProperty('--y', e.clientY - rect.top)
    })

    el.addEventListener('mouseleave', () => {
        el.style.setProperty('--x', '-9999px')
        el.style.setProperty('--y', '-9999px')
    })
})