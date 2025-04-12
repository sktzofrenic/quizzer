export default function getDinero (amt) {
    let USDollar = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        maximumFractionDigits: 0,
    })
    return USDollar.format(amt)
}
